# Q. 3 (Python 3.9)

x = int(input())  # x input

if x%2==0: # if x is even
    for a in range(1,(x*2)-1,2): # until a = x (∴ x = (x*2)-1)
        print(a,end=' ') # print pattern
        
else: # if x is odd
    x += 1 # convert to even
    for a in range(1,(x*2)-1,2): # until a = x (∴ x = (x*2)-1)
        print(a,end=' ') # print pattern