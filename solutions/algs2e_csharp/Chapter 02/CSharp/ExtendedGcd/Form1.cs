using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace ExtendedGcd
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void goButton_Click(object sender, EventArgs e)
        {
            long a = long.Parse(aTextBox.Text);
            long b = long.Parse(bTextBox.Text);
            long x, y;

            long gcd = ExtendedGcd(a, b, out x, out y);
            gcdTextBox.Text = gcd.ToString();
            long lcm = a * (b / gcd);
            lcmTextBox.Text = lcm.ToString();
            bezoutTextBox.Text = $"{a} * {x} + {b} * {y} = {gcd}";
            verifyTextBox.Text = (a * x + b * y == gcd).ToString();
        }

        // Perform the extended GCD algorithm.
        private long ExtendedGcd(long a, long b, out long x, out long y)
        {
            // Setup.
            long r = b;
            long prevR = a;

            x = 0;
            long prevX = 1;

            y = 1;
            long prevY = 0;

            // Run the algorithm.
            for (;;)
            {
                // See if we're done.
                long newR = prevR % r;
                if (newR == 0) return r;

                // Update x and y.
                long q = prevR / r;
                long newX = prevX - q * x;
                prevX = x;
                x = newX;

                long newY = prevY - q * y;
                prevY = y;
                y = newY;

                // Update r.
                prevR = r;
                r = newR;

                Console.WriteLine($"q: {q}, r: {r}, x: {x}, y: {y}");
            }
            Console.WriteLine();
        }
    }
}
