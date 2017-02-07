in_file = open("qbdata.txt", "r")
outfile = open("qb_names.txt", "w")

aline = in_file.readline()
while aline:
    items = aline.split()
    data_line = items[1] +"," + items[0]
    outfile.write(data_line + "\n")
    aline = in_file.readline()
in_file.close()
outfile.close()