def pal(mystring):
    for i in range(len(mystring) // 2):
        if mystring[i] != mystring[- 1 - i]:
            print('Not Palindrome')
            mystring.remove(mystring[i])
            print mystring

            break
    else:
        print('Palindrome')



mystring="Ab3bd"
print pal(mystring)