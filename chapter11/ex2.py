a_file = open("students_data.txt", "r")
a_line = a_file.readline()
while a_line:
    items = a_line.split()
    averages = items[1:]
    total_score = 0
    i = 0
    for average in averages:
        total_score += int(average)
        i += 1
    print(items[0], total_score/i) 
    a_line = a_file.readline()