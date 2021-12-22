name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
counts = dict()
bigCount = 0
bigName = 0
for line in handle:
    if 'From: ' in line:
        words = line.split()
        for key in words:
            counts[key] = counts.get(key, 0) + 1
for key, value in counts.items():
    if key != 'From:' and value > bigCount:
        bigCount = value
        bigName = key


print (bigName, bigCount)