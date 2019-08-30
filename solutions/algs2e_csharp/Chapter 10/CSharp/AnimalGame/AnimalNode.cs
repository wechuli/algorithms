using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AnimalGame
{
    public class AnimalNode
    {
        public string Question;
        public AnimalNode YesChild, NoChild;

        public AnimalNode(string question)
        {
            Question = question;
        }

        // Return the animal's name with an appropriate "a" or "an" in front.
        // This only works for leaf nodes.
        public string Name
        {
            get
            {
                string vowels = "aeiou";
                if (vowels.Contains(Question.ToLower()[0]))
                    return $"an {Question}";
                return $"a {Question}";
            }
        }
    }
}
