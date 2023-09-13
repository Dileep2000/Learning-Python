# import math
#
# # data = [69.3, 56, 22.1, 47.6, 53.2, 48.1, 52.7, 34.4, 60.2, 43.8, 23.2, 13.8]
# data = [28.6, 25.1, 26.4, 34.9, 29.8, 28.4, 38.5, 30.2, 30.6, 31.8, 41.6, 21.1, 36, 37.9, 13.9]
# data = [2.0, 3.0, 0.3, 3.3, 1.3, 0.4, 0.2, 6.0, 5.5, 6.5, 0.2, 2.3, 1.5, 4.0, 5.9, 1.8, 4.7, 0.7, 4.5, 0.3, 1.5, 0.5, 2.5, 5.0, 1.0, 6.0, 5.6, 6.0, 1.2, 0.2]
# squared_data = [i * i for i in data]
# for i in range(len(data)):
#     print(data[i], " ", squared_data[i])
# print("sums")
# print(sum(data), " ", sum(squared_data))
# print("Mean")
# print((sum(data) / len(data)))
# print("Sum of squares")
# print(sum(squared_data))
# print("mean square")
# print(sum(data) * sum(data))
# print((sum(data) * sum(data)) / 12)
# print((sum(squared_data) - ((sum(data) * sum(data)) / len(data))))
# print((sum(squared_data) - ((sum(data) * sum(data)) / len(data))) / (len(data) - 1))
# print("SD")
# print(math.sqrt((1 / (len(data) - 1)) * (sum(squared_data) - ((sum(data) * sum(data)) / len(data)))))
# print("C.V")
# print(math.sqrt((1 / (len(data) - 1)) * (sum(squared_data) - ((sum(data) * sum(data)) / len(data)))) / (sum(data) / len(data)))
# import time
#
# print("Hello user welcome to the guessing game of the year")
# print("Choose a number between 1 to 100")
# low = 0
# high = 100
# guessed = 50
# actual = 50
# time.sleep(3)
# while True:
#     print("I guess your number is {}".format(guessed))
#     value = input("Is guessed number to High or Low or Correct. Please select H if to High, L for to Low, and C for Correct Guess: ")
#     if value == "L":
#         guessed = int((guessed + high)/2)
#         low = 50
#     elif value == "H":
#         guessed = int((guessed + low)/2)
#         high = 50
#     else:
#         print("I guessed it right. You have chosen {} as your number".format(guessed))
#         break

