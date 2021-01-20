# Task from "Python Data Structures" course on Coursera by the University of Michigan. 

# Week 3. Files

# Assignment 7.2

# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
amount = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    words = line.split()
    amount = amount + float(words[1])
    count += 1
average = amount/count
print("Average spam confidence:", average)

# Week 4. Lists

# Assignment 8.4

fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    words = line.split()
    for word in words:
        if word not in lst:
        	lst.append(word)
lst.sort()
print(lst)

# Assignment 8.5

fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)

count = 0

for line in fh:
    line = line.rstrip()
    if not line.startswith('From '): continue
    count = count + 1
    words = line.split()
    print(words[1])
    
print("There were", count, "lines in the file with From as the first word")

# Week 5. Dictionaries

# Assignment 9.4

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

count_senders = dict()
#find sender
for line in handle:
    line = line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    sender = words[1]
#count each sender and put the value in a dict
    count_senders[sender] = count_senders.get(sender, 0) + 1         


#find max sender
count_max = 0
sender_max = list()
for senders,counts in count_senders.items():
    if counts > count_max:
        count_max = counts
        sender_max = (senders, counts)

print(sender_max[0], sender_max[1])

# Week 6. Tuples

# Assignment 10.2

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

count_hours = dict()
#find hour of the day
for line in handle:
    line = line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    time = words[5]
    pieces = time.split(':')
    hour = pieces[0]
#count each hour value and put it in a tuple
    count_hours[hour] = count_hours.get(hour, 0) + 1         

#sort by values
sorted_hours = list()
for hours,counts in count_hours.items():
    newtup = (hours,counts)
    sorted_hours.append(newtup)
sorted_hours = sorted(sorted_hours)

#print tuple items
for hours,counts in sorted_hours:
    print(hours, counts)