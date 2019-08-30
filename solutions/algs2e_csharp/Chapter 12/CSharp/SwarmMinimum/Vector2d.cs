using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using System.Drawing;

namespace SwarmMinimum
{
    class Vector2d
    {
        public double X, Y;

        public Vector2d()
        {
            X = 0;
            Y = 0;
        }
        public Vector2d(double x, double y)
        {
            X = x;
            Y = y;
        }
        public Vector2d(Point2d p1, Point2d p2)
        {
            X = p2.X - p1.X;
            Y = p2.Y - p1.Y;
        }

        public static Vector2d operator +(Vector2d v1, Vector2d v2)
        {
            return new Vector2d(v1.X + v2.X, v1.Y + v2.Y);
        }

        public static Vector2d operator -(Vector2d v1, Vector2d v2)
        {
            return new Vector2d(v1.X - v2.X, v1.Y - v2.Y);
        }
        public static Vector2d operator -(Vector2d v1)
        {
            return new Vector2d(-v1.X, -v1.Y);
        }
        public static Vector2d operator *(Vector2d v, double scale)
        {
            return new Vector2d(v.X * scale, v.Y * scale);
        }
        public static Vector2d operator *(double scale, Vector2d v)
        {
            return new Vector2d(v.X * scale, v.Y * scale);
        }
        public static Vector2d operator /(Vector2d v, double scale)
        {
            return new Vector2d(v.X / scale, v.Y / scale);
        }
        public double Length
        {
            get
            {
                return Math.Sqrt(X * X + Y * Y);
            }
        }
        public void SetLength(double newLength)
        {
            double oldLength = Length;
            X *= newLength / oldLength;
            Y *= newLength / oldLength;
        }
        public void Normalize()
        {
            SetLength(1);
        }

        public override string ToString()
        {
            return $"<{X}, {Y}>";
        }
    }
}
