"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv

cummulative_dict = {}

def isSeptember(month):
    if month[3] == "0" and month[4] == "9" and month[6] == "2" and month[7] == "0" and month[8] == "1" and month[9] == "6":
        return True
    else:
        return False

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    #loop through calls
    for call in calls:
        #check if call was made in september 2016
        if isSeptember(call[2]) :
            #update dictionary number 
            cummulative_dict[call[0]] = cummulative_dict.get(call[0], 0) + int(call[3])
            cummulative_dict[call[1]] = cummulative_dict.get(call[1], 0) + int(call[3])


# From https://pythonguides.com/python-find-max-value-in-a-dictionary/
# Getting maximum key and values in dictionary
max_time = max(cummulative_dict.values())
max_telephone = max(cummulative_dict, key=lambda x: cummulative_dict[x])

# print(cummulative_dict)
print("%s spent the longest time, %d seconds, on the phone during September 2016." % (max_telephone, max_time))

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

"""
    set cummulative dictionary set
    loop through calls sets and update cummulative dictionary set if call was made in september 2016
    get maximum key and value fro dictionary set
    return max(unique length set)
"""
