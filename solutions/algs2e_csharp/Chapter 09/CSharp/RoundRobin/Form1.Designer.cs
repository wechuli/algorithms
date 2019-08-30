namespace RoundRobin
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
            this.numTeamsTextBox = new System.Windows.Forms.TextBox();
            this.goButton = new System.Windows.Forms.Button();
            this.label2 = new System.Windows.Forms.Label();
            this.scheduleTreeView = new System.Windows.Forms.TreeView();
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(12, 17);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(52, 13);
            this.label1.TabIndex = 0;
            this.label1.Text = "# Teams:";
            // 
            // numTeamsTextBox
            // 
            this.numTeamsTextBox.Location = new System.Drawing.Point(70, 14);
            this.numTeamsTextBox.Name = "numTeamsTextBox";
            this.numTeamsTextBox.Size = new System.Drawing.Size(39, 20);
            this.numTeamsTextBox.TabIndex = 1;
            this.numTeamsTextBox.Text = "6";
            this.numTeamsTextBox.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // goButton
            // 
            this.goButton.Location = new System.Drawing.Point(143, 12);
            this.goButton.Name = "goButton";
            this.goButton.Size = new System.Drawing.Size(75, 23);
            this.goButton.TabIndex = 2;
            this.goButton.Text = "Go";
            this.goButton.UseVisualStyleBackColor = true;
            this.goButton.Click += new System.EventHandler(this.goButton_Click);
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(12, 59);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(55, 13);
            this.label2.TabIndex = 4;
            this.label2.Text = "Schedule:";
            // 
            // scheduleTreeView
            // 
            this.scheduleTreeView.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.scheduleTreeView.Location = new System.Drawing.Point(12, 75);
            this.scheduleTreeView.Name = "scheduleTreeView";
            this.scheduleTreeView.Size = new System.Drawing.Size(200, 204);
            this.scheduleTreeView.TabIndex = 5;
            // 
            // Form1
            // 
            this.AcceptButton = this.goButton;
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(224, 291);
            this.Controls.Add(this.scheduleTreeView);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.goButton);
            this.Controls.Add(this.numTeamsTextBox);
            this.Controls.Add(this.label1);
            this.Name = "Form1";
            this.Text = "RoundRobin";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TextBox numTeamsTextBox;
        private System.Windows.Forms.Button goButton;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.TreeView scheduleTreeView;
    }
}

