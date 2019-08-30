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

namespace PigeonholeSort
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // The items.
        private int[] Items;

        // The largest item in the array.
        private int MaxValue;

        // Make random items.
        private void generateButton_Click(object sender, EventArgs e)
        {
            itemsListBox.DataSource = null;
            int numItems = int.Parse(numItemsTextBox.Text);
            Items = new int[numItems];

            Random rand = new Random();
            MaxValue = int.Parse(maxItemTextBox.Text);
            for (int i = 0; i < numItems; i++) Items[i] = rand.Next(0, MaxValue + 1);

            itemsListBox.DataSource = Items.Take(1000).ToArray();
            sortButton.Enabled = true;
        }

        // Sort the items.
        private void sortButton_Click(object sender, EventArgs e)
        {
            itemsListBox.DataSource = null;

            // Sort.
            DateTime startTime = DateTime.Now;
            Pigeonholesort(Items, MaxValue);
            DateTime stopTime = DateTime.Now;
            TimeSpan elapsed = stopTime - startTime;
            Console.WriteLine(elapsed.TotalSeconds.ToString("0.00") + " seconds");

            // Validate the sort.
            for (int i = 1; i < Items.Length; i++)
                Debug.Assert(Items[i] >= Items[i - 1]);

            itemsListBox.DataSource = Items.Take(1000).ToArray();
        }

        // Use pigeonhole sort to sort the array.
        private void Pigeonholesort(int[] values, int max)
        {
            // Make the pigeonholes.
            Cell[] pigeonholes = new Cell[max + 1];

            // Initialize the linked lists.
            // (This is not necessary in C#.)
            //for (int i = 0; i < pigeonholes.Length; i++) pigeonholes[i] = null;

            // Move items into the pigeonholes.
            foreach (int value in values)
            {
                // Add this item to its pigeonhole.
                Cell cell = new Cell(value);
                cell.Next = pigeonholes[value];
                pigeonholes[value] = cell;
            }

            // Copy the items back into the values array.
            int index = 0;
            for (int i = 0; i < pigeonholes.Length; i++)
            {
                // Copy the items in pigeonhole i into the values array.
                for (Cell cell = pigeonholes[i];
                    cell != null;
                    cell = cell.Next)
                {
                    values[index] = cell.Value;
                    index++;
                }
            }
        }
    }
}
