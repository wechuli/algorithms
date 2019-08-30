namespace SelfOrganizingLists
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
            this.numValuesTextBox = new System.Windows.Forms.TextBox();
            this.numSearchesTextBox = new System.Windows.Forms.TextBox();
            this.label2 = new System.Windows.Forms.Label();
            this.goButton = new System.Windows.Forms.Button();
            this.mtfNumStepsTextBox = new System.Windows.Forms.TextBox();
            this.label3 = new System.Windows.Forms.Label();
            this.label4 = new System.Windows.Forms.Label();
            this.label5 = new System.Windows.Forms.Label();
            this.mtfExpectedStepsTextBox = new System.Windows.Forms.TextBox();
            this.noneExpectedStepsTextBox = new System.Windows.Forms.TextBox();
            this.noneNumStepsTextBox = new System.Windows.Forms.TextBox();
            this.label6 = new System.Windows.Forms.Label();
            this.swapExpectedStepsTextBox = new System.Windows.Forms.TextBox();
            this.swapNumStepsTextBox = new System.Windows.Forms.TextBox();
            this.label7 = new System.Windows.Forms.Label();
            this.countExpectedStepsTextBox = new System.Windows.Forms.TextBox();
            this.countNumStepsTextBox = new System.Windows.Forms.TextBox();
            this.label8 = new System.Windows.Forms.Label();
            this.equalRadioButton = new System.Windows.Forms.RadioButton();
            this.linearRadioButton = new System.Windows.Forms.RadioButton();
            this.label9 = new System.Windows.Forms.Label();
            this.quadraticRadioButton = new System.Windows.Forms.RadioButton();
            this.countAveStepsTextBox = new System.Windows.Forms.TextBox();
            this.swapAveStepsTextBox = new System.Windows.Forms.TextBox();
            this.noneAveStepsTextBox = new System.Windows.Forms.TextBox();
            this.label10 = new System.Windows.Forms.Label();
            this.mtfAveStepsTextBox = new System.Windows.Forms.TextBox();
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(12, 15);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(52, 13);
            this.label1.TabIndex = 0;
            this.label1.Text = "# Values:";
            // 
            // numValuesTextBox
            // 
            this.numValuesTextBox.Location = new System.Drawing.Point(83, 12);
            this.numValuesTextBox.Name = "numValuesTextBox";
            this.numValuesTextBox.Size = new System.Drawing.Size(75, 20);
            this.numValuesTextBox.TabIndex = 0;
            this.numValuesTextBox.Text = "100";
            this.numValuesTextBox.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // numTrialsTextBox
            // 
            this.numSearchesTextBox.Location = new System.Drawing.Point(83, 38);
            this.numSearchesTextBox.Name = "numTrialsTextBox";
            this.numSearchesTextBox.Size = new System.Drawing.Size(75, 20);
            this.numSearchesTextBox.TabIndex = 1;
            this.numSearchesTextBox.Text = "10000";
            this.numSearchesTextBox.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(12, 41);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(65, 13);
            this.label2.TabIndex = 2;
            this.label2.Text = "# Searches:";
            // 
            // goButton
            // 
            this.goButton.Anchor = System.Windows.Forms.AnchorStyles.Top;
            this.goButton.Location = new System.Drawing.Point(154, 74);
            this.goButton.Name = "goButton";
            this.goButton.Size = new System.Drawing.Size(75, 23);
            this.goButton.TabIndex = 5;
            this.goButton.Text = "Go";
            this.goButton.UseVisualStyleBackColor = true;
            this.goButton.Click += new System.EventHandler(this.goButton_Click);
            // 
            // mtfNumStepsTextBox
            // 
            this.mtfNumStepsTextBox.Anchor = System.Windows.Forms.AnchorStyles.Top;
            this.mtfNumStepsTextBox.Location = new System.Drawing.Point(104, 174);
            this.mtfNumStepsTextBox.Name = "mtfNumStepsTextBox";
            this.mtfNumStepsTextBox.ReadOnly = true;
            this.mtfNumStepsTextBox.Size = new System.Drawing.Size(75, 20);
            this.mtfNumStepsTextBox.TabIndex = 9;
            this.mtfNumStepsTextBox.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // label3
            // 
            this.label3.Anchor = System.Windows.Forms.AnchorStyles.Top;
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(41, 177);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(51, 13);
            this.label3.TabIndex = 5;
            this.label3.Text = "MTF List:";
            // 
            // label4
            // 
            this.label4.Anchor = System.Windows.Forms.AnchorStyles.Top;
            this.label4.Location = new System.Drawing.Point(101, 114);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(77, 31);
            this.label4.TabIndex = 7;
            this.label4.Text = "Steps";
            this.label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // label5
            // 
            this.label5.Anchor = System.Windows.Forms.AnchorStyles.Top;
            this.label5.Location = new System.Drawing.Point(263, 114);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(77, 31);
            this.label5.TabIndex = 9;
            this.label5.Text = "Expected Steps";
            this.label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // mtfExpectedStepsTextBox
            // 
            this.mtfExpectedStepsTextBox.Anchor = System.Windows.Forms.AnchorStyles.Top;
            this.mtfExpectedStepsTextBox.Location = new System.Drawing.Point(266, 174);
            this.mtfExpectedStepsTextBox.Name = "mtfExpectedStepsTextBox";
            this.mtfExpectedStepsTextBox.ReadOnly = true;
            this.mtfExpectedStepsTextBox.Size = new System.Drawing.Size(75, 20);
            this.mtfExpectedStepsTextBox.TabIndex = 11;
            this.mtfExpectedStepsTextBox.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // noneExpectedStepsTextBox
            // 
            this.noneExpectedStepsTextBox.Anchor = System.Windows.Forms.AnchorStyles.Top;
            this.noneExpectedStepsTextBox.Location = new System.Drawing.Point(266, 148);
            this.noneExpectedStepsTextBox.Name = "noneExpectedStepsTextBox";
            this.noneExpectedStepsTextBox.ReadOnly = true;
            this.noneExpectedStepsTextBox.Size = new System.Drawing.Size(75, 20);
            this.noneExpectedStepsTextBox.TabIndex = 8;
            this.noneExpectedStepsTextBox.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // noneNumStepsTextBox
            // 
            this.noneNumStepsTextBox.Anchor = System.Windows.Forms.AnchorStyles.Top;
            this.noneNumStepsTextBox.Location = new System.Drawing.Point(104, 148);
            this.noneNumStepsTextBox.Name = "noneNumStepsTextBox";
            this.noneNumStepsTextBox.ReadOnly = true;
            this.noneNumStepsTextBox.Size = new System.Drawing.Size(75, 20);
            this.noneNumStepsTextBox.TabIndex = 6;
            this.noneNumStepsTextBox.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // label6
            // 
            this.label6.Anchor = System.Windows.Forms.AnchorStyles.Top;
            this.label6.AutoSize = true;
            this.label6.Location = new System.Drawing.Point(41, 151);
            this.label6.Name = "label6";
            this.label6.Size = new System.Drawing.Size(55, 13);
            this.label6.TabIndex = 10;
            this.label6.Text = "None List:";
            // 
            // swapExpectedStepsTextBox
            // 
            this.swapExpectedStepsTextBox.Anchor = System.Windows.Forms.AnchorStyles.Top;
            this.swapExpectedStepsTextBox.Location = new System.Drawing.Point(266, 200);
            this.swapExpectedStepsTextBox.Name = "swapExpectedStepsTextBox";
            this.swapExpectedStepsTextBox.ReadOnly = true;
            this.swapExpectedStepsTextBox.Size = new System.Drawing.Size(75, 20);
            this.swapExpectedStepsTextBox.TabIndex = 14;
            this.swapExpectedStepsTextBox.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // swapNumStepsTextBox
            // 
            this.swapNumStepsTextBox.Anchor = System.Windows.Forms.AnchorStyles.Top;
            this.swapNumStepsTextBox.Location = new System.Drawing.Point(104, 200);
            this.swapNumStepsTextBox.Name = "swapNumStepsTextBox";
            this.swapNumStepsTextBox.ReadOnly = true;
            this.swapNumStepsTextBox.Size = new System.Drawing.Size(75, 20);
            this.swapNumStepsTextBox.TabIndex = 12;
            this.swapNumStepsTextBox.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // label7
            // 
            this.label7.Anchor = System.Windows.Forms.AnchorStyles.Top;
            this.label7.AutoSize = true;
            this.label7.Location = new System.Drawing.Point(41, 203);
            this.label7.Name = "label7";
            this.label7.Size = new System.Drawing.Size(56, 13);
            this.label7.TabIndex = 13;
            this.label7.Text = "Swap List:";
            // 
            // countExpectedStepsTextBox
            // 
            this.countExpectedStepsTextBox.Anchor = System.Windows.Forms.AnchorStyles.Top;
            this.countExpectedStepsTextBox.Location = new System.Drawing.Point(266, 226);
            this.countExpectedStepsTextBox.Name = "countExpectedStepsTextBox";
            this.countExpectedStepsTextBox.ReadOnly = true;
            this.countExpectedStepsTextBox.Size = new System.Drawing.Size(75, 20);
            this.countExpectedStepsTextBox.TabIndex = 17;
            this.countExpectedStepsTextBox.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // countNumStepsTextBox
            // 
            this.countNumStepsTextBox.Anchor = System.Windows.Forms.AnchorStyles.Top;
            this.countNumStepsTextBox.Location = new System.Drawing.Point(104, 226);
            this.countNumStepsTextBox.Name = "countNumStepsTextBox";
            this.countNumStepsTextBox.ReadOnly = true;
            this.countNumStepsTextBox.Size = new System.Drawing.Size(75, 20);
            this.countNumStepsTextBox.TabIndex = 15;
            this.countNumStepsTextBox.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // label8
            // 
            this.label8.Anchor = System.Windows.Forms.AnchorStyles.Top;
            this.label8.AutoSize = true;
            this.label8.Location = new System.Drawing.Point(41, 229);
            this.label8.Name = "label8";
            this.label8.Size = new System.Drawing.Size(57, 13);
            this.label8.TabIndex = 16;
            this.label8.Text = "Count List:";
            // 
            // equalRadioButton
            // 
            this.equalRadioButton.AutoSize = true;
            this.equalRadioButton.Checked = true;
            this.equalRadioButton.Location = new System.Drawing.Point(186, 39);
            this.equalRadioButton.Name = "equalRadioButton";
            this.equalRadioButton.Size = new System.Drawing.Size(52, 17);
            this.equalRadioButton.TabIndex = 2;
            this.equalRadioButton.TabStop = true;
            this.equalRadioButton.Text = "Equal";
            this.equalRadioButton.UseVisualStyleBackColor = true;
            // 
            // linearRadioButton
            // 
            this.linearRadioButton.AutoSize = true;
            this.linearRadioButton.Location = new System.Drawing.Point(244, 39);
            this.linearRadioButton.Name = "linearRadioButton";
            this.linearRadioButton.Size = new System.Drawing.Size(54, 17);
            this.linearRadioButton.TabIndex = 3;
            this.linearRadioButton.Text = "Linear";
            this.linearRadioButton.UseVisualStyleBackColor = true;
            // 
            // label9
            // 
            this.label9.AutoSize = true;
            this.label9.Location = new System.Drawing.Point(173, 15);
            this.label9.Name = "label9";
            this.label9.Size = new System.Drawing.Size(66, 13);
            this.label9.TabIndex = 21;
            this.label9.Text = "Probabilities:";
            // 
            // quadraticRadioButton
            // 
            this.quadraticRadioButton.AutoSize = true;
            this.quadraticRadioButton.Location = new System.Drawing.Point(304, 39);
            this.quadraticRadioButton.Name = "quadraticRadioButton";
            this.quadraticRadioButton.Size = new System.Drawing.Size(71, 17);
            this.quadraticRadioButton.TabIndex = 4;
            this.quadraticRadioButton.Text = "Quadratic";
            this.quadraticRadioButton.UseVisualStyleBackColor = true;
            // 
            // countAveStepsTextBox
            // 
            this.countAveStepsTextBox.Anchor = System.Windows.Forms.AnchorStyles.Top;
            this.countAveStepsTextBox.Location = new System.Drawing.Point(185, 226);
            this.countAveStepsTextBox.Name = "countAveStepsTextBox";
            this.countAveStepsTextBox.ReadOnly = true;
            this.countAveStepsTextBox.Size = new System.Drawing.Size(75, 20);
            this.countAveStepsTextBox.TabIndex = 16;
            this.countAveStepsTextBox.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // swapAveStepsTextBox
            // 
            this.swapAveStepsTextBox.Anchor = System.Windows.Forms.AnchorStyles.Top;
            this.swapAveStepsTextBox.Location = new System.Drawing.Point(185, 200);
            this.swapAveStepsTextBox.Name = "swapAveStepsTextBox";
            this.swapAveStepsTextBox.ReadOnly = true;
            this.swapAveStepsTextBox.Size = new System.Drawing.Size(75, 20);
            this.swapAveStepsTextBox.TabIndex = 13;
            this.swapAveStepsTextBox.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // noneAveStepsTextBox
            // 
            this.noneAveStepsTextBox.Anchor = System.Windows.Forms.AnchorStyles.Top;
            this.noneAveStepsTextBox.Location = new System.Drawing.Point(185, 148);
            this.noneAveStepsTextBox.Name = "noneAveStepsTextBox";
            this.noneAveStepsTextBox.ReadOnly = true;
            this.noneAveStepsTextBox.Size = new System.Drawing.Size(75, 20);
            this.noneAveStepsTextBox.TabIndex = 7;
            this.noneAveStepsTextBox.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // label10
            // 
            this.label10.Anchor = System.Windows.Forms.AnchorStyles.Top;
            this.label10.Location = new System.Drawing.Point(182, 114);
            this.label10.Name = "label10";
            this.label10.Size = new System.Drawing.Size(77, 31);
            this.label10.TabIndex = 24;
            this.label10.Text = "Average Steps";
            this.label10.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // mtfAveStepsTextBox
            // 
            this.mtfAveStepsTextBox.Anchor = System.Windows.Forms.AnchorStyles.Top;
            this.mtfAveStepsTextBox.Location = new System.Drawing.Point(185, 174);
            this.mtfAveStepsTextBox.Name = "mtfAveStepsTextBox";
            this.mtfAveStepsTextBox.ReadOnly = true;
            this.mtfAveStepsTextBox.Size = new System.Drawing.Size(75, 20);
            this.mtfAveStepsTextBox.TabIndex = 10;
            this.mtfAveStepsTextBox.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // Form1
            // 
            this.AcceptButton = this.goButton;
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(382, 261);
            this.Controls.Add(this.countAveStepsTextBox);
            this.Controls.Add(this.swapAveStepsTextBox);
            this.Controls.Add(this.noneAveStepsTextBox);
            this.Controls.Add(this.label10);
            this.Controls.Add(this.mtfAveStepsTextBox);
            this.Controls.Add(this.quadraticRadioButton);
            this.Controls.Add(this.label9);
            this.Controls.Add(this.linearRadioButton);
            this.Controls.Add(this.equalRadioButton);
            this.Controls.Add(this.countExpectedStepsTextBox);
            this.Controls.Add(this.countNumStepsTextBox);
            this.Controls.Add(this.label8);
            this.Controls.Add(this.swapExpectedStepsTextBox);
            this.Controls.Add(this.swapNumStepsTextBox);
            this.Controls.Add(this.label7);
            this.Controls.Add(this.noneExpectedStepsTextBox);
            this.Controls.Add(this.noneNumStepsTextBox);
            this.Controls.Add(this.label6);
            this.Controls.Add(this.label5);
            this.Controls.Add(this.mtfExpectedStepsTextBox);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.mtfNumStepsTextBox);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.goButton);
            this.Controls.Add(this.numSearchesTextBox);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.numValuesTextBox);
            this.Controls.Add(this.label1);
            this.Name = "Form1";
            this.Text = "SelfOrganizingLists";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TextBox numValuesTextBox;
        private System.Windows.Forms.TextBox numSearchesTextBox;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Button goButton;
        private System.Windows.Forms.TextBox mtfNumStepsTextBox;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.TextBox mtfExpectedStepsTextBox;
        private System.Windows.Forms.TextBox noneExpectedStepsTextBox;
        private System.Windows.Forms.TextBox noneNumStepsTextBox;
        private System.Windows.Forms.Label label6;
        private System.Windows.Forms.TextBox swapExpectedStepsTextBox;
        private System.Windows.Forms.TextBox swapNumStepsTextBox;
        private System.Windows.Forms.Label label7;
        private System.Windows.Forms.TextBox countExpectedStepsTextBox;
        private System.Windows.Forms.TextBox countNumStepsTextBox;
        private System.Windows.Forms.Label label8;
        private System.Windows.Forms.RadioButton equalRadioButton;
        private System.Windows.Forms.RadioButton linearRadioButton;
        private System.Windows.Forms.Label label9;
        private System.Windows.Forms.RadioButton quadraticRadioButton;
        private System.Windows.Forms.TextBox countAveStepsTextBox;
        private System.Windows.Forms.TextBox swapAveStepsTextBox;
        private System.Windows.Forms.TextBox noneAveStepsTextBox;
        private System.Windows.Forms.Label label10;
        private System.Windows.Forms.TextBox mtfAveStepsTextBox;
    }
}

