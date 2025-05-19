# binary Search 
# here we are returning the correct index for target element
# time complexity o(logN) + NlogN (for sorting)
# space complexity o(1)
def locate_card(arr, target):
    # first we have to sort the array
    arr.sort()
    low = 0
    high = len(arr) - 1
    while low <= high:
        # / gives a float. You need integer division using // 
        # to get the correct index
        mid = low + (high - low) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# linear search in python
# time complexity o(N)
# space complexity o(1)
def locate_element(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# find number of time rotations
# [5, 6, 9, 0, 2, 3, 4]
# element which is lesser then left and lesser then right
# pivot point - in rotated sorted array how many time the lowest move forwards
def no_of_time_rotation(arr):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2
        # protecting it from remains negative
        if  arr[(mid + 1) % len(arr)] >= arr[mid] and arr[(mid - 1 + len(arr)) % len(arr)] >= arr[mid]:
            return mid
        # if the left half is sorted then move to rght side
        elif arr[low] <= arr[mid]:
            low = mid + 1
        else: 
            high = mid - 1
    return 0

# As a senior backend engineer at jovain, you are tasked to develope the fast
# in memory data structre to manage profile information(username, name, email),
# for 100 million of users. it allows(insert, find, update, list(sorted by username)) 
class User: 
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email
        print('user created')

class UserDatabase:
    def __init__(self):
        self.arr = []

    def insert(self, username, name, email):
        new_user = User(username, name, email)
        self.arr.append(new_user)

    def find(self, username):
        for i in self.arr:
            if i.username == username:
                return i
        print('user not found')

    def update(self, username, name, email):
        for i in self.arr:
            if i.username == username:
                i.name = name
                i.email = email
                print('user updated')
                return
        print('user not found')

    # sort according to the username alphabet
    def get_all(self):
        # lambda is small function for short period of time
        # here in lambda passing user, sort on basis of user.username
        self.arr.sort(key=lambda user: user.username)
        return self.arr

# sort is only for list, it returns nothing as change origninal list
# sorted is for any itertable data structure, it returns sorted data structure instead of changing original

# finf height of tree
# this is structre of tree
class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def find_height_of_tree():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    return root

# 