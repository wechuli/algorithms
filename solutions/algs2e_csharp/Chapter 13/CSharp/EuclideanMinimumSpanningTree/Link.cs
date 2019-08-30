using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using System.Drawing;

namespace EuclideanMinimumSpanningTree
{
    class Link
    {
        public Node Node1, Node2;
        public float Length;
        public Link(Node node1, Node node2, float length)
        {
            Node1 = node1;
            Node2 = node2;
            Length = length;
        }

        public void Draw(Graphics gr, Pen pen)
        {
            gr.DrawLine(pen, Node1.Location, Node2.Location);
        }
    }
}
