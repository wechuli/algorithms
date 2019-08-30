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

namespace SwarmMinimum
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // World coordinates.
        private double Wxmin = -3.5;
        private double Wxmax = 3.5;
        private double Wymin = -3.5;
        private double Wymax = 3.5;

        // Device coordinates.
        private double Dxmin, Dxmax, Dymin, Dymax;
        private double Xscale, Yscale;

        // The bugs.
        private List<Bug> Bugs = new List<Bug>();

        // The best result found globally.
        private Point2d GlobalBestPoint = new Point2d();
        private double GlobalBestValue = double.PositiveInfinity;

        private double CogAccel = 1;
        private double SocAccel = 1;
        private long LastTicks = 0;

        // Get the device coordinates.
        private void Form1_Load(object sender, EventArgs e)
        {
            Dxmin = 0;
            Dxmax = canvasPictureBox.ClientSize.Width - 1;
            Dymin = 0;
            Dymax = canvasPictureBox.ClientSize.Height - 1;
            Xscale = (Dxmax - Dxmin) / (Wxmax - Wxmin);
            Yscale = (Dymax - Dymin) / (Wymax - Wymin);
        }

        // Map world to device coordinates.
        private Point2d WtoD(double x, double y)
        {
            double newX = Dxmin + (x - Wxmin) * Xscale;
            double newY = Dymin + (y - Wymin) * Yscale;
            return new Point2d((float)newX, (float)newY);
        }

        // Start or stop.
        private void startButton_Click(object sender, EventArgs e)
        {
            if (startButton.Text == "Start") Start();
            else Stop();
        }

        // Make some bugs and start the simulation.
        private void Start()
        {
            // Make the bugs.
            Random rand = new Random();
            int numBugs = int.Parse(numBugsTextBox.Text);
            CogAccel = double.Parse(cogAccelTextBox.Text);
            SocAccel = double.Parse(socAccelTextBox.Text);
            double maxSpeed = double.Parse(maxSpeedTextBox.Text);
            int lockAfter = int.Parse(lockAfterTextBox.Text);
            Bugs = new List<Bug>();
            for (int i = 0; i < numBugs; i++)
            {
                Point2d location = new Point2d(
                    Wxmin + rand.NextDouble() * (Wxmax - Wxmin),
                    Wymin + rand.NextDouble() * (Wymax - Wymin));
                Vector2d velocity = new Vector2d(
                    rand.Next(-1, 2),
                    rand.Next(-1, 2));
                Bugs.Add(new Bug(Strange, location,
                    velocity, maxSpeed, lockAfter));
            }

            // Initialize BestPoint and BestValue.
            GlobalBestPoint = new Point2d(Bugs[0].Location);
            GlobalBestValue = Bugs[0].Value;

            // Start the timer.
            startButton.Text = "Stop";
            LastTicks = DateTime.Now.Ticks;
            moveTimer.Enabled = true;
        }

        // Stop the timer.
        private void Stop()
        {
            moveTimer.Enabled = false;
            startButton.Text = "Start";
        }

        // Move the bugs.
        private void moveTimer_Tick(object sender, EventArgs e)
        {
            // Get the elapsed time in seconds.
            const double tenmillion = 10000000;
            long ticks = DateTime.Now.Ticks;
            double deltaTime = (ticks - LastTicks) / tenmillion;
            LastTicks = ticks;

            // Move the bugs.
            bool stillActive = false;
            foreach (Bug bug in Bugs)
            {
                bug.Move(deltaTime, CogAccel, SocAccel,
                    ref GlobalBestPoint, ref GlobalBestValue);
                if (bug.IsActive) stillActive = true;
            }

            // Display the current global minimum.
            minimumTextBox.Text = GlobalBestValue.ToString("0.000000");

            // Redraw.
            canvasPictureBox.Refresh();

            // If no bugs are active, stop the simulation.
            if (!stillActive) Stop();
        }

        // Convert world to device coordinates.
        private Point2d WtoD(Point2d point)
        {
            return WtoD(point.X, point.Y);
        }

        // Return the function's value F(x, y).
        private double Strange(Point2d point)
        {
            double r2 = (point.X * point.X + point.Y * point.Y) / 4;
            double r = Math.Sqrt(r2);

            double theta = Math.Atan2(point.Y, point.X);
            double z = 3 * Math.Exp(-r2) *
                Math.Sin(2 * Math.PI * r) *
                Math.Cos(3 * theta);
            return z;
        }

        // Draw.
        private void canvasPictureBox_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.Clear(canvasPictureBox.BackColor);
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;

            // Draw a checkerboard.
            for (int x = (int)Wxmin; x <= Wxmax; x++)
                e.Graphics.DrawLine(Pens.Gray, WtoD(x, Wymin), WtoD(x, Wymax));
            for (int y = (int)Wymin; y <= Wymax; y++)
                e.Graphics.DrawLine(Pens.Gray, WtoD(Wxmin, y), WtoD(Wxmax, y));

            // Draw the bugs.
            foreach (Bug bug in Bugs)
                DrawBug(e.Graphics, bug);

            // Draw the global best point.
            DrawCircle(e.Graphics, GlobalBestPoint, 5, Brushes.Blue);
        }

        // Draw a bug.
        private void DrawBug(Graphics gr, Bug bug)
        {
            if (bug.IsActive)
                DrawCircle(gr, bug.Location, 2, Brushes.Red);
            else
                DrawCircle(gr, bug.Location, 2, Brushes.Orange);
            DrawCircle(gr, bug.BestPoint, 3, Brushes.Green);
        }

        // Draw a circle at the given point (in world coordinates)
        // with the given radius (in device coordinates).
        private void DrawCircle(Graphics gr, Point2d point, float radius, Brush brush)
        {
            PointF center = WtoD(point);
            RectangleF rect = new RectangleF(
                center.X - radius,
                center.Y - radius,
                2 * radius, 2 * radius);
            gr.FillEllipse(brush, rect);
        }
    }
}
