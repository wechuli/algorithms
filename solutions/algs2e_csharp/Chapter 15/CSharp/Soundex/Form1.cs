using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Soundex
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // Encode some sample names.
        private void Form1_Load(object sender, EventArgs e)
        {
            string[] names =
            {
                "Robert", "Rupert", "Rubin", "Ashcraft",
                "Ashcroft", "Tymczak", "Pfister", "Honeyman",
                "Smith", "Smyth", "Smithe", "Smythe",
                "Allricht", "Kavanagh", "McGee", "Schafer",
                "Eberhard", "Lind", "OBrien","Shaeffer",
                "Hanselmann", "Lukaschowsky", "Oppenheimer", "Zita",
                "Heimbach", "McDonnell", "Riedemanas", "Zitzmeinn",
            };
            string[] desiredResults =
            {
                "R163", "R163", "R150", "A261",
                "A261", "T522", "P236", "H555",
                "S530", "S530", "S530", "S530",
                "A462", "K152", "M200", "S160",
                "E166", "L530", "O165", "S160",
                "H524", "L222", "O155", "Z300",
                "H512", "M235", "R355", "Z325",
            };

            // Run tests.
            for (int i = 0; i < names.Length; i++)
            {
                ListViewItem item = resultsListView.Items.Add(names[i]);
                item.SubItems.Add(Soundex(names[i]));
                item.SubItems.Add(desiredResults[i]);
            }
        }

        // Return the name's Soundex encoding.
        private string Soundex(string name)
        {
            // Save the first letter.
            string firstLetter = name.Substring(0, 1).ToUpper();

            // Convert to lower case.
            name = name.ToLower();

            // Remove w and h after the first character.
            string nameAfter1 = name.Substring(1);
            nameAfter1 = nameAfter1.Replace("w", "");
            nameAfter1 = nameAfter1.Replace("h", "");
            name = name.Substring(0, 1) + nameAfter1;

            // Encode the letters.
            name = EncodeLetters(name);

            // Remove adjacent duplicate codes.
            name = RemoveAdjacentDuplicates(name);

            // Replace the first code with the original letter.
            name = firstLetter + name.Substring(1);

            // Remove vowels (after the first letter).
            name = name.Replace("0", "");

            // Pad to 4 characters.
            name = (name + "000").Substring(0, 4);

            return name;
        }

        // Remove adjacent duplicate codes.
        private string RemoveAdjacentDuplicates(string name)
        {
            int j = 1;
            while (j < name.Length)
            {
                if (name[j] == name[j - 1])
                    name = name.Remove(j, 1);
                else
                    j++;
            }
            return name;
        }

        // Character codes.
        private string[] CharacterCodes =
        {
            "aeiouy",    // Vowels map to 0.
            "bfpv",      // 1
            "cgjkqsxz",  // 2
            "dt",        // 3
            "l",         // 4
            "mn",        // 5
            "r",         // 6
        };

        // Return a character's code.
        // If the character has no code, return it.
        private string CharacterCode(char ch)
        {
            for (int i = 0; i < CharacterCodes.Length; i++)
                if (CharacterCodes[i].Contains(ch))
                    return i.ToString();
            return ch.ToString();
        }

        // Encode the letters in a string.
        private string EncodeLetters(string name)
        {
            // Encode the letters.
            string result = "";
            foreach (char ch in name)
                result += CharacterCode(ch);
            return result;
        }
    }
}
