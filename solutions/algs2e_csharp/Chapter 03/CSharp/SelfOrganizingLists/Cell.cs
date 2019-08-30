using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SelfOrganizingLists
{
    // Store an item for a linked list.
    public class Cell
    {
        public Cell Next = null;
        public Cell Prev = null;
        public int Value = -1;
        public int Count = 0;

        public Cell(int value, Cell prev_cell, Cell next_cell)
        {
            Value = value;

            Prev = prev_cell;
            if (prev_cell != null) prev_cell.Next = this;

            Next = next_cell;
            if (next_cell != null) next_cell.Prev = this;
        }

        // Remove the cell from the list.
        public void Remove()
        {
            Prev.Next = Next;
            if (Next != null) Next.Prev = Prev;
        }

        // Insert the cell betweeen two others.
        public void Insert(Cell prev_cell, Cell after_cell)
        {
            prev_cell.Next = this;
            Next = after_cell;

            if (after_cell != null) after_cell.Prev = this;
            Prev = prev_cell;
        }

        public override string ToString()
        {
            return Value.ToString();
        }
    }
}
