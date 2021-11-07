"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

#stores checked phone number
check_phone_number = []
#count checked phone number
count = 0
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    # loop through texts
    for n in texts:
        if n[0] not in check_phone_number:
            count +=1
            #add incoming phone number to checker
            check_phone_number.append(n[0])
        if n[1] not in check_phone_number:
            count +=1
            #add answering phone number to checker
            check_phone_number.append(n[1])


with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    #loop through calls
    for n in calls:
        # check if first index of call object is in the phone checker
        if n[0] not in check_phone_number:
            count +=1
            #add incoming phone number to checker
            check_phone_number.append(n[0])
        if n[1] not in check_phone_number:
            count +=1
            #add answering phone number to checker
            check_phone_number.append(n[1])

print("There are %s different telephone numbers in the records." % count)

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
