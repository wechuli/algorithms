﻿namespace CompleteSelfAvoidingWalk
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
            this.drawButton = new System.Windows.Forms.Button();
            this.heightTextBox = new System.Windows.Forms.TextBox();
            this.label2 = new System.Windows.Forms.Label();
            this.widthTextBox = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.walkPictureBox = new System.Windows.Forms.PictureBox();
            ((System.ComponentModel.ISupportInitialize)(this.walkPictureBox)).BeginInit();
            this.SuspendLayout();
            // 
            // drawButton
            // 
            this.drawButton.Anchor = System.Windows.Forms.AnchorStyles.Bottom;
            this.drawButton.Location = new System.Drawing.Point(95, 286);
            this.drawButton.Name = "drawButton";
            this.drawButton.Size = new System.Drawing.Size(75, 23);
            this.drawButton.TabIndex = 54;
            this.drawButton.Text = "Draw";
            this.drawButton.UseVisualStyleBackColor = true;
            this.drawButton.Click += new System.EventHandler(this.drawButton_Click);
            // 
            // heightTextBox
            // 
            this.heightTextBox.Anchor = System.Windows.Forms.AnchorStyles.Bottom;
            this.heightTextBox.Location = new System.Drawing.Point(189, 260);
            this.heightTextBox.Name = "heightTextBox";
            this.heightTextBox.Size = new System.Drawing.Size(42, 20);
            this.heightTextBox.TabIndex = 53;
            this.heightTextBox.Text = "6";
            this.heightTextBox.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // label2
            // 
            this.label2.Anchor = System.Windows.Forms.AnchorStyles.Bottom;
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(145, 263);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(41, 13);
            this.label2.TabIndex = 52;
            this.label2.Text = "Height:";
            // 
            // widthTextBox
            // 
            this.widthTextBox.Anchor = System.Windows.Forms.AnchorStyles.Bottom;
            this.widthTextBox.Location = new System.Drawing.Point(78, 260);
            this.widthTextBox.Name = "widthTextBox";
            this.widthTextBox.Size = new System.Drawing.Size(42, 20);
            this.widthTextBox.TabIndex = 51;
            this.widthTextBox.Text = "6";
            this.widthTextBox.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // label1
            // 
            this.label1.Anchor = System.Windows.Forms.AnchorStyles.Bottom;
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(34, 263);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(38, 13);
            this.label1.TabIndex = 50;
            this.label1.Text = "Width:";
            // 
            // walkPictureBox
            // 
            this.walkPictureBox.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.walkPictureBox.BackColor = System.Drawing.Color.White;
            this.walkPictureBox.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.walkPictureBox.Location = new System.Drawing.Point(12, 12);
            this.walkPictureBox.Name = "walkPictureBox";
            this.walkPictureBox.Size = new System.Drawing.Size(240, 242);
            this.walkPictureBox.TabIndex = 49;
            this.walkPictureBox.TabStop = false;
            this.walkPictureBox.Paint += new System.Windows.Forms.PaintEventHandler(this.walkPictureBox_Paint);
            // 
            // Form1
            // 
            this.AcceptButton = this.drawButton;
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(264, 321);
            this.Controls.Add(this.drawButton);
            this.Controls.Add(this.heightTextBox);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.widthTextBox);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.walkPictureBox);
            this.Name = "Form1";
            this.Text = "CompleteSelfAvoidingWalk";
            ((System.ComponentModel.ISupportInitialize)(this.walkPictureBox)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button drawButton;
        private System.Windows.Forms.TextBox heightTextBox;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.TextBox widthTextBox;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.PictureBox walkPictureBox;
    }
}

