# =================== Simple Loop ===================
#  


# For Loops
for i in range(5):
    if i == 3:
        break
    print(i)


# While Loops

count = 0
while count < 5:
    print(count)    # Action before update
    count += 1 
    print(count)   # Action after update
    break


# break - end the loop
# continue - skip over a part of the loop