checkfile = open("challenge3file.txt", 'r')
file = checkfile.read()
print file
count = 0

list1 = []
for lop in file:
    count += 1
    if file[count-1].islower():
        print file[count-1]
        if file[count:count+3].isupper() and file[count-4:count-1].isupper():
            print file[count-4:count+3]
            list1.append(file[count-1])

print ''.join(list1)
