class LinkedList(object):
    def __init__(self, x):
        self.data = x 
        self.next = None


def createLL():
    node = LinkedList(3)
    head = node
    for i in range(7):
        newNode = LinkedList(i)
        node.next = newNode
        node = node.next
    return head

def showLL(linkList):
    while linkList.next != None:
        print(linkList.data)
        linkList = linkList.next

def removeDup(node):
    noDups = []
    prev = node
    noDups.append(node.data)
    node = node.next
    while node.next != None:
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
    while cur.next != None:
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

