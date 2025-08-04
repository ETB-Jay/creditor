# --- Packages --- 
import csv
import pandas as pd

#
if __name__ == "__main__":
    with open('eggs.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            print(row)
        