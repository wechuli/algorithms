namespace StronglyConnectedComponents
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
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            this.findComponentsButton = new System.Windows.Forms.Button();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            this.SuspendLayout();
            // 
            // pictureBox1
            // 
            this.pictureBox1.BackColor = System.Drawing.Color.White;
            this.pictureBox1.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.pictureBox1.Location = new System.Drawing.Point(12, 12);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(256, 256);
            this.pictureBox1.TabIndex = 3;
            this.pictureBox1.TabStop = false;
            this.pictureBox1.Paint += new System.Windows.Forms.PaintEventHandler(this.pictureBox1_Paint);
            // 
            // findComponentsButton
            // 
            this.findComponentsButton.Anchor = System.Windows.Forms.AnchorStyles.Top;
            this.findComponentsButton.Location = new System.Drawing.Point(90, 274);
            this.findComponentsButton.Name = "findComponentsButton";
            this.findComponentsButton.Size = new System.Drawing.Size(98, 23);
            this.findComponentsButton.TabIndex = 4;
            this.findComponentsButton.Text = "Find Components";
            this.findComponentsButton.UseVisualStyleBackColor = true;
            this.findComponentsButton.Click += new System.EventHandler(this.findComponentsButton_Click);
            // 
            // Form1
            // 
            this.AcceptButton = this.findComponentsButton;
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(278, 304);
            this.Controls.Add(this.findComponentsButton);
            this.Controls.Add(this.pictureBox1);
            this.Name = "Form1";
            this.Text = "StronglyConnectedComponents";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.PictureBox pictureBox1;
        private System.Windows.Forms.Button findComponentsButton;
    }
}

