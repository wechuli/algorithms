namespace BoidsGravity
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
            this.moveTimer = new System.Windows.Forms.Timer(this.components);
            this.maxSpeedTextBox = new System.Windows.Forms.TextBox();
            this.numBoidsTextBox = new System.Windows.Forms.TextBox();
            this.label6 = new System.Windows.Forms.Label();
            this.neighborDistTextBox = new System.Windows.Forms.TextBox();
            this.label5 = new System.Windows.Forms.Label();
            this.canvasPictureBox = new System.Windows.Forms.PictureBox();
            this.targetWgtTextBox = new System.Windows.Forms.TextBox();
            this.label4 = new System.Windows.Forms.Label();
            this.startButton = new System.Windows.Forms.Button();
            this.repulsionWgtTextBox = new System.Windows.Forms.TextBox();
            this.label2 = new System.Windows.Forms.Label();
            this.attractionWgtTextBox = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.targetMassTextBox = new System.Windows.Forms.TextBox();
            this.label3 = new System.Windows.Forms.Label();
            this.boidMassTextBox = new System.Windows.Forms.TextBox();
            this.label7 = new System.Windows.Forms.Label();
            this.personWgtTextBox = new System.Windows.Forms.TextBox();
            this.label9 = new System.Windows.Forms.Label();
            this.personMassTextBox = new System.Windows.Forms.TextBox();
            this.label10 = new System.Windows.Forms.Label();
            ((System.ComponentModel.ISupportInitialize)(this.canvasPictureBox)).BeginInit();
            this.SuspendLayout();
            // 
            // label8
            // 
            this.label8.AutoSize = true;
            this.label8.Location = new System.Drawing.Point(12, 137);
            this.label8.Name = "label8";
            this.label8.Size = new System.Drawing.Size(64, 13);
            this.label8.TabIndex = 32;
            this.label8.Text = "Max Speed:";
            // 
            // moveTimer
            // 
            this.moveTimer.Interval = 20;
            this.moveTimer.Tick += new System.EventHandler(this.moveTimer_Tick);
            // 
            // maxSpeedTextBox
            // 
            this.maxSpeedTextBox.Location = new System.Drawing.Point(102, 134);
            this.maxSpeedTextBox.Name = "maxSpeedTextBox";
            this.maxSpeedTextBox.Size = new System.Drawing.Size(62, 20);
            this.maxSpeedTextBox.TabIndex = 4;
            this.maxSpeedTextBox.Text = "100";
            this.maxSpeedTextBox.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // numBoidsTextBox
            // 
            this.numBoidsTextBox.Location = new System.Drawing.Point(102, 186);
            this.numBoidsTextBox.Name = "numBoidsTextBox";
            this.numBoidsTextBox.Size = new System.Drawing.Size(62, 20);
            this.numBoidsTextBox.TabIndex = 6;
            this.numBoidsTextBox.Text = "20";
            this.numBoidsTextBox.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // label6
            // 
            this.label6.AutoSize = true;
            this.label6.Location = new System.Drawing.Point(12, 189);
            this.label6.Name = "label6";
            this.label6.Size = new System.Drawing.Size(46, 13);
            this.label6.TabIndex = 31;
            this.label6.Text = "# Boids:";
            // 
            // neighborDistTextBox
            // 
            this.neighborDistTextBox.Location = new System.Drawing.Point(102, 160);
            this.neighborDistTextBox.Name = "neighborDistTextBox";
            this.neighborDistTextBox.Size = new System.Drawing.Size(62, 20);
            this.neighborDistTextBox.TabIndex = 5;
            this.neighborDistTextBox.Text = "10";
            this.neighborDistTextBox.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Location = new System.Drawing.Point(12, 163);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(74, 13);
            this.label5.TabIndex = 30;
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
            this.canvasPictureBox.TabIndex = 29;
            this.canvasPictureBox.TabStop = false;
            this.canvasPictureBox.Paint += new System.Windows.Forms.PaintEventHandler(this.canvasPictureBox_Paint);
            this.canvasPictureBox.MouseClick += new System.Windows.Forms.MouseEventHandler(this.canvasPictureBox_MouseClick);
            this.canvasPictureBox.MouseMove += new System.Windows.Forms.MouseEventHandler(this.canvasPictureBox_MouseMove);
            // 
            // targetWgtTextBox
            // 
            this.targetWgtTextBox.Location = new System.Drawing.Point(102, 64);
            this.targetWgtTextBox.Name = "targetWgtTextBox";
            this.targetWgtTextBox.Size = new System.Drawing.Size(62, 20);
            this.targetWgtTextBox.TabIndex = 2;
            this.targetWgtTextBox.Text = "50";
            this.targetWgtTextBox.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(12, 67);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(64, 13);
            this.label4.TabIndex = 26;
            this.label4.Text = "Target Wgt:";
            // 
            // startButton
            // 
            this.startButton.Location = new System.Drawing.Point(50, 301);
            this.startButton.Name = "startButton";
            this.startButton.Size = new System.Drawing.Size(75, 23);
            this.startButton.TabIndex = 10;
            this.startButton.Text = "Start";
            this.startButton.UseVisualStyleBackColor = true;
            this.startButton.Click += new System.EventHandler(this.startButton_Click);
            // 
            // repulsionWgtTextBox
            // 
            this.repulsionWgtTextBox.Location = new System.Drawing.Point(102, 38);
            this.repulsionWgtTextBox.Name = "repulsionWgtTextBox";
            this.repulsionWgtTextBox.Size = new System.Drawing.Size(62, 20);
            this.repulsionWgtTextBox.TabIndex = 1;
            this.repulsionWgtTextBox.Text = "100";
            this.repulsionWgtTextBox.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(12, 41);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(80, 13);
            this.label2.TabIndex = 20;
            this.label2.Text = "Repulsion Wgt:";
            // 
            // attractionWgtTextBox
            // 
            this.attractionWgtTextBox.Location = new System.Drawing.Point(102, 12);
            this.attractionWgtTextBox.Name = "attractionWgtTextBox";
            this.attractionWgtTextBox.Size = new System.Drawing.Size(62, 20);
            this.attractionWgtTextBox.TabIndex = 0;
            this.attractionWgtTextBox.Text = "10";
            this.attractionWgtTextBox.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(12, 15);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(78, 13);
            this.label1.TabIndex = 17;
            this.label1.Text = "Attraction Wgt:";
            // 
            // targetMassTextBox
            // 
            this.targetMassTextBox.Location = new System.Drawing.Point(102, 238);
            this.targetMassTextBox.Name = "targetMassTextBox";
            this.targetMassTextBox.Size = new System.Drawing.Size(62, 20);
            this.targetMassTextBox.TabIndex = 8;
            this.targetMassTextBox.Text = "1000";
            this.targetMassTextBox.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(12, 241);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(69, 13);
            this.label3.TabIndex = 36;
            this.label3.Text = "Target Mass:";
            // 
            // boidMassTextBox
            // 
            this.boidMassTextBox.Location = new System.Drawing.Point(102, 212);
            this.boidMassTextBox.Name = "boidMassTextBox";
            this.boidMassTextBox.Size = new System.Drawing.Size(62, 20);
            this.boidMassTextBox.TabIndex = 7;
            this.boidMassTextBox.Text = "100";
            this.boidMassTextBox.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // label7
            // 
            this.label7.AutoSize = true;
            this.label7.Location = new System.Drawing.Point(12, 215);
            this.label7.Name = "label7";
            this.label7.Size = new System.Drawing.Size(59, 13);
            this.label7.TabIndex = 35;
            this.label7.Text = "Boid Mass:";
            // 
            // personWgtTextBox
            // 
            this.personWgtTextBox.Location = new System.Drawing.Point(102, 90);
            this.personWgtTextBox.Name = "personWgtTextBox";
            this.personWgtTextBox.Size = new System.Drawing.Size(62, 20);
            this.personWgtTextBox.TabIndex = 3;
            this.personWgtTextBox.Text = "50";
            this.personWgtTextBox.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // label9
            // 
            this.label9.AutoSize = true;
            this.label9.Location = new System.Drawing.Point(12, 93);
            this.label9.Name = "label9";
            this.label9.Size = new System.Drawing.Size(66, 13);
            this.label9.TabIndex = 38;
            this.label9.Text = "Person Wgt:";
            // 
            // personMassTextBox
            // 
            this.personMassTextBox.Location = new System.Drawing.Point(102, 264);
            this.personMassTextBox.Name = "personMassTextBox";
            this.personMassTextBox.Size = new System.Drawing.Size(62, 20);
            this.personMassTextBox.TabIndex = 9;
            this.personMassTextBox.Text = "1000";
            this.personMassTextBox.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // label10
            // 
            this.label10.AutoSize = true;
            this.label10.Location = new System.Drawing.Point(12, 267);
            this.label10.Name = "label10";
            this.label10.Size = new System.Drawing.Size(71, 13);
            this.label10.TabIndex = 40;
            this.label10.Text = "Person Mass:";
            // 
            // Form1
            // 
            this.AcceptButton = this.startButton;
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(494, 351);
            this.Controls.Add(this.personMassTextBox);
            this.Controls.Add(this.label10);
            this.Controls.Add(this.personWgtTextBox);
            this.Controls.Add(this.label9);
            this.Controls.Add(this.targetMassTextBox);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.boidMassTextBox);
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
            this.Controls.Add(this.repulsionWgtTextBox);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.attractionWgtTextBox);
            this.Controls.Add(this.label1);
            this.Name = "Form1";
            this.Text = "BoidsGravity";
            ((System.ComponentModel.ISupportInitialize)(this.canvasPictureBox)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label label8;
        private System.Windows.Forms.Timer moveTimer;
        private System.Windows.Forms.TextBox maxSpeedTextBox;
        private System.Windows.Forms.TextBox numBoidsTextBox;
        private System.Windows.Forms.Label label6;
        private System.Windows.Forms.TextBox neighborDistTextBox;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.PictureBox canvasPictureBox;
        private System.Windows.Forms.TextBox targetWgtTextBox;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.Button startButton;
        private System.Windows.Forms.TextBox repulsionWgtTextBox;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.TextBox attractionWgtTextBox;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TextBox targetMassTextBox;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.TextBox boidMassTextBox;
        private System.Windows.Forms.Label label7;
        private System.Windows.Forms.TextBox personWgtTextBox;
        private System.Windows.Forms.Label label9;
        private System.Windows.Forms.TextBox personMassTextBox;
        private System.Windows.Forms.Label label10;
    }
}

