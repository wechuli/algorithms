using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using System.Drawing;

namespace Maze
{
    class Node
    {
        public int Row, Column;
        public List<Link> Links = new List<Link>();
        public bool Visited = false;

        public Node(int row, int column)
        {
            Row = row;
            Column = column;
        }

        public override string ToString()
        {
            return $"({Row}, {Column})";
        }
    }
}
