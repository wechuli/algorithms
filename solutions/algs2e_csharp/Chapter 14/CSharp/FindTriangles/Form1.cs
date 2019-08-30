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

// Search for //@ to find statements that print
// information about the calls to the algorithm.

namespace FindTriangles
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private List<Node> Nodes = new List<Node>();

        // Build the network.
        private void Form1_Load(object sender, EventArgs e)
        {
            Node nodeA = new Node("A", new Point(60, 20), Font);
            Node nodeB = new Node("B", new Point(200, 20), Font);
            Node nodeC = new Node("C", new Point(130, 70), Font);
            Node nodeD = new Node("D", new Point(90, 110), Font);
            Node nodeE = new Node("E", new Point(170, 110), Font);
            Node nodeF = new Node("F", new Point(40, 170), Font);
            Node nodeG = new Node("G", new Point(220, 170), Font);

            nodeA.AddLink(nodeB);
            nodeA.AddLink(nodeC);
            nodeA.AddLink(nodeD);
            nodeA.AddLink(nodeF);

            nodeB.AddLink(nodeC);
            nodeB.AddLink(nodeE);
            nodeB.AddLink(nodeG);

            nodeC.AddLink(nodeD);
            nodeC.AddLink(nodeE);

            nodeD.AddLink(nodeE);
            nodeD.AddLink(nodeF);
            nodeD.AddLink(nodeG);

            nodeE.AddLink(nodeF);
            nodeE.AddLink(nodeG);

            nodeF.AddLink(nodeG);

            Nodes = new List<Node>
                { nodeA, nodeB, nodeC, nodeD, nodeE, nodeF, nodeG };
        }

        // Find triangles.
        private void findButton_Click(object sender, EventArgs e)
        {
            trianglesListBox.Items.Clear();

            // Find the triangles.
            List<Node[]> triangles = FindAllTriangles();

            // List the triangles.
            foreach (Node[] triangle in triangles)
            {
                string txt = $"{triangle[0]} {triangle[1]} {triangle[2]}";
                trianglesListBox.Items.Add(txt);
            }
            Console.WriteLine($"Found {triangles.Count} triangles");
        }

        // Find the network's triangles.
        private List<Node[]> FindAllTriangles()
        {
            List<Node[]> results = new List<Node[]>();

            // Iterate over the nodes.
            foreach (Node node in Nodes)
            {
                // Mark the node's neighbors.
                MarkNeighbors(node, true);

                // Check each neighbor to see if it forms a
                // triangle with this node.
                foreach (Node nbr in node.Neighbors)
                {
                    if (nbr.Name.CompareTo(node.Name) <= 0) continue;
                    
                    foreach (Node nbrNbr in nbr.Neighbors)
                    {
                        if (nbrNbr.Name.CompareTo(node.Name) <= 0) continue;
                        if (nbrNbr.Name.CompareTo(nbr.Name) <= 0) continue;
                        if (nbrNbr.Marked)
                        {
                            results.Add(new Node[]
                                {node, nbr, nbrNbr});
                        }
                    }
                }

                // Unark the node's neighbors.
                MarkNeighbors(node, false);
            }

            return results;
        }

        // Mark this node's neighbors.
        private void MarkNeighbors(Node node, bool marked)
        {
            foreach (Node neighbor in node.Neighbors)
                neighbor.Marked = marked;
        }

        // Draw the network.
        private void canvasPictureBox_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.Clear(canvasPictureBox.BackColor);
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;

            foreach (Node node in Nodes) node.DrawLinks(e.Graphics);
            foreach (Node node in Nodes) node.DrawNode(e.Graphics);
        }
    }
}
