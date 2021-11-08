"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

possible_telemarketers = set()
recieved_text_checker = set()
sent_text_checker = set()
recieved_call_checker = set()

def checkTeleMarketer(call_list):
    # counter = 0
    for call in call_list:
        if call[0] not in recieved_text_checker and call[0] not in sent_text_checker and call[0] not in recieved_call_checker:        
            possible_telemarketers.add(call[0])

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    for text in texts:
        recieved_text_checker.add(text[0])
        sent_text_checker.add(text[1])

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    for call in calls:
        recieved_call_checker.add(call[1])
    checkTeleMarketer(calls)

print("These numbers could be telemarketers: ")
for marketer in sorted(possible_telemarketers):
    print(marketer)
"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

