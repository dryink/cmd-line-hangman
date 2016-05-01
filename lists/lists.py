# can be made of same types or various types
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c', 'd']
list3 = [1, "two", 3.0]

# access items directly
first_item_value = list1[0]  # zero indexed!
last_item_value = list1[len(list1) - 1]

# update items directly
list2[0] = 'A'
print "Updated item:", list2[0]

# delete an item
print "Length of list before deletion:", len(list2)
del list2[3]
print "Length of list after deletion:", len(list2)

# concatenate two lists
bigger_list = list1 + list3

# quick start a list with repeated values
quick_list = ['--'] * 5
print quick_list

# loop through a list
for item in list2:
    print item

# reference an item directly (left to right)
print "Should be 'A':", list2[0]

# or right to left
print "Should be 'b':", list2[-2]

# or multiple items by sections
print "Should be 3, 4, & 5", list1[2:]  # remember zero indexed!

# compare lists
print cmp(list1, list2)

# max/min values
print "Max:", max(list1)
print "Min:", min(list1)

# other ways to interact with a lists below...

new_list = [1, 2]
new_list.append(3)
new_list.append(4)
new_list.append(4)

print "'4' occurs", new_list.count(4), "times"

yet_another_list = [7, 8, 9]
new_list.extend(yet_another_list)
print new_list

print "Index of '3' is", new_list.index(3)

new_list.insert(0, -1)
print "New list with '-1' added to front:", new_list

new_list.remove(-1)
print "The negative is gone:", new_list

new_list.reverse()
print "Things are backwards now:", new_list

new_list.sort()
print "This looks better all sorted and such:", new_list