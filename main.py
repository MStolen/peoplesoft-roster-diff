import pandas as pd
import datetime
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo as popup


def drop_unused_cols(df):
    return df.drop(labels=['Notify', 'Grade Basis', 'Units', 'Program and Plan',
                           'Concentration', 'Minor', 'Level', 'Has Participated',
                           'Has NOT Participated', 'Early Alert', 'Gender Identity',
                           'Preferred Pronouns'],
                   axis=1)


if __name__ == "__main__":
    filetypes = [('Spreadsheet', ['*.csv', '*.xls', '*.xlsx'])]
    popup(title="Instructions", message="Select two files: 1. The old roster 2. The new roster")
    old_file = fd.askopenfilename(filetypes=filetypes, title="Select OLD file", )
    new_file = fd.askopenfilename(filetypes=filetypes, title="Select NEW file")

    if old_file.endswith(".csv"):
        old_file = pd.read_csv(old_file)
    else:
        old_file = pd.read_excel(old_file)

    if new_file.endswith(".csv"):
        new_file = pd.read_csv(new_file)
    else:
        new_file = pd.read_excel(new_file)

    old_file = drop_unused_cols(old_file)
    new_file = drop_unused_cols(new_file)

    old_file = old_file.dropna()
    new_file = new_file.dropna()

    old_ids = set(old_file["ID"])
    new_ids = set(new_file["ID"])

    add_ids = new_ids-old_ids
    drop_ids = old_ids-new_ids
    common_ids = new_ids.intersection(old_ids)
    old_enrolled_ids = set(old_file["ID"][list(old_file["ID"].isin(list(common_ids))) and old_file["Status"] == "Enrolled"])
    new_drop_ids = set(new_file["ID"][list(new_file["ID"].isin(list(common_ids))) and new_file["Status"] == "Dropped"])

    drop_ids = drop_ids.union(new_drop_ids.intersection(old_enrolled_ids))

    adds = new_file[new_file["ID"].isin(list(add_ids))]
    drops = new_file[new_file["ID"].isin(list(drop_ids))]

    frame_out = pd.concat([adds, drops])

    # datestring = datetime.date.today().strftime("%Y%m%d")
    # output_name = "add_drop_"+datestring+".csv"
    output_name = fd.asksaveasfilename(filetypes=[("CSV", ".csv")], defaultextension=".csv")
    frame_out.to_csv(output_name, index=False)

    popup("Done", "Done")

