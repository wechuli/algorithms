using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using System.Diagnostics;

namespace SelfOrganizingLists
{
    // Base class for self-organizing lists.
    public class OrganizingList
    {
        // The lists's sentinel.
        public Cell Sentinel = new Cell(-1, null, null);

        // Return the list's values.
        public override string ToString()
        {
            StringBuilder sb = new StringBuilder();
            for (Cell cell = Sentinel.Next; cell != null; cell = cell.Next)
                sb.Append(cell.ToString() + " ");
            return sb.ToString();
        }

        // Return the expected search length for
        // the values with the given probabilities.
        public double ExpectedSearch(double[] probs)
        {
            double total = 0;
            int numSteps = 0;
            for (Cell cell = Sentinel.Next; cell != null; cell = cell.Next)
            {
                numSteps++;
                total += numSteps * probs[cell.Value];
            }
            return total;
        }

        // Add an item at the beginning of the list after the sentinel.
        public void Add(int value)
        {
            Cell cell = new Cell(value, Sentinel, Sentinel.Next);
        }

        // Rearrange the list appropriately.
        public virtual void Rearrange(Cell cell)
        {
        }

        // Find an item, move it appropriately, and
        // return the number of steps it took.
        public int Find(int value)
        {
            int numSteps = 1;
            Cell cell = Sentinel.Next;
            while ((cell != null) && (cell.Value != value))
            {
                numSteps++;
                cell = cell.Next;
            }

            // Rearrange the list appropriately.
            Debug.Assert(cell != null, $"Could not find item {value}.");
            if (cell != null) Rearrange(cell);

            return numSteps;
        }

        // Swap two cells.
        public void SwapCells(Cell cell1, Cell cell2)
        {
            cell1.Remove();
            cell1.Insert(cell2, cell2.Next);
        }
    }
}
