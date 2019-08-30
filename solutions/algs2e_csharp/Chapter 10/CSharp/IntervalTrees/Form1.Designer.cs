namespace IntervalTrees
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
            this.canvasPictureBox = new System.Windows.Forms.PictureBox();
            this.buildTreeButton = new System.Windows.Forms.Button();
            ((System.ComponentModel.ISupportInitialize)(this.canvasPictureBox)).BeginInit();
            this.SuspendLayout();
            // 
            // canvasPictureBox
            // 
            this.canvasPictureBox.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.canvasPictureBox.BackColor = System.Drawing.Color.White;
            this.canvasPictureBox.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.canvasPictureBox.Location = new System.Drawing.Point(12, 12);
            this.canvasPictureBox.Name = "canvasPictureBox";
            this.canvasPictureBox.Size = new System.Drawing.Size(260, 208);
            this.canvasPictureBox.TabIndex = 0;
            this.canvasPictureBox.TabStop = false;
            this.canvasPictureBox.Paint += new System.Windows.Forms.PaintEventHandler(this.canvasPictureBox_Paint);
            this.canvasPictureBox.MouseDown += new System.Windows.Forms.MouseEventHandler(this.canvasPictureBox_MouseDown);
            this.canvasPictureBox.MouseMove += new System.Windows.Forms.MouseEventHandler(this.canvasPictureBox_MouseMove);
            this.canvasPictureBox.MouseUp += new System.Windows.Forms.MouseEventHandler(this.canvasPictureBox_MouseUp);
            // 
            // buildTreeButton
            // 
            this.buildTreeButton.Anchor = System.Windows.Forms.AnchorStyles.Bottom;
            this.buildTreeButton.Enabled = false;
            this.buildTreeButton.Location = new System.Drawing.Point(105, 226);
            this.buildTreeButton.Name = "buildTreeButton";
            this.buildTreeButton.Size = new System.Drawing.Size(75, 23);
            this.buildTreeButton.TabIndex = 1;
            this.buildTreeButton.Text = "Build Tree";
            this.buildTreeButton.UseVisualStyleBackColor = true;
            this.buildTreeButton.Click += new System.EventHandler(this.buildTreeButton_Click);
            // 
            // Form1
            // 
            this.AcceptButton = this.buildTreeButton;
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(284, 261);
            this.Controls.Add(this.buildTreeButton);
            this.Controls.Add(this.canvasPictureBox);
            this.Name = "Form1";
            this.Text = "IntervalTrees";
            ((System.ComponentModel.ISupportInitialize)(this.canvasPictureBox)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.PictureBox canvasPictureBox;
        private System.Windows.Forms.Button buildTreeButton;
    }
}

