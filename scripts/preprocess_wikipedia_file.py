import pandas as pd

def read_xls(path):
    return pd.read_excel(path, header=0)

def load_data():
    # Read in file
    data = read_xls("data/top2000_1999-2017_ready.xlsx")

    # Replace * with 0
    data.replace(to_replace='*', value=0, inplace=True)

    # Capitalize each word
    data['Artiest'] = data['Artiest'].str.title()
    data['Titel'] = data['Titel'].str.title()

    return data

def save_file(df):
    df.to_excel("Top2000 1999-2017.xlsx", sheet_name="Top2000 1999-2017")

if __name__ == '__main__':
    print "Started!"
    top2000 = load_data()

    print "Data loaded, now saving"
    save_file(top2000)