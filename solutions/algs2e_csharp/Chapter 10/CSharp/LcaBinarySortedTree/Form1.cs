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

namespace LcaBinarySortedTree
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

        // Make the tree.
        private void buildTreeButton_Click(object sender, EventArgs e)
        {
            int height = int.Parse(heightTextBox.Text);
            Root = TreeNode.BuildFullTree(height, new Point(5, 5));
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
                LcaNode = Root.FindLca(Node1.Value, Node2.Value);
                LcaNode.BgBrush = Brushes.Pink;
            }

            treePictureBox.Refresh();
        }
    }
}
