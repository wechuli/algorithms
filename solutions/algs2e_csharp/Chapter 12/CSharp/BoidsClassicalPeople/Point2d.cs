using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using System.Drawing;

namespace BoidsClassicalPeople
{
    class Point2d
    {
        public double X, Y;

        public Point2d()
        {
            X = 0;
            Y = 0;
        }
        public Point2d(double x, double y)
        {
            X = x;
            Y = y;
        }
        public Point2d(Point point)
        {
            X = point.X;
            Y = point.Y;
        }

        public static Point2d operator +(Point2d p, Vector2d v)
        {
            return new Point2d(p.X + v.X, p.Y + v.Y);
        }
        public static Point2d operator +(Point2d p1, Point2d p2)
        {
            return new Point2d(p1.X + p2.X, p1.Y + p2.Y);
        }
        public static Vector2d operator -(Point2d p1, Point2d p2)
        {
            return new Vector2d(p1.X - p2.X, p1.Y - p2.Y);
        }
        public static Point2d operator *(Point2d p, double scale)
        {
            return new Point2d(p.X * scale, p.Y * scale);
        }
        public static Point2d operator /(Point2d p, double scale)
        {
            return new Point2d(p.X / scale, p.Y / scale);
        }

        public override string ToString()
        {
            return $"({X}, {Y})";
        }
    }
}
