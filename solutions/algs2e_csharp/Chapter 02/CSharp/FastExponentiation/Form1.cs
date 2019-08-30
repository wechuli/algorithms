using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

// Add a reference to System.Numerics.
using System.Numerics;

namespace FastExponentiation
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // Demonstrate fast exponentiation.
        private void evaluateButton_Click(object sender, EventArgs e)
        {
            resultTextBox.Clear();

            BigInteger value = BigInteger.Parse(valueTextBox.Text);
            BigInteger exponent = BigInteger.Parse(exponentTextBox.Text);
            BigInteger result = Exponentiate(value, exponent);
            resultTextBox.Text = result.ToString();
        }

        // Perform the exponentiation.
        private BigInteger Exponentiate(BigInteger value, BigInteger exponent)
        {
            BigInteger result = 1;
            BigInteger factor = value;
            while (exponent != 0)
            {
                if (exponent % 2 == 1) result *= factor;
                factor *= factor;
                exponent /= 2;
            }
            return result;
        }
    }
}
