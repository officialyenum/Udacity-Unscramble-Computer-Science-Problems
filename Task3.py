"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

area_codes = []
percentage = 0
countTwoWayFixedCalls = 0
countAllCalls = 0

def isFixedLine(num):
  if num[0] is "(" and num[1] =="0":
    return True
  return False
  
def isBangaloreNumber(num):
  if num[0] is "(" and num[1] =="0" and num[2] =="8" and num[3] =="0" and num[4] ==")":
    return True
  return False

def isMobileLine(num):
  if num[0]=="7" or num[0] =="8" or num[0] =="9":
    return True
  return False

def isTelemarketerLine(num):
  if num[0]=="1" or num[1] =="4" or num[2] =="0":
    return True
  return False

def getCode(num):
  if isMobileLine(num):
    return num[:4]
  if isFixedLine(num):
        return num[:(num.index(")")+1)]
  if isTelemarketerLine:
    return num[:]

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    for call in calls:
      if isBangaloreNumber(call[0]) and isBangaloreNumber(call[1]):
        countTwoWayFixedCalls += 1
        # print(call[0],call[1])
        # print("two way = %d" % countTwoWayFixedCalls)
      if isFixedLine(call[0]):
        countAllCalls += 1
        # print("all = %d" % countAllCalls)
        if getCode(call[1]) not in area_codes:
            area_codes.append(getCode(call[1]))


print("The numbers called by people in Bangalore have codes:")
area_codes.sort()
for num in area_codes:
  print("%s" % num)


# print(countTwoWayFixedCalls)
# print(countAllCalls)
quotient = float(countTwoWayFixedCalls * 100)
percentage = round(quotient / countAllCalls, 2)

print("{}% percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(round(percentage,2)))

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
