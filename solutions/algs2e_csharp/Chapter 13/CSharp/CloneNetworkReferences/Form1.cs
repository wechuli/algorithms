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

namespace CloneNetworkReferences
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private Node[] Nodes1, Nodes2;

        // Build the first network.
        private void Form1_Load(object sender, EventArgs e)
        {
            Node nodeA = new Node("A", new Point(40, 80), Brushes.LightBlue, Brushes.Black, Pens.Blue, pictureBox1.Font, Brushes.Blue, Pens.Blue);
            Node nodeB = new Node("B", new Point(120, 30), Brushes.LightBlue, Brushes.Black, Pens.Blue, pictureBox1.Font, Brushes.Blue, Pens.Blue);
            Node nodeC = new Node("C", new Point(230, 75), Brushes.LightBlue, Brushes.Black, Pens.Blue, pictureBox1.Font, Brushes.Blue, Pens.Blue);
            Node nodeD = new Node("D", new Point(180, 140), Brushes.LightBlue, Brushes.Black, Pens.Blue, pictureBox1.Font, Brushes.Blue, Pens.Blue);
            Node nodeE = new Node("E", new Point(230, 190), Brushes.LightBlue, Brushes.Black, Pens.Blue, pictureBox1.Font, Brushes.Blue, Pens.Blue);
            Node nodeF = new Node("F", new Point(160, 225), Brushes.LightBlue, Brushes.Black, Pens.Blue, pictureBox1.Font, Brushes.Blue, Pens.Blue);
            Node nodeG = new Node("G", new Point(120, 120), Brushes.LightBlue, Brushes.Black, Pens.Blue, pictureBox1.Font, Brushes.Blue, Pens.Blue);
            Node nodeH = new Node("H", new Point(60, 215), Brushes.LightBlue, Brushes.Black, Pens.Blue, pictureBox1.Font, Brushes.Blue, Pens.Blue);
            Node nodeI = new Node("I", new Point(25, 145), Brushes.LightBlue, Brushes.Black, Pens.Blue, pictureBox1.Font, Brushes.Blue, Pens.Blue);
            nodeA.Neighbors.Add(nodeB);
            nodeA.Neighbors.Add(nodeG);
            nodeB.Neighbors.Add(nodeC);
            nodeC.Neighbors.Add(nodeG);
            nodeC.Neighbors.Add(nodeD);
            nodeG.Neighbors.Add(nodeA);
            nodeG.Neighbors.Add(nodeF);
            nodeA.Neighbors.Add(nodeB);
            nodeD.Neighbors.Add(nodeE);
            nodeE.Neighbors.Add(nodeD);
            nodeE.Neighbors.Add(nodeF);
            nodeH.Neighbors.Add(nodeI);
            Nodes1 = new Node[]
                { nodeA, nodeB, nodeC, nodeD, nodeE, nodeF, nodeG, nodeH, nodeI };

            // Clone the network.
            Nodes2 = CloneNetwork(Nodes1);
        }

        // Draw the original network.
        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
            DrawNetwork(e.Graphics, pictureBox1.BackColor, Nodes1);
        }

        // Draw the cloned network.
        private void pictureBox2_Paint(object sender, PaintEventArgs e)
        {
            DrawNetwork(e.Graphics, pictureBox2.BackColor, Nodes2);
        }

        // Draw a network on a Graphics object.
        private void DrawNetwork(Graphics gr, Color clearColor, Node[] nodes)
        {
            if (nodes == null) return;
            gr.Clear(clearColor);
            gr.SmoothingMode = SmoothingMode.AntiAlias;

            foreach (Node node in nodes) node.DrawLinks(gr);
            foreach (Node node in nodes) node.DrawNode(gr);
        }

        // Clone a network.
        private Node[] CloneNetwork(Node[] nodes)
        {
            // Clone the nodes.
            Node[] newNodes = new Node[nodes.Length];
            for (int i = 0; i < nodes.Length; i++)
            {
                Node oldNode = nodes[i];
                Node newNode = new Node(oldNode.Name.ToLower(),
                    oldNode.Location, Brushes.Pink, Brushes.Black,
                    Pens.Red, pictureBox2.Font, Brushes.Red, Pens.Red);
                newNodes[i] = newNode;
                oldNode.ClonedNode = newNode;
            }

            // Clone the links.
            for (int i = 0; i < nodes.Length; i++)
            {
                Node oldNode = nodes[i];
                Node newNode = newNodes[i];
                foreach (Node neighbor in oldNode.Neighbors)
                {
                    Node newNeighbor = neighbor.ClonedNode;
                    newNode.Neighbors.Add(newNeighbor);
                }
            }

            return newNodes;
        }
    }
}
