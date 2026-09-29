# suqure numbers problem  ( normal )

squares = []
for i in range (1,10):
 squares.append(i*i)
print (squares)


# in listed ccomprehensive approach 
squares = [i*i for i in range (1,10)]
print(squares)

#for odds 
odds = [1 for i in range (1,100) if i % 2 !=0]
print (odds)
  
#for even   
even = [i for i in range (100) if i%2==0]
print(even)
