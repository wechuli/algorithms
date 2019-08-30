using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

using System.Numerics;

namespace ExponentiateMod
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // Demonstrate fast exponentiation with a modulus.
        private void evaluateButton_Click(object sender, EventArgs e)
        {
            BigInteger value = BigInteger.Parse(valueTextBox.Text);
            BigInteger exponent = BigInteger.Parse(exponentTextBox.Text);
            BigInteger modulus = BigInteger.Parse(modulusTextBox.Text);
            BigInteger result = ExponentiateMod(value, exponent, modulus);
            resultTextBox.Text = result.ToString();
        }

        // Perform the exponentiation.
        private BigInteger ExponentiateMod(BigInteger value, BigInteger exponent, BigInteger modulus)
        {
            BigInteger result = 1;
            BigInteger factor = value;
            while (exponent != 0)
            {
                if (exponent % 2 == 1) result = (result * factor) % modulus;
                factor = (factor * factor) % modulus;
                exponent /= 2;
            }
            return result;
        }
    }
}
