import csv
import os  #used to check if a file already exists

FEEDBACK_FILE = "user_feedback.csv"

def save_feedback(message, label):
    """
    Saves user feedback into a CSV file.
    message: email/message text
    label: 'spam' or 'ham'
    """

    file_exists = os.path.isfile(FEEDBACK_FILE)  # Checks whether user_feedback.csv already exists

    with open(FEEDBACK_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f) #Used to write rows into the file easily
        if not file_exists:
            writer.writerow(["message", "label"]) #ensures no duplicate headers
        writer.writerow([message, label])
