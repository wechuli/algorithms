using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using System.Drawing;

namespace EuclideanMinimumSpanningTree
{
    class Node
    {
        public Point Location;
        public List<Link> Links = new List<Link>();
        public bool Visited = false;

        public Node(Point location)
        {
            Location = location;
        }
    }
}

