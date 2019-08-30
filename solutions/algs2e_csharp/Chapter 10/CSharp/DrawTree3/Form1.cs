#define COLOR

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

namespace DrawTree3
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // The tree's root.
        NAryNode Root;

        // Build a tree.
        private void Form1_Load(object sender, EventArgs e)
        {
            // Build the tree.
            Root = new NAryNode("E");
            NAryNode nodeA = new NAryNode("A");
            NAryNode nodeB = new NAryNode("B");
            NAryNode nodeC = new NAryNode("C");
            NAryNode nodeD = new NAryNode("D");
            NAryNode nodeF = new NAryNode("F");
            NAryNode nodeG = new NAryNode("G");
            NAryNode nodeH = new NAryNode("H");
            NAryNode nodeI = new NAryNode("I");
            NAryNode nodeJ = new NAryNode("J");
            NAryNode nodeK = new NAryNode("K");
            NAryNode nodeL = new NAryNode("L");
            NAryNode nodeM = new NAryNode("M");
            Root.Children.Add(nodeB);
            Root.Children.Add(nodeF);
            nodeB.Children.Add(nodeA);
            nodeB.Children.Add(nodeD);
            nodeD.Children.Add(nodeC);
            nodeF.Children.Add(nodeI);
            nodeI.Children.Add(nodeG);
            nodeI.Children.Add(nodeJ);
            nodeG.Children.Add(nodeH);
            nodeI.Children.Add(nodeK);
            nodeK.Children.Add(nodeL);
            nodeK.Children.Add(nodeM);
        }

        // Draw the tree.
        private void treePictureBox_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.Clear(Color.White);
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;

            // Position the tree.
            Root.PositionSubtree(10, 10);

#if COLOR
            // Draw the links.
            Root.DrawSubtreeLinks(e.Graphics, Pens.Blue);

            // Draw the nodes.
            Root.DrawSubtreeNodes(e.Graphics, this.Font,
                Brushes.Blue, Brushes.LightBlue, Pens.Blue);
#else
            // Draw the links.
            Root.DrawSubtreeLinks(e.Graphics, Pens.Black);

            // Draw the nodes.
            Root.DrawSubtreeNodes(e.Graphics, this.Font,
                Brushes.Black, Brushes.LightGray, Pens.Black);
#endif
        }
    }
}
