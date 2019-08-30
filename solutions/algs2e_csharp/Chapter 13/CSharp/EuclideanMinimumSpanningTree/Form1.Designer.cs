namespace EuclideanMinimumSpanningTree
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
            this.goButton = new System.Windows.Forms.Button();
            this.clearButton = new System.Windows.Forms.Button();
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
            this.canvasPictureBox.Size = new System.Drawing.Size(360, 308);
            this.canvasPictureBox.TabIndex = 0;
            this.canvasPictureBox.TabStop = false;
            this.canvasPictureBox.Paint += new System.Windows.Forms.PaintEventHandler(this.canvasPictureBox_Paint);
            this.canvasPictureBox.MouseClick += new System.Windows.Forms.MouseEventHandler(this.canvasPictureBox_MouseClick);
            // 
            // goButton
            // 
            this.goButton.Anchor = System.Windows.Forms.AnchorStyles.Bottom;
            this.goButton.Location = new System.Drawing.Point(103, 326);
            this.goButton.Name = "goButton";
            this.goButton.Size = new System.Drawing.Size(75, 23);
            this.goButton.TabIndex = 1;
            this.goButton.Text = "Go";
            this.goButton.UseVisualStyleBackColor = true;
            this.goButton.Click += new System.EventHandler(this.goButton_Click);
            // 
            // clearButton
            // 
            this.clearButton.Anchor = System.Windows.Forms.AnchorStyles.Bottom;
            this.clearButton.DialogResult = System.Windows.Forms.DialogResult.Cancel;
            this.clearButton.Location = new System.Drawing.Point(207, 326);
            this.clearButton.Name = "clearButton";
            this.clearButton.Size = new System.Drawing.Size(75, 23);
            this.clearButton.TabIndex = 2;
            this.clearButton.Text = "Clear";
            this.clearButton.UseVisualStyleBackColor = true;
            this.clearButton.Click += new System.EventHandler(this.clearButton_Click);
            // 
            // Form1
            // 
            this.AcceptButton = this.goButton;
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.CancelButton = this.clearButton;
            this.ClientSize = new System.Drawing.Size(384, 361);
            this.Controls.Add(this.clearButton);
            this.Controls.Add(this.goButton);
            this.Controls.Add(this.canvasPictureBox);
            this.Name = "Form1";
            this.Text = "EuclideanMinimumSpanningTree";
            ((System.ComponentModel.ISupportInitialize)(this.canvasPictureBox)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.PictureBox canvasPictureBox;
        private System.Windows.Forms.Button goButton;
        private System.Windows.Forms.Button clearButton;
    }
}

