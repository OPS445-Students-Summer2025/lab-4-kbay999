#!/usr/bin/env pyhton3

#Author ID:  kbay



t1 = ('Prime', 'Ix', 'Secundus', 'Caladan')
t2 = (1, 2, 3, 4, 5, 6)

# Access tuple values
print(t1[0])   # Output: Prime
print(t2[2:4]) # Output: (3, 4)

print('Ix' in t1)      # Output:True
print('Geidi' in t1)   # Output:False

# Create a list
list2 = [ 'uli101', 'ops235', 'ops335', 'ops445', 'ops535', 'ops635' ]

# Change a value in the list
list2[0]= 'ica100'
print(list2[0])        # Output: ica100
print(list2)           # Output: ['ica100', 'ops235', 'ops335', 'ops445', 'ops535', 'ops635']


# Try t change a value in the tuple (this will cuase an error)
try:
    t2[1] = 10
except TypeError as e:
    print("Error:", e)  # Output: Error message about tuple immutability

# Create a new tuple from a slice of t2

t3 = t2[2:3]
print(t3)               # Output: (3,)

# Iterate over a tuple with a for loop
for item in t1:
    print('item: ' + item)



#!/usr/bin/env python3

def join_sets(s1, s2):
    # join_sets will return a set that contains every value from both s1 and s2
    return s1 | s2  
def match_sets(s1, s2):
    # match_sets will return a set that contains all values found in both s1 and s2
     return s1 & s2 

def diff_sets(s1, s2):
    # diff_sets will return a set that contains all different values which are not shared between the sets

            return s1 ^ s2       

if __name__ == '__main__':
            set1 = set(range(1,10))
            set2 = set(range(5,15))
            print('set1: ', set1)
            print('set2: ', set2)
            print('join: ', join_sets(set1, set2))
            print('match: ', match_sets(set1, set2))
            print('diff: ', diff_sets(set1, set2))
            
            
            
import lab4a


set1 = {1,2,3,4,5}
set2 = {2,1,0,-1,-2}
print(lab4a.join_sets(set1,set2))
# Will output {-2, -1, 0, 1, 2, 3, 4, 5}
print(lab4a.match_sets(set1,set2))
# Will output {1, 2}
print(lab4a.diff_sets(set1,set2))
# Will output {-2, -1, 0, 3, 4, 5}