﻿namespace Countingsort
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.maxItemTextBox = new System.Windows.Forms.TextBox();
            this.label2 = new System.Windows.Forms.Label();
            this.itemsListBox = new System.Windows.Forms.ListBox();
            this.sortButton = new System.Windows.Forms.Button();
            this.generateButton = new System.Windows.Forms.Button();
            this.numItemsTextBox = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // maxItemTextBox
            // 
            this.maxItemTextBox.Location = new System.Drawing.Point(78, 40);
            this.maxItemTextBox.Name = "maxItemTextBox";
            this.maxItemTextBox.Size = new System.Drawing.Size(58, 20);
            this.maxItemTextBox.TabIndex = 39;
            this.maxItemTextBox.Text = "1000";
            this.maxItemTextBox.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(12, 43);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(60, 13);
            this.label2.TabIndex = 38;
            this.label2.Text = "Max Value:";
            // 
            // itemsListBox
            // 
            this.itemsListBox.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.itemsListBox.FormattingEnabled = true;
            this.itemsListBox.Location = new System.Drawing.Point(12, 90);
            this.itemsListBox.Name = "itemsListBox";
            this.itemsListBox.Size = new System.Drawing.Size(208, 147);
            this.itemsListBox.TabIndex = 37;
            // 
            // sortButton
            // 
            this.sortButton.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.sortButton.Enabled = false;
            this.sortButton.Location = new System.Drawing.Point(145, 41);
            this.sortButton.Name = "sortButton";
            this.sortButton.Size = new System.Drawing.Size(75, 23);
            this.sortButton.TabIndex = 36;
            this.sortButton.Text = "Sort";
            this.sortButton.UseVisualStyleBackColor = true;
            this.sortButton.Click += new System.EventHandler(this.sortButton_Click);
            // 
            // generateButton
            // 
            this.generateButton.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.generateButton.Location = new System.Drawing.Point(145, 12);
            this.generateButton.Name = "generateButton";
            this.generateButton.Size = new System.Drawing.Size(75, 23);
            this.generateButton.TabIndex = 35;
            this.generateButton.Text = "Generate";
            this.generateButton.UseVisualStyleBackColor = true;
            this.generateButton.Click += new System.EventHandler(this.generateButton_Click);
            // 
            // numItemsTextBox
            // 
            this.numItemsTextBox.Location = new System.Drawing.Point(78, 14);
            this.numItemsTextBox.Name = "numItemsTextBox";
            this.numItemsTextBox.Size = new System.Drawing.Size(58, 20);
            this.numItemsTextBox.TabIndex = 34;
            this.numItemsTextBox.Text = "100000";
            this.numItemsTextBox.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(12, 17);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(45, 13);
            this.label1.TabIndex = 33;
            this.label1.Text = "# Items:";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(12, 74);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(117, 13);
            this.label3.TabIndex = 40;
            this.label3.Text = "Items (1000 items max):";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(232, 249);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.maxItemTextBox);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.itemsListBox);
            this.Controls.Add(this.sortButton);
            this.Controls.Add(this.generateButton);
            this.Controls.Add(this.numItemsTextBox);
            this.Controls.Add(this.label1);
            this.Name = "Form1";
            this.Text = "Countingsort";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.TextBox maxItemTextBox;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.ListBox itemsListBox;
        private System.Windows.Forms.Button sortButton;
        private System.Windows.Forms.Button generateButton;
        private System.Windows.Forms.TextBox numItemsTextBox;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label3;
    }
}

