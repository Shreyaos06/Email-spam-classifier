import csv
import os

FEEDBACK_FILE = "user_feedback.csv"

def save_feedback(message, label):
    """
    Saves user feedback into a CSV file.
    message: email/message text
    label: 'spam' or 'ham'
    """

    file_exists = os.path.isfile(FEEDBACK_FILE)

    with open(FEEDBACK_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["message", "label"])
        writer.writerow([message, label])
