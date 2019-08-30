using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

using System.Diagnostics;

namespace RodCutting
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // Find optimal cuts.
        private void cutButton_Click(object sender, EventArgs e)
        {
            cutsTextBox.Clear();
            bestValueTextBox.Clear();
            Cursor = Cursors.WaitCursor;
            Refresh();

            // Read the values.
            string[] fields = valuesTextBox.Text.Split(' ');
            List<int> values = new List<int>();
            values.Add(0);      // For length 0.
            for (int i = 0; i < fields.Length; i++)
                values.Add(int.Parse(fields[i]));
            int length = int.Parse(rodLengthTextBox.Text);

            // Expand the values list up to values[length].
            for (int i = values.Count; i <= length; i++)
                values.Add(0);

            // Find the cuts.
            int bestValue;
            List<int> bestCuts;
            Stopwatch watch = new Stopwatch();
            watch.Start();
            FindOptimalCuts(length, values, out bestValue, out bestCuts);
            watch.Stop();

            // Display the cuts.
            cutsTextBox.Text = string.Join(" + ", bestCuts.ToArray());

            // Display the cut values.
            string cutValues = "";
            int totalValue = 0;
            foreach (int cut in bestCuts)
            {
                cutValues += $" + {values[cut]}";
                totalValue += values[cut];
            }
            cutValues = cutValues.Substring(3) + $" = {totalValue}";
            bestValueTextBox.Text = cutValues;

            Console.WriteLine(watch.Elapsed.TotalSeconds.ToString() + " seconds");
            Cursor = Cursors.Default;
        }

        // Find optimal cuts. Return the total value
        // and cuts through the output parameters.
        private void FindOptimalCuts(int length, List<int> values,
            out int bestValue, out List<int> bestCuts)
        {
            // Assume we make no cuts.
            bestValue = values[length];
            bestCuts = new List<int>();
            bestCuts.Add(length);

            // Try possible single cuts.
            for (int i = 1; i <= length / 2; i++)
            {
                // Try pieces with lengths i and length - i.
                int value1, value2;
                List<int> cuts1, cuts2;
                FindOptimalCuts(i, values, out value1, out cuts1);
                FindOptimalCuts(length - i, values, out value2, out cuts2);

                // See if this is an improvement.
                if (value1 + value2 > bestValue)
                {
                    bestValue = value1 + value2;
                    bestCuts = new List<int>(cuts1);
                    bestCuts.AddRange(cuts2);
                }
            }
        }
    }
}
