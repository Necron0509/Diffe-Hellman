
#Variables for the modulus and the base to be used throughout 
mod = 321411684795998371952705913685813950403 
base = 4116689149

# Exponant Modulo algorithim function to allow for fast computation of large numbers
# https://www.geeksforgeeks.org/modular-exponentiation-power-in-modular-arithmetic/
def timeComplex(x, y, p):
    res = 1
    x = x % p
    if (x == 0):
        return 0
    while (y > 0 ):
         if ((y & 1) == 1):        
             res = (res * x) % p
         y = y >> 1
         x = (x * x) % p 

    return res

# print the PPN of alice calling the hellman fucntion 
def aliceS1print():
   x = base; y = 288358649145066896504000974356927662371; p = mod
   print('Alice PPN =',timeComplex(x, y, p), 'mod', p) 


# print bob's PNN calling the hellman function 
def bobS1print():
    x = base; y = 266372873561836896319324784586721523627; p = mod
    print('Bob PPN=', timeComplex(x, y, p), 'mod', p) 

# print ALice final using Bob's PPN 
def aliceS2print():
    x = 38463287078112727244892760917610286014; y = 288358649145066896504000974356927662371; p= mod
    print('Alice Final =', timeComplex(x, y, p), 'mod', p)

# print Bob final using Alice ppn 
def bobS2print():
    x = 24004202547683770419016829657526486559; y = 266372873561836896319324784586721523627; p= mod

    print('Bob Final =', timeComplex(x, y, p), 'mod', p)

#initlizating the program and calling the functions 
if __name__ == "__main__":
    aliceS1print()
    bobS1print()
    aliceS2print()
    bobS2print()
