"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

#stores checked phone number
check_phone_number = set()
#count checked phone number
count = 0
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    # loop through texts
    for n in texts:
        # modified using set instead of not in as instructed by review
        check_phone_number.add(n[0])
        check_phone_number.add(n[1])

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    #loop through calls
    for n in calls:
        # modified using set instead of not in as instructed by review
        check_phone_number.add(n[0])
        check_phone_number.add(n[1])

print("There are %s different telephone numbers in the records." % len(check_phone_number))

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
