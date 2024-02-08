using System;
using System.Diagnostics;
using System.Security.Cryptography.X509Certificates;

namespace lightshotscrape_gui
{
    public partial class Form1 : Form
    {

        //skapar process för att köpra python skriptet
        public Process process = new Process();
        string rootdir = Directory.GetParent(Directory.GetCurrentDirectory()).Parent.Parent.Parent.FullName;

        public Form1()
        {
            InitializeComponent();
        }

        private void btnNyBild_Click(object sender, EventArgs e)
        {
            if (rootdir != null)
            {
                process.StartInfo.FileName = rootdir + "\\.venv\\Scripts\\python.exe";
                process.StartInfo.Arguments = rootdir + "\\lightshotscrape\\singleImage.py ";

                process.StartInfo.UseShellExecute = false;
                process.StartInfo.CreateNoWindow = true;
                process.StartInfo.RedirectStandardOutput = true;
                process.OutputDataReceived += new DataReceivedEventHandler(process_OutputDataReceived);
                process.Exited += new EventHandler(process_Exited);

                process.Start();
                
                


            }

            else
            {
                MessageBox.Show("Kunde inte hitta sökvägen till lightshotscrape.py");
            }

        }

        private void process_OutputDataReceived(object sender, DataReceivedEventArgs e)
        {
            MessageBox.Show(process.StandardOutput.ReadToEnd());

        }
        private void process_Exited(object sender, EventArgs e)
        {
            MessageBox.Show("Processen avslutades");
        }

    }
}
