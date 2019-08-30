using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace IntervalTrees
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // Thick pens.
        private const float PenThickness = 3;
        private Pen BlackPen = new Pen(Color.Black, PenThickness);
        private Pen RedPen = new Pen(Color.Red, PenThickness);
        private Pen GreenPen = new Pen(Color.Green, PenThickness);
        private Pen BluePen = new Pen(Color.Blue, PenThickness);

        // The X coordinate of the test line.
        private int TestX = -1;

        // The defined intervals.
        private List<Interval> Intervals = new List<Interval>();

        // Variables for drawing new intervals.
        private bool DrawingInterval = false;
        private Interval NewInterval = new Interval(
            Pens.Pink, new Point(0, 0), new Point(0, 0));

        // The interval tree.
        private IntervalNode Root = null;

        // Start drawing a new interval.
        private void canvasPictureBox_MouseDown(object sender, MouseEventArgs e)
        {
            // See which button is pressed.
            if (e.Button == MouseButtons.Right)
            {
                // Right button. Define the vertical test line.
                if (Root != null) TestX = e.X;

                // Apply the inverval tree if we have one.
                UseIntervalTree();
            }
            else
            {
                // Left button. Define a new horizontal interval.
                DrawingInterval = true;
                NewInterval.LeftPoint = e.Location;
                NewInterval.RightPoint = e.Location;
                TestX = -1;
                Root = null;
                ResetIntervalColors();
            }

            // Redraw.
            canvasPictureBox.Refresh();
        }

        // Continue drawing a new interval.
        private void canvasPictureBox_MouseMove(object sender, MouseEventArgs e)
        {
            if (!DrawingInterval) return;
            NewInterval.RightPoint.X = e.X;
            canvasPictureBox.Refresh();
        }

        // Stop drawing a new interval.
        private void canvasPictureBox_MouseUp(object sender, MouseEventArgs e)
        {
            if (!DrawingInterval) return;
            DrawingInterval = false;
            buildTreeButton.Enabled = true;

            // Don't make zero-length intervals.
            if (NewInterval.LeftPoint.X == NewInterval.RightPoint.X)
                return;

            // Make the new interval.
            Intervals.Add(new Interval(BlackPen,
                NewInterval.LeftPoint, NewInterval.RightPoint));
            canvasPictureBox.Refresh();
        }

        // Draw the intervals.
        private void canvasPictureBox_Paint(object sender, PaintEventArgs e)
        {
            // Draw existing intervals.
            foreach (Interval interval in Intervals)
            {
                e.Graphics.DrawLine(interval.Pen, interval.LeftPoint, interval.RightPoint);
            }

            // Draw the interval in progress (if any).
            if (DrawingInterval)
                e.Graphics.DrawLine(BluePen,
                    NewInterval.LeftPoint, NewInterval.RightPoint);

            // Draw the vertical test line.
            if (TestX >= 0)
                e.Graphics.DrawLine(GreenPen,
                    TestX, 0, TestX,
                    canvasPictureBox.ClientSize.Height);
        }

        // Build the interval tree.
        private void buildTreeButton_Click(object sender, EventArgs e)
        {
            TestX = -1;
            Root = IntervalNode.MakeIntervalTree(Intervals);
            canvasPictureBox.Refresh();
            buildTreeButton.Enabled = false;
        }

        // Use the interval tree to see which horizontal
        // lines intersect the vertical test line.
        private void UseIntervalTree()
        {
            if (Root == null) return;

            // Reset the colors of all horizontal intervals.
            ResetIntervalColors();

            // See which intervals intersect the vertical test line.
            List<Interval> hits = new List<Interval>();
            Root.FindOverlappingIntervals(hits, TestX);
            foreach (Interval interval in hits)
                interval.Pen = RedPen;
        }

        // Reset the colors of all horizontal intervals.
        private void ResetIntervalColors()
        {
            foreach (Interval interval in Intervals)
                interval.Pen = BlackPen;
        }
    }
}
