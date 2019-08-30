using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using System.Drawing;

namespace CloneNetworkDictionary
{
    class Node
    {
        private const float Radius = 10;
        public string Name;
        public PointF Location;
        public List<Node> Neighbors = new List<Node>();
        public Brush CircleBrush, NameBrush, ArrowheadBrush;
        public Pen CirclePen, LinkPen;
        public Font Font;

        public Node(string name, PointF location,
            Brush circleBrush, Brush nameBrush, Pen circlePen,
            Font font, Brush arrowheadBrush, Pen linkPen)
        {
            Name = name;
            Location = location;
            CircleBrush = circleBrush;
            NameBrush = nameBrush;
            CirclePen = circlePen;
            Font = font;
            ArrowheadBrush = arrowheadBrush;
            LinkPen = linkPen;
        }

        // Draw this node's links.
        public void DrawLinks(Graphics gr)
        {
            foreach (Node neighbor in Neighbors)
                DrawArrow(gr, Location, neighbor.Location, Radius);
        }

        // Draw this node's body.
        public void DrawNode(Graphics gr)
        {
            RectangleF rect = new RectangleF(
                Location.X - Radius, Location.Y - Radius,
                2 * Radius, 2 * Radius);
            gr.FillEllipse(CircleBrush, rect);
            gr.DrawEllipse(CirclePen, rect);
            using (StringFormat sf = new StringFormat())
            {
                sf.Alignment = StringAlignment.Center;
                sf.LineAlignment = StringAlignment.Center;
                gr.DrawString(Name, Font, NameBrush, Location, sf);
            }
        }

        // Draw an arrow between two nodes.
        private void DrawArrow(Graphics gr,
            PointF point1, PointF point2, float radius)
        {
            // Find the end points.
            float dx = point2.X - point1.X;
            float dy = point2.Y - point1.Y;
            float length = (float)Math.Sqrt(dx * dx + dy * dy);
            dx /= length;
            dy /= length;
            PointF end1 = new PointF(point1.X + dx * radius, point1.Y + dy * radius);
            PointF end2 = new PointF(point2.X - dx * radius, point2.Y - dy * radius);
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
            gr.DrawLine(LinkPen, end1, end2);
            gr.FillPolygon(ArrowheadBrush, arrowhead);
            // gr.DrawLines(LinkPen, arrowhead);
        }
    }
}
