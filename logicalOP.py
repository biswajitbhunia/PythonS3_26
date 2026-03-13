has_ticket = True
has_id = False

# AND requires both to be True
print(has_ticket and has_id)  # False 

# OR requires only one to be True
print(has_ticket or has_id)   # True 

# NOT flips the truth
print(not has_ticket)         # False