def octreePath(num):
    #BASE 4
    tmp = power = 0
    #Determine largest power
    while tmp <= num:
        tmp = pow(4,power)
        power += 1
    
    #Subtract from number to get Base 4 value
    val = '' 
    count = 0 
    while power >= 0:
        if num >= pow(4,power):
            num -= pow(4,power)
            count += 1
        else:
            power -= 1
            val += str(count)
            count = 0           
    return int(val)

def octreeToCartesian(octPath):
    x = y = 0
    l = len(str(octPath))-1
    for s in str(octPath):
        n = int(s)
        if n < 2: #Base
            y += 0
        else: # Top
            if l == 0:
                y += 1
            else:
                y += int(pow(2,l))
                print('y',y)
        if n == 0 or n == 2: #Left
            x += 0 
        else: #right
            if l == 0:
                x += 1
            else:
                x += int(pow(2,l))
                print('x',x)
        l -= 1
        
    return(x,y)

def octreeCoord(num):
    return octreeToCartesian(octreePath(num))

#TESTING
print("10 ",str(octreePath(4 )))  #10
print("0  ",str(octreePath(0 )))  #0
print("22 ",str(octreePath(10)))  #22
print("32 ",str(octreePath(14)))  #32
print("100",str(octreePath(16)))  #100

print()

print("(3,3)",octreeToCartesian(octreePath(15)))    #(3,3)
print("(0,0)",octreeToCartesian(0))                  #(0,0)
print("(1,2)",octreeToCartesian(octreePath(9)))     #(1,2)
print("(4,7)",octreeToCartesian(322))                #(4,7)
print("(3,5)",octreeToCartesian(213))                #(3,5)
print("(14,12)",octreeToCartesian(octreePath(244))) #(14,12)

for i in range(10):
    print(octreeCoord(i))
