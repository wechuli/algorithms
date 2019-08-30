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

namespace FindCliqueBruteForce
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

        // Find a clique of the desired size.
        private void findButton_Click(object sender, EventArgs e)
        {
            // Find the clique.
            int size = int.Parse(cliqueSizeTextBox.Text);
            List<Node> clique = FindClique(Nodes, size);

            // Color the clique.
            foreach (Node node in Nodes)
            {
                node.FgPen = Pens.Black;
                node.BgBrush = Brushes.White;
                node.TextBrush = Brushes.Black;
            }
            foreach (Node node in clique)
            {
                node.FgPen = Pens.Red;
                node.BgBrush = Brushes.Pink;
                node.TextBrush = Brushes.Red;
            }

            // Redraw.
            canvasPictureBox.Refresh();
        }

        // Find a clique of the given size.
        private List<Node> FindClique(List<Node> nodes, int size)
        {
            foreach (List<Node> combination in Combinations(nodes, size))
            {
                if (IsClique(combination)) return combination;
            }
            return new List<Node>();
        }

        // Return true if the nodes form a clique.
        private bool IsClique(List<Node> nodes)
        {
            int numNodes = nodes.Count;
            for (int i = 0; i < numNodes; i++)
            {
                for (int j = i + 1; j < numNodes; j++)
                {
                    if (!nodes[i].Neighbors.Contains(nodes[j]))
                        return false;
                }
            }
            return true;
        }

        // Generate combinations with the indicated number of nodes.
        private IEnumerable<List<Node>> Combinations(List<Node> nodes, int size)
        {
            bool[] isUsed = new bool[nodes.Count];
            List<Node> solution = new List<Node>();
            foreach (List<Node> combination in
                Combinations(nodes, isUsed, solution, 0, size))
            {
                yield return combination;
            }
        }
        private IEnumerable<List<Node>> Combinations(
            List<Node> nodes, bool[] isUsed, List<Node> solution,
            int nextAvailable, int numToAssign)
        {
            if (numToAssign == 0)
            {
                // Return the current combination.
                yield return solution;
            }
            else if (nodes.Count - nextAvailable < numToAssign)
            {
                // There aren't enough remaining items to use.
                yield break;
            }
            else
            {
                // Try using the remaining items.
                for (int i = nextAvailable; i < nodes.Count; i++)
                {
                    // Try using this item.
                    isUsed[i] = true;
                    solution.Add(nodes[i]);
                    foreach (List<Node> combination in
                        Combinations(nodes, isUsed, solution, i + 1, numToAssign - 1))
                    {
                        yield return combination;
                    }
                    solution.RemoveAt(solution.Count - 1);
                    isUsed[i] = false;
                }
            }
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
