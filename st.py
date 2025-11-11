import sys

if len(sys.argv) == 6:  # script name + 5 arguments
    m1 = int(sys.argv[1])
    m2 = int(sys.argv[2])
    m3 = int(sys.argv[3])
    m4 = int(sys.argv[4])
    m5 = int(sys.argv[5])
    print("User input provided")
else:
    m1 = 100
    m2 = 59
    m3 = 86
    m4 = 99
    m5 = 25

total = m1 + m2 + m3 + m4 + m5
avg = total / 5

print("The total marks is:", total)
print("The average is:", avg)
