namespace LinearLeastSquares
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
            this.solveButton = new System.Windows.Forms.Button();
            this.bTextBox = new System.Windows.Forms.TextBox();
            this.label2 = new System.Windows.Forms.Label();
            this.mTextBox = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.graphPictureBox = new System.Windows.Forms.PictureBox();
            this.resetButton = new System.Windows.Forms.Button();
            ((System.ComponentModel.ISupportInitialize)(this.graphPictureBox)).BeginInit();
            this.SuspendLayout();
            // 
            // solveButton
            // 
            this.solveButton.Anchor = System.Windows.Forms.AnchorStyles.Bottom;
            this.solveButton.Location = new System.Drawing.Point(64, 278);
            this.solveButton.Name = "solveButton";
            this.solveButton.Size = new System.Drawing.Size(75, 23);
            this.solveButton.TabIndex = 0;
            this.solveButton.Text = "Solve";
            this.solveButton.UseVisualStyleBackColor = true;
            this.solveButton.Click += new System.EventHandler(this.solveButton_Click);
            // 
            // bTextBox
            // 
            this.bTextBox.Anchor = System.Windows.Forms.AnchorStyles.Bottom;
            this.bTextBox.Location = new System.Drawing.Point(195, 307);
            this.bTextBox.Name = "bTextBox";
            this.bTextBox.ReadOnly = true;
            this.bTextBox.Size = new System.Drawing.Size(62, 20);
            this.bTextBox.TabIndex = 3;
            this.bTextBox.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // label2
            // 
            this.label2.Anchor = System.Windows.Forms.AnchorStyles.Bottom;
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(173, 310);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(16, 13);
            this.label2.TabIndex = 58;
            this.label2.Text = "b:";
            // 
            // mTextBox
            // 
            this.mTextBox.Anchor = System.Windows.Forms.AnchorStyles.Bottom;
            this.mTextBox.Location = new System.Drawing.Point(52, 307);
            this.mTextBox.Name = "mTextBox";
            this.mTextBox.ReadOnly = true;
            this.mTextBox.Size = new System.Drawing.Size(62, 20);
            this.mTextBox.TabIndex = 2;
            this.mTextBox.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // label1
            // 
            this.label1.Anchor = System.Windows.Forms.AnchorStyles.Bottom;
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(28, 310);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(18, 13);
            this.label1.TabIndex = 56;
            this.label1.Text = "m:";
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
            this.graphPictureBox.TabIndex = 55;
            this.graphPictureBox.TabStop = false;
            this.graphPictureBox.Paint += new System.Windows.Forms.PaintEventHandler(this.graphPictureBox_Paint);
            this.graphPictureBox.MouseClick += new System.Windows.Forms.MouseEventHandler(this.graphPictureBox_MouseClick);
            // 
            // resetButton
            // 
            this.resetButton.Anchor = System.Windows.Forms.AnchorStyles.Bottom;
            this.resetButton.Location = new System.Drawing.Point(145, 278);
            this.resetButton.Name = "resetButton";
            this.resetButton.Size = new System.Drawing.Size(75, 23);
            this.resetButton.TabIndex = 1;
            this.resetButton.Text = "Reset";
            this.resetButton.UseVisualStyleBackColor = true;
            this.resetButton.Click += new System.EventHandler(this.resetButton_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(284, 339);
            this.Controls.Add(this.resetButton);
            this.Controls.Add(this.solveButton);
            this.Controls.Add(this.bTextBox);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.mTextBox);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.graphPictureBox);
            this.Name = "Form1";
            this.Text = "LinearLeastSquares";
            ((System.ComponentModel.ISupportInitialize)(this.graphPictureBox)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button solveButton;
        private System.Windows.Forms.TextBox bTextBox;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.TextBox mTextBox;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.PictureBox graphPictureBox;
        private System.Windows.Forms.Button resetButton;
    }
}

