import pandas
import pandas as pd
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo as popup


def drop_unused_cols(df: pandas.DataFrame) -> pandas.DataFrame:
    """
    Remove unused columns from imported files and remove empty rows
    :rtype: pandas.DataFrame
    :return:
    :type df: pandas.DataFrame
    """
    # Drop listed columns
    df.drop(labels=['Notify', 'Grade Basis', 'Units', 'Program and Plan',
                    'Concentration', 'Minor', 'Level', 'Has Participated',
                    'Has NOT Participated', 'Early Alert', 'Gender Identity',
                    'Preferred Pronouns'],
            axis=1,
            inplace=True)
    # Remove empty rows (roes containing NaN)
    return df.dropna()


if __name__ == "__main__":
    # Give instructions and select input files
    filetypes = [('Spreadsheet', ['*.csv', '*.xls', '*.xlsx'])]
    popup(title="Instructions", message="Select two files:\n1. The old roster\n2. The new roster")
    old_file = fd.askopenfilename(filetypes=filetypes, title="Select OLD file")
    new_file = fd.askopenfilename(filetypes=filetypes, title="Select NEW file")

    # Handle no files selected
    if old_file == '' or new_file == '':
        popup("Missing File", "You have not selected one or more files")
        exit(1)

    # Read in roster files
    if old_file.endswith(".csv"):
        old_file = pd.read_csv(old_file)
    else:
        old_file = pd.read_excel(old_file)

    if new_file.endswith(".csv"):
        new_file = pd.read_csv(new_file)
    else:
        new_file = pd.read_excel(new_file)

    # Remove unneeded columns from file
    old_file = drop_unused_cols(old_file)
    new_file = drop_unused_cols(new_file)

    # Get all unique student ID numbers from files
    old_ids = set(old_file["ID"])
    new_ids = set(new_file["ID"])

    # Get IDs that have been added
    add_ids = new_ids - old_ids
    # Get IDs that have been removed
    drop_ids = old_ids - new_ids
    # Get IDs common to both files
    common_ids = new_ids.intersection(old_ids)
    # Get all IDs of students enrolled in old file
    old_enrolled_ids = set(
        old_file["ID"][list(old_file["ID"].isin(list(common_ids))) and old_file["Status"] == "Enrolled"])
    # Get all IDs of students who have dropped in new file
    new_drop_ids = set(new_file["ID"][list(new_file["ID"].isin(list(common_ids))) and new_file["Status"] == "Dropped"])

    # Add list of missing IDs in new file to students who have switched from enrolled to dropped
    drop_ids = drop_ids.union(new_drop_ids.intersection(old_enrolled_ids))

    # Get table entries of adds and drops
    adds = new_file[new_file["ID"].isin(list(add_ids))]
    drops = new_file[new_file["ID"].isin(list(drop_ids))]

    # Swap enrollment status for add or drop
    adds["Status"] = "Added"
    drops["Status"] = "Dropped"

    # Create single table of students who have added or dropped the class
    frame_out = pd.concat([adds, drops])

    # User selects output file
    output_name = fd.asksaveasfilename(filetypes=[("CSV", ".csv")], defaultextension=".csv")
    # Make sure file name ends in .csv
    output_name = output_name if output_name.endswith(".csv") else output_name + ".csv"
    frame_out.to_csv(output_name, index=False)

    # Notify user that program finished and file is saved
    popup("Done", "Done")
