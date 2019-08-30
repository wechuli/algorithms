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

namespace SkylineDivideAndConquer
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
            // Make the random rectangles.
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
            Skyline = MakeSkyline(Rectangles, 0, Rectangles.Count - 1);
            watch.Stop();
            Console.WriteLine($"{numRectangles} rectangles in {watch.Elapsed.TotalSeconds} seconds");
            Text = $"D&C: {watch.Elapsed.TotalSeconds} seconds";

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
                    points.Add(Skyline[0]);
                    for (int i = 1; i < Skyline.Count; i++)
                    {
                        points.Add(new Point(Skyline[i].X, Skyline[i - 1].Y));
                        points.Add(Skyline[i]);
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
        private List<Point> MakeSkyline(
            List<Rectangle> rectangles, int mini, int maxi)
        {
            // See if we need to process a single rectangle.
            if (mini == maxi)
            {
                List<Point> result = new List<Point>();
                result.Add(new Point(rectangles[mini].Left, rectangles[mini].Top));
                result.Add(new Point(rectangles[mini].Right, rectangles[mini].Bottom));
                return result;
            }

            // Process the two halves.
            int midi = (mini + maxi) / 2;
            List<Point> skyline1 = MakeSkyline(rectangles, mini, midi);
            List<Point> skyline2 = MakeSkyline(rectangles, midi + 1, maxi);

            // Merge and return the result.
            return MergeSkylines(skyline1, skyline2);
        }

        // Merge two skylines.
        private List<Point> MergeSkylines(
            List<Point> skyline1, List<Point> skyline2)
        {
            List<Point> results = new List<Point>();

            int count1 = skyline1.Count;
            int count2 = skyline2.Count;
            int index1 = 0;
            int index2 = 0;
            int y1 = skyline1[count1 - 1].Y;
            int y2 = y1;
            int currentY = y1;
            while ((index1 < count1) && (index2 < count2))
            {
                Point point1 = skyline1[index1];
                Point point2 = skyline2[index2];
                if (point1.X < point2.X)
                {
                    y1 = point1.Y;
                    int newY = Math.Min(y1, y2);
                    if (newY != currentY)
                    {
                        currentY = newY;
                        results.Add(new Point(point1.X, currentY));
                    }
                    index1++;
                }
                else if (point2.X < point1.X)
                {
                    y2 = point2.Y;
                    int newY = Math.Min(y1, y2);
                    if (newY != currentY)
                    {
                        currentY = newY;
                        results.Add(new Point(point2.X, currentY));
                    }
                    index2++;
                }
                else
                {
                    y1 = point1.Y;
                    y2 = point2.Y;
                    int newY = Math.Min(y1, y2);
                    if (newY != currentY)
                    {
                        currentY = newY;
                        results.Add(new Point(point1.X, currentY));
                    }
                    index1++;
                    index2++;
                }
            }

            // Add any remaining points.
            for (int i = index1; i < count1; i++)
            {
                Point point1 = skyline1[i];
                if (point1.Y != currentY)
                {
                    results.Add(point1);
                    currentY = point1.Y;
                }
            }
            for (int i = index2; i < count2; i++)
            {
                Point point2 = skyline2[i];
                if (point2.Y != currentY)
                {
                    results.Add(point2);
                    currentY = point2.Y;
                }
            }

            return results;
        }
    }
}
