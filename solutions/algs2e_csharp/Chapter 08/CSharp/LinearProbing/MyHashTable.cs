using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LinearProbing
{
    class MyHashTable
    {
        public int NumEntries, NumUsed;
        public DataItem[] Table;

        public MyHashTable(int numEntries)
        {
            NumEntries = numEntries;
            NumUsed = 0;
            Table = new DataItem[NumEntries];
        }

        // Add an item to the hash table.
        // Throw an exception if the item is already in the table.
        public void Add(int key, string value, out int numProbes)
        {
            // See if the table is full.
            if (NumUsed == NumEntries)
                throw new IndexOutOfRangeException(
                    $"Cannot add key {key}. The hash table is full.");

            int probe = key % NumEntries;
            int stride = 1;
            numProbes = 0;
            for (;;)
            {
                numProbes++;

                // See if this spot is empty.
                if (Table[probe] == null)
                {
                    // Put the value here.
                    Table[probe] = new DataItem(key, value);
                    NumUsed++;
                    return;
                }

                // See if the target key is here.
                if (Table[probe].Key == key)
                    throw new ArgumentException(
                        $"Key {key} is already in the hash table at index {probe}. ({numProbes} probes.)");

                // Try the next probe.
                probe = (probe + stride) % NumEntries;
            }
        }

        // Return the item's cell or null if it's not present.
        public DataItem Find(int key, out int numProbes)
        {
            int probe = key % NumEntries;
            int stride = 1;
            numProbes = 0;
            for (;;)
            {
                numProbes++;

                // See if this spot is empty.
                if (Table[probe] == null)
                    // The key isn't in the table.
                    return null;

                // See if the key is here.
                if (Table[probe].Key == key)
                    // We found the key.
                    return Table[probe];

                if (numProbes == NumEntries)
                    // The key isn't in the table (and the table is full).
                    return null;

                // Try the next probe.
                probe = (probe + stride) % NumEntries;
            }
        }

        // Return a textual representation of the table.
        public override string ToString()
        {
            string text = "";
            for (int i = 0; i < NumEntries; i++)
            {
                if (Table[i] == null)
                    text += "[--------] ";
                else
                    text += $"{Table[i]} ";

                if ((i + 1) % 10 == 0)
                    text = text.Substring(0, text.Length - 1) +
                        Environment.NewLine;
            }
            return text;
        }

        // Return the fill percentage.
        public float FillPercentage()
        {
            return 100f * NumUsed / NumEntries;
        }

        // Return the average and maximum sequence lengths for the given values.
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
