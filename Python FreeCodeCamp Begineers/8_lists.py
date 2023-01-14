"""
Lists
    
Create a list by naming a variable and put the [] on the right
    Place elements if needed

Return list item using index
    list[0] returns first element

Negative numbers can be used as index
    list[-1] returns the last element

Using indexes with ":" can return a sublist
    list[1:] returns the list ranging from second item to last

Specify a range to return a sublist
    list[2:5] returns the list ranging from second item to fourth
    
Modify list items by getting the index and declaring modified value
    list[1] = "tom" modifies the second element value to "tom"
    
"""

friends = ["Kevin", "Karen", "Jim"]
print(friends[0])
print(friends[1:])
print(friends[0:1])
friends[1] = "Molly"
print(friends)
