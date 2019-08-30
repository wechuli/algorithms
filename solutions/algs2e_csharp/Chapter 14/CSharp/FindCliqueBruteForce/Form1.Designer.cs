namespace FindCliqueBruteForce
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
            this.label1 = new System.Windows.Forms.Label();
            this.cliqueSizeTextBox = new System.Windows.Forms.TextBox();
            this.findButton = new System.Windows.Forms.Button();
            this.canvasPictureBox = new System.Windows.Forms.PictureBox();
            ((System.ComponentModel.ISupportInitialize)(this.canvasPictureBox)).BeginInit();
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(12, 17);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(62, 13);
            this.label1.TabIndex = 0;
            this.label1.Text = "Clique Size:";
            // 
            // cliqueSizeTextBox
            // 
            this.cliqueSizeTextBox.Location = new System.Drawing.Point(80, 14);
            this.cliqueSizeTextBox.Name = "cliqueSizeTextBox";
            this.cliqueSizeTextBox.Size = new System.Drawing.Size(30, 20);
            this.cliqueSizeTextBox.TabIndex = 1;
            this.cliqueSizeTextBox.Text = "4";
            this.cliqueSizeTextBox.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // findButton
            // 
            this.findButton.Location = new System.Drawing.Point(150, 12);
            this.findButton.Name = "findButton";
            this.findButton.Size = new System.Drawing.Size(75, 23);
            this.findButton.TabIndex = 2;
            this.findButton.Text = "Find";
            this.findButton.UseVisualStyleBackColor = true;
            this.findButton.Click += new System.EventHandler(this.findButton_Click);
            // 
            // canvasPictureBox
            // 
            this.canvasPictureBox.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.canvasPictureBox.BackColor = System.Drawing.Color.White;
            this.canvasPictureBox.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.canvasPictureBox.Location = new System.Drawing.Point(12, 41);
            this.canvasPictureBox.Name = "canvasPictureBox";
            this.canvasPictureBox.Size = new System.Drawing.Size(260, 208);
            this.canvasPictureBox.TabIndex = 3;
            this.canvasPictureBox.TabStop = false;
            this.canvasPictureBox.Paint += new System.Windows.Forms.PaintEventHandler(this.canvasPictureBox_Paint);
            // 
            // Form1
            // 
            this.AcceptButton = this.findButton;
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(284, 261);
            this.Controls.Add(this.canvasPictureBox);
            this.Controls.Add(this.findButton);
            this.Controls.Add(this.cliqueSizeTextBox);
            this.Controls.Add(this.label1);
            this.Name = "Form1";
            this.Text = "FindCliqueBruteForce";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.canvasPictureBox)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TextBox cliqueSizeTextBox;
        private System.Windows.Forms.Button findButton;
        private System.Windows.Forms.PictureBox canvasPictureBox;
    }
}

