using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SortedChaining
{
    public class Cell
    {
        public int Key;
        public string Value;
        public Cell Next;

        public Cell(int key, string value, Cell next)
        {
            Key = key;
            Value = value;
            Next = next;
        }

        public override string ToString()
        {
            return $"[{Key}:{Value}]";
        }
    }
}
