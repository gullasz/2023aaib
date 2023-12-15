#理解set怎麼用
s=[1,2,3,4] #第一種用大括號
print(s)
s=set((1,3,5,7))#第二種用set 裡面放要加入的東西，可用圓括號
print(s)
s=set((1,2,5,8))#第二種用set 裡面也可用方括號list的陣列
print(s)
s=set(('Hello'))#第二種用set 裡面也可放字串 會一個個拆開
print(s)

#試.add和.remove
s.add(100)
print(s)
s.remove('H')
print(s)