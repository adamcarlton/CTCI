def checkUnique(string):
    return len(set(list(string))) == len(string)

print("Checking Unique")
print(checkUnique("abcdef"))
print(checkUnique("aabbcc"))
print("\n")


def checkPerm(str1, str2):
    if len(str1) != len(str2):
        return False
    strDict = {}
    for char in str1:
        if char not in strDict:
            strDict[char] = 0
        strDict[char] += 1
    
    for char in str2:
        if char in strDict:
            strDict[char] -= 1
        else:
            return False
    
    for key in strDict:
        if strDict[key] != 0:
            return False
    
    return True

print("Checking Permutation")
print(checkPerm("abcd", "acdb"))
print(checkPerm("abacd", "acdab"))
print(checkPerm("abacd", "acdcb"))
print(checkPerm("avds", "abds"))
print("\n")

def URLify(string):
    strList = string.split(" ")
    URLstring = ""
    for i in range(len(strList) - 1):
        URLstring += strList[i] + "%20"
    URLstring += strList[-1]
    return URLstring

print("Making it a URL")
print(URLify("my name is adam"))
print("\n")

def palindromePerm(string):
    string = string.lower()
    charDict = {}
    oddCount = 0
    for char in string:
        if char == " ":
            continue
        if char in charDict:
            charDict[char] += 1
        else:
            charDict[char] = 1
    
    for key in charDict:
        if charDict[key] % 2 != 0:
                oddCount += 1
        if oddCount > 1:
            return False
    
    return True

print("Checking palindrome permutation")
print(palindromePerm("Tact Coa"))
print(palindromePerm("Tat Coa"))
print(palindromePerm("atata"))
print(palindromePerm("aatta"))
print("\n")

def oneAway(str1, str2):
    if str1 == str2:
        return True
    if abs(len(str1) - len(str2)) > 1:
        return False
    smallWord = str1
    bigWord = str2
    if len(str1) != len(str2):
        smallWord = str1.lower() if len(str1) < len(str2) else str2.lower()
        bigWord = str1.lower() if len(str2) < len(str1) else str2.lower()
    i,j = 0,0
    foundDiff = False
    while(i < len(smallWord) and j < len(bigWord)):
        if smallWord[i] != bigWord[j]:
            if foundDiff:
                return False
            foundDiff = True
            if len(smallWord) == len(bigWord):
                i += 1
        else:
            i += 1
        j += 1
    return True

print("Checking one away")
print(oneAway("pale", "ple"))
print(oneAway("pale", "pales"))
print(oneAway("pale", "bale"))
print(oneAway("pale", "bake"))
print(oneAway("pale", "paal"))
print("\n")

def stringComp(string):
    valCount = 0
    finalString = ""
    cur = string[0]
    for i in range(len(string)):
        if string[i] != cur:
            finalString += cur + str(valCount)
            valCount = 0
            cur = string[i]
        valCount += 1
    
    finalString += string[-1] + str(valCount)
    
    if len(finalString) >= len(string):
        return string
    return finalString

print("Checking string compression")
print(stringComp("aabbbccccaaa"))
print(stringComp("bcccccccccccaba"))
print("\n")

def rotateImage(a):
    afterImage = [[0 for x in range(len(a))] for y in range(len(a))]
    for i in range(len(a)):
        for j in range(len(a)):
            afterImage[j][len(a) - (i+1)] = a[i][j]
    return afterImage

print("Rotating Image")
print(rotateImage([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]))
print("\n")

def zeroMatrix(arr):
    idxList = []
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 0:
                idxList.append((i,j))
    return zero(arr, idxList)

def zero(arr, indexList):
    for item in indexList:
        for idx in range(len(arr[item[0]])):
            arr[item[0]][idx] = 0
        for idx in range(len(arr)):
            arr[idx][item[1]] = 0
    
    return arr

print("Zeroing Matrix")
print(zeroMatrix(
    [[1, 2, 3],
     [4, 0, 6],
     [0, 8, 9]]
))
print(zeroMatrix(
    [[1, 2, 3],
     [4, 9, 6],
     [0, 8, 9]]
))
print(zeroMatrix(
    [[1, 2, 3],
     [4, 11, 6],
     [5, 8, 9]]
))
print("\n")

def isSubstring(s1, s2):
    if len(s1) != len(s2):
        return False
    if s2 == s1:
        return True
    ogS2 = s2
    s2 = s2[1:] + s2[0:1]
    while s2 != ogS2:
        if s2 == s1:
            return True
        s2 = s2[1:] + s2[0:1]
    return False

print("Determining isSubstring based on rotation")
print(isSubstring("erbottlewat", "waterbottle"))
print(isSubstring("erbottlewatz", "waterbottle"))
