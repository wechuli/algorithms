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

namespace CompleteSelfAvoidingWalk
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // The locations of the grid points on the PictureBox.
        private PointF[,] GridPoints = null;

        // The walk. A point's coordinates give the indices of
        // the point's location in the GridPoints array.
        private List<Point> WalkPoints = null;

        // A Random object to use throughout.
        Random Rand = new Random();

        // Make a random walk.
        private void Form1_Load(object sender, EventArgs e)
        {
            MakeWalk();
        }
        private void drawButton_Click(object sender, EventArgs e)
        {
            MakeWalk();
        }

        // Make and display a walk.
        private void MakeWalk()
        {
            // Get the grid size.
            int width = int.Parse(widthTextBox.Text);
            int height = int.Parse(heightTextBox.Text);

            // Find the walk.
            WalkPoints = FindWalk(width, height);

            // Define the grid points.
            float dx = walkPictureBox.ClientSize.Width / (width + 1);
            float dy = walkPictureBox.ClientSize.Height / (height + 1);
            GridPoints = new PointF[height, width];
            for (int row = 0; row < height; row++)
            {
                float y = (row + 1) * dy;
                for (int col = 0; col < width; col++)
                {
                    float x = (col + 1) * dx;
                    GridPoints[row, col] = new PointF(x, y);
                }
            }

            walkPictureBox.Refresh();
        }

        // Find a random self-avoiding walk.
        private List<Point> FindWalk(int width, int height)
        {
            // Make an array to show where we have been.
            bool[,] visited = new bool[width, height];

            // Start at a random vertex.
            int x = Rand.Next(0, width);
            int y = Rand.Next(0, height);

            // Start the walk at (x, y).
            List<Point> walk = new List<Point>();
            walk.Add(new Point(x, y));
            visited[x, y] = true;

            // Extend the walk.
            ExtendWalk(width, height, x, y, walk, visited);

            return walk;
        }

        // Extend the walk from position [x, y].
        // Return true if we find a complete walk.
        private bool ExtendWalk(int width, int height,
            int x, int y, List<Point> walk, bool[,] visited)
        {
            // If the list is already long enough,
            // we've found the walk.
            if (walk.Count == width * height) return true;

            // Make a list of potential neighbors.
            List<Point> candidates = new List<Point>();
            candidates.Add(new Point(x - 1, y));
            candidates.Add(new Point(x + 1, y));
            candidates.Add(new Point(x, y - 1));
            candidates.Add(new Point(x, y + 1));

            // See which neighbors are on the lattice and unvisited.
            List<Point> neighbors = new List<Point>();
            foreach (Point point in candidates)
                if ((point.X >= 0) && (point.X < width) &&
                    (point.Y >= 0) && (point.Y < height) &&
                    !visited[point.X, point.Y])
                    neighbors.Add(point);

            // If we have no unvisited neighbors, then we're stuck.
            if (neighbors.Count == 0) return false;

            // Randomize the neighbors.
            neighbors.Randomize();

            // Try each of the neighbors.
            foreach (Point point in neighbors)
            {
                // Try adding this neighbor to the walk.
                walk.Add(point);
                visited[point.X, point.Y] = true;
                if (ExtendWalk(width, height, point.X, point.Y, walk, visited))
                    return true;

                // That didn't work. Remove the neighbor from the walk.
                walk.RemoveAt(walk.Count - 1);
                visited[point.X, point.Y] = false;
            }

            // We couldn't find a complete path from this point.
            return false;
        }

        // Draw the walk.
        private void walkPictureBox_Paint(object sender, PaintEventArgs e)
        {
            if (WalkPoints == null) return;

            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;
            e.Graphics.Clear(Color.White);

            // Draw the grid points.
            const float radius = 3;
            foreach (PointF point in GridPoints)
            {
                RectangleF dotRect = new RectangleF(
                    point.X - radius, point.Y - radius,
                    2 * radius, 2 * radius);
                e.Graphics.FillEllipse(Brushes.Blue, dotRect);
            }

            // Draw the walk.
            if (WalkPoints.Count > 1)
            {
                List<PointF> points = new List<PointF>();
                foreach (Point point in WalkPoints)
                {
                    points.Add(GridPoints[point.Y, point.X]);
                }
                e.Graphics.DrawLines(Pens.Red, points.ToArray());
            }

            // Circle the starting point.
            PointF startPoint = GridPoints[WalkPoints[0].Y, WalkPoints[0].X];
            RectangleF startRect = new RectangleF(
                startPoint.X - 2 * radius, startPoint.Y - 2 * radius,
                4 * radius, 4 * radius);
            e.Graphics.DrawEllipse(Pens.Red, startRect);
        }
    }
}
