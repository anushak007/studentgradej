import sys

if len(sys.argv) == 6:  # script name + 5 marks
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

# Determine grade based on average
if avg >= 90:
    grade = "A+"
elif avg >= 80:
    grade = "A"
elif avg >= 70:
    grade = "B"
elif avg >= 60:
    grade = "C"
elif avg >= 50:
    grade = "D"
else:
    grade = "F"

print("The total marks is:", total)
print("The average is:", avg)
print("The grade is:", grade)
