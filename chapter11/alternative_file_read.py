infile = open("qbdata.txt", "r")
print(infile.readline())
print(infile.readline())

infile2 = open("qbdata.txt", "r")
line_list = infile2.readlines()
print(len(line_list))
print(line_list[0:4])
