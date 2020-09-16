seats = []
seats.append([0, 0, 0, 0, 0, 0, 1, 1])
seats.append([0, 1, 1, 0, 0, 1, 0, 1])
seats.append([1, 0, 0, 1, 0, 1, 1, 0])
seats.append([0, 1, 1, 0, 0, 0, 0, 1])
seats.append([0, 0, 1, 0, 0, 0, 0, 0])
seats.append([1, 0, 1, 1, 0, 0, 1, 1])

def displayBookings():
   print("")
   print("(AVAILABLE SEATS)")
   print("")
   for row in seats:
       print(row)
   print("")
   print(" ")

def checkSeat():
   seats_needed = int(input("enter amount of people"))
   row = int(input("Enter a row number (between 0 and 5)"))
   for i in range(seats_needed):
       column = int(input("Enter a column number (between 0 and 7)"))
   if seats[row][column] == 1:
       print("These seats are already booked.")
   else:
       print("These seats are empty.")
checkSeat()
displayBookings()
