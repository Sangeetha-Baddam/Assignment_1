#FIRST CODE 
#orginal file link: https://colab.research.google.com/drive/13pqevne9BX-fTtcdthKvNDyH7RlWqHgM#scrollTo=VTM1YHQpQoDa
s1 = input("Enter the string :")
s2 =list(s1.strip())
print(type(s1))
print(s2)
s2.pop(-3)
s2.pop(-2)
print(s2)
s2.reverse()
s1 = ''.join(s2)
print(s1)
num1 = 10
num2 = 5
#taking two numbers and performing arithmetic operstions.
sum = num1 + num2
#addition
difference = num1 - num2
#subtraction
product = num1 * num2
#multiplicaton
quotient = num1 / num2
#division
print(f"Sum: {sum}")
print(f"Difference: {difference}")
print(f"Product: {product}")
print(f"Quotient: {quotient}")



#SECOND CODE 

temp = input("Enter the sentence :")
temp = temp.replace('python', 'pythons')
print("Updated string is : ")
print(temp)

#THIRD CODE 

class_score = int(input("Enter your class score: "))
if class_score >= 90:
    letter_grade = "A"
elif class_score >= 80:
    letter_grade = "B"
elif class_score >= 70:
    letter_grade = "C"
elif class_score >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"
print(f"Your letter grade for a score of {class_score} is: {letter_grade}")
