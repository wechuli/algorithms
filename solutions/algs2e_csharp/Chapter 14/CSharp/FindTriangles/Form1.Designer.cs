namespace FindTriangles
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
            this.findButton = new System.Windows.Forms.Button();
            this.canvasPictureBox = new System.Windows.Forms.PictureBox();
            this.trianglesListBox = new System.Windows.Forms.ListBox();
            ((System.ComponentModel.ISupportInitialize)(this.canvasPictureBox)).BeginInit();
            this.SuspendLayout();
            // 
            // findButton
            // 
            this.findButton.Anchor = System.Windows.Forms.AnchorStyles.Top;
            this.findButton.Location = new System.Drawing.Point(147, 12);
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
            this.canvasPictureBox.Size = new System.Drawing.Size(268, 208);
            this.canvasPictureBox.TabIndex = 3;
            this.canvasPictureBox.TabStop = false;
            this.canvasPictureBox.Paint += new System.Windows.Forms.PaintEventHandler(this.canvasPictureBox_Paint);
            // 
            // trianglesListBox
            // 
            this.trianglesListBox.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.trianglesListBox.FormattingEnabled = true;
            this.trianglesListBox.IntegralHeight = false;
            this.trianglesListBox.Location = new System.Drawing.Point(286, 41);
            this.trianglesListBox.Name = "trianglesListBox";
            this.trianglesListBox.Size = new System.Drawing.Size(71, 208);
            this.trianglesListBox.TabIndex = 4;
            // 
            // Form1
            // 
            this.AcceptButton = this.findButton;
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(369, 261);
            this.Controls.Add(this.trianglesListBox);
            this.Controls.Add(this.canvasPictureBox);
            this.Controls.Add(this.findButton);
            this.Name = "Form1";
            this.Text = "FindTriangles";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.canvasPictureBox)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion
        private System.Windows.Forms.Button findButton;
        private System.Windows.Forms.PictureBox canvasPictureBox;
        private System.Windows.Forms.ListBox trianglesListBox;
    }
}

