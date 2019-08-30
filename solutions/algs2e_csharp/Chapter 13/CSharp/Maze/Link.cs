using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using System.Drawing;

namespace Maze
{
    class Link
    {
        public Node Node1, Node2;
        public Link(Node node1, Node node2)
        {
            Node1 = node1;
            Node2 = node2;
        }

        public override string ToString()
        {
            return $"{Node1.ToString()} --> {Node2.ToString()}";
        }
    }
}
