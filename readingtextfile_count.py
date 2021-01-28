text = "X-DSPAM-Confidence:    0.8475";

x = text.find('0')
print(x)
z = text.find('5')
print(z)

print(float(text[x:z+1]))

"""
7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:

X-DSPAM-Confidence:    0.8475

Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below.
Do not use the sum() function or a variable named sum in your solution. 
"""
# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
number = []
total = 0
for line in fh:
    line = line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:") : 
        continue
    y = line.find('0')
    #converting string to float
    x = float(line[y:])
    #adding all the float values to a list
    number.append(x)    
    count =count+1
    total=0
    #adding all the float values using a for loop
    for x in number: 
        total+=x
        
avg = total/count
print('Average spam confidence:', avg)


