﻿using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

using System.Diagnostics;

namespace FibonacciNumbers
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void calculateButton_Click(object sender, EventArgs e)
        {
            long n = int.Parse(nTextBox.Text);
            Stopwatch watch = new Stopwatch();
            watch.Start();
            long result = Fibonacci(n);
            watch.Stop();
            resultTextBox.Text = result.ToString();
            Console.WriteLine($"{watch.Elapsed.TotalSeconds.ToString("0.00")} seconds");
        }

        // Return the n-th Fibonacci number.
        private long Fibonacci(long n)
        {
            if (n <= 1) return n;
            return Fibonacci(n - 1) + Fibonacci(n - 2);
        }
    }
}
