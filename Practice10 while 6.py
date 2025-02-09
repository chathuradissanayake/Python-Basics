marks = 1
total = 0
student_count = 0
while marks != 0:
    marks= int(input("Please Enter Marks "))
    if marks !=0 and marks <= 100:   #prosess between 0-101 marks only
        total = total + marks
        student_count+= 1
    elif marks > 100:        #ignore above 100
        continue
    else:              #break when input 0
        break
average = total/student_count
print("Average marks for ICT ", average)