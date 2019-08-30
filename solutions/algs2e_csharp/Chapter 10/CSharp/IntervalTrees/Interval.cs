using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using System.Drawing;

namespace IntervalTrees
{
    // Represent a horizontal segment composed of two points.
    class Interval
    {
        public Point LeftPoint, RightPoint;
        public Pen Pen = Pens.Black;

        public Interval(Pen pen, Point point1, Point point2)
        {
            Pen = pen;

            // Save the points in order.
            if (point1.X < point2.X)
            {
                LeftPoint = point1;
                RightPoint = point2;
            }
            else
            {
                LeftPoint = point2;
                RightPoint = point1;
            }
        }

        public override string ToString()
        {
            return $"({LeftPoint.X}, {LeftPoint.Y})--({RightPoint.X}, {RightPoint.Y})";
        }
    }
}
