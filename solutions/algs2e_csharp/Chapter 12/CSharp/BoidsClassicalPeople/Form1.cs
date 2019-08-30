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

namespace BoidsClassicalPeople
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private List<Boid> Boids = null;
        private double SeparationWgt = 0;
        private double AlignmentWgt = 0;
        private double CohesionWgt = 0;
        private double TargetWgt = 0;
        private double PersonWgt = 0;
        private Point MouseLocation = new Point(0, 0);
        private long LastTicks = 0;

        private List<Point2d> People = null;

        // Start or stop the simulation.
        private void startButton_Click(object sender, EventArgs e)
        {
            if (startButton.Text == "Start") Start();
            else Stop();
        }

        private void Start()
        {
            Boids = new List<Boid>();
            People = new List<Point2d>();
            Random rand = new Random();
            float cx = canvasPictureBox.ClientSize.Width / 2;
            float cy = canvasPictureBox.ClientSize.Height / 2;
            int numBoids = int.Parse(numBoidsTextBox.Text);
            double maxSpeed = double.Parse(maxSpeedTextBox.Text);
            double neighborDist = double.Parse(neighborDistTextBox.Text);
            for (int i = 0; i < numBoids; i++)
            {
                Point2d location = new Point2d(
                    cx + rand.Next(-20, 21),
                    cy + rand.Next(-20, 21));
                Vector2d velocity = new Vector2d(
                    rand.Next(-5, 6),
                    rand.Next(-5, 6));
                Boids.Add(new Boid(location, velocity, maxSpeed, neighborDist));
            }

            // Save the weights.
            SeparationWgt = double.Parse(separationWgtTextBox.Text);
            AlignmentWgt = double.Parse(alignmentWgtTextBox.Text);
            CohesionWgt = double.Parse(cohesionWgtTextBox.Text);
            TargetWgt = double.Parse(targetWgtTextBox.Text);
            PersonWgt = double.Parse(personWgtTextBox.Text);

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

        private void moveTimer_Tick(object sender, EventArgs e)
        {
            // Get the elapsed time in seconds.
            const double tenmillion = 10000000;
            long ticks = DateTime.Now.Ticks;
            double deltaTime = (ticks - LastTicks) / tenmillion;
            LastTicks = ticks;

            Point2d target = new Point2d(MouseLocation);

            foreach (Boid boid in Boids)
            {
                boid.Move(Boids, People, target, deltaTime,
                    SeparationWgt, AlignmentWgt, CohesionWgt,
                    TargetWgt, PersonWgt);
            }
            canvasPictureBox.Refresh();
        }

        // Save the mouse position.
        private void canvasPictureBox_MouseMove(object sender, MouseEventArgs e)
        {
            MouseLocation = e.Location;
        }

        // Draw the boids.
        private void canvasPictureBox_Paint(object sender, PaintEventArgs e)
        {
            if (Boids == null) return;
            e.Graphics.Clear(canvasPictureBox.BackColor);
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;

            // Draw the people.
            const int personRadius = 4;
            foreach (Point2d person in People)
            {
                RectangleF personRect = new RectangleF(
                    (float)(person.X - personRadius),
                    (float)(person.Y - personRadius),
                    2 * personRadius, 2 * personRadius);
                e.Graphics.FillEllipse(Brushes.Blue, personRect);
            }

            // Draw the Boids.
            foreach (Boid boid in Boids)
            {
                boid.Draw(e.Graphics);
            }

            // Draw the mouse position.
            const int mouseRadius = 3;
            Rectangle mouseRect = new Rectangle(
                MouseLocation.X - mouseRadius,
                MouseLocation.Y - mouseRadius,
                2 * mouseRadius, 2 * mouseRadius);
            e.Graphics.FillEllipse(Brushes.Red, mouseRect);
        }

        // Make a person.
        private void canvasPictureBox_MouseClick(object sender, MouseEventArgs e)
        {
            if (People == null) return;
            People.Add(new Point2d(e.Location));
        }
    }
}
