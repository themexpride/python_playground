"""
More Control Flow Tools - for statements

for statement
    iteration over number progression
        not existent
    iteration over defined step and halting
        not existent
    iteration over items of any sequence (list, string...)
        in the order they appear

iterating and modifying collection
    deleting and adding items can be tricky
    better to loop over a copy or create new collection
        copy() method returns new copy of collection
"""

words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

users = {'Hans':'active', 'Elenore':'inactive', 'Chi':'active'}
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status
