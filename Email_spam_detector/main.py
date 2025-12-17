import wx
from gui import SpamGUI

app = wx.App(False)  #(false)-Do not redirect standard output to a window
SpamGUI()  #Create an instance of the SpamGUI class
            #runs the code inside the __init__ method of SpamGUI class
app.MainLoop()   #Keeps the window open and responsive.
 