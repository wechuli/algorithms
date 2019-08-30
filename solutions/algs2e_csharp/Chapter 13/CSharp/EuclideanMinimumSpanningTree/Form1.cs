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

namespace EuclideanMinimumSpanningTree
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private List<Point> Points = new List<Point>();
        private List<Link> Links = new List<Link>();

        // Find the Euclidean minimum spanning tree.
        private void goButton_Click(object sender, EventArgs e)
        {
            Links = FindEMST(Points);
            canvasPictureBox.Refresh();
        }

        private void canvasPictureBox_MouseClick(object sender, MouseEventArgs e)
        {
            Points.Add(e.Location);
            canvasPictureBox.Refresh();
        }

        private void canvasPictureBox_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.Clear(canvasPictureBox.BackColor);
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;

            // Draw the links.
            foreach (Link link in Links)
                link.Draw(e.Graphics, Pens.Black);

            // Draw the points.
            foreach (Point point in Points)
                DrawCircle(e.Graphics, Brushes.LightBlue, Pens.Blue, point);
        }

        // Find a Euclidean minimum spanning tree.
        private List<Link> FindEMST(List<Point> points)
        {
            if (points.Count < 2) return new List<Link>();

            // Build the nodes.
            int numNodes = points.Count;
            Node[] nodes = new Node[numNodes];
            for (int i = 0; i < numNodes; i++)
                nodes[i] = new Node(points[i]);

            // Build the links.
            for (int i = 0; i < numNodes; i++)
            {
                for (int j = i + 1; j < numNodes; j++)
                {
                    float length = Distance(points[i], points[j]);
                    Link link = new Link(nodes[i], nodes[j], length);
                    nodes[i].Links.Add(link);
                    nodes[j].Links.Add(link);
                }
            }

            // Make a candidate list.
            Node root = nodes[0];
            root.Visited = true;
            List<Link> candidates = new List<Link>(root.Links);

            // Build the EMST.
            List<Link> results = new List<Link>();
            while (candidates.Count > 0)
            {
                // Find the shortest candidate.
                float bestLength = float.MaxValue;
                Link bestLink = null;
                foreach (Link link in candidates)
                    if (link.Length < bestLength)
                    {
                        bestLength = link.Length;
                        bestLink = link;
                    }

                // Use this candidate.
                results.Add(bestLink);

                // See which node is not yet in the tree.
                Node newNode = bestLink.Node1;
                if (newNode.Visited)
                    newNode = bestLink.Node2;

                // Add the node to the tree.
                newNode.Visited = true;

                // Add the node's links to the candidate list.
                foreach (Link link in newNode.Links)
                    if (!link.Node1.Visited || !link.Node2.Visited)
                        candidates.Add(link);

                // Remove any unneeded candidates.
                for (int i = candidates.Count - 1; i >= 0; i--)
                {
                    if (candidates[i].Node1.Visited && candidates[i].Node2.Visited)
                        candidates.RemoveAt(i);
                }
            }

            return results;
        }

        // Return the distance between two points.
        private float Distance(Point point1, Point point2)
        {
            float dx = point1.X - point2.X;
            float dy = point1.Y - point2.Y;
            return (float)Math.Sqrt(dx * dx + dy * dy);
        }

        public void DrawCircle(Graphics gr, Brush brush, Pen pen, Point center)
        {
            const int radius = 5;
            RectangleF rect = new RectangleF(
                center.X - radius, center.Y - radius,
                2 * radius, 2 * radius);
            gr.FillEllipse(brush, rect);
            gr.DrawEllipse(pen, rect);
        }

        // Start over.
        private void clearButton_Click(object sender, EventArgs e)
        {
            Points = new List<Point>();
            Links = new List<Link>();
            canvasPictureBox.Refresh();
        }
    }
}
