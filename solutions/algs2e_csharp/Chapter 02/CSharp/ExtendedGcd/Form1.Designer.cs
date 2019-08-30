namespace ExtendedGcd
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
            this.aTextBox = new System.Windows.Forms.TextBox();
            this.bTextBox = new System.Windows.Forms.TextBox();
            this.label2 = new System.Windows.Forms.Label();
            this.goButton = new System.Windows.Forms.Button();
            this.label3 = new System.Windows.Forms.Label();
            this.gcdTextBox = new System.Windows.Forms.TextBox();
            this.lcmTextBox = new System.Windows.Forms.TextBox();
            this.label4 = new System.Windows.Forms.Label();
            this.bezoutTextBox = new System.Windows.Forms.TextBox();
            this.label5 = new System.Windows.Forms.Label();
            this.verifyTextBox = new System.Windows.Forms.TextBox();
            this.label6 = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(12, 17);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(17, 13);
            this.label1.TabIndex = 0;
            this.label1.Text = "A:";
            // 
            // aTextBox
            // 
            this.aTextBox.Location = new System.Drawing.Point(61, 14);
            this.aTextBox.Name = "aTextBox";
            this.aTextBox.Size = new System.Drawing.Size(130, 20);
            this.aTextBox.TabIndex = 1;
            this.aTextBox.Text = "210";
            this.aTextBox.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // bTextBox
            // 
            this.bTextBox.Location = new System.Drawing.Point(61, 40);
            this.bTextBox.Name = "bTextBox";
            this.bTextBox.Size = new System.Drawing.Size(130, 20);
            this.bTextBox.TabIndex = 3;
            this.bTextBox.Text = "154";
            this.bTextBox.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(12, 43);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(17, 13);
            this.label2.TabIndex = 2;
            this.label2.Text = "B:";
            // 
            // goButton
            // 
            this.goButton.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.goButton.Location = new System.Drawing.Point(197, 12);
            this.goButton.Name = "goButton";
            this.goButton.Size = new System.Drawing.Size(75, 23);
            this.goButton.TabIndex = 4;
            this.goButton.Text = "Go";
            this.goButton.UseVisualStyleBackColor = true;
            this.goButton.Click += new System.EventHandler(this.goButton_Click);
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(12, 99);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(33, 13);
            this.label3.TabIndex = 5;
            this.label3.Text = "GCD:";
            // 
            // gcdTextBox
            // 
            this.gcdTextBox.Location = new System.Drawing.Point(61, 96);
            this.gcdTextBox.Name = "gcdTextBox";
            this.gcdTextBox.ReadOnly = true;
            this.gcdTextBox.Size = new System.Drawing.Size(130, 20);
            this.gcdTextBox.TabIndex = 6;
            this.gcdTextBox.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // lcmTextBox
            // 
            this.lcmTextBox.Location = new System.Drawing.Point(61, 122);
            this.lcmTextBox.Name = "lcmTextBox";
            this.lcmTextBox.ReadOnly = true;
            this.lcmTextBox.Size = new System.Drawing.Size(130, 20);
            this.lcmTextBox.TabIndex = 8;
            this.lcmTextBox.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(12, 125);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(32, 13);
            this.label4.TabIndex = 7;
            this.label4.Text = "LCM:";
            // 
            // bezoutTextBox
            // 
            this.bezoutTextBox.Location = new System.Drawing.Point(61, 148);
            this.bezoutTextBox.Name = "bezoutTextBox";
            this.bezoutTextBox.ReadOnly = true;
            this.bezoutTextBox.Size = new System.Drawing.Size(130, 20);
            this.bezoutTextBox.TabIndex = 10;
            this.bezoutTextBox.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Location = new System.Drawing.Point(12, 151);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(43, 13);
            this.label5.TabIndex = 9;
            this.label5.Text = "Bézout:";
            // 
            // verifyTextBox
            // 
            this.verifyTextBox.Location = new System.Drawing.Point(61, 174);
            this.verifyTextBox.Name = "verifyTextBox";
            this.verifyTextBox.ReadOnly = true;
            this.verifyTextBox.Size = new System.Drawing.Size(130, 20);
            this.verifyTextBox.TabIndex = 12;
            this.verifyTextBox.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // label6
            // 
            this.label6.AutoSize = true;
            this.label6.Location = new System.Drawing.Point(12, 177);
            this.label6.Name = "label6";
            this.label6.Size = new System.Drawing.Size(36, 13);
            this.label6.TabIndex = 11;
            this.label6.Text = "Verify:";
            // 
            // Form1
            // 
            this.AcceptButton = this.goButton;
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(284, 207);
            this.Controls.Add(this.verifyTextBox);
            this.Controls.Add(this.label6);
            this.Controls.Add(this.bezoutTextBox);
            this.Controls.Add(this.label5);
            this.Controls.Add(this.lcmTextBox);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.gcdTextBox);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.goButton);
            this.Controls.Add(this.bTextBox);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.aTextBox);
            this.Controls.Add(this.label1);
            this.Name = "Form1";
            this.Text = "ExtendedGcd";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TextBox aTextBox;
        private System.Windows.Forms.TextBox bTextBox;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Button goButton;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.TextBox gcdTextBox;
        private System.Windows.Forms.TextBox lcmTextBox;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.TextBox bezoutTextBox;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.TextBox verifyTextBox;
        private System.Windows.Forms.Label label6;
    }
}

