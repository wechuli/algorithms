using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace MajorityVoting
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // Find the majority outcome.
        private void findMajorityButton_Click(object sender, EventArgs e)
        {
            stepsListBox.Items.Clear();

            // Break the outcome list into elements.
            string[] separators = { " " };
            string[] outcomes = outcomesTextBox.Text.Split(
                separators, StringSplitOptions.RemoveEmptyEntries);

            // Perform the Boyer-Moore algorithm.
            string majority = "";
            int counter = 0;
            foreach (string outcome in outcomes)
            {
                if (counter == 0)
                {
                    majority = outcome;
                    counter = 1;
                }
                else if (outcome == majority)
                    counter++;
                else
                    counter--;

                // Display the current step.
                stepsListBox.Items.Add($"{outcome}: {majority} {counter}");
            }

            // Display the result.
            majorityTextBox.Text = majority;
        }
    }
}
