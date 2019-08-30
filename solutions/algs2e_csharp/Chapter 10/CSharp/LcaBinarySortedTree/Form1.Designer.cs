namespace LcaBinarySortedTree
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
            this.heightTextBox = new System.Windows.Forms.TextBox();
            this.buildTreeButton = new System.Windows.Forms.Button();
            this.treePictureBox = new System.Windows.Forms.PictureBox();
            ((System.ComponentModel.ISupportInitialize)(this.treePictureBox)).BeginInit();
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(12, 17);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(66, 13);
            this.label1.TabIndex = 0;
            this.label1.Text = "Tree Height:";
            // 
            // heightTextBox
            // 
            this.heightTextBox.Location = new System.Drawing.Point(84, 14);
            this.heightTextBox.Name = "heightTextBox";
            this.heightTextBox.Size = new System.Drawing.Size(41, 20);
            this.heightTextBox.TabIndex = 1;
            this.heightTextBox.Text = "3";
            this.heightTextBox.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // buildTreeButton
            // 
            this.buildTreeButton.Location = new System.Drawing.Point(147, 12);
            this.buildTreeButton.Name = "buildTreeButton";
            this.buildTreeButton.Size = new System.Drawing.Size(75, 23);
            this.buildTreeButton.TabIndex = 2;
            this.buildTreeButton.Text = "Build Tree";
            this.buildTreeButton.UseVisualStyleBackColor = true;
            this.buildTreeButton.Click += new System.EventHandler(this.buildTreeButton_Click);
            // 
            // treePictureBox
            // 
            this.treePictureBox.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.treePictureBox.BackColor = System.Drawing.Color.White;
            this.treePictureBox.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.treePictureBox.Location = new System.Drawing.Point(12, 40);
            this.treePictureBox.Name = "treePictureBox";
            this.treePictureBox.Size = new System.Drawing.Size(280, 189);
            this.treePictureBox.TabIndex = 3;
            this.treePictureBox.TabStop = false;
            this.treePictureBox.Paint += new System.Windows.Forms.PaintEventHandler(this.treePictureBox_Paint);
            this.treePictureBox.MouseClick += new System.Windows.Forms.MouseEventHandler(this.treePictureBox_MouseClick);
            // 
            // Form1
            // 
            this.AcceptButton = this.buildTreeButton;
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(304, 241);
            this.Controls.Add(this.treePictureBox);
            this.Controls.Add(this.buildTreeButton);
            this.Controls.Add(this.heightTextBox);
            this.Controls.Add(this.label1);
            this.Name = "Form1";
            this.Text = "LcaBinarySortedTree";
            ((System.ComponentModel.ISupportInitialize)(this.treePictureBox)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TextBox heightTextBox;
        private System.Windows.Forms.Button buildTreeButton;
        private System.Windows.Forms.PictureBox treePictureBox;
    }
}

