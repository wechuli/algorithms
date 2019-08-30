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

namespace TriangleWalk
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // The walk's points.
        private PointF[] WalkPoints = null;

        // Make a new walk.
        private void drawButton_Click(object sender, EventArgs e)
        {
            int stepSize = int.Parse(stepSizeTextBox.Text);
            int numSteps = int.Parse(numStepsTextBox.Text);

            WalkPoints = new PointF[numSteps];
            float x = walkPictureBox.ClientSize.Width / 2;
            float y = walkPictureBox.ClientSize.Height / 2;
            WalkPoints[0] = new PointF(x, y);

            float angleY = (float)(stepSize * Math.Sin(Math.PI / 3));
            float angleX = (float)(stepSize * Math.Cos(Math.PI / 3));

            Random rand = new Random();
            for (int i = 1; i < numSteps; i++)
            {
                switch (rand.Next(6))
                {
                    case 0:     // Northeast
                        y -= angleY;
                        x += angleX;
                        break;
                    case 1:     // East
                        x += stepSize;
                        break;
                    case 2:     // Southeast
                        y += angleY;
                        x += angleX;
                        break;
                    case 3:     // Southwest
                        y += angleY;
                        x -= angleX;
                        break;
                    case 4:     // West
                        x -= stepSize;
                        break;
                    default:    // Northwest
                        y -= angleY;
                        x -= angleX;
                        break;
                }
                WalkPoints[i] = new PointF(x, y);
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
