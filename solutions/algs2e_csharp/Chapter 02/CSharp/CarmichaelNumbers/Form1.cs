﻿using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

using System.Numerics;

namespace CarmichaelNumbers
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // Generate Carmichael numbers.
        private void goButton_Click(object sender, EventArgs e)
        {
            resultListBox.Items.Clear();
            Cursor = Cursors.WaitCursor;
            Refresh();

            // Get the number of numbers to check.
            int maxNumber = int.Parse(maxNumberTextBox.Text);

            // Make a Sieve of Eratosthenes.
            bool[] isComposite = MakeSieve(maxNumber);

            // Check for Carmichael numbers.
            for (int i = 3; i < maxNumber; i += 2)
            {
                // Only check non-primes.
                if (isComposite[i])
                {
                    // See if i is a Carmichael number.
                    if (IsCarmichael(i))
                    {
                        string txt = i.ToString() + " = ";
                        List<int> factors = PrimeFactors(i);
                        foreach (int factor in factors)
                            txt += factor.ToString() + " x ";
                        txt = txt.Substring(0, txt.Length - 3);
                        resultListBox.Items.Add(txt);
                    }
                }
            }

            countLabel.Text =
                resultListBox.Items.Count.ToString() +
                " Carmichael numbers";
            Cursor = Cursors.Default;
        }

        // Make a Sieve of Eratosthenes.
        private bool[] MakeSieve(int maxNumber)
        {
            bool[] isComposite = new bool[maxNumber + 1];

            // "Cross out" multiples of 2.
            for (long i = 4; i <= maxNumber; i += 2)
            {
                isComposite[i] = true;
            }

            // "Cross out" multiples of primes found so far.
            long nextPrime = 3;
            long stopAt = (long)Math.Sqrt(maxNumber);
            while (nextPrime <= stopAt)
            {
                // "Cross out" multiples of this prime.
                for (long i = nextPrime * 2; i <= maxNumber; i += nextPrime)
                {
                    isComposite[i] = true;
                }

                // Move to the next prime.
                do
                    nextPrime += 2;
                while ((nextPrime <= maxNumber) && (isComposite[nextPrime]));
            }

            return isComposite;
        }

        // Return true if the number is a Carmichael number.
        private bool IsCarmichael(int number)
        {
            // Check all possible witnesses.
            for (int i = 2; i < number; i++)
            {
                // Only check numbers with GCD(number, 1) = 1.
                if (Gcd(number, i) == 1)
                {
                    // Calculate: i ^ (number-1) mod number.
                    int result = (int)ExponentiateMod(i, number - 1, number);

                    // If we found a Fermat witness,
                    // then this is not a Carmichael number.
                    if (result != 1) return false;
                }
            }

            // They're all a bunch of liars!
            // This is a Carmichael number.
            return true;
        }

        // Find GCD(a, b).
        // GCD(a, b) = GCD(b, a mod b).
        private long Gcd(long a, long b)
        {
            while (b != 0)
            {
                // Calculate the remainder.
                long remainder = a % b;

                // Calculate GCD(b, remainder).
                a = b;
                b = remainder;
            }

            // GCD(a, 0) is a.
            return a;
        }

        // Return the number's factors.
        private List<int> PrimeFactors(int number)
        {
            List<int> factors = new List<int>();

            // Pull out factors of 2.
            while (number % 2 == 0)
            {
                factors.Add(2);
                number /= 2;
            }

            // Check odd numbers up to Sqrt(number).
            int maxFactor = (int)Math.Sqrt(number);
            int testFactor = 3;
            while (testFactor <= maxFactor)
            {
                while (number % testFactor == 0)
                {
                    factors.Add(testFactor);
                    number /= testFactor;
                }
                maxFactor = (int)Math.Sqrt(number);
                testFactor += 2;
            }

            // If there's anything left of the number, add it.
            if (number > 1) factors.Add(number);

            return factors;
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
