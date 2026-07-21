#          --LOOPS--


#          --For Loops--

Name = "Keshav"

for i in Name:
    print(i)

colors = ["Red","Green","Blue","Violet"]

for x in colors:
    print(x)
    for i in x:
        print(i)

a = str(input("Enter the Word: "))

for i in a:
    print(i)

#            --Range--

for i in range(10):
   print(i)

for i in range(10):
   print(i+1)

for i in range(1,11):
    print(i)

for i in range(1,15,2):
    print(i)

a = int(input("Enter the Number: "))

for i in range(a):
    print(i + 1)

a = int(input("Enter the number: "))
b = int(input("Enter the number: "))
c = int(input("Enter the number: "))

for i in range(a,b,c):
    print(i)


#            --While Loops--

i = 0
while(i<3):
    print(i)
    i = i + 1
    

print("moved out of the loop")

i = int(input("Enter the number: "))
while(i>0):
    print(i)
    i = i - 1


i = int(input("Enter the number: "))
while(i<=32):
    i = int(input("Enter the number: "))
    print(i)
    
print("Done ")    

i = 0
while(i<9):
    print(i)
    i = i + 1

else:
    print("The loop is done")

# --------------------------------------------

a = range(10)

for i in a:
    if (i == 6):
        print("we reached")
        break
    print(i)

for i in a:
    if (i == 6):
        print("Special number")
        continue
    print(i)

for i in range(11):
     print("5","x",i,"=",5*i) #Table of 5 by for loop

for i in range(11):
     if (i == 5):
          break
     else:
      print("5","x",i,"=",5*i)

i = 0

while(i<11):
    print("5","x",i,"=",5*i) #Table of 5 by while loop
    
    i = i + 1

     






