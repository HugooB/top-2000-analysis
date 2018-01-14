import pandas as pd
import matplotlib.pyplot as plt


def load_data():
    # Read in file
    data = pd.read_excel("..\Top2000 1999-2017.xlsx", header=0)
    return data


def count_artists(year, data):
    # Select all songs of this year
    print "Now analysing artist of " + str(year)
    data_year = data[data[year] >= 1]

    # Counting number of songs per artist
    counts = data_year['Artiest'].value_counts()

    # Select and return only the first 10 rows
    return counts.head(10)


def visualize_artist_counts(data, year):
    # Plot the counts in a bar chart and show it to the user
    ax = data.plot(kind='bar', title="Top 10 artiesten van de Top 2000 editie " + str(year), legend=False, rot=45)
    ax.set_xlabel("Artiest", fontsize=12)
    ax.set_ylabel("Aantal noteringen", fontsize=12)
    plt.show()


if __name__ == '__main__':
    print "Started!"
    top2000 = load_data()

    # Ask the user which year he wants to analyse
    year = int(raw_input("What year do you want to analyse?").strip())
    if 1999 <= year <= 2017:
        # Get the counts of this edition
        artist_counts = count_artists(year, top2000).to_frame()

        # Visualize results
        visualize_artist_counts(artist_counts, year)
    else:
        print "The year " + str(year) + " is not an edition of the Top2000"
