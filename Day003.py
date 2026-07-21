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



