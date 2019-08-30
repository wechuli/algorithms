namespace PolynomialLeastSquares
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
            this.resetButton = new System.Windows.Forms.Button();
            this.solveButton = new System.Windows.Forms.Button();
            this.label2 = new System.Windows.Forms.Label();
            this.label1 = new System.Windows.Forms.Label();
            this.graphPictureBox = new System.Windows.Forms.PictureBox();
            this.degreeTextBox = new System.Windows.Forms.TextBox();
            this.aValueListBox = new System.Windows.Forms.ListBox();
            ((System.ComponentModel.ISupportInitialize)(this.graphPictureBox)).BeginInit();
            this.SuspendLayout();
            // 
            // resetButton
            // 
            this.resetButton.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)));
            this.resetButton.Location = new System.Drawing.Point(197, 278);
            this.resetButton.Name = "resetButton";
            this.resetButton.Size = new System.Drawing.Size(75, 23);
            this.resetButton.TabIndex = 60;
            this.resetButton.Text = "Reset";
            this.resetButton.UseVisualStyleBackColor = true;
            this.resetButton.Click += new System.EventHandler(this.resetButton_Click);
            // 
            // solveButton
            // 
            this.solveButton.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)));
            this.solveButton.Location = new System.Drawing.Point(116, 278);
            this.solveButton.Name = "solveButton";
            this.solveButton.Size = new System.Drawing.Size(75, 23);
            this.solveButton.TabIndex = 59;
            this.solveButton.Text = "Solve";
            this.solveButton.UseVisualStyleBackColor = true;
            this.solveButton.Click += new System.EventHandler(this.solveButton_Click);
            // 
            // label2
            // 
            this.label2.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)));
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(12, 306);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(22, 13);
            this.label2.TabIndex = 65;
            this.label2.Text = "As:";
            // 
            // label1
            // 
            this.label1.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)));
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(12, 283);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(45, 13);
            this.label1.TabIndex = 64;
            this.label1.Text = "Degree:";
            // 
            // graphPictureBox
            // 
            this.graphPictureBox.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.graphPictureBox.BackColor = System.Drawing.Color.White;
            this.graphPictureBox.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.graphPictureBox.Location = new System.Drawing.Point(12, 12);
            this.graphPictureBox.Name = "graphPictureBox";
            this.graphPictureBox.Size = new System.Drawing.Size(260, 260);
            this.graphPictureBox.TabIndex = 63;
            this.graphPictureBox.TabStop = false;
            this.graphPictureBox.Paint += new System.Windows.Forms.PaintEventHandler(this.graphPictureBox_Paint);
            this.graphPictureBox.MouseClick += new System.Windows.Forms.MouseEventHandler(this.graphPictureBox_MouseClick);
            // 
            // degreeTextBox
            // 
            this.degreeTextBox.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)));
            this.degreeTextBox.Location = new System.Drawing.Point(63, 280);
            this.degreeTextBox.Name = "degreeTextBox";
            this.degreeTextBox.Size = new System.Drawing.Size(38, 20);
            this.degreeTextBox.TabIndex = 66;
            this.degreeTextBox.Text = "3";
            this.degreeTextBox.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            this.degreeTextBox.TextChanged += new System.EventHandler(this.degreeTextBox_TextChanged);
            // 
            // asListBox
            // 
            this.aValueListBox.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.aValueListBox.FormattingEnabled = true;
            this.aValueListBox.IntegralHeight = false;
            this.aValueListBox.Location = new System.Drawing.Point(63, 306);
            this.aValueListBox.Name = "asListBox";
            this.aValueListBox.Size = new System.Drawing.Size(209, 106);
            this.aValueListBox.TabIndex = 67;
            // 
            // Form1
            // 
            this.AcceptButton = this.solveButton;
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(284, 424);
            this.Controls.Add(this.aValueListBox);
            this.Controls.Add(this.degreeTextBox);
            this.Controls.Add(this.resetButton);
            this.Controls.Add(this.solveButton);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.graphPictureBox);
            this.Name = "Form1";
            this.Text = "PolynomialLeastSquares";
            ((System.ComponentModel.ISupportInitialize)(this.graphPictureBox)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button resetButton;
        private System.Windows.Forms.Button solveButton;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.PictureBox graphPictureBox;
        private System.Windows.Forms.TextBox degreeTextBox;
        private System.Windows.Forms.ListBox aValueListBox;
    }
}

