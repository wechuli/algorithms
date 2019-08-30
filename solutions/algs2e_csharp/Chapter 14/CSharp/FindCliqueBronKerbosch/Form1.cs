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

namespace FindCliqueBronKerbosch
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

        // Find maximal cliques.
        private void findButton_Click(object sender, EventArgs e)
        {
            cliqueListBox.Items.Clear();

            // Make the initial sets of nodes.
            HashSet<Node> R = new HashSet<Node>();
            HashSet<Node> P = new HashSet<Node>(Nodes);
            HashSet<Node> X = new HashSet<Node>();

            // Find the cliques.
            List<HashSet<Node>> cliques = BronKerbosch(R, P, X);

            // List the cliques.
            foreach (HashSet<Node> clique in cliques)
            {
                string txt = "";
                foreach (Node node in clique)
                    txt += $"{node} ";
                cliqueListBox.Items.Add(txt);
            }
        }

        // Return a string holding the items in the set."""
        private string PrintSet(HashSet<Node> set)
        {
            if (set.Count == 0) return "{ }";

            string txt = "";
            foreach (Node node in set) txt += $", {node}";
            return "{" + txt.Substring(2) + "}";
        }

        // Find maximal cliques for these sets.
        private List<HashSet<Node>> BronKerbosch(
            HashSet<Node> R, HashSet<Node> P, HashSet<Node> X)
        {
            //@ Console.WriteLine($"BK - R: {PrintSet(R)}, P: {PrintSet(P)}, X: {PrintSet(X)}");
            List<HashSet<Node>> results = new List<HashSet<Node>>();

            // See if P and X are both empty.
            if ((P.Count == 0) && (X.Count == 0))
            {
                // R is a maximal clique.
                results.Add(CopyHashset(R));
                //@ Console.WriteLine($"Maximal: {PrintSet(R)}");
            }

            foreach (Node node in CopyHashset(P))
            {
                // Make the recursive call.
                HashSet<Node> newR = CopyHashset(R);
                newR.Add(node);
                HashSet<Node> newP = Neighbors(node, P);
                HashSet<Node> newX = Neighbors(node, X);
                results.AddRange(BronKerbosch(newR, newP, newX));

                // Update P and X.
                P.Remove(node);
                X.Add(node);
            }

            return results;
        }

        // Return the neighbors of this node that are within the set.
        private HashSet<Node> Neighbors(Node node, HashSet<Node> set)
        {
            HashSet<Node> result = new HashSet<Node>();
            foreach (Node neighbor in node.Neighbors)
                if (set.Contains(neighbor)) result.Add(neighbor);
            return result;
        }

        // Return a copy of a HashSet.
        private HashSet<T> CopyHashset<T>(HashSet<T> set)
        {
            return new HashSet<T>(set);
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
