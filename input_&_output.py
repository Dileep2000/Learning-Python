# var = input("Message to the user")
# name = input("Please Enter Your Name: ")
# print(name)
# age = int(input("Please Enter Your age"))
file = open('input_&_output.txt', "r")
file.close()

file = open('input_&_output_playground.txt', "w")
for i in range(1, 10):
    file.write(str(i) + "\n")
file.close()

for line in open('input_&_output_playground.txt', 'r'):
    print(line, end="")
with open("input_&_output.txt") as file_read:
    print(file_read.readlines())
