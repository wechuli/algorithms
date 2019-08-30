using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

using System.Drawing.Drawing2D;
using System.Drawing.Text;

namespace LcaAllPairs
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // The tree's root.
        private TreeNode Root = null;

        // The current special nodes.
        private TreeNode Node1 = null;
        private TreeNode Node2 = null;
        private TreeNode LcaNode = null;

        // The tree's Euler tour.
        private List<TreeNode> EulerTour = null;
        private TreeNode[,] Lcas = null;

        // Make the tree.
        private void Form1_Load(object sender, EventArgs e)
        {
            Root = new TreeNode(null, 0);
            TreeNode node1 = new TreeNode(Root, 1);
            TreeNode node5 = new TreeNode(node1, 5);
            TreeNode node6 = new TreeNode(node1, 6);
            TreeNode node2 = new TreeNode(Root, 2);
            TreeNode node7 = new TreeNode(node2, 7);
            TreeNode node8 = new TreeNode(node2, 8);
            TreeNode node9 = new TreeNode(node2, 9);
            TreeNode node11 = new TreeNode(node7, 11);
            TreeNode node3 = new TreeNode(Root, 3);
            TreeNode node4 = new TreeNode(Root, 4);
            TreeNode node10 = new TreeNode(node4, 10);
            TreeNode node12 = new TreeNode(node10, 12);
            TreeNode node13 = new TreeNode(node10, 13);
            TreeNode node14 = new TreeNode(node10, 14);
            Root.ArrangeTree(5, 5);

            // Make the Euler tour.
            EulerTour = new List<TreeNode>();
            Root.AddToEulerTour(EulerTour);
            foreach (TreeNode node in EulerTour)
                Console.Write(node.Value + " ");

            // Make an array of the nodes.
            TreeNode[] nodes =
            {
                Root, node1, node2, node3, node4, node5, node6, node7,
                node8, node9, node10, node11, node12, node13, node14,
            };

            // Build the LCA array.
            // This assumes the nodes are numbered
            // starting with 0 and with no gaps.
            int numNodes = nodes.Length;
            Lcas = new TreeNode[numNodes, numNodes];
            for (int i = 0; i < numNodes; i++)
            {
                for (int j = i; j < numNodes; j++)
                {
                    Lcas[i, j] = Root.FindLca(EulerTour, nodes[i], nodes[j]);
                    Lcas[j, i] = Lcas[i, j];
                }
            }

            // Draw the tree.
            treePictureBox.Refresh();
        }

        // Draw the tree.
        private void treePictureBox_Paint(object sender, PaintEventArgs e)
        {
            if (Root == null) return;

            // Get ready.
            e.Graphics.Clear(treePictureBox.BackColor);
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;
            e.Graphics.TextRenderingHint = TextRenderingHint.AntiAliasGridFit;

            // Draw the tree.
            using (StringFormat sf = new StringFormat())
            {
                sf.Alignment = StringAlignment.Center;
                sf.LineAlignment = StringAlignment.Center;
                Root.DrawTree(e.Graphics, Brushes.Black, Pens.Black, this.Font, sf);
            }
        }

        // Select nodes.
        private void treePictureBox_MouseClick(object sender, MouseEventArgs e)
        {
            // Deselect the previous LCA.
            if (LcaNode != null)
            {
                LcaNode.BgBrush = Brushes.White;
                LcaNode = null;
            }

            // See which mouse button is pressed.
            if (e.Button == MouseButtons.Left)
            {
                // Deselect the current Node1.
                if (Node1 != null) Node1.BgBrush = Brushes.White;

                // Select a new Node1.
                Node1 = Root.NodeAtPosition(e.Location);
            }
            else
            {
                // Deselect the current Node2.
                if (Node2 != null) Node2.BgBrush = Brushes.White;

                // Select a new Node2.
                Node2 = Root.NodeAtPosition(e.Location);
            }

            // Color the selected nodes.
            if (Node1 != null) Node1.BgBrush = Brushes.LightGreen;
            if (Node2 != null) Node2.BgBrush = Brushes.LightBlue;

            // See if we have two nodes selected.
            if ((Node1 != null) && (Node2 != null))
            {
                // Find the LCA.
                LcaNode = Lcas[Node1.Value, Node2.Value];
                LcaNode.BgBrush = Brushes.Pink;
            }

            treePictureBox.Refresh();
        }
    }
}
