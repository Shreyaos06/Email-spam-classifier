import csv
from collections import defaultdict
from filelookup import find_value_with_csv
from preprocess import clean_text
import math

CSV_PATH = "C:\\Users\\shrey\\OneDrive\\Desktop\\Python_Jackfruit\\Email_spam_detector\\data\\emails.csv"

class NaiveBayesSpamClassifier:
    def __init__(self):
        self.spam_counts = defaultdict(int)  #Stores how many times each word appears in spam emails
        self.ham_counts = defaultdict(int)   #Stores how many times each word appears in ham (non-spam) emails
        self.total_spam = 0 #total no of spam words
        self.total_ham = 0  #total no of ham words
        self.vocab = set()  #stores all unique words that appear in both spam and ham emails
        self.load_and_train()  #analyse info from email.csv file first

    def load_and_train(self):
        self.spam_counts.clear()
        self.ham_counts.clear()
        self.total_spam = 0
        self.total_ham = 0
        self.vocab = set()
        with open(CSV_PATH, newline='', encoding='utf-8') as f: 
            reader = csv.DictReader(f)
            for row in reader:
                tokens = clean_text(row['text'])  #clean_text() prepares the email text for machine learning.
                                                #row['text'] access the content of each row
                if row['label'] == 'spam':
                    for t in tokens:
                        self.spam_counts[t] += 1
                        self.total_spam += 1
                        self.vocab.add(t)
                else:
                    for t in tokens:
                        self.ham_counts[t] += 1
                        self.total_ham += 1
                        self.vocab.add(t)

    
    def predict(self, text):
        # first check whether the text is available directly in the lookup file
        spam_or_ham = find_value_with_csv('user_feedbackcd.csv', text)
        if spam_or_ham == 'spam':
            return 'SPAM'
        elif spam_or_ham == 'ham':
            return 'HAM'
        
        tokens = clean_text(text)
        spam_log_prob = 0.0
        ham_log_prob = 0.0
        vocab_size = len(self.vocab) + 1  #no of unique words
                                          #The +1 is added for Laplace smoothing
                                          #laplace smoothing is used to calculate probability
                                        #In Naive Bayes, probabilities of all words are multiplied.
                                        #If even one probability is 0, the final result becomes 0.
        for t in tokens:
        #For each word in the email, the code adds how likely that word is to appear in spam and ham, using logarithmic probabilities.
            spam_log_prob += math.log(
            (   self.spam_counts[t] + 1) / (self.total_spam + vocab_size)
            )
            ham_log_prob += math.log(
                (self.ham_counts[t] + 1) / (self.total_ham + vocab_size)
            )

        spam_log_prob += math.log(self.total_spam + 1)
        ham_log_prob += math.log(self.total_ham + 1)

        return 'SPAM' if spam_log_prob > ham_log_prob else 'HAM'


    def learn_from_feedback(self, text, correct_label):
        with open(CSV_PATH, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([text, correct_label.lower()])
        self.load_and_train()  #Reloads the entire dataset
                                #Retrains the spam detector
                                #Includes the new feedback
