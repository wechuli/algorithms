﻿namespace LcaParentsAndDepths
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
            this.treePictureBox = new System.Windows.Forms.PictureBox();
            ((System.ComponentModel.ISupportInitialize)(this.treePictureBox)).BeginInit();
            this.SuspendLayout();
            // 
            // treePictureBox
            // 
            this.treePictureBox.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.treePictureBox.BackColor = System.Drawing.Color.White;
            this.treePictureBox.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.treePictureBox.Location = new System.Drawing.Point(12, 12);
            this.treePictureBox.Name = "treePictureBox";
            this.treePictureBox.Size = new System.Drawing.Size(315, 172);
            this.treePictureBox.TabIndex = 9;
            this.treePictureBox.TabStop = false;
            this.treePictureBox.Paint += new System.Windows.Forms.PaintEventHandler(this.treePictureBox_Paint);
            this.treePictureBox.MouseClick += new System.Windows.Forms.MouseEventHandler(this.treePictureBox_MouseClick);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(339, 196);
            this.Controls.Add(this.treePictureBox);
            this.Name = "Form1";
            this.Text = "LcaParentsAndDepths";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.treePictureBox)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.PictureBox treePictureBox;
    }
}

