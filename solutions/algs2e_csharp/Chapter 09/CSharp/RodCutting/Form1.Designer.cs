namespace RodCutting
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
            this.label3 = new System.Windows.Forms.Label();
            this.rodLengthTextBox = new System.Windows.Forms.TextBox();
            this.cutButton = new System.Windows.Forms.Button();
            this.valuesTextBox = new System.Windows.Forms.TextBox();
            this.label5 = new System.Windows.Forms.Label();
            this.cutsTextBox = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.bestValueTextBox = new System.Windows.Forms.TextBox();
            this.label2 = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(12, 43);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(43, 13);
            this.label3.TabIndex = 3;
            this.label3.Text = "Length:";
            // 
            // rodLengthTextBox
            // 
            this.rodLengthTextBox.Location = new System.Drawing.Point(61, 40);
            this.rodLengthTextBox.Name = "rodLengthTextBox";
            this.rodLengthTextBox.Size = new System.Drawing.Size(37, 20);
            this.rodLengthTextBox.TabIndex = 1;
            this.rodLengthTextBox.Text = "10";
            this.rodLengthTextBox.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // cutButton
            // 
            this.cutButton.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.cutButton.Location = new System.Drawing.Point(247, 12);
            this.cutButton.Name = "cutButton";
            this.cutButton.Size = new System.Drawing.Size(75, 23);
            this.cutButton.TabIndex = 2;
            this.cutButton.Text = "Cut";
            this.cutButton.UseVisualStyleBackColor = true;
            this.cutButton.Click += new System.EventHandler(this.cutButton_Click);
            // 
            // valuesTextBox
            // 
            this.valuesTextBox.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.valuesTextBox.Location = new System.Drawing.Point(61, 14);
            this.valuesTextBox.Name = "valuesTextBox";
            this.valuesTextBox.Size = new System.Drawing.Size(180, 20);
            this.valuesTextBox.TabIndex = 0;
            this.valuesTextBox.Text = "1 5 8 9 10 17 17 20 25 26 31 32 35 39 40 44 46 48 55 58 60 63 67 70 72";
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Location = new System.Drawing.Point(12, 17);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(42, 13);
            this.label5.TabIndex = 8;
            this.label5.Text = "Values:";
            // 
            // cutsTextBox
            // 
            this.cutsTextBox.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.cutsTextBox.Location = new System.Drawing.Point(61, 98);
            this.cutsTextBox.Name = "cutsTextBox";
            this.cutsTextBox.Size = new System.Drawing.Size(180, 20);
            this.cutsTextBox.TabIndex = 3;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(12, 101);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(31, 13);
            this.label1.TabIndex = 12;
            this.label1.Text = "Cuts:";
            // 
            // bestValueTextBox
            // 
            this.bestValueTextBox.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.bestValueTextBox.Location = new System.Drawing.Point(61, 124);
            this.bestValueTextBox.Name = "bestValueTextBox";
            this.bestValueTextBox.Size = new System.Drawing.Size(180, 20);
            this.bestValueTextBox.TabIndex = 4;
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(12, 127);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(42, 13);
            this.label2.TabIndex = 10;
            this.label2.Text = "Values:";
            // 
            // Form1
            // 
            this.AcceptButton = this.cutButton;
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(334, 161);
            this.Controls.Add(this.cutsTextBox);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.bestValueTextBox);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.valuesTextBox);
            this.Controls.Add(this.label5);
            this.Controls.Add(this.cutButton);
            this.Controls.Add(this.rodLengthTextBox);
            this.Controls.Add(this.label3);
            this.Name = "Form1";
            this.Text = "RodCutting";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.TextBox rodLengthTextBox;
        private System.Windows.Forms.Button cutButton;
        private System.Windows.Forms.TextBox valuesTextBox;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.TextBox cutsTextBox;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TextBox bestValueTextBox;
        private System.Windows.Forms.Label label2;
    }
}

