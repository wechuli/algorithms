using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LinearProbing
{
    class DataItem
    {
        public int Key;
        public string Value;

        public DataItem(int key, string value)
        {
            Key = key;
            Value = value;
        }

        public override string ToString()
        {
            return $"[{Key}:{Value}]";
        }
    }
}
