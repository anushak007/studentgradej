import sys

if len(sys.argv) == 5:
    m1 = sys.argv[0]
    m2 = sys.argv[1]
    m3 = sys.argv[2]
    m4 = sys.argv[3]
    m5 = sys.argv[4]
    print("user input provided")
else:
    m1 = 100
    m2 = 59
    m3 = 86
    m4 = 99
    m5 = 25

total = m1+m2+m3+m4+m5
avg = (total)/5    

print("marks for subject 1:",m1)
print("marks for subject 2:",m2)
print("marks for subject 3:",m3)
print("marks for subject 4:",m4)
print("marks for subject 5:",m5)
print("The total marks is: ",total)
print("The Avg is: ", avg)
