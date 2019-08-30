using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace GaussianElmination
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // Regard this as zero.
        private double TINY = 0.00001;

        private void Form1_Load(object sender, EventArgs e)
        {
            xsLabel.Text = "x1\nx2\nx3 =\nx4\n...";

            // Another example to try.
            //coeffsTextBox.Text =
            //    "2  4  6\r\n" +
            //    "3  6  7\r\n" +
            //    "6 10  4";
            //valuesTextBox.Text =
            //    "-2\r\n" +
            //    " 2\r\n" +
            //    " 1";
        }

        // Build and solve the augmented matrix.
        private void calculateButton_Click(object sender, EventArgs e)
        {
            // Get the coefficients and values.
            double[][] coeffs = LoadCoeffs();
            double[] values = LoadValues();

            // Solve.
            xListBox.Items.Clear();
            checkListBox.Items.Clear();
            errorsListBox.Items.Clear();
            double[] xs;
            try
            {
                xs = GaussianEliminate(coeffs, values);
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message, "Calculation Error");
                return;
            }

            // Display the values.
            int numRows = xs.Length;
            for (int r = 0; r < numRows; r++)
                xListBox.Items.Add($"x[{r}] = {xs[r]}");

            // Verify.
            int numCols = coeffs[0].Length;
            for (int r = 0; r < numRows; r++)
            {
                double tmp = 0;
                for (int c = 0; c < numCols; c++)
                    tmp += coeffs[r][c] * xs[c];
                checkListBox.Items.Add($"{tmp}");

                double error = tmp - values[r];
                errorsListBox.Items.Add($"{error}");
            }
        }

        // Perform Gaussian elimination and return the results in a list.
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

        // Load the coefficients array.
        private double[][] LoadCoeffs()
        {
            // Get the coefficients text.
            string coeffsText = coeffsTextBox.Text;

            // Split the text into rows.
            string[] coeffsRows = coeffsText.Split('\n');
            int numRows = coeffsRows.Length;

            // Process the rows.
            char[] separators = { ' ' };
            int numCols = coeffsRows[0].Split(separators,
                StringSplitOptions.RemoveEmptyEntries).Length;
            double[][] arr = new double[numRows][];
            for (int r = 0; r < numRows; r++)
            {
                string[] fields = coeffsRows[r].Split(separators,
                    StringSplitOptions.RemoveEmptyEntries);
                arr[r] = new double[numCols];
                for (int c = 0; c < numCols; c++)
                {
                    arr[r][c] = double.Parse(fields[c]);
                }
            }
            return arr;
        }

        // Load the values array.
        private double[] LoadValues()
        {
            // Get the values text.
            string valuesText = valuesTextBox.Text;

            // Split the text into rows.
            char[] separators = { '\n' };
            string[] valuesRows = valuesText.Split(separators,
                StringSplitOptions.RemoveEmptyEntries);

            // Process the rows.
            int numRows = valuesRows.Length;
            double[] arr = new double[numRows];
            for (int r = 0; r < numRows; r++)
                arr[r] = double.Parse(valuesRows[r]);
            return arr;
        }

        private void DumpArray(double[][] arr)
        {
            int numRows = arr.Length;
            int numCols = arr[0].Length;
            for (int r = 0; r < numRows; r++)
            {
                for (int c = 0; c < numCols; c++)
                {
                    double value = Math.Round(arr[r][c], 4);
                    Console.Write($"[{value,10}]");
                }
                Console.WriteLine();
            }
            Console.WriteLine();
        }
    }
}
