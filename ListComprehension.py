#writing a program to learn the concept of List Comprehension
# Let try the Traditional 'For' loop first :
grades=[76,45,67,89];
print("<<<<<<<<<<<These are the original grades>>>>>>>>>>>>>>>");
print(grades);
for grade in grades:
    grades=(grade+5);
print("<<<<<<<<<<These are the result of the grades after computation inside the loop >>>>>>>>>>>>>>>>>>>");
print(grades);
#In the above for loop only the last element is printed with the computation.
#Lets run a for loop to run all.
marks=[45,67,90];
for i in range(len(marks)):
    marks[i]=marks[i]+5;
print(marks);
#Let me pratice another one.
randomNumbers=[67,89,34,67];
#lets add 3 to ech of those
for s in range(len(randomNumbers)):
    randomNumbers[s]=randomNumbers[s]+3;
print(randomNumbers);
#Lets see the list comprehension.
evenNumbers=[2,4,6,8,10,12,16];
print(evenNumbers);
evenNumbers=[marks+ 5 for marks in evenNumbers];
print(evenNumbers);
