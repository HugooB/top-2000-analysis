import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def load_data():
    # Read in file
    data = pd.read_excel("..\Top2000 1999-2017.xlsx", header=0)
    return data


def count_artists(artist, data):
    # Select all songs of this artist
    songs_list = data[data['Artiest'] == artist]
    print str(len(songs_list)) + " songs of " + str(artist) + " found!"
    print songs_list
    return songs_list


def visualize_artist_counts(artist, song_list):
    # Switch all 0 with 2001 to let songs start on the right side of the graph
    song_list = song_list.replace(0, 2001)
    # Plot the song's positions of the selected artist
    plt.figure()
    for index, row in song_list.iterrows():
        plt.plot(row[3:], c=np.random.rand(3,), label=row['Titel'])
    plt.axis([years.min(), years.max(), 2000, 0])
    plt.title('Posities van de ' + str(len(song_list)) + ' platen van ' + str(artist) + " in de Top 2000")
    plt.xlabel('Jaar')
    plt.ylabel('Positie')
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    plt.show()

if __name__ == '__main__':
    print "Started!"
    top2000 = load_data()

    # Set the number of editions
    years = top2000.columns[3:]

    # Ask the user which artist he want's to analyse
    artist = raw_input("What is the name of the artist you want to analyse?").strip().title()
    song_list = count_artists(artist, top2000)
    if len(song_list) > 0:
        # Visualize results
        visualize_artist_counts(artist, song_list)
    else:
        print "Artist can not be found!"