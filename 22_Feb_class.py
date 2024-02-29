# #tsv_2_csv.py


# filename = input("INput filename: ")
# infile = open(filename)
# filename = input("Result filename: ")
# outfile = open("filename","w")

# for line in infile:
#     line.strip()
#     line = line.replace("\t",",")
    
#     print(line)
#     line += "\n"
#     outfile.write(line)


# tsv or csv

filename = input("filename: ")
if filename[-4:] == ".csv":
    csv = True
else:
    csv = False

infile = open(filename)

#get values to keep and put in list
outlines = []
keep = input("Column to keep")
index = int(keep) - 1

for line in infile:
    line = line.rstrip("\n")
    if csv:
        cols = line.split(",")
    else:
        cols = line.split("\t")
    value = cols[index]
    outlines.append(value)

filename = input("Ourfilename: ")
outfile = open(filename,"w")
print(line)


