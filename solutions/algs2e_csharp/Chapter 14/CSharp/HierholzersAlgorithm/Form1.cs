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

namespace HierholzersAlgorithm
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
            Nodes = MakeNetwork1();
            Nodes = MakeNetwork2();
        }

        // Build a network.
        private List<Node> MakeNetwork1()
        {
            Node nodeA = new Node("A", new Point(20, 20), Font);
            Node nodeB = new Node("B", new Point(140, 20), Font);
            Node nodeC = new Node("C", new Point(80, 50), Font);
            Node nodeD = new Node("D", new Point(50, 80), Font);
            Node nodeE = new Node("E", new Point(110, 80), Font);
            Node nodeF = new Node("F", new Point(80, 110), Font);
            Node nodeG = new Node("G", new Point(20, 140), Font);
            Node nodeH = new Node("H", new Point(140, 140), Font);

            nodeA.AddLink(nodeB);
            nodeA.AddLink(nodeC);
            nodeA.AddLink(nodeD);
            nodeA.AddLink(nodeG);

            nodeB.AddLink(nodeC);
            nodeB.AddLink(nodeE);
            nodeB.AddLink(nodeH);

            nodeC.AddLink(nodeD);
            nodeC.AddLink(nodeE);

            nodeD.AddLink(nodeF);
            nodeD.AddLink(nodeG);

            nodeE.AddLink(nodeF);
            nodeE.AddLink(nodeH);

            nodeF.AddLink(nodeG);
            nodeF.AddLink(nodeH);

            nodeG.AddLink(nodeH);

            return new List<Node>
                { nodeA, nodeB, nodeC, nodeD, nodeE, nodeF, nodeG, nodeH };
        }

        // Build a network.
        private List<Node> MakeNetwork2()
        {
            Node nodeA = new Node("A", new Point(100, 20), Font);
            Node nodeB = new Node("B", new Point(100, 50), Font);
            Node nodeC = new Node("C", new Point(70, 80), Font);
            Node nodeD = new Node("D", new Point(130, 80), Font);
            Node nodeE = new Node("E", new Point(40, 110), Font);
            Node nodeF = new Node("F", new Point(100, 110), Font);
            Node nodeG = new Node("G", new Point(160, 110), Font);
            Node nodeH = new Node("H", new Point(70, 140), Font);
            Node nodeI = new Node("I", new Point(130, 140), Font);
            Node nodeJ = new Node("J", new Point(100, 170), Font);
            Node nodeK = new Node("K", new Point(100, 200), Font);

            nodeA.AddLink(nodeC);
            nodeA.AddLink(nodeD);

            nodeB.AddLink(nodeC);
            nodeB.AddLink(nodeD);

            nodeC.AddLink(nodeE);
            nodeC.AddLink(nodeF);

            nodeD.AddLink(nodeF);
            nodeD.AddLink(nodeG);

            nodeE.AddLink(nodeH);

            nodeF.AddLink(nodeH);
            nodeF.AddLink(nodeI);

            nodeG.AddLink(nodeI);

            nodeH.AddLink(nodeJ);
            nodeH.AddLink(nodeK);

            nodeI.AddLink(nodeJ);
            nodeI.AddLink(nodeK);

            return new List<Node>
                { nodeA, nodeB, nodeC, nodeD, nodeE, nodeF, nodeG, nodeH, nodeI, nodeJ, nodeK };
        }

        // Find an Eulerian cycle.
        private void findButton_Click(object sender, EventArgs e)
        {
            // Find an Eulerian cycle.
            List<Node> cycle = FindEulerianCycle(Nodes);

            // Show the nodes in the cycle.
            cycleTextBox.Text = string.Join(" ", cycle);

            // Validate the cycle. If a node has N neighbors,
            // then it should be visited N / 2 times.
            // Except for the start node,
            // which is visited an extra time.
            foreach (Node node in Nodes) node.TimesVisited = 0;
            for (int i = 0; i < cycle.Count; i++)
                Nodes[cycle[i].Index].TimesVisited++;
            foreach (Node node in Nodes)
                Console.WriteLine($"{node}: Visited {node.TimesVisited} times");
        }

        // Find an Eulerian cycle in the network.
        private List<Node> FindEulerianCycle(List<Node> nodes)
        {
            // Make a copy of the network and work with the copy.
            List<Node> copyNodes = CloneNetwork(nodes);

            // Set the node indices.
            for (int i = 0; i < nodes.Count; i++)
            {
                nodes[i].Index = i;
                copyNodes[i].Index = i;
            }

            // Start with a cycle that only includes the first node.
            List<Node> copyCycle = new List<Node>();
            copyCycle.Add(copyNodes[0]);

            // Repeat until all links have been removed.
            for (;;)
            {
                // Find a node in the cycle that has unvisited links.
                int startIndex = -1;
                for (int i = 0; i < copyCycle.Count; i++)
                {
                    if (copyCycle[i].Neighbors.Count > 0)
                    {
                        startIndex = i;
                        break;
                    }
                }

                // If there is no node with unvisited links, then we're done.
                if (startIndex < 0) break;

                // Make a loop starting at this node.
                Node startNode = copyCycle[startIndex];
                List<Node> newCycle = FindLoop(startNode);

                Console.WriteLine($"Old: {string.Join(" ", copyCycle)}");
                Console.WriteLine($"New: {string.Join(" ", newCycle)}");

                // Insert the new cycle before the node in the main loop.
                copyCycle.InsertRange(startIndex, newCycle);
                Console.WriteLine($"Res: {string.Join(" ", copyCycle)}\n");
            }

            // Convert the cycle in the copied network
            // into a cycle in the original network.
            List<Node> cycle = new List<Node>();
            for (int i = 0; i < copyCycle.Count; i++)
                cycle.Add(nodes[copyCycle[i].Index]);

            return cycle;
        }

        // Find a loop starting at the indicated node.
        private List<Node> FindLoop(Node startNode)
        {
            List<Node> cycle = new List<Node>();
            Node currentNode = startNode;

            do
            {
                cycle.Add(currentNode);

                // Move to a neighboring node.
                Node nextNode = currentNode.Neighbors[0];
                currentNode.Neighbors.RemoveAt(0);
                nextNode.Neighbors.Remove(currentNode);
                currentNode = nextNode;
            } while (currentNode != startNode);

            return cycle;
        }

        // Clone a network.
        private List<Node> CloneNetwork(List<Node> nodes)
        {
            // Make a dictionary to hold the new nodes.
            Dictionary<Node, Node> nodeDict =
                new Dictionary<Node, Node>();

            // Clone the nodes.
            List<Node> newNodes = new List<Node>();
            for (int i = 0; i < nodes.Count; i++)
            {
                Node oldNode = nodes[i];
                Node newNode = new Node(
                    oldNode.Name,
                    oldNode.Location,
                    oldNode.Font);
                newNodes.Add(newNode);
                nodeDict.Add(oldNode, newNode);
            }

            // Clone the links.
            for (int i = 0; i < nodes.Count; i++)
            {
                Node oldNode = nodes[i];
                Node newNode = newNodes[i];
                foreach (Node neighbor in oldNode.Neighbors)
                {
                    Node newNeighbor = nodeDict[neighbor];
                    newNode.Neighbors.Add(newNeighbor);
                }
            }

            return newNodes;
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
