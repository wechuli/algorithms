namespace RodCuttingWithCutCosts
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
            this.cutsTextBox = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.bestValueTextBox = new System.Windows.Forms.TextBox();
            this.label2 = new System.Windows.Forms.Label();
            this.valuesTextBox = new System.Windows.Forms.TextBox();
            this.label5 = new System.Windows.Forms.Label();
            this.cutButton = new System.Windows.Forms.Button();
            this.rodLengthTextBox = new System.Windows.Forms.TextBox();
            this.label3 = new System.Windows.Forms.Label();
            this.cutCostTextBox = new System.Windows.Forms.TextBox();
            this.label4 = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // cutsTextBox
            // 
            this.cutsTextBox.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.cutsTextBox.Location = new System.Drawing.Point(68, 126);
            this.cutsTextBox.Name = "cutsTextBox";
            this.cutsTextBox.Size = new System.Drawing.Size(173, 20);
            this.cutsTextBox.TabIndex = 4;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(12, 129);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(31, 13);
            this.label1.TabIndex = 30;
            this.label1.Text = "Cuts:";
            // 
            // bestValueTextBox
            // 
            this.bestValueTextBox.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.bestValueTextBox.Location = new System.Drawing.Point(68, 152);
            this.bestValueTextBox.Name = "bestValueTextBox";
            this.bestValueTextBox.Size = new System.Drawing.Size(173, 20);
            this.bestValueTextBox.TabIndex = 5;
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(12, 155);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(42, 13);
            this.label2.TabIndex = 29;
            this.label2.Text = "Values:";
            // 
            // valuesTextBox
            // 
            this.valuesTextBox.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.valuesTextBox.Location = new System.Drawing.Point(68, 16);
            this.valuesTextBox.Name = "valuesTextBox";
            this.valuesTextBox.Size = new System.Drawing.Size(173, 20);
            this.valuesTextBox.TabIndex = 0;
            this.valuesTextBox.Text = "1 2 3 5 5 6 7 8 9 11 11 12 13 14 16 16 17 18 19 21";
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Location = new System.Drawing.Point(12, 19);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(42, 13);
            this.label5.TabIndex = 28;
            this.label5.Text = "Values:";
            // 
            // cutButton
            // 
            this.cutButton.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.cutButton.Location = new System.Drawing.Point(247, 14);
            this.cutButton.Name = "cutButton";
            this.cutButton.Size = new System.Drawing.Size(75, 23);
            this.cutButton.TabIndex = 3;
            this.cutButton.Text = "Cut";
            this.cutButton.UseVisualStyleBackColor = true;
            this.cutButton.Click += new System.EventHandler(this.cutButton_Click);
            // 
            // rodLengthTextBox
            // 
            this.rodLengthTextBox.Location = new System.Drawing.Point(68, 68);
            this.rodLengthTextBox.Name = "rodLengthTextBox";
            this.rodLengthTextBox.Size = new System.Drawing.Size(37, 20);
            this.rodLengthTextBox.TabIndex = 2;
            this.rodLengthTextBox.Text = "17";
            this.rodLengthTextBox.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(12, 71);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(43, 13);
            this.label3.TabIndex = 26;
            this.label3.Text = "Length:";
            // 
            // cutCostTextBox
            // 
            this.cutCostTextBox.Location = new System.Drawing.Point(68, 42);
            this.cutCostTextBox.Name = "cutCostTextBox";
            this.cutCostTextBox.Size = new System.Drawing.Size(37, 20);
            this.cutCostTextBox.TabIndex = 1;
            this.cutCostTextBox.Text = "0.5";
            this.cutCostTextBox.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(12, 45);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(50, 13);
            this.label4.TabIndex = 32;
            this.label4.Text = "Cut Cost:";
            // 
            // Form1
            // 
            this.AcceptButton = this.cutButton;
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(334, 186);
            this.Controls.Add(this.cutCostTextBox);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.cutsTextBox);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.bestValueTextBox);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.valuesTextBox);
            this.Controls.Add(this.label5);
            this.Controls.Add(this.cutButton);
            this.Controls.Add(this.rodLengthTextBox);
            this.Controls.Add(this.label3);
            this.Name = "Form1";
            this.Text = "RodCuttingWithCutCosts";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.TextBox cutsTextBox;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TextBox bestValueTextBox;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.TextBox valuesTextBox;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.Button cutButton;
        private System.Windows.Forms.TextBox rodLengthTextBox;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.TextBox cutCostTextBox;
        private System.Windows.Forms.Label label4;
    }
}

