namespace lightshotscrape_gui
{
    partial class Form1
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
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
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            btnNyBild = new Button();
            pictureBox1 = new PictureBox();
            btnLaddaNer = new Button();
            textBox1 = new TextBox();
            numericUpDown1 = new NumericUpDown();
            label1 = new Label();
            checkBox1 = new CheckBox();
            gbxNerladdning = new GroupBox();
            textBox3 = new TextBox();
            progressBar1 = new ProgressBar();
            btnFilepathSelect = new Button();
            label2 = new Label();
            textBox2 = new TextBox();
            folderBrowserDialog1 = new FolderBrowserDialog();
            ((System.ComponentModel.ISupportInitialize)pictureBox1).BeginInit();
            ((System.ComponentModel.ISupportInitialize)numericUpDown1).BeginInit();
            gbxNerladdning.SuspendLayout();
            SuspendLayout();
            // 
            // btnNyBild
            // 
            btnNyBild.Location = new Point(12, 386);
            btnNyBild.Name = "btnNyBild";
            btnNyBild.Size = new Size(75, 23);
            btnNyBild.TabIndex = 0;
            btnNyBild.Text = "Ny bild";
            btnNyBild.UseVisualStyleBackColor = true;
            btnNyBild.Click += btnNyBild_Click;
            // 
            // pictureBox1
            // 
            pictureBox1.Location = new Point(12, 12);
            pictureBox1.Name = "pictureBox1";
            pictureBox1.Size = new Size(368, 368);
            pictureBox1.TabIndex = 1;
            pictureBox1.TabStop = false;
            // 
            // btnLaddaNer
            // 
            btnLaddaNer.Location = new Point(93, 386);
            btnLaddaNer.Name = "btnLaddaNer";
            btnLaddaNer.Size = new Size(75, 23);
            btnLaddaNer.TabIndex = 2;
            btnLaddaNer.Text = "Ladda ner";
            btnLaddaNer.UseVisualStyleBackColor = true;
            // 
            // textBox1
            // 
            textBox1.Location = new Point(174, 387);
            textBox1.Name = "textBox1";
            textBox1.Size = new Size(594, 23);
            textBox1.TabIndex = 3;
            // 
            // numericUpDown1
            // 
            numericUpDown1.Location = new Point(6, 43);
            numericUpDown1.Maximum = new decimal(new int[] { 10000000, 0, 0, 0 });
            numericUpDown1.Name = "numericUpDown1";
            numericUpDown1.Size = new Size(120, 23);
            numericUpDown1.TabIndex = 4;
            // 
            // label1
            // 
            label1.AutoSize = true;
            label1.Location = new Point(6, 25);
            label1.Name = "label1";
            label1.Size = new Size(68, 15);
            label1.TabIndex = 5;
            label1.Text = "Antal bilder";
            // 
            // checkBox1
            // 
            checkBox1.AutoSize = true;
            checkBox1.Location = new Point(6, 72);
            checkBox1.Name = "checkBox1";
            checkBox1.Size = new Size(88, 19);
            checkBox1.TabIndex = 6;
            checkBox1.Text = "Kör föralltid";
            checkBox1.UseVisualStyleBackColor = true;
            // 
            // gbxNerladdning
            // 
            gbxNerladdning.Controls.Add(textBox3);
            gbxNerladdning.Controls.Add(progressBar1);
            gbxNerladdning.Controls.Add(btnFilepathSelect);
            gbxNerladdning.Controls.Add(label2);
            gbxNerladdning.Controls.Add(textBox2);
            gbxNerladdning.Controls.Add(label1);
            gbxNerladdning.Controls.Add(checkBox1);
            gbxNerladdning.Controls.Add(numericUpDown1);
            gbxNerladdning.Location = new Point(390, 12);
            gbxNerladdning.Name = "gbxNerladdning";
            gbxNerladdning.Size = new Size(378, 368);
            gbxNerladdning.TabIndex = 7;
            gbxNerladdning.TabStop = false;
            gbxNerladdning.Text = "Nerladdning";
            // 
            // textBox3
            // 
            textBox3.Location = new Point(6, 339);
            textBox3.Name = "textBox3";
            textBox3.Size = new Size(366, 23);
            textBox3.TabIndex = 11;
            // 
            // progressBar1
            // 
            progressBar1.Location = new Point(6, 310);
            progressBar1.Name = "progressBar1";
            progressBar1.Size = new Size(366, 23);
            progressBar1.TabIndex = 10;
            // 
            // btnFilepathSelect
            // 
            btnFilepathSelect.Location = new Point(297, 126);
            btnFilepathSelect.Name = "btnFilepathSelect";
            btnFilepathSelect.Size = new Size(75, 23);
            btnFilepathSelect.TabIndex = 9;
            btnFilepathSelect.Text = "Välj...";
            btnFilepathSelect.UseVisualStyleBackColor = true;
            // 
            // label2
            // 
            label2.AutoSize = true;
            label2.Location = new Point(6, 108);
            label2.Name = "label2";
            label2.Size = new Size(106, 15);
            label2.TabIndex = 8;
            label2.Text = "Nedladdningsplats";
            // 
            // textBox2
            // 
            textBox2.Location = new Point(6, 126);
            textBox2.Name = "textBox2";
            textBox2.Size = new Size(285, 23);
            textBox2.TabIndex = 7;
            // 
            // Form1
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(780, 416);
            Controls.Add(gbxNerladdning);
            Controls.Add(textBox1);
            Controls.Add(btnLaddaNer);
            Controls.Add(pictureBox1);
            Controls.Add(btnNyBild);
            Name = "Form1";
            Text = "Form1";
            ((System.ComponentModel.ISupportInitialize)pictureBox1).EndInit();
            ((System.ComponentModel.ISupportInitialize)numericUpDown1).EndInit();
            gbxNerladdning.ResumeLayout(false);
            gbxNerladdning.PerformLayout();
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private Button btnNyBild;
        private PictureBox pictureBox1;
        private Button btnLaddaNer;
        private TextBox textBox1;
        private NumericUpDown numericUpDown1;
        private Label label1;
        private CheckBox checkBox1;
        private GroupBox gbxNerladdning;
        private Button btnFilepathSelect;
        private Label label2;
        private TextBox textBox2;
        private FolderBrowserDialog folderBrowserDialog1;
        private TextBox textBox3;
        private ProgressBar progressBar1;
    }
}
