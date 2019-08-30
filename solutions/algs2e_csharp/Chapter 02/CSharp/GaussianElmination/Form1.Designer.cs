namespace GaussianElmination
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
            this.coeffsTextBox = new System.Windows.Forms.TextBox();
            this.xsLabel = new System.Windows.Forms.Label();
            this.valuesTextBox = new System.Windows.Forms.TextBox();
            this.calculateButton = new System.Windows.Forms.Button();
            this.label1 = new System.Windows.Forms.Label();
            this.xListBox = new System.Windows.Forms.ListBox();
            this.checkListBox = new System.Windows.Forms.ListBox();
            this.label2 = new System.Windows.Forms.Label();
            this.errorsListBox = new System.Windows.Forms.ListBox();
            this.label3 = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // coeffsTextBox
            // 
            this.coeffsTextBox.Font = new System.Drawing.Font("Courier New", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.coeffsTextBox.Location = new System.Drawing.Point(12, 12);
            this.coeffsTextBox.Multiline = true;
            this.coeffsTextBox.Name = "coeffsTextBox";
            this.coeffsTextBox.Size = new System.Drawing.Size(140, 84);
            this.coeffsTextBox.TabIndex = 0;
            this.coeffsTextBox.Text = "   1   1   1  1 1\r\n  32  16   8  4 2\r\n 243  81  27  9 3\r\n1024 256  64 16 4\r\n3125 " +
    "625 125 25 5";
            // 
            // xsLabel
            // 
            this.xsLabel.Font = new System.Drawing.Font("Courier New", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.xsLabel.Location = new System.Drawing.Point(158, 12);
            this.xsLabel.Name = "xsLabel";
            this.xsLabel.Size = new System.Drawing.Size(35, 84);
            this.xsLabel.TabIndex = 1;
            this.xsLabel.Text = "x1";
            // 
            // valuesTextBox
            // 
            this.valuesTextBox.Font = new System.Drawing.Font("Courier New", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.valuesTextBox.Location = new System.Drawing.Point(199, 12);
            this.valuesTextBox.Multiline = true;
            this.valuesTextBox.Name = "valuesTextBox";
            this.valuesTextBox.Size = new System.Drawing.Size(51, 84);
            this.valuesTextBox.TabIndex = 2;
            this.valuesTextBox.Text = "  1\r\n -1\r\n  8\r\n-56\r\n569";
            this.valuesTextBox.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // calculateButton
            // 
            this.calculateButton.Anchor = System.Windows.Forms.AnchorStyles.Top;
            this.calculateButton.Location = new System.Drawing.Point(94, 102);
            this.calculateButton.Name = "calculateButton";
            this.calculateButton.Size = new System.Drawing.Size(75, 23);
            this.calculateButton.TabIndex = 3;
            this.calculateButton.Text = "Calculate";
            this.calculateButton.UseVisualStyleBackColor = true;
            this.calculateButton.Click += new System.EventHandler(this.calculateButton_Click);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(12, 140);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(22, 13);
            this.label1.TabIndex = 4;
            this.label1.Text = "Xs:";
            // 
            // xListBox
            // 
            this.xListBox.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.xListBox.FormattingEnabled = true;
            this.xListBox.IntegralHeight = false;
            this.xListBox.Location = new System.Drawing.Point(12, 156);
            this.xListBox.Name = "xListBox";
            this.xListBox.Size = new System.Drawing.Size(238, 70);
            this.xListBox.TabIndex = 5;
            // 
            // checkListBox
            // 
            this.checkListBox.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.checkListBox.FormattingEnabled = true;
            this.checkListBox.IntegralHeight = false;
            this.checkListBox.Location = new System.Drawing.Point(12, 245);
            this.checkListBox.Name = "checkListBox";
            this.checkListBox.Size = new System.Drawing.Size(238, 70);
            this.checkListBox.TabIndex = 7;
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(12, 229);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(41, 13);
            this.label2.TabIndex = 6;
            this.label2.Text = "Check:";
            // 
            // errorsListBox
            // 
            this.errorsListBox.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.errorsListBox.FormattingEnabled = true;
            this.errorsListBox.IntegralHeight = false;
            this.errorsListBox.Location = new System.Drawing.Point(12, 334);
            this.errorsListBox.Name = "errorsListBox";
            this.errorsListBox.Size = new System.Drawing.Size(238, 70);
            this.errorsListBox.TabIndex = 9;
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(12, 318);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(37, 13);
            this.label3.TabIndex = 8;
            this.label3.Text = "Errors:";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(262, 416);
            this.Controls.Add(this.errorsListBox);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.checkListBox);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.xListBox);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.calculateButton);
            this.Controls.Add(this.valuesTextBox);
            this.Controls.Add(this.xsLabel);
            this.Controls.Add(this.coeffsTextBox);
            this.Name = "Form1";
            this.Text = "GaussianElmination";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.TextBox coeffsTextBox;
        private System.Windows.Forms.Label xsLabel;
        private System.Windows.Forms.TextBox valuesTextBox;
        private System.Windows.Forms.Button calculateButton;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.ListBox xListBox;
        private System.Windows.Forms.ListBox checkListBox;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.ListBox errorsListBox;
        private System.Windows.Forms.Label label3;
    }
}

