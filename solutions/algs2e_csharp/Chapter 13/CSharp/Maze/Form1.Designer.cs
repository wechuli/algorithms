namespace Maze
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
            this.label1 = new System.Windows.Forms.Label();
            this.numRowsTextBox = new System.Windows.Forms.TextBox();
            this.numColumnsTextBox = new System.Windows.Forms.TextBox();
            this.label2 = new System.Windows.Forms.Label();
            this.showTreeCheckBox = new System.Windows.Forms.CheckBox();
            ((System.ComponentModel.ISupportInitialize)(this.canvasPictureBox)).BeginInit();
            this.SuspendLayout();
            // 
            // canvasPictureBox
            // 
            this.canvasPictureBox.BackColor = System.Drawing.Color.White;
            this.canvasPictureBox.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.canvasPictureBox.Location = new System.Drawing.Point(133, 12);
            this.canvasPictureBox.Name = "canvasPictureBox";
            this.canvasPictureBox.Size = new System.Drawing.Size(256, 256);
            this.canvasPictureBox.TabIndex = 0;
            this.canvasPictureBox.TabStop = false;
            this.canvasPictureBox.Paint += new System.Windows.Forms.PaintEventHandler(this.canvasPictureBox_Paint);
            // 
            // goButton
            // 
            this.goButton.Location = new System.Drawing.Point(32, 102);
            this.goButton.Name = "goButton";
            this.goButton.Size = new System.Drawing.Size(75, 23);
            this.goButton.TabIndex = 3;
            this.goButton.Text = "Go";
            this.goButton.UseVisualStyleBackColor = true;
            this.goButton.Click += new System.EventHandler(this.goButton_Click);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(12, 15);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(47, 13);
            this.label1.TabIndex = 2;
            this.label1.Text = "# Rows:";
            // 
            // numRowsTextBox
            // 
            this.numRowsTextBox.Location = new System.Drawing.Point(78, 12);
            this.numRowsTextBox.Name = "numRowsTextBox";
            this.numRowsTextBox.Size = new System.Drawing.Size(49, 20);
            this.numRowsTextBox.TabIndex = 0;
            this.numRowsTextBox.Text = "10";
            this.numRowsTextBox.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // numColumnsTextBox
            // 
            this.numColumnsTextBox.Location = new System.Drawing.Point(78, 38);
            this.numColumnsTextBox.Name = "numColumnsTextBox";
            this.numColumnsTextBox.Size = new System.Drawing.Size(49, 20);
            this.numColumnsTextBox.TabIndex = 1;
            this.numColumnsTextBox.Text = "10";
            this.numColumnsTextBox.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(12, 41);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(60, 13);
            this.label2.TabIndex = 4;
            this.label2.Text = "# Columns:";
            // 
            // showTreeCheckBox
            // 
            this.showTreeCheckBox.AutoSize = true;
            this.showTreeCheckBox.Location = new System.Drawing.Point(30, 64);
            this.showTreeCheckBox.Name = "showTreeCheckBox";
            this.showTreeCheckBox.Size = new System.Drawing.Size(78, 17);
            this.showTreeCheckBox.TabIndex = 2;
            this.showTreeCheckBox.Text = "Show Tree";
            this.showTreeCheckBox.UseVisualStyleBackColor = true;
            this.showTreeCheckBox.CheckedChanged += new System.EventHandler(this.showTreeCheckBox_CheckedChanged);
            // 
            // Form1
            // 
            this.AcceptButton = this.goButton;
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(398, 277);
            this.Controls.Add(this.showTreeCheckBox);
            this.Controls.Add(this.numColumnsTextBox);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.numRowsTextBox);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.goButton);
            this.Controls.Add(this.canvasPictureBox);
            this.Name = "Form1";
            this.Text = "Maze";
            ((System.ComponentModel.ISupportInitialize)(this.canvasPictureBox)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.PictureBox canvasPictureBox;
        private System.Windows.Forms.Button goButton;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TextBox numRowsTextBox;
        private System.Windows.Forms.TextBox numColumnsTextBox;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.CheckBox showTreeCheckBox;
    }
}

