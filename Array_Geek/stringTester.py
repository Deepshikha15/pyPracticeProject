from collections import Counter, OrderedDict
from itertools import groupby

from string import ascii_lowercase as asc_lower

# def winner(input):
#     # convert list of candidates into dictionary
#     # output will be likes candidates = {'A':2, 'B':4}
#     votes = Counter(input)
#
#     # create another dictionary and it's key will
#     # be count of votes values will be name of
#     # candidates
#     dict = {}
#
#     for value in votes.values():
#         # initialize empty list to each key to
#         # insert candidate names having same
#         # number of votes
#         dict[value] = []
#
#     for (key, value) in votes.iteritems():
#         dict[value].append(key)
#
#         # sort keys in descending order to get maximum
#     # value of votes
#     maxVote = sorted(dict.keys(), reverse=True)[0]
#
#     # check if more than 1 candidates have same
#     # number of votes. If yes, then sort the list
#     # first and print first element
#     if len(dict[maxVote]) > 1:
#         print
#         sorted(dict[maxVote])[0]
#     else:
#         print
#         dict[maxVote][0]

def maxConsecutive1(input_string):
    print(max(map(len,input_string.split('0'))))

def common(str1,str2):
    #conert into deictionaries

    dict_str1=Counter(str1)
    dict_str2 =Counter(str2)

    commonChar = dict_str1 & dict_str2
    print(commonChar)

    commonCharList= list(commonChar)
    print(commonCharList)

    sortedList = sorted(commonCharList)
    print(''.join(sortedList))

def removeChar(first_string,second_string):
    d_fisrt = Counter(first_string)
    print(d_fisrt)
    d_second = Counter(second_string)

    key1 = d_fisrt.keys()
    print(key1)
    key2 = d_second.keys()

    count1 = len(key1)
    print(count1)
    count2 = len(key2)
    print(count2)

    set1= set(key1)
    set2=set(key2)
    commonkey = len(set1.intersection(set2))
    print(commonkey)

    if commonkey == 0 :
        print (count1+count2)
    else:
        print (max(count1,count2)-commonkey)

def reverseString(input_char):
    str =" "
    for i in input_char:
        str = i + str
    print (str)

def removeduplicate(inp):
    result =[]
    for (key , group) in groupby(inp):
        result.append(key)
    print("".join(result))

def generate_string(a):
    dictionary_a =Counter(a)

    onlyOne = [key for (key,count) in dictionary_a.items() if count ==1]
    multiple = [key for (key,count) in dictionary_a.items() if count > 1]

    print(''.join(onlyOne))
    print(''.join(multiple))

def mirrorChars(input, k):
    original = 'abcdefghijklmnopqrstuvwxyz'
    reverse = 'zyxwvutsrqponmlkjihgfedcba'
    dictChars = dict(zip(original, reverse))

    prefix = input[0:k - 1]
    print(prefix)
    suffix = input[k - 1:]
    print(suffix)

    mirror =''

    for i in range(0, len(suffix)):
        mirror = mirror + dictChars[suffix[i]]
    print(mirror)

    print(prefix + mirror)

def convertToString(list):
    new=''
    for i in list:
        new += i
    print(new)

def newString(charSet, input):
    origCharSet = 'abcdefghijklmnopqrstuvwxyz'
    mapChar = dict(zip(charSet, origCharSet))
    print(mapChar)
    for i in input:
        print(mapChar[i], end="")

def printName(name):

    name = name.split()
    new_list=''
    print(name)
    for i in range(len(name)-1):
        s = name[i]
        new_list = new_list + s[0].upper() +'.'
        print(new_list)

    new_list = new_list + name[-1].title()

    print(new_list)

def makeString(nameOne, nameTwo):
    dict = Counter(nameOne)
    dict2 = Counter(nameTwo)

    common = dict & dict2

    return common== dict

def countVowels(new_string):
    count =0
    vowels=set("aeiouAEIOU")

    for alphabet in new_string:
        if alphabet in vowels:
            count += 1
    print(count)

def check(s):
    return set(asc_lower) - set(s.lower()) == set([])

def removeZeros(ip):
    new_ip = ".".join([str(int(i)) for i in ip.split(".")])
    return new_ip;


def checkTwoHalves(input):
    length = len(input)
    if (length % 2 ==0):
        first = input[0:length]
        print(first)
        second = input[length:]
        print(second)
    else:
        first = input[0:length]
        print(first)
        second = input[(length) + 1:]
        print(second)

    if Counter(first) == Counter(second):
        print('YES')
    else:
        print('NO')

def uncommonConcatenate(S1,S2):

    set1= set(S1)
    set2= set(S2)

    comm=set1 & set2
    result = [ch for ch in str1 if ch not in comm] + [ch for ch in str2 if ch not in comm]
    print(''.join(result))
    return

# def RunLength(strrr):
#     dict=OrderedDict.fromkeys(strrr, 0)
#     print(dict)
#     for ch in strrr:
#         dict[ch] += 1
#         print(dict)
#
#     output = ''
#     for key, value in dict.iteritems():
#         output = output + key + str(value)
#     return output


if __name__ == "__main__":
    input = ['john', 'johnny', 'jackie', 'johnny', 'john', 'jackie', 'jamie', 'jamie',
                 'john', 'johnny', 'jamie', 'johnny', 'john']

    input_string = '11000111101010111'
    maxConsecutive1(input_string)

    str1= "deeps"
    str2="deepshikha"

    common(str1,str2)

    first_string ="ghhj"
    second_string ="hola"
    removeChar(first_string,second_string)


    input_char = "Geeksforgeeks"
    reverseString(input_char)

    inp = "aaaabb"
    removeduplicate(inp)

    a="geeksforgeeks"
    generate_string(a)

    input = 'paradox'
    k =3
    mirrorChars(input, k)

    list =['a','p','e']
    convertToString(list)

    charSet = 'qwertyuiopasdfghjklzxcvbnm'
    input = 'utta'
    newString(charSet, input)

    name = "deepshikha mishra"
    printName(name)

    nameOne = 'ABHISHEKsinGH'
    nameTwo = 'gfhfBHkooIHnfndSHEKsiAnG'
    if (makeString(nameOne, nameTwo) == True):
        print("Possible")
    else:
        print("Not Possible")

    new_string="rahul"
    countVowels(new_string)

    strng = "The quick brown fox jumps over the lazy dog"
    if (check(strng) == True):
        print("The string is a pangram")
    else:
        print("The string isn't a pangram")

    ip = "100.020.003.400"
    print(removeZeros(ip))

    input = 'abccba'
    checkTwoHalves(input)

    S1 = "aacdb"
    S2 = "gafd"
    uncommonConcatenate(S1,S2)

    strrr= "wwwwxxyyyxyxyx"
    RunLength(strrr)




