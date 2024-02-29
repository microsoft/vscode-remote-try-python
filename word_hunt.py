
# how many times that word ## appear in the passage
filename = input("Enter filename:")
query = input("Enter query:")

infile = open(filename)

matching_lines = 0

for line in infile:
    line = line.strip("\n")
    query_lower = line.lower()
    if query.lower() in line.lower():
        print(line)
        num_matches = line.lower().count(query.lower())
        matching_lines = matching_lines +1
        

print(matching_lines)
