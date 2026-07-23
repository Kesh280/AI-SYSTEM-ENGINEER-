# Print Counting (while): 1 se 50 tak numbers print karo.

# i = 0
# while(i<51):
#     print(i)
#     i = i + 1

# Print Counting (for): 1 se 50 tak numbers print karo range() use karke.

# for i in range (51):
#     print(i)

# Sum of N: 1 se lekar 100 tak ke sabhi numbers ko add karke total Sum print karo.

# for i in range(1,101):
#     print(i*(i+1)/2)

# ---------------------------------------- Both approaches are right.
  
# total_sum = 0
# for i in range(1, 101):
#    total_sum = total_sum + i
# print("1 se 100 tak ka total sum hai:", total_sum)

# total_sum = 0
# i = 1


# while(i<=100):
#     total_sum = total_sum + i
#     i = i + 1
#     print("SUM: ",total_sum)

# Multiplication Table: Ek number lo (jaise 5) aur uska poora table print karo (5 x 1 = 5...).

# By For loop:-

# for i in range(11):
#     print("4","x",i,"=",4*i)

# By While loop:- 

# i = 0
# while(i<=10):
#     print("4","x",i,"=",4*i)
#     i = i + 1

# Even Numbers Only: 1 se 50 ke beech aane wale sirf Even (sam) numbers print karo.

# By For Loop  

# for i in range(1,51):
#     if(i%2==0):
#         print(i)

# By While Loop 

# i = 1
# while(i<=50):
#     if(i%2==0):
#         print(i)
#     i = i + 1

# Count Digits: Ek number mein total kitne digits hain, yeh count karo (e.g., 4567 mein 4 hain).

# By for loop

# n = "893"
# count = 0
# for i in n:
#     count = count + 1
# print(count)

# By While loop

# n = 893
# count = 0
# while(n>0):
#     n = n//10
#     count = count + 1
# print(count)

# Sum of Digits: Ek number ke saare digits ko aapas mein plus karo (e.g., 123 ➔ 1+2+3 = 6).

# By While Loop

# n = 456
# total = 0
# while(n>0):
#     last_digit = n%10
#     total = total + last_digit
#     n = n//10
# print("Total sum:",total)

# By For loop

# n = "875"
# sum = 0
# for i in n:
#     sum = sum + int(i)
# print(sum)

# Reverse the Number: Kisi number ko ulta kardo (e.g., 876 ➔ 678).

# By While loop

# n = 568
# new = 0
# while(n>0):
#     last_digit = n%10
#     new = (new*10) + last_digit
#     n = n//10
# print(new)

# By For loop

# n = "345"
# new = ""
# for i in n:
#     new = i + new 
# print(new)

# Palindrome Check: Check karo ki koi number ulta karne par original number jaisa same rehta hai ya nahi (e.g., 121).

# By For Loop

# n = str(input("Enter the number: "))
# new = ""
# for i in n:
#     new = i + new
# if (n==new):
#     print(n,"is a palindrome")
# else:
#     print(n,"is not a palindrome")

# By While Loop

# n = int(input("Enter the number: "))
# original = n
# new = 0
# while(n>0):
#     last_digit = n%10
#     new = (new*10) + last_digit
#     n = n//10
# if(original==new):
#    print(original,"is a palindrome")
# else:
#    print(original,"is not a palindrome")
      




    
    

    




    
