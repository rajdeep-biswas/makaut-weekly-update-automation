import pandas as pd
from dtparser import parsedatetme

xlids = [2, 3, 4, 5, 6]

subjects = []

for xlid in xlids:
    xlname = "sheets/" + str(xlid) + ".xlsx"
    df = pd.read_excel(xlname)
    print("week: " + str(xlid))
    for index, row in df.iterrows():
        if row["Semester"] not in ["6", 6]:
            continue

        # "1997-10-28 00:35"                
        have = row["Date/Time"]
        print(parsedatetme(have))

        if row["Subject"] not in subjects:
            subjects.append(row["Subject"])
