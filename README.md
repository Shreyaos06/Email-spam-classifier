Objectives of the Project:
1.To understand how Naive Bayes classification works
2.To apply text preprocessing techniques in Python
3.To build a simple machine learning model for spam detection
4.To design a user-friendly GUI using wxPython
5.To allow the model to learn from user feedback

Technologies Used
1.Python
2.wxPython (for GUI)
3.Naive Bayes Algorithm
4.Regular Expressions (re module)
5.CSV file handling
6.Basic Natural Language Processing concepts

How the System Works
1.The user enters a message into the GUI text box.
2.The message is cleaned by:
-Converting text to lowercase
-Removing special characters and numbers
-Removing unnecessary words
3.The processed text is sent to the Naive Bayes classifier.
4.The model calculates probabilities for:
-Spam
-Ham
5.The class with the higher probability is selected as the result.
6.The output is displayed on the GUI.

Graphical User Interface (GUI)
The GUI is built using wxPython and includes:
1.A multiline text box to enter the message
2.A Classify button to check whether the message is spam or ham
3.A result label to display the prediction
4.A feedback dialog that allows the user to correct the model if the prediction is wrong

User Feedback and Model Learning
If the model gives a wrong prediction:
1.The user can provide the correct label (Spam or Ham)
2.The feedback is saved into a CSV file
3.The model is retrained using the updated data
This allows the system to improve over time.

Naive Bayes Algorithm (Brief Explanation)

Naive Bayes is a probabilistic machine learning algorithm based on Bayes’ Theorem.
It assumes that each word in a message contributes independently to the probability of the message being spam or ham.

Log probabilities are used to:
-Avoid very small numbers
-Improve numerical stability

Sample Output

Input:
“Congratulations! You have won a free gift.”

Output:
Spam

Learning Outcomes

Through this project, I learned:
-How machine learning can be applied to real-world problems
-How Naive Bayes works for text classification
-How to build GUI applications using wxPython
-How to structure a Python project properly
-How feedback can improve model performance

Conclusion

This project demonstrates a simple yet effective approach to email spam detection using Python.
By combining machine learning with a graphical interface, the system becomes both powerful and easy to use. The feedback mechanism makes the project more practical and closer to real-world applications.

