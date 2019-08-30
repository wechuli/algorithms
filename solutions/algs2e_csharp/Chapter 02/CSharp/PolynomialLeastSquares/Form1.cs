using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

using System.Drawing.Drawing2D;

namespace PolynomialLeastSquares
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // The data points.
        private List<Point> Points = new List<Point>();

        // The polynomial's parameters.
        private bool Solved = false;
        private double[] AValues = null;

        // Perform linear least squares.
        private void solveButton_Click(object sender, EventArgs e)
        {
            try
            {
                aValueListBox.Items.Clear();
                Solved = false;

                int degree = int.Parse(degreeTextBox.Text);
                AValues = FindPolynomialLeastSquaresFit(Points, degree);

                // Display the A values.
                foreach (double value in AValues)
                    aValueListBox.Items.Add(value);

                Solved = true;
                graphPictureBox.Refresh();
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message, "Error");
            }

            graphPictureBox.Refresh();
        }

        // Find a linear least squares fit for the points.
        private double[] FindPolynomialLeastSquaresFit(
            List<Point> points, int degree)
        {
            if (degree >= points.Count)
                throw new Exception("The degree should be smaller than the number of points.");

            // Allocate space for degree + 1 equations with
            // unknowns degree + 2 unknowns.
            double[][] coeffs = new double[degree + 1][];

            // Calculate in the coefficients.
            for (int k = 0; k <= degree; k++)
            {
                coeffs[k] = new double[degree + 1];

                // Fill in coefficients for the partial
                // derivative with respect to Ak.
                for (int aSub = 0; aSub <= degree; aSub++)
                {
                    // Calculate in the A<aSub> term.
                    coeffs[k][aSub] = 0;
                    for (int i = 0; i < points.Count; i++)
                        coeffs[k][aSub] += Math.Pow(points[i].X, k + aSub);
                }
            }

            // Calculate the constant values.
            double[] values = new double[degree + 1];
            for (int k = 0; k <= degree; k++)
            {
                values[k] = 0;
                for (int i = 0; i < points.Count; i++)
                    values[k] += points[i].Y * Math.Pow(points[i].X, k);
            }

            // Solve the equations.
            return GaussianEliminate(coeffs, values);
        }

        // Perform Gaussian elimination and return the results in a list.
        private const double TINY = 0.00001;
        private double[] GaussianEliminate(double[][] coeffs, double[] values)
        {
            // The values numRows and numCols are the number of rows
            // and columns in the matrix, not the augmented matrix.
            int numRows = coeffs.Length;
            int numCols = coeffs[0].Length;

            // Build the agumented array.
            double[][] aug = new double[numRows][];
            for (int r = 0; r < numRows; r++)
            {
                aug[r] = new double[numCols + 1];
                for (int c = 0; c < numCols; c++)
                    aug[r][c] = coeffs[r][c];

                aug[r][numCols] = values[r];
            }

            // Solve.
            for (int r = 0; r < numRows - 1; r++)
            {
                // Zero out all entries in column r after this row.
                // See if this row has a non-zero entry in column r.
                if (Math.Abs(aug[r][r]) < TINY)
                {
                    // Too close to zero. Try to swap with a later row.
                    for (int r2 = r + 1; r2 < numRows; r2++)
                    {
                        if (Math.Abs(aug[r2][r]) > TINY)
                        {
                            // This row will work. Swap them.
                            for (int c = 0; c < numCols + 1; c++)
                            {
                                double tmp = aug[r][c];
                                aug[r][c] = aug[r2][c];
                                aug[r2][c] = tmp;
                            }
                            break;
                        }
                    }
                }

                // See if aug[r][r] is still zero.
                if (Math.Abs(aug[r][r]) < TINY)
                {
                    // No later row has a non-zero entry in this column.
                    throw new Exception("There is no unique solution.");
                }

                // Zero out this column in later rows.
                for (int r2 = r + 1; r2 < numRows; r2++)
                {
                    double factor = -aug[r2][r] / aug[r][r];
                    for (int c = r; c <= numCols; c++)
                        aug[r2][c] = aug[r2][c] + factor * aug[r][c];
                }
            }

            // See if we have a solution.
            if (Math.Abs(aug[numRows - 1][numCols - 1]) < TINY)
            {
                // We have no solution.
                // See if all of the entries in this row are 0.
                bool allZeros = true;
                for (int c = 0; c < numCols + 2; c++)
                {
                    if (Math.Abs(aug[numRows - 1][c]) > TINY)
                    {
                        allZeros = false;
                        break;
                    }
                }
                if (allZeros)
                    throw new Exception("The solution is not unique.");
                else
                    throw new Exception("There is no solution.");
            }

            // Back substitute.
            double[] xs = new double[numRows];
            for (int r = numRows - 1; r >= 0; r--)
            {
                xs[r] = aug[r][numCols];
                for (int r2 = r + 1; r2 < numRows; r2++)
                    xs[r] -= aug[r][r2] * xs[r2];
                xs[r] /= aug[r][r];
            }
            return xs;
        }

        // Remove the data points.
        private void resetButton_Click(object sender, EventArgs e)
        {
            Points = new List<Point>();
            AValues = null;
            Solved = false;
            graphPictureBox.Refresh();
        }

        // Add another data point.
        private void graphPictureBox_MouseClick(object sender, MouseEventArgs e)
        {
            Points.Add(e.Location);
            Solved = false;
            graphPictureBox.Refresh();
        }

        // Perform linear least squares.
        private void graphPictureBox_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.Clear(graphPictureBox.BackColor);
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;

            // Draw the data points.
            const int radius = 2;
            foreach (Point point in Points)
            {
                Rectangle rect = new Rectangle(
                    point.X - radius, point.Y - radius,
                    2 * radius, 2 * radius);
                e.Graphics.FillEllipse(Brushes.Red, rect);
            }

            // If we have a solution, draw it.
            if (Solved)
            {
                List<PointF> curve = new List<PointF>();
                for (int x = 0; x < graphPictureBox.ClientSize.Width; x++)
                {
                    curve.Add(new PointF(x, F(AValues, x)));
                }
                e.Graphics.DrawLines(Pens.Blue, curve.ToArray());
            }
        }

        // Calculate the value of the function at this X value.
        private float F(double[] a, double x)
        {
            double result = 0;
            double factor = 1;
            for (int i = 0; i < a.Length; i++)
            {
                result += a[i] * factor;
                factor *= x;
            }
            return (float)result;
        }

        private void degreeTextBox_TextChanged(object sender, EventArgs e)
        {
            AValues = null;
            Solved = false;
            graphPictureBox.Refresh();
        }
    }
}
