namespace TriangleWalk
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
            this.numStepsTextBox = new System.Windows.Forms.TextBox();
            this.label2 = new System.Windows.Forms.Label();
            this.stepSizeTextBox = new System.Windows.Forms.TextBox();
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
            this.drawButton.TabIndex = 11;
            this.drawButton.Text = "Draw";
            this.drawButton.UseVisualStyleBackColor = true;
            this.drawButton.Click += new System.EventHandler(this.drawButton_Click);
            // 
            // numStepsTextBox
            // 
            this.numStepsTextBox.Anchor = System.Windows.Forms.AnchorStyles.Bottom;
            this.numStepsTextBox.Location = new System.Drawing.Point(134, 260);
            this.numStepsTextBox.Name = "numStepsTextBox";
            this.numStepsTextBox.Size = new System.Drawing.Size(57, 20);
            this.numStepsTextBox.TabIndex = 10;
            this.numStepsTextBox.Text = "10000";
            this.numStepsTextBox.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // label2
            // 
            this.label2.Anchor = System.Windows.Forms.AnchorStyles.Bottom;
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(73, 263);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(47, 13);
            this.label2.TabIndex = 9;
            this.label2.Text = "# Steps:";
            // 
            // stepSizeTextBox
            // 
            this.stepSizeTextBox.Anchor = System.Windows.Forms.AnchorStyles.Bottom;
            this.stepSizeTextBox.Location = new System.Drawing.Point(134, 234);
            this.stepSizeTextBox.Name = "stepSizeTextBox";
            this.stepSizeTextBox.Size = new System.Drawing.Size(57, 20);
            this.stepSizeTextBox.TabIndex = 8;
            this.stepSizeTextBox.Text = "4";
            this.stepSizeTextBox.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // label1
            // 
            this.label1.Anchor = System.Windows.Forms.AnchorStyles.Bottom;
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(73, 237);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(55, 13);
            this.label1.TabIndex = 7;
            this.label1.Text = "Step Size:";
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
            this.walkPictureBox.Size = new System.Drawing.Size(240, 216);
            this.walkPictureBox.TabIndex = 6;
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
            this.Controls.Add(this.numStepsTextBox);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.stepSizeTextBox);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.walkPictureBox);
            this.Name = "Form1";
            this.Text = "TriangleWalk";
            ((System.ComponentModel.ISupportInitialize)(this.walkPictureBox)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button drawButton;
        private System.Windows.Forms.TextBox numStepsTextBox;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.TextBox stepSizeTextBox;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.PictureBox walkPictureBox;
    }
}

