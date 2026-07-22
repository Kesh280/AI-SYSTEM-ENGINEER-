#Print Counting (while): 1 se 50 tak numbers print karo.

# i = 0
# while(i<51):
#     print(i)
#     i = i + 1

#Print Counting (for): 1 se 50 tak numbers print karo range() use karke.

# for i in range (51):
#     print(i)

#Sum of N: 1 se lekar 100 tak ke sabhi numbers ko add karke total Sum print karo.

# for i in range(1,101):
#     print(i*(i+1)/2)

#---------------------------------------- Both approaches are right.
  
# total_sum = 0
# for i in range(1, 101):
#    total_sum = total_sum + i
# print("1 se 100 tak ka total sum hai:", total_sum)

total_sum = 0
i = 1
while(i<=100):
    total_sum = total_sum + i
    i = i + 1
    print("SUM: ",total_sum)
    
   

