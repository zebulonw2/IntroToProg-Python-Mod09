# if __name__ == "__main__":
#     from DataClasses import Employee as Emp
#     from ProcessingClasses import FileProcessor as FP
#     from IOClasses import EmployeeIO as EIO
# else:
#     raise Exception("This file was not created to be imported")
#
#
#
# #Test DataClasses
# objP1 = Emp(1, "Bob", "Smith")
# objP2 = Emp(2, "Sue", "Jones")
# lstTable = [objP1, objP2]
# for row in lstTable:
#     print(row.to_string(), type(row))
#
#
# #Test ProcessingClasses
# FP.save_data_to_file("EmployeeData.txt", lstTable)
# lstFileData = FP.read_data_from_file("EmployeeData.txt")
# lstTable.clear()
# for line in lstFileData:
#     lstTable.append(Emp(line[0], line[1], line[2].strip()))
# for row in lstTable:
#     print(row.to_string(), type(row))
#
#
# # Test IO classes
# EIO.print_menu_items()
# EIO.print_current_list_items(lstTable)
# print(EIO.input_employee_data())
# print(EIO.input_menu_options())