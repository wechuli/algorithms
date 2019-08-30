#define RANDOM_RECTS
//#define PYRAMID_RECTS
//#define THIN_RECTS
//#define FOUR_RECTS

using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

using System.Diagnostics;

namespace SkylineList
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // The rectangle and skyline definitions.
        private int GroundY = 0;
        private List<Rectangle> Rectangles = null;
        private List<Point> Skyline = null;

        private const int SkylineThickness = 7;
        private const int BuildingThickness = 3;

        // Make rectangles and build the skyline.
        private void goButton_Click(object sender, EventArgs e)
        {
            // Make the rectangles.
            const int margin = 20;
            int numRectangles = int.Parse(numRectanglesTextBox.Text);
            int xmin = margin;
            int xmax = canvasPictureBox.ClientSize.Width - margin;
            GroundY = canvasPictureBox.ClientSize.Height - margin;
            const int minWidth = 10;
            int maxWidth = (int)(3 * xmax / numRectangles);
            if (maxWidth < 20) maxWidth = 20;
            int minHeight = 20;
            int maxHeight = 150;
            Rectangles = new List<Rectangle>();

            // Different kinds of rectangle tests.
#if RANDOM_RECTS
            Random rand = new Random();
            for (int i = 0; i < numRectangles; i++)
            {
                int width = rand.Next(minWidth, maxWidth);
                int x = rand.Next(xmin, xmax - width);
                int height = rand.Next(minHeight, maxHeight);
                int y = GroundY - height;
                Rectangles.Add(new Rectangle(x, y, width, height));
            }
#elif PYRAMID_RECTS
            int wid = canvasPictureBox.ClientSize.Width;
            for (int i = 1; i < wid / 2; i++)
            {
                int height = i;
                int y = GroundY - height;
                Rectangles.Add(new Rectangle(i, y, wid - 2 * i, height));
            }
#elif THIN_RECTS
            int wid = canvasPictureBox.ClientSize.Width;
            int height = 50;
            int y = GroundY - height;
            for (int i = 1; i < wid; i += 2)
            {
                Rectangles.Add(new Rectangle(i, y, 1, height));
            }
#elif FOUR_RECTS
            Rectangles.Add(new Rectangle(30, GroundY - 50, 100, 50));
            Rectangles.Add(new Rectangle(50, GroundY - 70, 50, 70));
            Rectangles.Add(new Rectangle(70, GroundY - 60, 50, 60));
            Rectangles.Add(new Rectangle(150, GroundY - 60, 50, 60));
#endif

            // Make the skyline.
            Stopwatch watch = new Stopwatch();
            watch.Start();
            Skyline = MakeSkyline(Rectangles);
            watch.Stop();
            Console.WriteLine($"{numRectangles} rectangles in {watch.Elapsed.TotalSeconds} seconds");
            Text = $"List: {watch.Elapsed.TotalSeconds} seconds";

            // Redraw.
            canvasPictureBox.Refresh();
        }

        // Draw the rectangles and skyline.
        private void canvasPictureBox_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.Clear(canvasPictureBox.BackColor);
            if (Rectangles == null) return;

            using (Pen pen = new Pen(Color.Black, SkylineThickness))
            {
                if (Skyline != null)
                {
                    // Convert the key points into a polyline.
                    List<Point> points = new List<Point>();
                    points.Add(new Point(Skyline[0].X, Skyline[Skyline.Count - 1].Y));
                    points.Add(new Point(Skyline[0].X, Skyline[0].Y));
                    for (int i = 1; i < Skyline.Count; i++)
                    {
                        points.Add(new Point(Skyline[i].X, Skyline[i - 1].Y));
                        points.Add(new Point(Skyline[i].X, Skyline[i].Y));
                    }

                    // Draw the skyline.
                    e.Graphics.DrawLines(pen, points.ToArray());
                }

                // Draw the rectangles.
                pen.Width = BuildingThickness;
                pen.Color = Color.LightGreen;
                foreach (Rectangle rect in Rectangles)
                    e.Graphics.DrawRectangle(pen, rect);
            }

            // Draw the ground.
            e.Graphics.FillRectangle(Brushes.SandyBrown,
                0, GroundY,
                canvasPictureBox.ClientSize.Width,
                canvasPictureBox.ClientSize.Height);
        }

        // Make the skyline points.
        private List<Point> MakeSkyline(List<Rectangle> rectangles)
        {
            // Make a sorted list of HeightChange objects.
            List<HeightChange> changes = new List<HeightChange>();
            foreach (Rectangle rect in rectangles)
            {
                changes.Add(new HeightChange(true, rect));
                changes.Add(new HeightChange(false, rect));
            }
            changes.Sort();

            // Process the changes.
            List<int> activeTops = new List<int>();
            List<Point> skyline = new List<Point>();
            int currentY = rectangles[0].Bottom;
            foreach (HeightChange change in changes)
            {
                // See if we are starting or stopping a building.
                if (change.Starting)
                {
                    // Starting a building.
                    // See if we are decreasing the current height.
                    if (change.Rectangle.Top < currentY)
                    {
                        currentY = change.Rectangle.Top;
                        skyline.Add(new Point(change.Rectangle.Left, currentY));
                    }

                    // Add the top to the active list.
                    activeTops.Add(change.Rectangle.Top);
                }
                else
                {
                    // Ending a building.
                    // Remove this top from the active list.
                    activeTops.Remove(change.Rectangle.Top);

                    // Find the smallest active top.
                    int newY = change.Rectangle.Bottom;
                    foreach (int top in activeTops)
                    {
                        if (top < newY) newY = top;
                    }
                    if (newY != currentY)
                    {
                        currentY = newY;
                        skyline.Add(new Point(change.Rectangle.Right, currentY));
                    }
                }
            }

            return skyline;
        }
    }
}
