import System.Windows.Forms
import System.Drawing

from System.Drawing import *
from System.Windows.Forms import *


class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()

    def InitializeComponent(self):
        self.SuspendLayout()
        # MainForm
        self.ClientSize = System.Drawing.Size(360,240)
        self.Name = "MainForm"
        self.Text = "Forms"
        self.ResumeLayout(False)

    