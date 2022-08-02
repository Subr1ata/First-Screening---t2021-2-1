# Q. 4 (Python 3.9)

array = [int(i) for i in input().split()] #[1,2,8,9,12,46,76,82,15,20,30]

dic = {} # dictionary

cnt = 0 # count var initializes to 0.

for index in range(1,10): # iterates from 1 to 9 (to check and count every element in array divisible from 1-9)
    for column in array: # iterates from starting to ending in array (iterates over every element in array)
        if column%index == 0:  # condition checks whether each & every element in array(0...n) divisible by index(1-9) 
            cnt += 1 # if above condition satisfies then cnt updates by cnt + 1 each time (to count each element when above condition satisfies)
    dic[index] = cnt # stores key(index),value(cnt) pair in dic (to store total count for every index)
    cnt = 0 # initializes cnt = 0 after coming out of column loop each time (to count the next element from 0)
    
print(dic) # to print dictionary as a key, value pair