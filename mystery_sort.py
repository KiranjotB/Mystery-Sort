#This program is to run the mystery sort assignment
#Input: User provides a sequence of non-negative data terminated by -1
#Output: First print the list after entry, then print after mystery sort

def main():
  # Initialize an empty list to store the data(set of numbers)
  data = []

  # Control variable for the loop
  continue_input = 1

  # Checking the control variable in the while loop  
  while continue_input:
	  num = int(input("Enter a non-negative number (-1 to end): "))

	  # Terminating at -1
	  if num == -1:
		  continue_input = 0  # This ends the loop
	  else:
		  # The number here makes the list sorted
		  place = 0  # Gets the new place for the new number
		  while place < len(data) and data[place] < num:
			  place += 1
		  data.insert(place, num)

  # Remove the last number (-1) from the list
  if data and data[-1] == -1:
	  data.pop()

  # Prints the sorted list
  print("Sorted list:", data)

# main function is named here
main()