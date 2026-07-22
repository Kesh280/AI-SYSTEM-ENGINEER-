#Print Counting (while): 1 se 50 tak numbers print karo.

i = 0
while(i<51):
    print(i)
    i = i + 1

#Print Counting (for): 1 se 50 tak numbers print karo range() use karke.

for i in range (51):
    print(i)

#Sum of N: 1 se lekar 100 tak ke sabhi numbers ko add karke total Sum print karo.

for i in range(1,101):
    print(i*(i+1)/2)

#---------------------------------------- Both approaches are right.
  
total_sum = 0
for i in range(1, 101):
   total_sum = total_sum + i
print("1 se 100 tak ka total sum hai:", total_sum)

total_sum = 0
i = 1


while(i<=100):
    total_sum = total_sum + i
    i = i + 1
    print("SUM: ",total_sum)

# Multiplication Table: Ek number lo (jaise 5) aur uska poora table print karo (5 x 1 = 5...).

# By For loop:-

for i in range(11):
    print("4","x",i,"=",4*i)

# By While loop:- 

i = 0
while(i<=10):
    print("4","x",i,"=",4*i)
    i = i + 1

# Even Numbers Only: 1 se 50 ke beech aane wale sirf Even (sam) numbers print karo.

# By For Loop  

for i in range(1,51):
    if(i%2==0):
        print(i)

# By While Loop 

i = 1
while(i<=50):
    if(i%2==0):
        print(i)
    i = i + 1
    




    
   

