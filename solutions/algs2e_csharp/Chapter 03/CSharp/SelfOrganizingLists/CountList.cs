using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SelfOrganizingLists
{
    // A linked list that moves found items up
    // in the list until their counts are ordered.
    public class CountList : OrganizingList
    {
        // Intialize the sentinel's count.
        public CountList() : base()
        {
            Sentinel.Count = int.MaxValue;
        }

        // Swap the found cell with the cell
        // before it until the counts are ordered.
        public override void Rearrange(Cell cell)
        {
            // Increment the count.
            cell.Count++;

            // Swap the cell up as long as its count is
            // greater than the count of the cell before it.
            while (cell.Count > cell.Prev.Count)
                SwapCells(cell.Prev, cell);
        }
    }
}
