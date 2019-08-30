namespace BinomialHeap
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
            this.heapTreeView = new System.Windows.Forms.TreeView();
            this.dequeueButton = new System.Windows.Forms.Button();
            this.enqueueButton = new System.Windows.Forms.Button();
            this.valueTextBox = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.addValuesButton = new System.Windows.Forms.Button();
            this.label2 = new System.Windows.Forms.Label();
            this.numValuesTextBox = new System.Windows.Forms.TextBox();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.label4 = new System.Windows.Forms.Label();
            this.maxTextBox = new System.Windows.Forms.TextBox();
            this.label3 = new System.Windows.Forms.Label();
            this.minTextBox = new System.Windows.Forms.TextBox();
            this.groupBox1.SuspendLayout();
            this.SuspendLayout();
            // 
            // heapTreeView
            // 
            this.heapTreeView.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.heapTreeView.Location = new System.Drawing.Point(254, 12);
            this.heapTreeView.Name = "heapTreeView";
            this.heapTreeView.Size = new System.Drawing.Size(336, 162);
            this.heapTreeView.TabIndex = 3;
            // 
            // dequeueButton
            // 
            this.dequeueButton.DialogResult = System.Windows.Forms.DialogResult.Cancel;
            this.dequeueButton.Location = new System.Drawing.Point(165, 151);
            this.dequeueButton.Name = "dequeueButton";
            this.dequeueButton.Size = new System.Drawing.Size(75, 23);
            this.dequeueButton.TabIndex = 2;
            this.dequeueButton.Text = "Dequeue";
            this.dequeueButton.UseVisualStyleBackColor = true;
            this.dequeueButton.Click += new System.EventHandler(this.dequeueButton_Click);
            // 
            // enqueueButton
            // 
            this.enqueueButton.DialogResult = System.Windows.Forms.DialogResult.Cancel;
            this.enqueueButton.Location = new System.Drawing.Point(165, 122);
            this.enqueueButton.Name = "enqueueButton";
            this.enqueueButton.Size = new System.Drawing.Size(75, 23);
            this.enqueueButton.TabIndex = 1;
            this.enqueueButton.Text = "Enqueue";
            this.enqueueButton.UseVisualStyleBackColor = true;
            this.enqueueButton.Click += new System.EventHandler(this.enqueueButton_Click);
            // 
            // valueTextBox
            // 
            this.valueTextBox.Location = new System.Drawing.Point(92, 135);
            this.valueTextBox.Name = "valueTextBox";
            this.valueTextBox.Size = new System.Drawing.Size(58, 20);
            this.valueTextBox.TabIndex = 0;
            this.valueTextBox.Text = "10";
            this.valueTextBox.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(32, 138);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(37, 13);
            this.label1.TabIndex = 9;
            this.label1.Text = "Value:";
            // 
            // addValuesButton
            // 
            this.addValuesButton.Location = new System.Drawing.Point(153, 43);
            this.addValuesButton.Name = "addValuesButton";
            this.addValuesButton.Size = new System.Drawing.Size(75, 23);
            this.addValuesButton.TabIndex = 3;
            this.addValuesButton.Text = "Add Values";
            this.addValuesButton.UseVisualStyleBackColor = true;
            this.addValuesButton.Click += new System.EventHandler(this.addValuesButton_Click);
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(20, 74);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(52, 13);
            this.label2.TabIndex = 4;
            this.label2.Text = "# Values:";
            // 
            // numValuesTextBox
            // 
            this.numValuesTextBox.Location = new System.Drawing.Point(80, 71);
            this.numValuesTextBox.Name = "numValuesTextBox";
            this.numValuesTextBox.Size = new System.Drawing.Size(58, 20);
            this.numValuesTextBox.TabIndex = 2;
            this.numValuesTextBox.Text = "10";
            this.numValuesTextBox.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.label4);
            this.groupBox1.Controls.Add(this.maxTextBox);
            this.groupBox1.Controls.Add(this.label3);
            this.groupBox1.Controls.Add(this.minTextBox);
            this.groupBox1.Controls.Add(this.addValuesButton);
            this.groupBox1.Controls.Add(this.label2);
            this.groupBox1.Controls.Add(this.numValuesTextBox);
            this.groupBox1.Location = new System.Drawing.Point(12, 12);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(236, 104);
            this.groupBox1.TabIndex = 13;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "Random Values";
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(20, 48);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(54, 13);
            this.label4.TabIndex = 9;
            this.label4.Text = "Maximum:";
            // 
            // maxTextBox
            // 
            this.maxTextBox.Location = new System.Drawing.Point(80, 45);
            this.maxTextBox.Name = "maxTextBox";
            this.maxTextBox.Size = new System.Drawing.Size(58, 20);
            this.maxTextBox.TabIndex = 1;
            this.maxTextBox.Text = "100";
            this.maxTextBox.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(20, 22);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(51, 13);
            this.label3.TabIndex = 7;
            this.label3.Text = "Minimum:";
            // 
            // minTextBox
            // 
            this.minTextBox.Location = new System.Drawing.Point(80, 19);
            this.minTextBox.Name = "minTextBox";
            this.minTextBox.Size = new System.Drawing.Size(58, 20);
            this.minTextBox.TabIndex = 0;
            this.minTextBox.Text = "1";
            this.minTextBox.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // Form1
            // 
            this.AcceptButton = this.enqueueButton;
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.CancelButton = this.dequeueButton;
            this.ClientSize = new System.Drawing.Size(602, 186);
            this.Controls.Add(this.heapTreeView);
            this.Controls.Add(this.dequeueButton);
            this.Controls.Add(this.enqueueButton);
            this.Controls.Add(this.valueTextBox);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.groupBox1);
            this.Name = "Form1";
            this.Text = "BinomialHeap";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.groupBox1.ResumeLayout(false);
            this.groupBox1.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.TreeView heapTreeView;
        private System.Windows.Forms.Button dequeueButton;
        private System.Windows.Forms.Button enqueueButton;
        private System.Windows.Forms.TextBox valueTextBox;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Button addValuesButton;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.TextBox numValuesTextBox;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.TextBox maxTextBox;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.TextBox minTextBox;
    }
}

