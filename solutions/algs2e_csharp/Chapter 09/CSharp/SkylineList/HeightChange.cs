using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using System.Drawing;

namespace SkylineList
{
    class HeightChange : IComparable<HeightChange>
    {
        public bool Starting;
        public Rectangle Rectangle;
        public int X;

        public HeightChange(bool starting, Rectangle rect)
        {
            Starting = starting;
            Rectangle = rect;
            if (starting) X = rect.Left;
            else X = rect.Right;
        }

        public int CompareTo(HeightChange other)
        {
            return this.X.CompareTo(other.X);
        }

        public override string ToString()
        {
            if (Starting) return $"Starting ({Rectangle.Left}, {Rectangle.Y})";
            return $"Ending ({Rectangle.Right}, {Rectangle.Y})";
        }
    }
}
