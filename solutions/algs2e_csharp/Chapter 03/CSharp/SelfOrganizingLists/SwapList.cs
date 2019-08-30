using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SelfOrganizingLists
{
    // A linked list that swaps the most recently
    // found item with the item before it.
    public class SwapList : OrganizingList
    {
        // Swap the found cell with the cell before it.
        public override void Rearrange(Cell cell)
        {
            // Don't bother if the cell is already at the top.
            if (cell.Prev == Sentinel) return;

            SwapCells(cell.Prev, cell);
        }
    }
}
