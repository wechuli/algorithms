using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SelfOrganizingLists
{
    // A linked list that moves the most
    // recently accessed value to the top.
    public class MtfList : OrganizingList
    {
        // Move the found cell to the top of the list.
        public override void Rearrange(Cell cell)
        {
            // Don't bother if the cell is already at the top.
            if (cell == Sentinel.Next) return;

            // Remove the cell from its current position.
            cell.Remove();

            // Move the cell to the top.
            cell.Insert(Sentinel, Sentinel.Next);
        }
    }
}
