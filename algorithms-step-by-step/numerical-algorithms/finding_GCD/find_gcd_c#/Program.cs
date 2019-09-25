using System;

namespace find_gcd_c_
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine(FindGCDOfTwoNumbers(4851, 3003));
        }

        static int FindGCDOfTwoNumbers(int number1, int number2)
        {
            while (number2 != 0)
            {
                int remainder = number1 % number2;
                number1 = number2;
                number2 = remainder;
            }
            return number1;
        }
    }
}
