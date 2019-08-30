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

namespace StronglyConnectedComponents
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // The network.
        private Node[] Nodes;

        // Build the first network.
        private void Form1_Load(object sender, EventArgs e)
        {
            Node nodeA = new Node("A", new Point(27, 36));
            Node nodeB = new Node("B", new Point(80, 35));
            Node nodeC = new Node("C", new Point(20, 104));
            Node nodeD = new Node("D", new Point(70, 140));
            Node nodeE = new Node("E", new Point(131, 155));
            Node nodeF = new Node("F", new Point(109, 202));
            Node nodeG = new Node("G", new Point(170, 210));
            Node nodeH = new Node("H", new Point(130, 45));
            Node nodeI = new Node("I", new Point(206, 18));
            Node nodeJ = new Node("J", new Point(230, 83));
            Node nodeK = new Node("K", new Point(188, 60));
            Node nodeL = new Node("L", new Point(180, 120));
            Node nodeM = new Node("M", new Point(210, 180));

            nodeA.AddLink(nodeB);
            nodeA.AddLink(nodeC);
            nodeB.AddLink(nodeD);
            nodeB.AddLink(nodeE);
            nodeC.AddLink(nodeD);
            nodeD.AddLink(nodeA);
            nodeD.AddLink(nodeE);
            nodeE.AddLink(nodeG);
            nodeG.AddLink(nodeF);
            nodeF.AddLink(nodeE);
            nodeH.AddLink(nodeL);
            nodeI.AddLink(nodeH);
            nodeI.AddLink(nodeK);
            nodeJ.AddLink(nodeI);
            nodeK.AddLink(nodeJ);
            nodeL.AddLink(nodeE);
            nodeL.AddLink(nodeG);
            nodeL.AddLink(nodeK);
            nodeM.AddLink(nodeL);
            Nodes = new Node[] {
                nodeA, nodeB, nodeC, nodeD, nodeE, nodeF,
                nodeG, nodeH, nodeI, nodeJ, nodeK, nodeL, nodeM,
            };
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

        // Find the strongly connected components.
        private void findComponentsButton_Click(object sender, EventArgs e)
        {
            // Find the strongly connected components.
            SetStronglyConnectedComponents(Nodes);

            // Color the strongly connected components.
            ColorComponents(Nodes);

            // Redraw the network.
            pictureBox1.Refresh();
        }

        // Find the strongly connected components.
        private void SetStronglyConnectedComponents(Node[] nodes)
        {
            // Clear each node's Visited,
            // ComponentRoot, and InLinks values.
            foreach (Node node in nodes)
            {
                node.Visited = false;
                node.ComponentRoot = null;
                node.InLinks = new List<Link>();
            }

            // Set each node's InLinks.
            foreach (Node node in nodes)
            {
                foreach (Link link in node.Links)
                {
                    Node toNode = link.ToNode;
                    toNode.InLinks.Add(new Link(node, toNode));
                }
            }

            // Make a list to hold visited nodes.
            List<Node> visitedNodes = new List<Node>();

            // Visit each node.
            foreach (Node node in nodes) Visit(node, visitedNodes);

            // Add the nodes to components.
            foreach (Node node in visitedNodes) Assign(node, node);
        }

        // Recursively visit nodes that are reachable from this one.
        private void Visit(Node node, List<Node> visitedNodes)
        {
            if (node.Visited) return;
                
            node.Visited = true;
            foreach (Link link in node.Links)
                Visit(link.ToNode, visitedNodes);
            visitedNodes.Insert(0, node);
        }

        // Recursively assign nodes to a component root.
        private void Assign(Node node, Node root)
        {
            if (node.ComponentRoot != null) return;

            node.ComponentRoot = root;
            foreach (Link link in node.InLinks)
                Assign(link.FromNode, root);
        }

        // Color the strongly connected components.
        private void ColorComponents(Node[] nodes)
        {
            // Color the nodes.
            Brush[] brushes =
            {
                Brushes.Pink, Brushes.Yellow, Brushes.LightBlue,
                Brushes.Lime, Brushes.White, Brushes.LightGreen,
                Brushes.Orange, Brushes.Magenta, Brushes.Cyan,
            };
            Dictionary<Node, Brush> rootBrushes = new Dictionary<Node, Brush>();
            foreach (Node node in nodes)
            {
                if (!rootBrushes.ContainsKey(node.ComponentRoot))
                {
                    rootBrushes.Add(
                        node.ComponentRoot,
                        brushes[rootBrushes.Count]);
                }
                node.CircleBrush = rootBrushes[node.ComponentRoot];
            }
        }
    }
}
