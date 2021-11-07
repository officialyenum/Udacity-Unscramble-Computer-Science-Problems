"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

possible_telemarketers = []
recieved_text_checker = []
sent_text_checker = []
recieved_call_checker = []
def checkIfTeleMarketer(num):
  if num[0] == "1" and num[1] =="4" and num[2] =="0":
    return True
  return False

def checkTeleMarketer(call_list):
    counter = 0
    for call in call_list:
        if checkIfTeleMarketer(call[0]):
            if call[0] not in recieved_text_checker or call[0] not in sent_text_checker or call[0] not in recieved_call_checker:
                if call[0] not in possible_telemarketers:
                    # counter += 1
                    # print("Telemarketer Found")
                    # print(call[0])
                    possible_telemarketers.append(call[0])
                    # print(counter) 

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    for text in texts:
        recieved_text_checker.append(text[0])
        sent_text_checker.append(text[1])

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    for call in calls:
        recieved_call_checker.append(call[1])
    checkTeleMarketer(calls)

print("These numbers could be telemarketers: ")
possible_telemarketers.sort()
for marketer in possible_telemarketers:
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

