# defining a hash function
def h(e):
    return e%64

# creating a list
L=[]
for i in range(101):
    L.append(i)
  
# hash search starts here  
def search(e):
    def HashSearch(L,h,e):
        D={}
        for i in range(len(L)):
            D[h(i)]=[]
        for j in range(len(L)):
            D[h(j)].append(L[j])
        for k in D[h(e)]:
            if k==e:
                return True
        return False
    return HashSearch(L,h,e)