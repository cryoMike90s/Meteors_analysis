import csv

def export_to_sheet(key, gc, working_spreadsheet):
    """Function which import stored data in files/meteor_file.csv and push it to given google spreadsheet worksheet
    :param key: actual worksheet id (defined in console.py)
    :param gc: variable for storing credentials for service (located in files/main.py)
    :param working_spreadsheet: actual worksheet instance (defined in console.py)

    """
    SheetName = "Main_data"
    working_spreadsheet.values_update(
        SheetName,
        params={'valueInputOption': 'USER_ENTERED'},
        body={'values': list(csv.reader(open("files/csv_meteor_file.csv", encoding='utf-8')))}
    )
