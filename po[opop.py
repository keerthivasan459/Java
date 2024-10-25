class queue:
    def _init_(self):
        self.arr=[]
    def enrear(self,data):
        self.arr.append(data)
    def enfront(self,data):
        self.arr.insert(0,data)
    def derear(self):
        return self.arr.pop()
    def defront(self):
        return self.arr.pop(0)
    def peekleft(self):
        return self.arr[0]
    def peekright(self):
        return self.arr[-1]
    def size(self):
        return len(self.arr)
    def is_empty(self):
        return len(self.arr)==0

    obj = queue()
    n = int (input())
    for i in range(n):
        choose = input().split()
        if choose [0]=="append":
            obj.enrear(int(choose[1]))
        elif choose[0]=="appendleft":
            obj.enfront(int(choose[1]))
        elif choose[0]=="pop":
            res=obj.derear()
            print(res)
        elif choose[0]=="popleft":
            res=obj.defront()
            print(res)
        elif choose[0]=="peek":
            res=obj.peekright()
            print(res)
        elif choose[0]=="peekleft":
            res=obj.peekleft()
            print(res)
        elif choose[0]=="size":
           res=obj.size()
           print(res)
        else:
            res=obj.is_empty()
            print(res)
