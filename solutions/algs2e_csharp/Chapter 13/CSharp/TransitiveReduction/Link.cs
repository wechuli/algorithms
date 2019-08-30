using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using System.Drawing;

namespace TransitiveReduction
{
    class Link
    {
        public Node FromNode, ToNode;
        public float Length;

        public Pen Pen = Pens.Blue;
        public Brush Brush = Brushes.Blue;

        public Link(Node fromNode, Node toNode)
        {
            FromNode = fromNode;
            ToNode = toNode;

            float dx = FromNode.Location.X - ToNode.Location.X;
            float dy = FromNode.Location.Y - ToNode.Location.Y;
            Length = (float)Math.Sqrt(dx * dx + dy * dy);
        }

        // Draw an arrow between two nodes.
        public void Draw(Graphics gr, float radius)
        {
            // Find the end points.
            float dx = ToNode.Location.X - FromNode.Location.X;
            float dy = ToNode.Location.Y - FromNode.Location.Y;
            float length = (float)Math.Sqrt(dx * dx + dy * dy);
            dx /= length;
            dy /= length;
            PointF end1 = new PointF(
                FromNode.Location.X + dx * radius,
                FromNode.Location.Y + dy * radius);
            PointF end2 = new PointF(
                ToNode.Location.X - dx * radius,
                ToNode.Location.Y - dy * radius);
            PointF[] arrowhead =
            {
                new PointF(
                    end2.X - radius * dx + radius * dy / 2,
                    end2.Y - radius * dy - radius * dx / 2),
                end2,
                new PointF(
                    end2.X - radius * dx - radius * dy / 2,
                    end2.Y - radius * dy + radius * dx / 2),
            };
            gr.DrawLine(Pen, end1, end2);
            gr.FillPolygon(Brush, arrowhead);
        }
    }
}
