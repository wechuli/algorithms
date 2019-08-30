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

namespace SelfOrganizingLists
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private Random Rand = new Random();
        private int NumValues;

        // Prepare the lists and run the searches.
        private void goButton_Click(object sender, EventArgs e)
        {
            Cursor = Cursors.WaitCursor;
            noneNumStepsTextBox.Clear();
            noneAveStepsTextBox.Clear();
            noneExpectedStepsTextBox.Clear();
            mtfNumStepsTextBox.Clear();
            mtfAveStepsTextBox.Clear();
            mtfExpectedStepsTextBox.Clear();
            swapNumStepsTextBox.Clear();
            swapAveStepsTextBox.Clear();
            swapExpectedStepsTextBox.Clear();
            countNumStepsTextBox.Clear();
            countAveStepsTextBox.Clear();
            countExpectedStepsTextBox.Clear();
            Refresh();

            // Build the probabilities.
            NumValues = int.Parse(numValuesTextBox.Text);
            double[] probs;
            if (equalRadioButton.Checked)
                probs = EqualProbs(NumValues);
            else if (linearRadioButton.Checked)
                probs = LinearProbs(NumValues);
            else
                probs = QuadraticProbs(NumValues);
            double total = probs.Sum();
            Debug.Assert(Math.Abs(total - 1.0) < 0.001,
                "Probabilities do not add up to 1.0");

            // Build the lists.
            OrganizingList noneList = new OrganizingList();
            MtfList mtfList = new MtfList();
            SwapList swapList = new SwapList();
            CountList countList = new CountList();
            for (int i = NumValues - 1; i >= 0; i--)
            {
                noneList.Add(i);
                mtfList.Add(i);
                swapList.Add(i);
                countList.Add(i);
            }

            // Perform the searches.
            int noneSteps = 0;
            int mtfSteps = 0;
            int swapSteps = 0;
            int countSteps = 0;
            int numSearches = int.Parse(numSearchesTextBox.Text);
            for (int i = 0; i < numSearches; i++)
            {
                int value = PickValue(probs);
                noneSteps += noneList.Find(value);
                mtfSteps += mtfList.Find(value);
                swapSteps += swapList.Find(value);
                countSteps += countList.Find(value);
            }

            // Display the results.
            noneNumStepsTextBox.Text = noneSteps.ToString();
            noneAveStepsTextBox.Text = $"{noneSteps / (float)numSearches:0.00}";
            noneExpectedStepsTextBox.Text =
                noneList.ExpectedSearch(probs).ToString("0.00");

            mtfNumStepsTextBox.Text = mtfSteps.ToString();
            mtfAveStepsTextBox.Text = $"{mtfSteps / (float)numSearches:0.00}";
            mtfExpectedStepsTextBox.Text =
                mtfList.ExpectedSearch(probs).ToString("0.00");

            swapNumStepsTextBox.Text = swapSteps.ToString();
            swapAveStepsTextBox.Text = $"{swapSteps / (float)numSearches:0.00}";
            swapExpectedStepsTextBox.Text =
                swapList.ExpectedSearch(probs).ToString("0.00");

            countNumStepsTextBox.Text = countSteps.ToString();
            countAveStepsTextBox.Text = $"{countSteps / (float)numSearches:0.00}";
            countExpectedStepsTextBox.Text =
                countList.ExpectedSearch(probs).ToString("0.00");

            Cursor = Cursors.Default;
        }

        // Make an array of equal probabilities.
        private double[] EqualProbs(int num)
        {
            double prob = 1.0 / num;
            double[] probs = new double[num];
            for (int i = 0; i < num; i++) probs[i] = prob;
            return probs;
        }

        // Make an array containing linearly increasing probabilities.
        private double[] LinearProbs(int num)
        {
            double[] probs = new double[num];
            double total = num * (num - 1) / 2.0;
            for (int i = 0; i < num; i++) probs[i] = i / total;
            return probs;
        }

        // Make an array containing quadratically increasing probabilities.
        private double[] QuadraticProbs(int num)
        {
            double[] probs = new double[num];
            double total = (num - 1) * num * (2 * (num - 1) + 1) / 6.0;
            for (int i = 0; i < num; i++) probs[i] = i * i / total;
            return probs;
        }

        // Pick a value with the given probabilities.
        private int PickValue(double[] probs)
        {
            double prob = Rand.NextDouble();
            for (int i = 0; i < NumValues; i++)
            {
                prob -= probs[i];
                if (prob <= 0) return i;
            }
            Debug.Assert(false, "Error picking a random value.");
            return -1;
        }
    }
}
