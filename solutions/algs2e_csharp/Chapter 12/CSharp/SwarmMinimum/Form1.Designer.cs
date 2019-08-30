namespace SwarmMinimum
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
            this.components = new System.ComponentModel.Container();
            this.label1 = new System.Windows.Forms.Label();
            this.numBugsTextBox = new System.Windows.Forms.TextBox();
            this.cogAccelTextBox = new System.Windows.Forms.TextBox();
            this.label2 = new System.Windows.Forms.Label();
            this.socAccelTextBox = new System.Windows.Forms.TextBox();
            this.label3 = new System.Windows.Forms.Label();
            this.maxSpeedTextBox = new System.Windows.Forms.TextBox();
            this.label4 = new System.Windows.Forms.Label();
            this.startButton = new System.Windows.Forms.Button();
            this.canvasPictureBox = new System.Windows.Forms.PictureBox();
            this.moveTimer = new System.Windows.Forms.Timer(this.components);
            this.label5 = new System.Windows.Forms.Label();
            this.minimumTextBox = new System.Windows.Forms.TextBox();
            this.lockAfterTextBox = new System.Windows.Forms.TextBox();
            this.label6 = new System.Windows.Forms.Label();
            ((System.ComponentModel.ISupportInitialize)(this.canvasPictureBox)).BeginInit();
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(12, 15);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(44, 13);
            this.label1.TabIndex = 0;
            this.label1.Text = "# Bugs:";
            // 
            // numBugsTextBox
            // 
            this.numBugsTextBox.Location = new System.Drawing.Point(134, 12);
            this.numBugsTextBox.Name = "numBugsTextBox";
            this.numBugsTextBox.Size = new System.Drawing.Size(59, 20);
            this.numBugsTextBox.TabIndex = 0;
            this.numBugsTextBox.Text = "100";
            this.numBugsTextBox.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // cogAccelTextBox
            // 
            this.cogAccelTextBox.Location = new System.Drawing.Point(134, 38);
            this.cogAccelTextBox.Name = "cogAccelTextBox";
            this.cogAccelTextBox.Size = new System.Drawing.Size(59, 20);
            this.cogAccelTextBox.TabIndex = 1;
            this.cogAccelTextBox.Text = "2";
            this.cogAccelTextBox.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(12, 41);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(116, 13);
            this.label2.TabIndex = 2;
            this.label2.Text = "Cognition Acceleration:";
            // 
            // socAccelTextBox
            // 
            this.socAccelTextBox.Location = new System.Drawing.Point(134, 64);
            this.socAccelTextBox.Name = "socAccelTextBox";
            this.socAccelTextBox.Size = new System.Drawing.Size(59, 20);
            this.socAccelTextBox.TabIndex = 2;
            this.socAccelTextBox.Text = "2";
            this.socAccelTextBox.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(12, 67);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(101, 13);
            this.label3.TabIndex = 4;
            this.label3.Text = "Social Acceleration:";
            // 
            // maxSpeedTextBox
            // 
            this.maxSpeedTextBox.Location = new System.Drawing.Point(134, 90);
            this.maxSpeedTextBox.Name = "maxSpeedTextBox";
            this.maxSpeedTextBox.Size = new System.Drawing.Size(59, 20);
            this.maxSpeedTextBox.TabIndex = 3;
            this.maxSpeedTextBox.Text = "1";
            this.maxSpeedTextBox.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(12, 93);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(64, 13);
            this.label4.TabIndex = 6;
            this.label4.Text = "Max Speed:";
            // 
            // startButton
            // 
            this.startButton.Location = new System.Drawing.Point(63, 162);
            this.startButton.Name = "startButton";
            this.startButton.Size = new System.Drawing.Size(75, 23);
            this.startButton.TabIndex = 5;
            this.startButton.Text = "Start";
            this.startButton.UseVisualStyleBackColor = true;
            this.startButton.Click += new System.EventHandler(this.startButton_Click);
            // 
            // canvasPictureBox
            // 
            this.canvasPictureBox.BackColor = System.Drawing.Color.White;
            this.canvasPictureBox.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.canvasPictureBox.Location = new System.Drawing.Point(199, 12);
            this.canvasPictureBox.Name = "canvasPictureBox";
            this.canvasPictureBox.Size = new System.Drawing.Size(256, 256);
            this.canvasPictureBox.TabIndex = 9;
            this.canvasPictureBox.TabStop = false;
            this.canvasPictureBox.Paint += new System.Windows.Forms.PaintEventHandler(this.canvasPictureBox_Paint);
            // 
            // moveTimer
            // 
            this.moveTimer.Interval = 20;
            this.moveTimer.Tick += new System.EventHandler(this.moveTimer_Tick);
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Location = new System.Drawing.Point(9, 206);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(51, 13);
            this.label5.TabIndex = 10;
            this.label5.Text = "Minimum:";
            // 
            // minimumTextBox
            // 
            this.minimumTextBox.Location = new System.Drawing.Point(12, 222);
            this.minimumTextBox.Name = "minimumTextBox";
            this.minimumTextBox.ReadOnly = true;
            this.minimumTextBox.Size = new System.Drawing.Size(177, 20);
            this.minimumTextBox.TabIndex = 6;
            // 
            // lockAfterTextBox
            // 
            this.lockAfterTextBox.Location = new System.Drawing.Point(134, 116);
            this.lockAfterTextBox.Name = "lockAfterTextBox";
            this.lockAfterTextBox.Size = new System.Drawing.Size(59, 20);
            this.lockAfterTextBox.TabIndex = 4;
            this.lockAfterTextBox.Text = "100";
            this.lockAfterTextBox.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // label6
            // 
            this.label6.AutoSize = true;
            this.label6.Location = new System.Drawing.Point(12, 119);
            this.label6.Name = "label6";
            this.label6.Size = new System.Drawing.Size(59, 13);
            this.label6.TabIndex = 12;
            this.label6.Text = "Lock After:";
            // 
            // Form1
            // 
            this.AcceptButton = this.startButton;
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(465, 277);
            this.Controls.Add(this.lockAfterTextBox);
            this.Controls.Add(this.label6);
            this.Controls.Add(this.minimumTextBox);
            this.Controls.Add(this.label5);
            this.Controls.Add(this.canvasPictureBox);
            this.Controls.Add(this.startButton);
            this.Controls.Add(this.maxSpeedTextBox);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.socAccelTextBox);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.cogAccelTextBox);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.numBugsTextBox);
            this.Controls.Add(this.label1);
            this.Name = "Form1";
            this.Text = "SwarmMinimum";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.canvasPictureBox)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TextBox numBugsTextBox;
        private System.Windows.Forms.TextBox cogAccelTextBox;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.TextBox socAccelTextBox;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.TextBox maxSpeedTextBox;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.Button startButton;
        private System.Windows.Forms.PictureBox canvasPictureBox;
        private System.Windows.Forms.Timer moveTimer;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.TextBox minimumTextBox;
        private System.Windows.Forms.TextBox lockAfterTextBox;
        private System.Windows.Forms.Label label6;
    }
}

