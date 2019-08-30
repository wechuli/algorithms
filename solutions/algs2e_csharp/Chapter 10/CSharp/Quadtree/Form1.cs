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

namespace Quadtree
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // The quadtree's root.
        private QuadtreeNode Root;

        // The selected point.
        private PointF SelectedPoint =
            new PointF(float.NegativeInfinity, float.NegativeInfinity);

        // The radius of a drawn point.
        private const float Radius = 5;

        // Initialize the quadtree.
        private void Form1_Load(object sender, EventArgs e)
        {
            Root = new QuadtreeNode(0, 0,
                pointsPictureBox.ClientSize.Width - 1,
                pointsPictureBox.ClientSize.Height - 1);
        }

        // Redraw with or without the quadtree areas.
        private void drawBoxesCheckBox_CheckedChanged(object sender, EventArgs e)
        {
            pointsPictureBox.Refresh();
        }

        // Display the points.
        private void pointsPictureBox_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;

            // Draw the points.
            //Root.DrawPoints(e.Graphics, Brushes.LightGray, Pens.Gray, Radius);
            Root.DrawPoints(e.Graphics, Brushes.White, Pens.Blue, Radius);

            // Draw the selected point.
            if (SelectedPoint.X > float.NegativeInfinity)
            {
                e.Graphics.FillEllipse(Brushes.LightGreen,
                    SelectedPoint.X - Radius, SelectedPoint.Y - Radius,
                    2 * Radius, 2 * Radius);
                e.Graphics.DrawEllipse(Pens.Green,
                    SelectedPoint.X - Radius, SelectedPoint.Y - Radius,
                    2 * Radius, 2 * Radius);
            }

            // Draw the quadtree if desired.
            if (drawBoxesCheckBox.Checked)
            {
                e.Graphics.SmoothingMode = SmoothingMode.None;
                //Root.DrawAreas(e.Graphics, Pens.Black);
                Root.DrawAreas(e.Graphics, Pens.Red);
            }
        }

        // Add random points to the quadtree.
        private Random rand = new Random(0);
        private void createButton_Click(object sender, EventArgs e)
        {
            try
            {
                int numPoints = int.Parse(numPointsTextBox.Text);
                float xmin = Radius;
                float ymin = Radius;
                float xmax = (pointsPictureBox.ClientSize.Width - Radius) / 3;
                float ymax = (pointsPictureBox.ClientSize.Height - Radius) / 3;
                for (int i = 0; i < numPoints; i++)
                {
                    float x = xmin + (float)(
                        (rand.NextDouble() * xmax - xmin) +
                        (rand.NextDouble() * xmax - xmin) +
                        (rand.NextDouble() * xmax - xmin));
                    float y = ymin + (float)(
                        (rand.NextDouble() * ymax - ymin) +
                        (rand.NextDouble() * ymax - ymin) +
                        (rand.NextDouble() * ymax - ymin));
                    Root.AddPoint(new PointF(x, y));
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }

            // Redraw.
            pointsPictureBox.Refresh();
        }

        // Select the clicked point.
        private void pointsPictureBox_MouseClick(object sender, MouseEventArgs e)
        {
            // Find the point closest to the selected point.
            SelectedPoint = Root.FindPoint(e.Location, Radius);

            // Redraw.
            pointsPictureBox.Refresh();
        }

        // Return the distance between two points.
        private float Distance(PointF point1, PointF point2)
        {
            float dx = point1.X - point2.X;
            float dy = point1.Y - point2.Y;
            return (float)Math.Sqrt(dx * dx + dy * dy);
        }
    }
}
