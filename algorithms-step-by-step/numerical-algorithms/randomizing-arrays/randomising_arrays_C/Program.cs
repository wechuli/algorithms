using System;

namespace randomising_arrays_C
{
    class Program
    {
        static void Main(string[] args)
        {

            string[] myarray = new string[] { "Caro", "Mary", "Mercy", "Jess", "Eve", "Carole", "Faith", "June" };
            string[] newArray = RandomizeValues(myarray);
            foreach (var girl in newArray)
            {
                Console.Write($"{girl} ");
            }
        }

        static string[] RandomizeValues(string[] array)
        {
            var random = new Random();
            int arrayLength = array.Length;
            for (var i = 0; i < arrayLength - 1; i++)
            {
                int randomPosition = random.Next(i, arrayLength);
                var randValue = array[randomPosition];
                array[randomPosition] = array[i];
                array[i] = randValue;
            }

            return array;
        }
    }
}
