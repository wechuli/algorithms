using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace OneTimePad
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // The ont-time pad.
        private string PadString;

        // The number of offsets used to encrypt and decrypt.
        private int NumUsedToEncrypt, NumUsedToDecrypt;

        // Initialize the one-time pad.
        private void Form1_Load(object sender, EventArgs e)
        {
            // Initialize the pad.
            PadString = "GCMURLJYCQAGIZRRHPSSYCEJUEUHVXOSSAZUWBNNHZRKLRRMGJNEJRKEYCZMQBDFCIOHZWUFCELYKUYDMIBMJKJAQVWUCAXFWMHDDJMJOHBEGLTEDWZIZQWSYOREAADBHFCYMVZDVSXBIFTECRQGAOGFQPEPRIJNEZWBJVSIWWMHTUJTUNCIKXBSYWHWQKLNIJWIIRVG";
            NumUsedToEncrypt = 0;
            NumUsedToDecrypt = 0;

            // Display the pad.
            DisplayPad();
        }

        // Encrypt.
        private void encryptButton_Click(object sender, EventArgs e)
        {
            string message = messageTextBox.Text.ToUpper().Replace(" ", "");
            string ciphertext = Encrypt(PadString, NumUsedToEncrypt, message);
            ciphertextTextBox.Text = ToNGrams(ciphertext);
            plaintextTextBox.Clear();

            NumUsedToEncrypt += ciphertext.Length;
            DisplayPad();
        }

        // Decrypt.
        private void decryptButton_Click(object sender, EventArgs e)
        {
            string ciphertext = ciphertextTextBox.Text;
            string plaintext = Decrypt(PadString, NumUsedToDecrypt, ciphertext);
            plaintextTextBox.Text = ToNGrams(plaintext);

            NumUsedToDecrypt += plaintext.Length;
            DisplayPad();
        }

        // Encrypt.
        private string Encrypt(string pad, int startIndex, string plaintext)
        {
            return EncryptDecrypt(pad, startIndex, plaintext, false);
        }

        // Decrypt.
        private string Decrypt(string pad, int startIndex, string ciphertext)
        {
            return EncryptDecrypt(pad, startIndex, ciphertext, true);
        }

        // Use the one-time pad to encrypt or decrypt the text.
        private string EncryptDecrypt(string pad, int startIndex, string text, bool decrypt)
        {
            text = text.ToUpper().Replace(" ", "");

            // Start at the right entry in the pad.
            int i = startIndex;

            // Make sure we have enough pad left for this message.
            if (i + text.Length > pad.Length)
            {
                MessageBox.Show("The pad doesn't contain enough unnused characters for this operation.");
                return "**********";
            }

            string result = "";
            foreach (char ch in text)
            {
                int chNum = ch - 'A';
                int padNum = pad[i] - 'A';

                int newCh;
                if (decrypt)
                    newCh = 'A' + (chNum - padNum + 26) % 26;
                else
                    newCh = 'A' + (chNum + padNum) % 26;
                result += (char)newCh;
                i++;
            }

            // Return the ciphertext.
            return result;
        }

        // Display the one-time pad.
        private void DisplayPad()
        {
            padRichTextBox.Text = PadString;
            padRichTextBox.Select(0, PadString.Length);
            padRichTextBox.SelectionColor = padRichTextBox.ForeColor;
            padRichTextBox.SelectionBackColor = padRichTextBox.BackColor;

            padRichTextBox.Select(0, NumUsedToEncrypt);
            padRichTextBox.SelectionColor = Color.Blue;

            padRichTextBox.Select(0, NumUsedToDecrypt);
            padRichTextBox.SelectionBackColor = Color.Yellow;
        }

        // Break the text into 5-character chunks.
        private string ToNGrams(string message)
        {
            // Pad the message in case its length isn't a multiple of 5.
            message += "     ";

            // Create the 5-character chunks.
            string result = "";
            for (int i = 0; i < message.Length - 5; i += 5)
                result += message.Substring(i, 5) + " ";

            // Remove trailing spaces.
            return result.TrimEnd();
        }
    }
}
