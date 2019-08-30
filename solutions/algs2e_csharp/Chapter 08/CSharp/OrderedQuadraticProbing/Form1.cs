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

namespace OrderedQuadraticProbing
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // The hash table.
        MyHashTable Table = null;

        // Used to make random values.
        Random Rand = new Random();

        // Value properties.
        private int MinValue = 0;
        private int MaxValue = 0;

        // The special value marking empty spots.
        private const int Empty = int.MinValue;

        // Make the hash table.
        private void createButton_Click(object sender, EventArgs e)
        {
            try
            {
                int tableSize = int.Parse(sizeTextBox.Text);
                Table = new MyHashTable(tableSize);

                ShowStatistics();
                AcceptButton = makeItemsButton;
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }

        // Make some items.
        private void makeItemsButton_Click(object sender, EventArgs e)
        {
            try
            {
                int numItems = int.Parse(numItemsTextBox.Text);
                MinValue = int.Parse(minTextBox.Text);
                MaxValue = int.Parse(maxTextBox.Text);
                int itemsAdded = 0;
                while (itemsAdded < numItems)
                {
                    try
                    {
                        int key = Rand.Next(MinValue, MaxValue + 1);
                        string value = $"v{key:D3}";
                        int numProbes;
                        Table.Add(key, value, out numProbes);
                        itemsAdded++;
                    }
                    catch (ArgumentException ex)
                    {
                        if (!ex.Message.Contains("is already in the hash table at index"))
                            // unknown error.
                            MessageBox.Show(ex.Message);

                        // Duplicate value. Try again.
                    }
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }

            ShowStatistics();
        }

        private void insertButton_Click(object sender, EventArgs e)
        {
            try
            {
                int key = int.Parse(itemTextBox.Text);
                string value = $"v{key:D3}";
                int numProbes;
                Table.Add(key, value, out numProbes);
                MessageBox.Show($"Added key {key} in {numProbes} probes");

                ShowStatistics();
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }

        // Find the indicated item.
        private void findButton_Click(object sender, EventArgs e)
        {
            try
            {
                int key = int.Parse(itemTextBox.Text);
                int numProbes;
                DataItem item = Table.Find(key, out numProbes);
                if (item == null)
                    MessageBox.Show($"Did not find key {key} in {numProbes} probes");
                else
                    MessageBox.Show($"Found {item} in {numProbes} probes");
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }

        // Display the table's contents and statistics.
        private void ShowStatistics()
        {
            // Display the items in the table.
            tableTextBox.Text = Table.ToString();
            tableTextBox.Select(0, 0);

            // Fill percentage.
            fillPercentTextBox.Text =
                $"{Table.FillPercentage():0.00}";

            // Probe sequence lengths.
            float aveLength;
            int maxLength;
            Table.GetSequenceLengths(MinValue, MaxValue, out aveLength, out maxLength);
            longestTextBox.Text = maxLength.ToString();
            averageTextBox.Text = aveLength.ToString("0.00");
        }

        // Rehash the values in a random order.
        private void rehashButton_Click(object sender, EventArgs e)
        {
            // Get the values in the table.
            List<DataItem> valueList = Table.Items();

            // Randomize the values.
            DataItem[] values = valueList.ToArray();
            Randomize(values);

            // Make a new table.
            Table = new MyHashTable(Table.NumEntries);

            // Rehash the values.
            foreach (DataItem item in values)
            {
                int numProbes;
                Table.Add(item.Key, item.Value, out numProbes);
            }

            // Display the result.
            ShowStatistics();
            MessageBox.Show("Done", "Rehash");
        }

        // Randomize an array.
        public void Randomize<T>(T[] items)
        {
            Random rand = new Random();

            // For each spot in the array, pick
            // a random item to swap into that spot.
            for (int i = 0; i < items.Length - 1; i++)
            {
                int j = rand.Next(i, items.Length);
                T temp = items[i];
                items[i] = items[j];
                items[j] = temp;
            }
        }

        // Verify that FindItem can find every item in the
        // table and no items that are not in the table.
        private void verifyButton_Click(object sender, EventArgs e)
        {
            // Get the values in the table.
            List<DataItem> valueList = Table.Items();

            for (int key = MinValue; key <= MaxValue; key++)
            {
                int numProbes;
                DataItem item = Table.Find(key, out numProbes);

                Debug.Assert((item != null) == (Table.ScanTable(key)));
            }
            MessageBox.Show("OK", "Verify");
        }
    }
}
