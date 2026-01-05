import wx
from classifier import NaiveBayesSpamClassifier  #Imports the spam detection model.
from feedback import save_feedback

class SpamGUI(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Smart Spam Detector", size=(600, 400))  #main application window
                                                                            #refers to the parent class here,wx.Frame
        panel = wx.Panel(self)  
        #panel.SetBackgroundColour("light blue")    

        self.model = NaiveBayesSpamClassifier()
        self.last_text = "" 
        self.last_prediction = ""
         #Stores the last entered message and its prediction

        vbox = wx.BoxSizer(wx.VERTICAL) #arrange items vertically from top to bottom

        self.text_box = wx.TextCtrl(panel, style=wx.TE_MULTILINE)
        self.text_box.SetBackgroundColour('orange')
        vbox.Add(self.text_box, 1, wx.EXPAND | wx.ALL, 10)
        classify_btn = wx.Button(panel, label="Classify")
        classify_btn.SetBackgroundColour(wx.YELLOW)
        classify_btn.Bind(wx.EVT_BUTTON, self.classify)  #This line connects the Classify button to the function that runs when the button is clicked.
        vbox.Add(classify_btn, 0, wx.ALL | wx.CENTER, 5)

        self.result = wx.StaticText(panel, wx.ID_ANY, "")
        vbox.Add(self.result, 0, wx.ALL | wx.CENTER, 5)

        hbox = wx.BoxSizer(wx.HORIZONTAL)

        right_btn = wx.Button(panel, label="Right")
        right_btn.SetBackgroundColour(wx.GREEN)
        wrong_btn = wx.Button(panel, label="Wrong")
        wrong_btn.SetBackgroundColour(wx.RED)

        right_btn.Bind(wx.EVT_BUTTON, self.correct)
        wrong_btn.Bind(wx.EVT_BUTTON, self.wrong)

        hbox.Add(right_btn, 0, wx.ALL, 5)
        hbox.Add(wrong_btn, 0, wx.ALL, 5)

        vbox.Add(hbox, 0, wx.CENTER)

        panel.SetSizer(vbox)
        self.Show()  #displays the GUI window

    def classify(self, event):  #runs whne classify button is clicked
        self.last_text = self.text_box.GetValue().strip()  #Reads text from input box and removes extra spaces

        if not self.last_text:  #if input is empty it displays the following message and stops execution
            wx.MessageBox("Please enter a message")
            return

        self.last_prediction = self.model.predict(self.last_text)   #Uses model to predict SPAM or HAM
        self.result.SetLabel(f"Prediction: {self.last_prediction}")   #Displays the result on screen

    def correct(self, event):  #runs when right button is clicked
        save_feedback(self.last_text, self.last_prediction)  #Saves message and predicted label
        self.model.load_and_train()   #Retrains the model with new feedback
        wx.MessageBox("Feedback saved & model updated ✔")


    def wrong(self, event):
        dlg = wx.SingleChoiceDialog(
            self, "Select correct label", "Feedback", ["spam", "ham"])  #Opens a dialog box
                                                                        #User selects correct label
        
        if dlg.ShowModal() == wx.ID_OK:  #ShowModal() shows the dialog box and pauses the program until the user closes it.
            correct_label = dlg.GetStringSelection()  #This gets the option selected by the user in the dialog.
            save_feedback(self.last_text, correct_label) #Saves message that was last classified and correct label
            self.model.load_and_train()   
            wx.MessageBox("Correct feedback saved & model updated ✔")
        dlg.Destroy()


