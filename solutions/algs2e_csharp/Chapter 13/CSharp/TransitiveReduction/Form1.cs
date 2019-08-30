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

namespace TransitiveReduction
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // The network.
        private Node[] Nodes;

        // The distances and via nodes.
        private const float Infinity = float.MaxValue / 2;
        private float[,] Distances = null;
        private int[,] Via = null;

        // Build the first network.
        private void Form1_Load(object sender, EventArgs e)
        {
            Node nodeA = new Node("A", new Point(130, 40));
            Node nodeB = new Node("B", new Point(60, 90));
            Node nodeC = new Node("C", new Point(200, 90));
            Node nodeD = new Node("D", new Point(40, 150));
            Node nodeE = new Node("E", new Point(200, 150));
            Node nodeF = new Node("F", new Point(100, 210));
            nodeA.AddLink(nodeC);
            nodeA.AddLink(nodeD);
            nodeA.AddLink(nodeE);
            nodeB.AddLink(nodeD);
            nodeB.AddLink(nodeE);
            nodeB.AddLink(nodeF);
            nodeC.AddLink(nodeD);
            nodeC.AddLink(nodeE);
            nodeC.AddLink(nodeF);
            nodeE.AddLink(nodeF);
            Nodes = new Node[]
                { nodeA, nodeB, nodeC, nodeD, nodeE, nodeF };

            // Set the node indices.
            for (int i = 0; i < Nodes.Length; i++) Nodes[i].Index = i;

            // Find all pairs shortest paths.
            FindAllPairPaths(Nodes, out Distances, out Via);

            // Print the reachability matrix.
            PrintReachabilityMatrix(Nodes, Distances);
        }

        // Draw the original network.
        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
            DrawNetwork(e.Graphics, pictureBox1.BackColor, Nodes);
        }

        // Draw a network on a Graphics object.
        private void DrawNetwork(Graphics gr, Color clearColor, Node[] nodes)
        {
            if (nodes == null) return;
            gr.Clear(clearColor);
            gr.SmoothingMode = SmoothingMode.AntiAlias;

            foreach (Node node in nodes) node.DrawLinks(gr);
            foreach (Node node in nodes) node.DrawNode(gr, pictureBox1.Font);
        }

        // Color the node clicked and the nodes it can reach.
        private void pictureBox1_MouseClick(object sender, MouseEventArgs e)
        {
            // Unhighlight all of the nodes.
            foreach (Node node in Nodes)
                node.CircleBrush = Brushes.LightBlue;

            // Find and highlight the clicked node.
            Node clickedNode = NodeAtPoint(e.Location);
            if (clickedNode != null)
            {
                clickedNode.CircleBrush = Brushes.Pink;

                // Highlight nodes that can be reached from the clicked node.
                int index = clickedNode.Index;
                for (int i = 0; i < Nodes.Length; i++)
                {
                    if ((index != i) && (Distances[index, i] < Infinity))
                        Nodes[i].CircleBrush = Brushes.LightGreen;
                }
            }

            // Redraw.
            pictureBox1.Refresh();
        }

        // Return the node at this point (if any).
        private Node NodeAtPoint(PointF point)
        {
            foreach (Node node in Nodes)
                if (node.IsAtPoint(point)) return node;
            return null;
        }

        // Find all pairs shortest paths.
        private void FindAllPairPaths(Node[] nodes,
            out float[,] distances, out int[,] via)
        {
            // Create the distance and via arrays.
            int N = nodes.Length;

            // Initialize the distance array.
            distances = new float[N, N];
            for (int i = 0; i < N; i++)
                for (int j = 0; j < N; j++)
                    distances[i, j] = Infinity;
            for (int i = 0; i < N; i++) distances[i, i] = 0;
            foreach (Node node in nodes)
                foreach (Link link in node.Links)
                {
                    int fromNode = link.FromNode.Index;
                    int toNode = link.ToNode.Index;
                    if (distances[fromNode, toNode] > link.Length)
                        distances[fromNode, toNode] = link.Length;
                }

            // Initialize the via array.
            via = new int[N, N];

            // Set via[i, j] = j if there is a link from i to j.
            for (int i = 0; i < N; i++)
                for (int j = 0; j < N; j++)
                {
                    if (distances[i, j] < Infinity) via[i, j] = j;
                    else via[i, j] = -1;
                }

            // Find improvements.
            checked
            {
                for (int via_node = 0; via_node < N; via_node++)
                {
                    for (int from_node = 0; from_node < N; from_node++)
                    {
                        for (int to_node = 0; to_node < N; to_node++)
                        {
                            float new_dist =
                                distances[from_node, via_node] +
                                distances[via_node, to_node];
                            if (new_dist < distances[from_node, to_node])
                            {
                                // This is an improved path. Update it.
                                distances[from_node, to_node] = new_dist;
                                via[from_node, to_node] = via_node;
                            }
                        } // Next to_node
                    } // Next from_node
                } // Next via_node
            } // checked
        }

        // Find the transitive reduction.
        private void findReductionButton_Click(object sender, EventArgs e)
        {
            // Find the transitive reduction.
            FindTransitiveReduction(Nodes, Distances);

            // Find all pairs shortest paths.
            FindAllPairPaths(Nodes, out Distances, out Via);

            // Print the reachability matrix.
            PrintReachabilityMatrix(Nodes, Distances);

            // Redraw the network.
            pictureBox1.Refresh();
        }

        // Find the transitive reduction.
        private void FindTransitiveReduction(Node[] nodes, float[,] distances)
        {
            int numNodes = nodes.Length;

            // Remove self-links.
            for (int i = 0; i < numNodes; i++)
                distances[i, i] = Infinity;

            // Remove other unnecessary links.
            for (int i = 0; i < numNodes; i++)
                for (int j = 0; j < numNodes; j++)
                    // Consider link i --> j.
                    if (distances[i, j] < Infinity)
                    {
                        // See if there is a node k with
                        // paths i --> k and k --> j.
                        for (int k = 0; k < numNodes; k++)
                            if ((distances[i, k] < Infinity) &&
                                (distances[k, j] < Infinity))
                            {
                                distances[i, j] = Infinity;
                                break;
                            }
                    }

            // Update the nodes to remove unnecessary links.
            foreach (Node node in nodes)
            {
                for (int i = node.Links.Count - 1; i >= 0; i--)
                {
                    Link link = node.Links[i];
                    int fromIndex = link.FromNode.Index;
                    int toIndex = link.ToNode.Index;
                    if (distances[fromIndex, toIndex] >= Infinity)
                        node.Links.RemoveAt(i);
                }
            }
        }

        // Print the reachability matrix in the Console window.
        private void PrintReachabilityMatrix(Node[] nodes, float[,] distances)
        {
            int numNodes = distances.GetUpperBound(0);

            // Write node names across the top.
            Console.Write("   ");
            for (int c = 0; c < numNodes; c++)
            {
                Console.Write($" {nodes[c].Name} ");
            }
            Console.WriteLine();

            for (int r = 0; r < numNodes; r++)
            {
                Console.Write($"{nodes[r].Name}: ");
                for (int c = 0; c < numNodes; c++)
                {
                    if (distances[r, c] < Infinity)
                        Console.Write(" X ");
                    else
                        Console.Write("   ");
                }
                Console.WriteLine();
            }
        }
    }
}
