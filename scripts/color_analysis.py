import pandas as pd
import matplotlib.pyplot as plt


def load_data():
    # Read in file
    data = pd.read_excel("Top2000 1999-2017.xlsx", header=0)
    return data


def count_colors(data):
    # Colors in different languages
    red_list = ['rood', 'red', 'rouge']
    blue_list = ['blauw', 'blue', 'bleu']
    green_list = ['groen', 'green', 'vert']
    yellow_list = ['geel', 'yellow', 'jaune']
    purple_list = [ 'paars', 'purple', 'violet']
    orange_list = ['oranje', 'orange', 'orange']
    black_list = ['zwart', 'black', 'noir']
    white_list = ['wit', 'white', 'blanc']

    # Make empty arrays to fill
    red_arr = []
    blue_arr = []
    green_arr = []
    yellow_arr = []
    purple_arr = []
    orange_arr = []
    black_arr = []
    white_arr = []

    # Loop over each year
    years = data.columns[3:]
    for year in years:

        # Loop over all songs of that year
        print "Now analysing: " + str(year)
        data_year = data[data[year] >= 1]

        # Reset counters to zero
        reds = blues = greens = yellows = purples = oranges = blacks = whites = 0

        for index, row in data_year.iterrows():
            if isinstance(row['Titel'], basestring):
                lowercase = row['Titel'].lower()
                text = lowercase.split(' ')

                # Now count for each color
                for red in red_list:
                    if red in text:
                        reds = reds + 1
                for blue in blue_list:
                    if blue in text:
                        blues = blues + 1
                for green in green_list:
                    if green in text:
                        greens = greens + 1
                for yellow in yellow_list:
                    if yellow in text:
                        yellows = yellows + 1
                for purple in purple_list:
                    if purple in text:
                        purples = purples + 1
                for orange in orange_list:
                    if orange in text:
                        oranges = oranges + 1
                for black in black_list:
                    if black in text:
                        blacks = blacks + 1
                for white in white_list:
                    if white in text:
                        whites = whites + 1

        # Now appending it to the globals
        red_arr.append(reds)
        blue_arr.append(blues)
        green_arr.append(greens)
        yellow_arr.append(yellows)
        purple_arr.append(purples)
        orange_arr.append(oranges)
        black_arr.append(blacks)
        white_arr.append(whites)

    # Combine it all to one dataframe
    years = pd.Series(years, name='Jaar')
    s1 = pd.Series(red_arr, name='Rood')
    s2 = pd.Series(blue_arr, name='Blauw', index=years.index)
    s3 = pd.Series(green_arr, name='Groen', index=years.index)
    s4 = pd.Series(yellow_arr, name='Geel', index=years.index)
    s5 = pd.Series(purple_arr, name='Paars', index=years.index)
    s6 = pd.Series(orange_arr, name='Oranje', index=years.index)
    s7 = pd.Series(black_arr, name='Zwart', index=years.index)
    s8 = pd.Series(white_arr, name='Wit', index=years.index)

    result = pd.concat([years, s1, s2, s3, s4, s5, s6, s7, s8], axis=1)
    result.set_index('Jaar')
    print result
    return result


def visualize_color_counts(data):
    plt.figure()
    plt.plot(data['Jaar'], data['Rood'], color='red')
    plt.plot(data['Jaar'], data['Blauw'], color='blue')
    plt.plot(data['Jaar'], data['Groen'], color='green')
    plt.plot(data['Jaar'], data['Geel'], color='yellow')
    plt.plot(data['Jaar'], data['Paars'], color='purple')
    plt.plot(data['Jaar'], data['Oranje'], color='orange')
    plt.plot(data['Jaar'], data['Zwart'], color='black')
    plt.plot(data['Jaar'], data['Wit'], color='grey')
    plt.axis([1999, 2017, 0, 16])
    plt.title('Kleuren van de Top 2000')
    plt.xlabel('Jaar')
    plt.ylabel('Frequentie van kleur')
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    plt.show()


if __name__ == '__main__':
    print "Started!"
    top2000 = load_data()

    # print top2000.head()

    counted_colors = count_colors(top2000)

    visualize_color_counts(counted_colors)
