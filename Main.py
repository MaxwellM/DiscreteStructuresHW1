__author__ = 'Maxwell Morin'
import itertools


myList = [1, 2, 3, 4, 4, 6, 8, 10]          # A list I made up containing duplicates
myList2 = [1, 2, 2, 3, 4, 5, 6, 8, 10, 11]  # A second list I made up containing duplicates


def setFromList(A):                         # Converts a list into a list that resembles a set
    output = []
    for x in A:
        if x not in output:
            output.append(x)
    output.sort()
    return output


def intersection(A, B):                     # Creates an intersection between two lists
    A = setFromList(A)
    B = setFromList(B)
    i = [x for x in B if x in A]
    #    s = filter(lambda x: x in B, A)
    print "intersection of myList and myList2: ", i
    return i


def union(A, B):                             # Creates a union of two lists
    A = setFromList(A)
    B = setFromList(B)
    u = [x for x in B and A]
    print "Union of myList and myList2: ", u
    return u


def subset(A, B):                            # Gives a BOOL for whether list A is a subset of list B
    A = setFromList(A)
    B = setFromList(B)
    s = True if [x for x in A and B] else False
    print "Subset of myList and myList2: ", s
    return s


def cartesianProduct(A, B):                   # Creates the Cartesian Product of two lists
    A = setFromList(A)
    B = setFromList(B)
    print "Cartesian Product of myList and myList2: "
    for i in itertools.product(A, B):
        print i
    return i


intersection(myList, myList2)                 # Calling the intersection function
union(myList, myList2)                        # Calling the union function
subset(myList, myList2)                       # Calling the subset function
cartesianProduct(myList, myList2)             # Calling the Cartesian Product function
