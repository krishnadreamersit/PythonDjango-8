# import library
import sys
# sys.exit()
# quit()

# Alternate of elif statement

# match case statement
# declare
num1  = None
result = None

# input
num1  = input("Enter number (1-7) : ")

# process
num1 = int(num1)
match num1:
	case 1:
		print("One")
	case 2:
		print("Two")
	case 3:
		print("Three")
	# .....
	case 7:
		print("Seven")
	case_default:
		print("Other")
# output
print("Result : ", result)











