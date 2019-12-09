# ------------------------------------------------------------------------ #
# Title: Assignment 09
# Description: Modules
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# PShoup,12.8.2019, Modified script to complete assignment 9
# ------------------------------------------------------------------------ #

if __name__ == "__main__":
    from DataClasses import Employee as Em
    from ProcessingClasses import FileProcessor as Fp
    from IOClasses import EmployeeIO as Eio
else:
    raise Exception("This file was not created to be imported")

# Declare variables #
lstEmployeeTable = []
lstFileData = []

# Load data from file #
lstFileData = Fp.read_data_from_file("EmployeeData.txt")
for row in lstFileData:
    lstEmployeeTable.append(Em(row[0], row[1], row[2].strip()))

# Display menu options #
while True:
    Eio.print_menu_items()
    strOption = Eio.input_menu_options()
    if strOption == "1":
        Eio.print_current_list_items(lstEmployeeTable)
        continue
    elif strOption == "2":
        lstEmployeeTable.append(Eio.input_employee_data())
        continue
    elif strOption == "3":
        Fp.save_data_to_file("EmployeeData.txt", lstEmployeeTable)
        continue
    elif strOption == "4":
        break
