import pandas as pd

def read_xls(path):
    return pd.read_excel(path, header=0)

def load_data():
    top19992014 = read_xls("data/lijsten_alle_jaren.xlsx")
    top19992014['artiest'] = top19992014['artiest'].str.lower()
    top19992014['titel'] = top19992014['titel'].str.lower()
    # print top19992014.head(10)

    top2015 = read_xls("data/TOP-2000-2015.xls")
    top2015['artiest'] = top2015['artiest'].str.lower()
    top2015['titel'] = top2015['titel'].str.lower()
    # print top2015.head(10)

    top2016 = read_xls("data/TOP-2000-2016.xls")
    top2016.drop('Datum', axis=1, inplace=True)
    top2016.drop('datum2', axis=1, inplace=True)
    top2016['artiest'] = top2016['artiest'].str.lower()
    top2016['titel'] = top2016['titel'].str.lower()
    top2016.rename(columns={'pos 2016': '2016', 'titel': 'titel', 'artiest': 'artiest'}, inplace=True)
    # print top2016.head(10)

    top2017 = read_xls("data/TOP-2000-2017v2.xls")
    top2017 = top2017[top2017["pos 2017"].notnull()]
    top2017["pos 2017"] = top2017["pos 2017"].astype(int)
    top2017['artiest'] = top2017['artiest'].str.lower()
    top2017['titel'] = top2017['titel'].str.lower()
    top2017.rename(columns={'pos 2017': '2017', 'titel': 'titel', 'artiest': 'artiest'}, inplace=True)
    # print top2017.tail(30)

    return top19992014, top2015, top2016, top2017

def merge_files(top19992014, top2015, top2016, top2017):
    top2015.drop('jaar', axis=1, inplace=True)
    top199920142015 = pd.merge(top19992014, top2015, how="outer", right_on=['titel', 'artiest'], left_on=['titel', 'artiest'])
    top2016.drop('jaar', axis=1, inplace=True)
    top1999201420152016 = pd.merge(top199920142015, top2016, how="outer", right_on=['titel', 'artiest'], left_on=['titel', 'artiest'])
    top19992014201520162017 = pd.merge(top1999201420152016, top2017, how="outer", right_on=['titel', 'artiest'], left_on=['titel', 'artiest'])
    return top19992014201520162017

def save_file(df):
    df.to_excel("Top2000_1999-2017.xlsx", sheet_name="Top2000")

def final_cleaning(df):
    # Fill NaN's with 0's
    df.fillna(value=0, inplace=True)

    # TODO: convert to int
    return df

if __name__ == '__main__':
    print "Started!"
    top19992014, top2015, top2016, top2017 = load_data()

    print "Data loaded, now merging"
    merged_top2000 = merge_files(top19992014, top2015, top2016, top2017)
    full_top2000 = final_cleaning(merged_top2000)

    print "Data merged and cleaned"
    print full_top2000.head(100)
    print "Now saving..."
    save_file(full_top2000)
    print "Saved!"