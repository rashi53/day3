def asc(sym,n):
 for j in range(1,n,1):
    print(sym*j)
 return None   
def desc(sym,n):
 for i in range(n,0,-1):
    print(sym*i)
 return None

asc('*',5)
desc('*',5)
def attherate(sym,n):
 for j in range(1,n,1):
    print(sym*j)
 return None   
def hash(sym,n):
 for i in range(n,0,-1):
    print(sym*i)
 return None
def fullpyramid():
 print("Print full Triangle pyramid using stars ")
 size = 7
 m = (2 * size) - 2
 for i in range(0, size):
    for j in range(0, m):
        print(end=" ")
    m = m - 1 
    for j in range(0, i + 1):
        print("* ", end=' ')
    print(" ")
 return None
fullpyramid()    
