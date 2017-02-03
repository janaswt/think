a_file = open("students_data.txt", "r")
a_line = a_file.readline()
while a_line:
    items = a_line.split()
    if len(items[1:]) > 6:
        print(items[0])
    a_line = a_file.readline()