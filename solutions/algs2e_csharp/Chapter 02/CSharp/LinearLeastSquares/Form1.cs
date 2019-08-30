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

namespace LinearLeastSquares
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // The data points.
        private List<Point> Points = new List<Point>();

        // The line's parameters.
        private bool Solved = false;
        private double m, b;

        // Perform linear least squares.
        private void solveButton_Click(object sender, EventArgs e)
        {
            try
            {
                mTextBox.Clear();
                bTextBox.Clear();
                Solved = false;

                FindLinearLeastSquaresFit(Points, out m, out b);

                Solved = true;
                mTextBox.Text = m.ToString();
                bTextBox.Text = b.ToString();
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message, "Error");
            }

            graphPictureBox.Refresh();
        }

        // Find a linear least squares fit for the points.
        private void FindLinearLeastSquaresFit(
            List<Point> points, out double m, out double b)
        {
            if (points.Count < 2)
                throw new Exception("A linear least squares fit requires at least two points.");

            // Calculate the S values.
            double Sx = 0;
            double Sxx = 0;
            double Sxy = 0;
            double Sy = 0;
            foreach (Point point in points)
            {
                Sx += point.X;
                Sxx += point.X * point.X;
                Sxy += point.X * point.Y;
                Sy += point.Y;
            }
            double S1 = Points.Count;
            m = (Sxy * S1 - Sx * Sy) / (Sxx * S1 - Sx * Sx);
            b = (Sxy * Sx - Sy * Sxx) / (Sx * Sx - S1 * Sxx);

            if (double.IsNaN(m) || double.IsNaN(b))
                throw new Exception("Error finding least squares fit.");
        }

        // Remove the data points.
        private void resetButton_Click(object sender, EventArgs e)
        {
            Points = new List<Point>();
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
                float x0 = 0;
                float y0 = (float)m * x0 + (float)b;
                float x1 = graphPictureBox.ClientSize.Width;
                float y1 = (float)m * x1 + (float)b;
                e.Graphics.DrawLine(Pens.Blue, x0, y0, x1, y1);
            }
        }
    }
}
