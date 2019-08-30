using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SortedChaining
{
    class MyHashTable
    {
        public int NumBuckets, NumUsed;
        public Cell[] Buckets;

        public MyHashTable(int numBuckets)
        {
            NumBuckets = numBuckets;
            NumUsed = 0;
            Buckets = new Cell[NumBuckets];
            for (int i = 0; i < NumBuckets; i++)
            {
                Cell bottomSentinel = new Cell(int.MaxValue, "*", null);
                Buckets[i] = new Cell(int.MinValue, "*", bottomSentinel);
            }
        }

        // Add an item to the hash table.
        // Throw an exception if the item is already in the table.
        public void Add(int key, string value, out int numProbes)
        {
            // Find the cell before where this key belongs.
            Cell cellBefore = FindCellBefore(key, out numProbes);
            numProbes++;

            // Make sure the item isn't already in the table.
            if (cellBefore.Next.Key == key)
                throw new ArgumentException(
                    $"The key {key} is already in the hash table.");

            // Add the item.
            Cell newCell = new Cell(key, value, cellBefore.Next);
            cellBefore.Next = newCell;

            // Update NumUsed.
            NumUsed++;
        }

        // Return the item's cell or null if it's not present.
        public Cell Find(int key, out int numProbes)
        {
            // Find the cell before this one.
            Cell cellBefore = FindCellBefore(key, out numProbes);
            numProbes++;
            if (cellBefore.Next.Key != key) return null;

            // Return the cell.
            return cellBefore.Next;
        }

        // Delete an item and return the number of probes required.
        // Throw an exception if the item isn't in the hash table.
        public void Delete(int key, out int numProbes)
        {
            // Find the cell before the target cell.
            Cell cellBefore = FindCellBefore(key, out numProbes);

            // See if the item is present.
            if (cellBefore.Next.Key != key)
                throw new ArgumentException(
                    $"The key {key} is not in the hash table.");

            // Remove the target cell.
            numProbes++;
            cellBefore.Next = cellBefore.Next.Next;

            // Update NumUsed.
            NumUsed--;
        }

        // Return the cell before the one containing the key.
        // If the key is not present, return the cell before
        // where this key belongs.
        private Cell FindCellBefore(int key, out int numProbes)
        {
            // Find the key's bucket.
            int bucketNum = key % NumBuckets;
            Cell sentinel = Buckets[bucketNum];

            // Find the desired cell.
            numProbes = 0;
            Cell cell = sentinel;
            while (cell.Next.Key < key)
            {
                numProbes++;
                cell = cell.Next;
            }
            return cell;
        }

        // Return a textual representation of the table.
        public override string ToString()
        {
            string text = "";
            for (int i = 0; i < NumBuckets; i++)
            {
                text += ">";
                for (Cell cell = Buckets[i].Next;
                    cell.Next != null;
                    cell = cell.Next)
                {
                    text += $" {cell}";
                }
                text += Environment.NewLine;
            }
            return text;
        }

        // Return the average number of keys per bucket.
        public float AverageBucketSize()
        {
            return NumUsed / (float)NumBuckets;
        }

        // Return the average probe sequence for the given values.
        public void GetSequenceLengths(int minValue, int maxValue,
            out float aveLength, out int maxLength)
        {
            int totalProbes = 0;
            maxLength = 0;
            for (int key = minValue; key <= maxValue; key++)
            {
                int numProbes;
                Find(key, out numProbes);
                totalProbes += numProbes;
                if (maxLength < numProbes) maxLength = numProbes;
            }

            aveLength = totalProbes / (maxValue - minValue + 1f);
        }
    }
}
