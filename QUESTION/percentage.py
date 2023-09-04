#Program to calculate percentage of a given number of subjects.
print("We'll calculate percentage. What's the maximum marks ? ")
max = int(input("Enter max marks:"))
subn = int(input("Enter no. of subjects:"))
totalmarks = max * subn
print("Enter subject marks !")
marks = dict()
while(subn>0):
    sname = input("Enter subject name:")
    smarks = float(input('Enter subject marks:'))
    marks[sname] = smarks
    subn-=1
total = 0
for k in range(1,20):
    print('.',end=" ")
print('Result\n')
for i in marks:
    print(i + ' :', marks[i])
    total += marks[i]
print(f'Total marks obtained : {total}\nYour percentage is : {(total*100)/totalmarks}')
print("\n")