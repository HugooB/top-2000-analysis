import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from langdetect import detect
from langdetect import detect_langs


def load_data():
    # Read in file
    data = pd.read_excel("..\Top2000 1999-2017.xlsx", header=0)
    return data

def get_languages(data):
    # Get column of song titles
    titles = data['Titel']
    print titles

    data['Taal'] = data.apply(lambda row: detect_language(row), axis=1)
    print data['Taal']
    return

def detect_language(row):
    if type(row['Titel']) != int:
        try:
            search = removeNonAscii(row['Titel'] + " " + row['Artiest'])
            output = detect(search)
            if output not in ['en', 'fr', 'nl', 'de', 'es' ,'it']:
                output = "en"
                print str(row['Titel']) + " - " + output
                return output
            else:
                print str(row['Titel']) + " - " + output
                return output
        except:
            return "unknown"
    else:
        return "unknown"


def removeNonAscii(s):
    return "".join(i for i in s if ord(i) < 128)


def plot_languages(data):
    return


if __name__ == '__main__':
    print "Started!"
    top2000 = load_data()

    # Set the number of editions
    years = top2000.columns[3:]

    print detect_langs("If I Can'T Have You")

    top2000_languages = get_languages(top2000)


