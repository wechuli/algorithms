using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using System.Drawing;

namespace FindCliqueBruteForce
{
    class Node
    {
        public static int Radius = 10;
        public String Name;
        public Point Location;
        public List<Node> Neighbors = new List<Node>();

        public Brush BgBrush = Brushes.White;
        public Brush TextBrush = Brushes.Black;
        public Pen FgPen = Pens.Black;
        public Pen LinkPen = Pens.Blue;
        public Font Font;

        public Node(string name, Point location, Font font)
        {
            Name = name;
            Location = location;
            Font = font;
        }

        // Add an undirected link between these nodes.
        public void AddLink(Node other)
        {
            Neighbors.Add(other);
            other.Neighbors.Add(this);
        }

        // Draw the node's links.
        public void DrawLinks(Graphics gr)
        {
            foreach (Node neighbor in Neighbors)
            {
                // Draw each link only once.
                if (Name.CompareTo(neighbor.Name) < 0)
                    gr.DrawLine(LinkPen, Location, neighbor.Location);
            }
        }

        // Draw the node.
        public void DrawNode(Graphics gr)
        {
            Rectangle rect = new Rectangle(
                Location.X - Radius, Location.Y - Radius,
                2 * Radius, 2 * Radius);
            gr.FillEllipse(BgBrush, rect);
            gr.DrawEllipse(FgPen, rect);
            using (StringFormat sf = new StringFormat())
            {
                sf.Alignment = StringAlignment.Center;
                sf.LineAlignment = StringAlignment.Center;
                gr.DrawString(Name, Font, TextBrush, rect, sf);
            }
        }
    }
}
