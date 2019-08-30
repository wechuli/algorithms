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

namespace BinomialHeap
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // The main heap.
        private BinomialHeap TheHeap = new BinomialHeap();

        // Display the heap.
        private void ShowHeap()
        {
            heapTreeView.Nodes.Clear();
            TheHeap.AddToTreeView(heapTreeView.Nodes);
            heapTreeView.ExpandAll();
        }

        // Add random values to the heap.
        private void addValuesButton_Click(object sender, EventArgs e)
        {
            try
            {
                int min = int.Parse(minTextBox.Text);
                int max = int.Parse(maxTextBox.Text);
                int numValues = int.Parse(numValuesTextBox.Text);

                Random rand = new Random();
                for (int i = 0; i < numValues; i++)
                {
                    TheHeap.Enqueue(rand.Next(min, max + 1));
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }

            ShowHeap();
        }

        // Add a value to the heap.
        private void enqueueButton_Click(object sender, EventArgs e)
        {
            try
            {
                int value = int.Parse(valueTextBox.Text);
                TheHeap.Enqueue(value);
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
            valueTextBox.Clear();
            valueTextBox.Focus();
            ShowHeap();
        }

        // Remove the smallest value from the heap.
        private void dequeueButton_Click(object sender, EventArgs e)
        {
            try
            {
                valueTextBox.Text = TheHeap.Dequeue().ToString();
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
            ShowHeap();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            // RunTest1();
            // RunTest2();
            // RunTest3();
        }

        // Run some tests.
        private void RunTest1()
        {
            // Make heap 1.
            BinomialHeap heap1 = new BinomialHeap();
            BinomialNode node12 = new BinomialNode(12);
            BinomialNode node7 = new BinomialNode(7);
            BinomialNode node25 = new BinomialNode(25);
            BinomialNode node15 = new BinomialNode(15);
            BinomialNode node28 = new BinomialNode(28);
            BinomialNode node33 = new BinomialNode(33);
            BinomialNode node41 = new BinomialNode(41);

            node28.InsertChild(node41);
            node15.InsertChild(node33);
            node15.InsertChild(node28);
            heap1.AddRoot(node15);

            node7.InsertChild(node25);
            heap1.AddRoot(node7);

            heap1.AddRoot(node12);

            // Make heap 2.
            BinomialHeap heap2 = new BinomialHeap();
            BinomialNode node18 = new BinomialNode(18);
            BinomialNode node3 = new BinomialNode(3);
            BinomialNode node37 = new BinomialNode(37);
            BinomialNode node6 = new BinomialNode(6);
            BinomialNode node8 = new BinomialNode(8);
            BinomialNode node29 = new BinomialNode(29);
            BinomialNode node10 = new BinomialNode(10);
            BinomialNode node44 = new BinomialNode(44);
            BinomialNode node30 = new BinomialNode(30);
            BinomialNode node23 = new BinomialNode(23);
            BinomialNode node22 = new BinomialNode(22);
            BinomialNode node48 = new BinomialNode(48);
            BinomialNode node31 = new BinomialNode(31);
            BinomialNode node17 = new BinomialNode(17);
            BinomialNode node45 = new BinomialNode(45);
            BinomialNode node32 = new BinomialNode(32);
            BinomialNode node24 = new BinomialNode(24);
            BinomialNode node50 = new BinomialNode(50);
            BinomialNode node55 = new BinomialNode(55);

            node3.InsertChild(node37);
            node45.InsertChild(node55);
            node30.InsertChild(node32);
            node30.InsertChild(node45);
            node23.InsertChild(node24);
            node8.InsertChild(node22);
            node8.InsertChild(node23);
            node8.InsertChild(node30);
            node48.InsertChild(node50);
            node29.InsertChild(node31);
            node29.InsertChild(node48);
            node10.InsertChild(node17);
            node6.InsertChild(node44);
            node6.InsertChild(node10);
            node6.InsertChild(node29);
            node6.InsertChild(node8);
            heap2.AddRoot(node6);
            heap2.AddRoot(node3);
            heap2.AddRoot(node18);

            node12.SetOrder();
            node7.SetOrder();
            node15.SetOrder();
            node18.SetOrder();
            node3.SetOrder();
            node6.SetOrder();

            heapTreeView.Nodes.Clear();
            heap1.AddToTreeView(heapTreeView.Nodes);
            heap2.AddToTreeView(heapTreeView.Nodes);

            //BinomialNode merged = BinomialHeap.MergeRootLists(heap1, heap2);

            //BinomialHeap mergedHeap = BinomialHeap.MergeHeaps(heap1, heap2);
            //TreeNode mergedNode = heapTreeView.Nodes.Add("Merged");
            //mergedHeap.AddToTreeView(mergedNode.Nodes);

            //heap1.MergeWithHeap(heap2);
            //TreeNode mergedNode = heapTreeView.Nodes.Add("Merged");
            //heap1.AddToTreeView(mergedNode.Nodes);

            heap2.MergeWithHeap(heap1);
            TreeNode mergedNode = heapTreeView.Nodes.Add("Merged");
            heap2.AddToTreeView(mergedNode.Nodes);


            heapTreeView.ExpandAll();
        }

        // Run some tests.
        private void RunTest2()
        {
            const int numTrials = 99;
            const int numItems = 99;
            for (int trial = 0; trial < numTrials; trial++)
            {
                // Randomize the values 0 through numItems.
                List<int> values =
                    new List<int>(Enumerable.Range(0, numItems));
                values.Randomize();

                // Add the items to the heap.
                foreach (int value in values)
                    TheHeap.Enqueue(value);

                // Display the first trial's structure.
                if (trial == 0) ShowHeap();

                // Pull them off in order.
                for (int i = 0; i < numItems; i++)
                {
                    int value = TheHeap.Dequeue();
                    Debug.Assert(value == i,
                        $"Dequeued value is {value} but should be {i}.");
                }
            }
            MessageBox.Show("Done");
        }

        // Run some tests.
        private void RunTest3()
        {
            // Make heap 1.
            BinomialHeap heap1 = new BinomialHeap();
            heap1.Enqueue(28);
            heap1.Enqueue(58);
            heap1.Enqueue(24);
            heap1.Enqueue(56);
            heap1.Enqueue(76);
            heap1.Enqueue(48);
            heap1.Enqueue(15);

            // Make heap 2.
            BinomialHeap heap2 = new BinomialHeap();
            heap2.Enqueue(93);
            heap2.Enqueue(16);
            heap2.Enqueue(78);
            heap2.Enqueue(74);
            heap2.Enqueue(83);
            heap2.Enqueue(63);

            heapTreeView.Nodes.Clear();
            heap1.AddToTreeView(heapTreeView.Nodes);
            heap2.AddToTreeView(heapTreeView.Nodes);

            heap1.MergeWithHeap(heap2);
            TreeNode mergedNode = heapTreeView.Nodes.Add("Merged");
            heap1.AddToTreeView(mergedNode.Nodes);


            TheHeap = heap1;
            ShowHeap();

            heapTreeView.ExpandAll();
        }
    }
}
