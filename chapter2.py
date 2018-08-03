class LinkedList(object):
    def __init__(self, x):
        self.data = x 
        self.next = None


def createLL():
    node = LinkedList(0)
    head = node
    for i in range(11):
        newNode = LinkedList(i)
        node.next = newNode
        node = node.next
    return head

def showLL(linkList):
    while linkList:
        print(linkList.data)
        linkList = linkList.next

def removeDup(node):
    noDups = []
    prev = node
    noDups.append(node.data)
    node = node.next
    while node:
        if node.data in noDups:
            prev.next = node.next
        else:
            noDups.append(node.data)
            prev = node
        node = node.next

print("Testing removeDup with temp buffer\n")
testList = createLL()
print("Beginning Linked List")
showLL(testList)
print("\n=====\n")
print("Removed duplicates Linked List")
removeDup(testList)
showLL(testList)
print("\n")

def removeDupNoBuff(node):
    prev = node
    cur = node
    node = cur.next
    while cur:
        if node.data == cur.data:
            prev.next = node.next
            cur = cur.next
        if node.next == None:
            break
        prev = node
        node = node.next
    

print("Testing removeDup without temp buffer\n")
testList = createLL()
print("Beginning Linked List")
showLL(testList)
print("\n=====\n")
print("Removed duplicates Linked List")
removeDup(testList)
showLL(testList)
print("\n")

def findKthToLast(ll, k):
    node1 = ll
    node2 = ll
    for _ in range(k):
        if not node1.next:
            return None
        node1 = node1.next
    
    while node1:
        node1 = node1.next
        node2 = node2.next
    return node2.data


print("Testing findKthToLast\n")
testList = createLL()
print("Beginning Linked List")
showLL(testList)
print("\n")
print(findKthToLast(testList, 3))
print("\n")


def deleteMiddleNode(node):
    if not node or not node.next:
        return None
    node.data = node.next.data
    node.next = node.next.next

def getMiddleNode(node, k):
    while node.data != k:
        node = node.next
    return node

print("Testing deleteMiddleNode\n")
testList = createLL()
print("Beginning Linked List")
showLL(testList)
print("\n")
deleteMiddleNode(getMiddleNode(testList, 5))
print("List after removing")
showLL(testList)
print("\n")


def partition(ll, value):
    head = ll
    tail = ll
    while ll:
        nextNode = ll.next
        if ll.data < value:
            ll.next = head
            head = ll
        else:
            tail.next = ll
            tail = ll
        ll = nextNode
    tail.next = None
    return head


print("Testing partition\n")
testList = createLL()
print("Beginning Linked List")
showLL(testList)
print("\n")
print("List after removing")
showLL(partition(testList, 5))
print("\n")


def sumLists(l1, l2):
    strL1 = ""
    strL2 = ""
    while l1:
        strL1 += str(l1.data)
        l1 = l1.next
    while l2:
        strL2 += str(l2.data)
        l2 = l2.next

    intL1 = int(strL1[::-1])
    intL2 = int(strL2[::-1])

    final = intL1 + intL2
    finalStr = str(final)[::-1]

    node = LinkedList(int(finalStr[0]))
    head = node
    finalStr = finalStr[1:]
    for i in range(len(finalStr)):
        newNode = LinkedList(int(finalStr[i]))
        node.next = newNode
        node = node.next
    return head


def createNewLL():
    node = LinkedList(3)
    head = node
    for i in range(4):
        newNode = LinkedList(i)
        node.next = newNode
        node = node.next
    return head

print("Testing sumLists\n")
testList1 = createNewLL()
testList2 = createNewLL()
print("Beginning Linked List")
showLL(testList1)
print("\n")
showLL(sumLists(testList1, testList2))
print("\n")


def sumListsForward(l1, l2):
    strL1 = ""
    strL2 = ""
    while l1:
        strL1 += str(l1.data)
        l1 = l1.next
    while l2:
        strL2 += str(l2.data)
        l2 = l2.next

    intL1 = int(strL1)
    intL2 = int(strL2)

    final = intL1 + intL2
    finalStr = str(final)

    node = LinkedList(int(finalStr[0]))
    head = node
    finalStr = finalStr[1:]
    for i in range(len(finalStr)):
        newNode = LinkedList(int(finalStr[i]))
        node.next = newNode
        node = node.next
    return head


print("Testing sumListsForward\n")
testList1 = createNewLL()
testList2 = createNewLL()
print("Beginning Linked List")
showLL(testList1)
print("\n")
showLL(sumListsForward(testList1, testList2))
print("\n")


def isLLPalindrome(ll):
    llStr = ""
    while ll:
        llStr += ll.data
        ll = ll.next
    return llStr == llStr[::-1]

def createLLPalindrome(palindrome):
    node = LinkedList(palindrome[0])
    head = node
    palindrome = palindrome[1:]
    for i in range(len(palindrome)):
        newNode = LinkedList(palindrome[i])
        node.next = newNode
        node = node.next
    return head

print("Testing isPalindrome")
palLL = createLLPalindrome("catac")
print("Input")
showLL(palLL)
print("\n=====\n")
print("Output")
print(isLLPalindrome(palLL))
print("\n")
palLL = createLLPalindrome("asdasds")
print("Input")
showLL(palLL)
print("\n=====\n")
print("Output")
print(isLLPalindrome(palLL))
print("\n")