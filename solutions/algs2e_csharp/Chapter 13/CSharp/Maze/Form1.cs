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

namespace Maze
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // The spanning tree.
        private float X0, Y0;
        private List<Link> TreeLinks = new List<Link>();

        // Segments representing the walls to draw.
        private List<Tuple<PointF, PointF>> Walls =
            new List<Tuple<PointF, PointF>>();

        // Build the maze.
        private void goButton_Click(object sender, EventArgs e)
        {
            // Make the network.
            int numRows = int.Parse(numRowsTextBox.Text);
            int numColumns = int.Parse(numColumnsTextBox.Text);
            Node[,] mazeNodes = MakeNetwork(numRows, numColumns);

            // Find a random spanning tree.
            TreeLinks = FindSpanningTree(mazeNodes);

            // Build the walls.
            X0 = canvasPictureBox.ClientSize.Width / (numColumns + 2f);
            Y0 = canvasPictureBox.ClientSize.Height / (numRows + 2f);
            Walls = BuildWalls(TreeLinks, numRows, numColumns, X0, Y0, X0, Y0);

            // Draw the maze.
            canvasPictureBox.Refresh();
        }

        // Draw the maze if we have one.
        private void canvasPictureBox_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.Clear(canvasPictureBox.BackColor);
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;

        // Draw the walls.
        foreach (Tuple<PointF, PointF> tuple in Walls)
            e.Graphics.DrawLine(Pens.Black, tuple.Item1, tuple.Item2);

        // Draw the spanning tree.
        if (showTreeCheckBox.Checked)
        {
            foreach (Link link in TreeLinks)
            {
                float x1 = X0 * (link.Node1.Column + 1.5f);
                float y1 = Y0 * (link.Node1.Row + 1.5f);
                float x2 = X0 * (link.Node2.Column + 1.5f);
                float y2 = Y0 * (link.Node2.Row + 1.5f);
                e.Graphics.DrawLine(Pens.Red, x1, y1, x2, y2);
            }
        }
    }

        // Build the network.
        private Node[,] MakeNetwork(int numRows, int numColumns)
        {
            // Make an array of nodes.
            Node[,] nodes = new Node[numRows, numColumns];
            for (int r = 0; r < numRows; r++)
                for (int c = 0; c < numColumns; c++)
                    nodes[r, c] = new Node(r, c);

            // Make horizontal links.
            for (int r = 0; r < numRows; r++)
            {
                for (int c = 1; c < numColumns; c++)
                {
                    Link link = new Link(nodes[r, c - 1], nodes[r, c]);
                    nodes[r, c - 1].Links.Add(link);
                    nodes[r, c].Links.Add(link);
                }
            }

            // Make vertical links.
            for (int c = 0; c < numColumns; c++)
            {
                for (int r = 1; r < numRows; r++)
                {
                    Link link = new Link(nodes[r - 1, c], nodes[r, c]);
                    nodes[r - 1, c].Links.Add(link);
                    nodes[r, c].Links.Add(link);
                }
            }

            return nodes;
        }

        // Find a random spanning tree.
        private List<Link> FindSpanningTree(Node[,] nodes)
        {
            // Start with a random node.
            Random rand = new Random();
            int row = rand.Next(nodes.GetUpperBound(0));
            int column = rand.Next(nodes.GetUpperBound(1));
            Node root = nodes[row, column];
            root.Visited = true;

            // Create the candidate list.
            List<Link> candidates = new List<Link>(root.Links);

            // Process the candidate list.
            List<Link> results = new List<Link>();
            while (candidates.Count > 0)
            {
                // Pick a random link.
                int index = rand.Next(candidates.Count);
                Link bestLink = candidates[index];
                candidates.RemoveAt(index);
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

            // Return the tree's links.
            return results;
        }

        // Redraw.
        private void showTreeCheckBox_CheckedChanged(object sender, EventArgs e)
        {
            canvasPictureBox.Refresh();
        }

        // Build segments representing the maze's walls.
        private List<Tuple<PointF, PointF>> BuildWalls(
            List<Link> treeLinks, int numRows, int numColumns,
            float x0, float y0, float dx, float dy)
        {
            // Make arrays to indicates whether a node's
            // left or top wall is broken by the tree.
            bool[,] leftSideBroken = new bool[numRows, numColumns + 1];
            bool[,] topSideBroken = new bool[numRows + 1, numColumns];

            // Mark the walls that should be broken.
            foreach (Link link in treeLinks)
            {
                // See if this is a vertical or horizontal link.
                if (link.Node1.Row == link.Node2.Row)
                {
                    // Horizontal link.
                    int row = link.Node1.Row;
                    int column = Math.Max(link.Node1.Column, link.Node2.Column);
                    leftSideBroken[row, column] = true;
                }
                else
                {
                    // Vertical link.
                    int row = Math.Max(link.Node1.Row, link.Node2.Row);
                    int column = link.Node1.Column;
                    topSideBroken[row, column] = true;
                }
            }

            // Build the wall list.
            List<Tuple<PointF, PointF>> walls = new List<Tuple<PointF, PointF>>();
            for (int r = 0; r < numRows; r++)
                for (int c = 0; c <= numColumns; c++)
                    if (!leftSideBroken[r, c])
                    {
                        // Make this wall.
                        float x = x0 + c * dx;
                        float y = y0 + r * dx;
                        PointF p0 = new PointF(x, y);
                        PointF p1 = new PointF(x, y + dy);
                        walls.Add(Tuple.Create(p0, p1));
                    }
            for (int c = 0; c < numColumns; c++)
                for (int r = 0; r <= numRows; r++)
                    if (!topSideBroken[r, c])
                    {
                        // Make this wall.
                        float x = x0 + c * dx;
                        float y = y0 + r * dx;
                        PointF p0 = new PointF(x, y);
                        PointF p1 = new PointF(x + dx, y);
                        walls.Add(Tuple.Create(p0, p1));
                    }

            return walls;
        }
    }
}
