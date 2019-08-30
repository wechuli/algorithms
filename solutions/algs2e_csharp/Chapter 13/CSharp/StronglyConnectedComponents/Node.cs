using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using System.Drawing;

namespace StronglyConnectedComponents
{
    class Node
    {
        private const float Radius = 10;
        public string Name;
        public PointF Location;
        public List<Link> Links = new List<Link>();
        public List<Link> InLinks = new List<Link>();
        public bool Visited;
        public Node ComponentRoot;

        public Brush CircleBrush = Brushes.LightBlue;
        public Pen CirclePen = Pens.Blue;
        public Brush NameBrush = Brushes.Black;

        public Node(string name, PointF location)
        {
            Name = name;
            Location = location;
        }

        // Add a link to this node.
        public void AddLink(Node other)
        {
            Links.Add(new Link(this, other));
        }

        // Draw this node's links.
        public void DrawLinks(Graphics gr)
        {
            foreach (Link link in Links)
                link.Draw(gr, Radius);
        }

        // Draw this node's body.
        public void DrawNode(Graphics gr, Font font)
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
                gr.DrawString(Name, font, NameBrush, Location, sf);
            }
        }

        // Return true if the node is at this point.
        public bool IsAtPoint(PointF point)
        {
            float dx = Location.X - point.X;
            float dy = Location.Y - point.Y;
            return (Math.Sqrt(dx * dx + dy * dy) <= Radius);
        }

        public override string ToString()
        {
            return Name;
        }
    }
}
