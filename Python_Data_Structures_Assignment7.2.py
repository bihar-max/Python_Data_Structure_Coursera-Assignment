fname = input("Enter file name: ")
fhand = open(fname)
count=0
total=0
for line in fhand:
    line = line.rstrip()
    if line.startswith("X-DSPAM-Confidence:"):
        count = count + 1
        s = line.find("0")
        x = line[s:]
        total = total + float(x)
avg=total/count
print("Average spam confidence:",avg)
