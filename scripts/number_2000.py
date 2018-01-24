import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def load_data():
    # Read in file
    data = pd.read_excel("..\Top2000 1999-2017.xlsx", header=0)
    return data


def filter_data(data, years):
    # Create first year to append to it
    number_2000 = data[years[0]] == 2000
    numbers_2000 = pd.DataFrame(data[number_2000])

    # Now iterate over the year that followed
    for year in years[1:]:
        number_2000 = data[year] == 2000
        new_year = pd.DataFrame(data[number_2000])
        numbers_2000 = pd.concat([numbers_2000, new_year], ignore_index=True)

    # Filter out the duplicates
    numbers_2000.drop_duplicates(keep="first", inplace=True)
    return numbers_2000


def visualize_number2000s(song_list):
    # Switch all 0 with 2001 to let songs start on the right side of the graph
    song_list = song_list.replace(0, 2001)

    # Plot the song's positions of the selected artist
    plt.figure()
    for index, row in song_list.iterrows():
        plt.plot(row[3:], c=np.random.rand(3,), label=str(row['Artiest'] + " - " + row['Titel']))
    plt.axis([years.min(), years.max(), 2000, 0])
    plt.title("Posities van de nummer 2000 in de Top 2000")
    plt.xlabel('Jaar')
    plt.ylabel('Positie')
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    plt.show()


if __name__ == '__main__':
    print "Started!"
    top2000 = load_data()

    # Set the number of editions
    years = top2000.columns[3:]

    # Filter on songs that have been on the 2000th place
    numbers_2000 = filter_data(top2000, years)

    # Visualize songs
    visualize_number2000s(numbers_2000)



