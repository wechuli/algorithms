namespace BoidsClassicalPeople
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
            this.label8 = new System.Windows.Forms.Label();
            this.maxSpeedTextBox = new System.Windows.Forms.TextBox();
            this.numBoidsTextBox = new System.Windows.Forms.TextBox();
            this.label6 = new System.Windows.Forms.Label();
            this.neighborDistTextBox = new System.Windows.Forms.TextBox();
            this.label5 = new System.Windows.Forms.Label();
            this.canvasPictureBox = new System.Windows.Forms.PictureBox();
            this.targetWgtTextBox = new System.Windows.Forms.TextBox();
            this.label4 = new System.Windows.Forms.Label();
            this.startButton = new System.Windows.Forms.Button();
            this.cohesionWgtTextBox = new System.Windows.Forms.TextBox();
            this.label3 = new System.Windows.Forms.Label();
            this.alignmentWgtTextBox = new System.Windows.Forms.TextBox();
            this.label2 = new System.Windows.Forms.Label();
            this.separationWgtTextBox = new System.Windows.Forms.TextBox();
            this.moveTimer = new System.Windows.Forms.Timer(this.components);
            this.label1 = new System.Windows.Forms.Label();
            this.personWgtTextBox = new System.Windows.Forms.TextBox();
            this.label7 = new System.Windows.Forms.Label();
            ((System.ComponentModel.ISupportInitialize)(this.canvasPictureBox)).BeginInit();
            this.SuspendLayout();
            // 
            // label8
            // 
            this.label8.AutoSize = true;
            this.label8.Location = new System.Drawing.Point(12, 174);
            this.label8.Name = "label8";
            this.label8.Size = new System.Drawing.Size(64, 13);
            this.label8.TabIndex = 48;
            this.label8.Text = "Max Speed:";
            // 
            // maxSpeedTextBox
            // 
            this.maxSpeedTextBox.Location = new System.Drawing.Point(102, 171);
            this.maxSpeedTextBox.Name = "maxSpeedTextBox";
            this.maxSpeedTextBox.Size = new System.Drawing.Size(62, 20);
            this.maxSpeedTextBox.TabIndex = 5;
            this.maxSpeedTextBox.Text = "100";
            this.maxSpeedTextBox.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // numBoidsTextBox
            // 
            this.numBoidsTextBox.Location = new System.Drawing.Point(102, 223);
            this.numBoidsTextBox.Name = "numBoidsTextBox";
            this.numBoidsTextBox.Size = new System.Drawing.Size(62, 20);
            this.numBoidsTextBox.TabIndex = 7;
            this.numBoidsTextBox.Text = "20";
            this.numBoidsTextBox.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // label6
            // 
            this.label6.AutoSize = true;
            this.label6.Location = new System.Drawing.Point(12, 226);
            this.label6.Name = "label6";
            this.label6.Size = new System.Drawing.Size(46, 13);
            this.label6.TabIndex = 47;
            this.label6.Text = "# Boids:";
            // 
            // neighborDistTextBox
            // 
            this.neighborDistTextBox.Location = new System.Drawing.Point(102, 197);
            this.neighborDistTextBox.Name = "neighborDistTextBox";
            this.neighborDistTextBox.Size = new System.Drawing.Size(62, 20);
            this.neighborDistTextBox.TabIndex = 6;
            this.neighborDistTextBox.Text = "10";
            this.neighborDistTextBox.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Location = new System.Drawing.Point(12, 200);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(74, 13);
            this.label5.TabIndex = 46;
            this.label5.Text = "Neighbor Dist:";
            // 
            // canvasPictureBox
            // 
            this.canvasPictureBox.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.canvasPictureBox.BackColor = System.Drawing.Color.White;
            this.canvasPictureBox.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.canvasPictureBox.Location = new System.Drawing.Point(170, 12);
            this.canvasPictureBox.Name = "canvasPictureBox";
            this.canvasPictureBox.Size = new System.Drawing.Size(312, 327);
            this.canvasPictureBox.TabIndex = 45;
            this.canvasPictureBox.TabStop = false;
            this.canvasPictureBox.Paint += new System.Windows.Forms.PaintEventHandler(this.canvasPictureBox_Paint);
            this.canvasPictureBox.MouseClick += new System.Windows.Forms.MouseEventHandler(this.canvasPictureBox_MouseClick);
            this.canvasPictureBox.MouseMove += new System.Windows.Forms.MouseEventHandler(this.canvasPictureBox_MouseMove);
            // 
            // targetWgtTextBox
            // 
            this.targetWgtTextBox.Location = new System.Drawing.Point(102, 90);
            this.targetWgtTextBox.Name = "targetWgtTextBox";
            this.targetWgtTextBox.Size = new System.Drawing.Size(62, 20);
            this.targetWgtTextBox.TabIndex = 3;
            this.targetWgtTextBox.Text = "500";
            this.targetWgtTextBox.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(12, 93);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(64, 13);
            this.label4.TabIndex = 42;
            this.label4.Text = "Target Wgt:";
            // 
            // startButton
            // 
            this.startButton.Location = new System.Drawing.Point(50, 249);
            this.startButton.Name = "startButton";
            this.startButton.Size = new System.Drawing.Size(75, 23);
            this.startButton.TabIndex = 8;
            this.startButton.Text = "Start";
            this.startButton.UseVisualStyleBackColor = true;
            this.startButton.Click += new System.EventHandler(this.startButton_Click);
            // 
            // cohesionTextBox
            // 
            this.cohesionWgtTextBox.Location = new System.Drawing.Point(102, 64);
            this.cohesionWgtTextBox.Name = "cohesionTextBox";
            this.cohesionWgtTextBox.Size = new System.Drawing.Size(62, 20);
            this.cohesionWgtTextBox.TabIndex = 2;
            this.cohesionWgtTextBox.Text = "50";
            this.cohesionWgtTextBox.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(12, 67);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(77, 13);
            this.label3.TabIndex = 39;
            this.label3.Text = "Cohesion Wgt:";
            // 
            // alignmentTextBox
            // 
            this.alignmentWgtTextBox.Location = new System.Drawing.Point(102, 38);
            this.alignmentWgtTextBox.Name = "alignmentTextBox";
            this.alignmentWgtTextBox.Size = new System.Drawing.Size(62, 20);
            this.alignmentWgtTextBox.TabIndex = 1;
            this.alignmentWgtTextBox.Text = "10";
            this.alignmentWgtTextBox.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(12, 41);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(79, 13);
            this.label2.TabIndex = 36;
            this.label2.Text = "Alignment Wgt:";
            // 
            // separationTextBox
            // 
            this.separationWgtTextBox.Location = new System.Drawing.Point(102, 12);
            this.separationWgtTextBox.Name = "separationTextBox";
            this.separationWgtTextBox.Size = new System.Drawing.Size(62, 20);
            this.separationWgtTextBox.TabIndex = 0;
            this.separationWgtTextBox.Text = "100";
            this.separationWgtTextBox.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // moveTimer
            // 
            this.moveTimer.Interval = 20;
            this.moveTimer.Tick += new System.EventHandler(this.moveTimer_Tick);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(12, 15);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(84, 13);
            this.label1.TabIndex = 33;
            this.label1.Text = "Separation Wgt:";
            // 
            // personWgtTextBox
            // 
            this.personWgtTextBox.Location = new System.Drawing.Point(102, 116);
            this.personWgtTextBox.Name = "personWgtTextBox";
            this.personWgtTextBox.Size = new System.Drawing.Size(62, 20);
            this.personWgtTextBox.TabIndex = 4;
            this.personWgtTextBox.Text = "500";
            this.personWgtTextBox.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // label7
            // 
            this.label7.AutoSize = true;
            this.label7.Location = new System.Drawing.Point(12, 119);
            this.label7.Name = "label7";
            this.label7.Size = new System.Drawing.Size(66, 13);
            this.label7.TabIndex = 50;
            this.label7.Text = "Person Wgt:";
            // 
            // Form1
            // 
            this.AcceptButton = this.startButton;
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(494, 351);
            this.Controls.Add(this.personWgtTextBox);
            this.Controls.Add(this.label7);
            this.Controls.Add(this.label8);
            this.Controls.Add(this.maxSpeedTextBox);
            this.Controls.Add(this.numBoidsTextBox);
            this.Controls.Add(this.label6);
            this.Controls.Add(this.neighborDistTextBox);
            this.Controls.Add(this.label5);
            this.Controls.Add(this.canvasPictureBox);
            this.Controls.Add(this.targetWgtTextBox);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.startButton);
            this.Controls.Add(this.cohesionWgtTextBox);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.alignmentWgtTextBox);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.separationWgtTextBox);
            this.Controls.Add(this.label1);
            this.Name = "Form1";
            this.Text = "BoidsClassicalPeople";
            ((System.ComponentModel.ISupportInitialize)(this.canvasPictureBox)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label label8;
        private System.Windows.Forms.TextBox maxSpeedTextBox;
        private System.Windows.Forms.TextBox numBoidsTextBox;
        private System.Windows.Forms.Label label6;
        private System.Windows.Forms.TextBox neighborDistTextBox;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.PictureBox canvasPictureBox;
        private System.Windows.Forms.TextBox targetWgtTextBox;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.Button startButton;
        private System.Windows.Forms.TextBox cohesionWgtTextBox;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.TextBox alignmentWgtTextBox;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.TextBox separationWgtTextBox;
        private System.Windows.Forms.Timer moveTimer;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TextBox personWgtTextBox;
        private System.Windows.Forms.Label label7;
    }
}

