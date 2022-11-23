# print star in python like
'''
*****
****
***
**
*
'''
userinput = int(input('please input number : '))
for x in range(userinput, 0, -1):
    for y in range(x-1):
        print("*", end='')
    print("*")    

   
   