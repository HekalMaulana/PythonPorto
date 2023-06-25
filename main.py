# total_students_height = 0


# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row
# SUM or total number of the list work
total_height = 0
for height in student_heights:
  total_height += height

print(total_height)

# LEN or length of the list work
number_of_student = 0
for student in student_heights:
  number_of_student += 1

print(number_of_student)

# Average Calculation and round function work

average_students_height = total_height / number_of_student

print(round(average_students_height))


#   total_students_height += student_heights[n]
#   len_student_height = n + 1
#
# average_student_height = total_students_height / len_student_height
#
# print(round(average_student_height))


