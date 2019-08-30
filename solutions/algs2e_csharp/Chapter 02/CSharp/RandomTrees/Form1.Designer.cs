namespace RandomTrees
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
            this.randomButton = new System.Windows.Forms.Button();
            this.goButton = new System.Windows.Forms.Button();
            this.seedTextBox = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.canvasPictureBox = new System.Windows.Forms.PictureBox();
            ((System.ComponentModel.ISupportInitialize)(this.canvasPictureBox)).BeginInit();
            this.SuspendLayout();
            // 
            // randomButton
            // 
            this.randomButton.Anchor = System.Windows.Forms.AnchorStyles.Bottom;
            this.randomButton.DialogResult = System.Windows.Forms.DialogResult.Cancel;
            this.randomButton.Location = new System.Drawing.Point(220, 12);
            this.randomButton.Name = "randomButton";
            this.randomButton.Size = new System.Drawing.Size(75, 23);
            this.randomButton.TabIndex = 7;
            this.randomButton.Text = "Random";
            this.randomButton.UseVisualStyleBackColor = true;
            this.randomButton.Click += new System.EventHandler(this.randomButton_Click);
            // 
            // goButton
            // 
            this.goButton.Anchor = System.Windows.Forms.AnchorStyles.Bottom;
            this.goButton.DialogResult = System.Windows.Forms.DialogResult.Cancel;
            this.goButton.Location = new System.Drawing.Point(139, 12);
            this.goButton.Name = "goButton";
            this.goButton.Size = new System.Drawing.Size(75, 23);
            this.goButton.TabIndex = 6;
            this.goButton.Text = "Go";
            this.goButton.UseVisualStyleBackColor = true;
            this.goButton.Click += new System.EventHandler(this.goButton_Click);
            // 
            // seedTextBox
            // 
            this.seedTextBox.Anchor = System.Windows.Forms.AnchorStyles.Bottom;
            this.seedTextBox.Location = new System.Drawing.Point(53, 14);
            this.seedTextBox.Name = "seedTextBox";
            this.seedTextBox.Size = new System.Drawing.Size(80, 20);
            this.seedTextBox.TabIndex = 5;
            this.seedTextBox.Text = "470229991";
            this.seedTextBox.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // label1
            // 
            this.label1.Anchor = System.Windows.Forms.AnchorStyles.Bottom;
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(12, 17);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(35, 13);
            this.label1.TabIndex = 4;
            this.label1.Text = "Seed:";
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
            this.canvasPictureBox.Size = new System.Drawing.Size(293, 244);
            this.canvasPictureBox.TabIndex = 8;
            this.canvasPictureBox.TabStop = false;
            this.canvasPictureBox.Paint += new System.Windows.Forms.PaintEventHandler(this.canvasPictureBox_Paint);
            // 
            // Form1
            // 
            this.AcceptButton = this.goButton;
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(317, 297);
            this.Controls.Add(this.canvasPictureBox);
            this.Controls.Add(this.randomButton);
            this.Controls.Add(this.goButton);
            this.Controls.Add(this.seedTextBox);
            this.Controls.Add(this.label1);
            this.Name = "Form1";
            this.Text = "RandomTrees";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.canvasPictureBox)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button randomButton;
        private System.Windows.Forms.Button goButton;
        private System.Windows.Forms.TextBox seedTextBox;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.PictureBox canvasPictureBox;
    }
}

