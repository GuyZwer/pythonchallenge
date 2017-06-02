checkfile = open("challenge3file.txt", 'r')
file = checkfile.read()
file2 = file.replace('\n', '')
print file2

count = 0

def checkletters(letters1, letters2):
    if letters1 == letters2:
        return True

list1 = []
for lop in file:
    count += 1
    if file[count-1].islower():
        if file[count:count+3].isupper() and file[count-4:count-1].isupper():
            print 'yes'
            if checkletters(file[count:count+3], file[count-4:count+1]):
                print file[count-4:count+3]
                list1.append(file[count-1])

print ''.join(list1)
