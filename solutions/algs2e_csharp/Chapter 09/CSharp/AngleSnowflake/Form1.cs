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
using System.Drawing.Imaging;

namespace AngleSnowflake
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void drawButton_Click(object sender, EventArgs e)
        {
            int depth = (int)depthNumericUpDown.Value;
            double theta = double.Parse(angleTextBox.Text);
            theta *= Math.PI / 180.0;

            Bitmap bm = new Bitmap(
                snowflakePictureBox.ClientSize.Width,
                snowflakePictureBox.ClientSize.Height);
            using (Graphics gr = Graphics.FromImage(bm))
            {
                gr.Clear(Color.White);
                gr.SmoothingMode = SmoothingMode.AntiAlias;
                using (Pen pen = new Pen(Color.Blue, 0))
                {
                    // Figure out where to put the corners.
                    const int margin = 10;
                    float canvas_width = bm.Width;
                    float canvas_height = bm.Height;
                    float area_width = canvas_width - 2 * margin;
                    float area_height = canvas_height - 2 * margin;

                    float radius = Math.Min(area_height, area_width) / 2f;

                    float cx = canvas_width / 2f;
                    float cy = canvas_height / 2f;

                    double angle120 = 120 * Math.PI / 180;
                    double angle240 = 240 * Math.PI / 180;
                    double alpha = (90 + 120) * Math.PI / 180;
                    PointF pt1 = new PointF(
                        (float)(cx + radius * Math.Cos(alpha)),
                        (float)(cy + radius * Math.Sin(alpha)));
                    alpha += angle120;
                    PointF pt2 = new PointF(
                        (float)(cx + radius * Math.Cos(alpha)),
                        (float)(cy + radius * Math.Sin(alpha)));
                    alpha += angle120;
                    PointF pt3 = new PointF(
                        (float)(cx + radius * Math.Cos(alpha)),
                        (float)(cy + radius * Math.Sin(alpha)));

                    // Draw the sides.
                    float triangle_width = (float)(2 * radius * Math.Sqrt(3) / 2);
                    DrawKoch(gr, pen, depth, theta, pt1, 0, triangle_width);
                    DrawKoch(gr, pen, depth, theta, pt2, angle120, triangle_width);
                    DrawKoch(gr, pen, depth, theta, pt3, angle240, triangle_width);
                }
            }
            snowflakePictureBox.Image = bm;
            bm.Save("KochSnowflake" + depth.ToString() + ".jpg", ImageFormat.Png);
        }

        private void DrawKoch(Graphics gr, Pen pen, int depth, double theta, PointF pt1, double angle, float length)
        {
            if (depth == 0)
            {
                PointF pt2 = new PointF(
                    (float)(pt1.X + length * Math.Cos(angle)),
                    (float)(pt1.Y + length * Math.Sin(angle)));
                gr.DrawLine(pen, pt1, pt2);
            }
            else
            {
                float newLength = (float)(length / 2.0 / (1.0 + Math.Cos(theta)));

                PointF pt2 = new PointF(
                    (float)(pt1.X + newLength * Math.Cos(angle)),
                    (float)(pt1.Y + newLength * Math.Sin(angle)));

                double theta1 = angle - theta;
                double theta2 = angle + theta;
                PointF pt3 = new PointF(
                    (float)(pt2.X + newLength * Math.Cos(theta1)),
                    (float)(pt2.Y + newLength * Math.Sin(theta1)));

                PointF pt4 = new PointF(
                    (float)(pt3.X + newLength * Math.Cos(theta2)),
                    (float)(pt3.Y + newLength * Math.Sin(theta2)));

                DrawKoch(gr, pen, depth - 1, theta, pt1, angle, newLength);
                DrawKoch(gr, pen, depth - 1, theta, pt2, theta1, newLength);
                DrawKoch(gr, pen, depth - 1, theta, pt3, theta2, newLength);
                DrawKoch(gr, pen, depth - 1, theta, pt4, angle, newLength);
            }
        }
    }
}
