#s is the tested string
s = 'asdfjasdlkfjsdlfjsf'


y = 0
string = str(s[y])
biggest = str(s[y])

while y < (len(s)-1):
    if s[y] > s[y+1]: 
        string = ""
    y += 1
    string += str(s[y]) 
    if len(biggest) < len(string): 
        biggest = string
print("Longest substring in alphabetical order is:",biggest)