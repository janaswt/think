in_file = open("qbdata.txt", "r")
line = in_file.readline()

while line:
    values = line.split()
    print('QB ', values[0], values[1], 'had a rating of ', values[10] )
    line = in_file.readline()
in_file.close()