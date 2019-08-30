using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DynamicRodCutting
{
    public class Cut
    {
        public int Length1, Length2, Value;

        public Cut(int length1, int length2, int value)
        {
            Length1 = length1;
            Length2 = length2;
            Value = value;
        }

        public override string ToString()
        {
            return $"[{Length1}+{Length2}: {Value}]";
        }
    }
}
