# ------------------------------------------------- #
# Title: ZW-Assignment09
# Description: Working with Modules
# ChangeLog: (Who, When, What)
# Zeb W. 14Dec2021, Created Script
# ------------------------------------------------- #

# Imports
if __name__ == "__main__":
    from DataClasses import Employee as EMP
    from ProcessingClasses import FileProcessor as FP
    from IOClasses import EmployeeIO as EIO
else:
    raise Exception("This file was not created to be imported")

# Main Body

# Data #
lstFileData = []  # 2D list of strings from file
lstEmpTable = []  # 2D list of employee objects


# load data from file into a list of employee objects when script starts
lstFileData = FP.read_data_from_file("EmployeeData.txt")
for row in lstFileData:
    lstEmpTable.append(EMP(row[0], row[1], row[2].strip()))
# show user a menu of options
while True:
    EIO.print_menu_items()
    # Get user's menu choice
    strUserInput = EIO.input_menu_options()
    if strUserInput == "1":
        # show user current data in the list of employee objects
        EIO.print_current_list_items(lstEmpTable)
        continue
    if strUserInput == "2":
        # let user add data to the list of employee objects
        lstEmpTable.append(EIO.input_employee_data())
        continue
    if strUserInput == "3":
        # let user save the current data to file and exit program
        FP.save_data_to_file("EmployeeData.txt", lstEmpTable)
        continue
    if strUserInput == "4":
        break