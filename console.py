from code.source_data_operations import export_to_csv, export_to_database
from code.create_spreadsheet import create_new_spreadsheet
from code.import_csv_to_google import export_to_sheet
from code.create_pivot_table_v2 import pivot_table_creation
from code.sql_queries import create_sheets
from code.main import service, gc


print("************* Welcome in meteors landing analysis *************")
option = input("> Do You want to download up to date data from indicated in read.me file site? (y/n) >>: ")
print("> To quit please enter '0'")

while option != "0":
    if option.casefold() == "y":
        export_to_csv()
        export_to_database()

        print("Now data is already up to date, it is time for create new file. Please make sure that all OAuth"
              "requirements are met conditions accordingly to read.me file")
        name = input(str("> Please enter name of spreadsheet: >>: "))

        create_new_spreadsheet(name, gc)
        working_spreadsheet = gc.open(name)
        key = working_spreadsheet.id

        # exports file from csv file into google sheet
        export_to_sheet(key, gc, working_spreadsheet)

        next_op = input("> Do You want to create pivot table? (y/n) >>: ")
        if next_op.casefold() == "y":
            # create pivot table from first sheet data
            pivot_table_creation(key, gc, working_spreadsheet, service)
            sql = input("> Do You want to create sql queries representation (y/n)?: ")
            if sql.casefold() == "y":
                # create new sheets for sql queries output
                create_sheets(key, gc, working_spreadsheet)
                print("Data successfully exported!!")
                print("Your worksheet is already done!!")
                break
            elif sql.casefold() == "n":
                print("Your worksheet is already done!!")
                break
            else:
                while sql not in {"y", "n"}:
                    sql = input("> Do You want to create sql queries representation?: ")
        elif next_op.casefold() == "n":
            print("Your sheet is already done!!")
            break
        else:
            while next_op.casefold() not in {"y", "n"}:
                next_op = input("> Do You want to create pivot table? (y/n) >>: ")
    else:
        while option.casefold() != "y":
            option = input("> Do You want to download up to date data from indicated in read.me file site? (y/n) >>: ")

print("Goodbye!!!")
