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

namespace RandomWalk
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // The walk's points.
        private Point[] WalkPoints = null;

        // Make a new walk.
        private void drawButton_Click(object sender, EventArgs e)
        {
            int stepSize = int.Parse(stepSizeTextBox.Text);
            int numSteps = int.Parse(numStepsTextBox.Text);

            WalkPoints = new Point[numSteps];
            int x = walkPictureBox.ClientSize.Width / 2;
            int y = walkPictureBox.ClientSize.Height / 2;
            WalkPoints[0] = new Point(x, y);

            Random rand = new Random();
            for (int i = 1; i < numSteps; i++)
            {
                int direction = rand.Next(4);
                if (direction == 0)         // Up
                    y -= stepSize;
                else if (direction == 1)    // Right
                    x += stepSize;
                else if (direction == 2)    // Down
                    y += stepSize;
                else                        // Left
                    x -= stepSize;
                WalkPoints[i] = new Point(x, y);
            }

            walkPictureBox.Refresh();
        }

        // Draw the walk.
        private void walkPictureBox_Paint(object sender, PaintEventArgs e)
        {
            if (WalkPoints == null) return;
            e.Graphics.Clear(walkPictureBox.BackColor);
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;
            e.Graphics.DrawLines(Pens.Red, WalkPoints);
        }
    }
}
