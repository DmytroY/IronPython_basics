import clr
clr.AddReference('System.Windows.Forms')
clr.AddReference('System.Drawing')

from System.Windows.Forms import Application, MessageBox
import MainForm

Application.EnableVisualStyles()
form = MainForm.MainForm()
Application.Run(form)

MessageBox.Show("That is all, budy !")