from datetime import datetime

def check_birthdate(year, month, day):
	# write code here
	birthdate = datetime(year, month, day)
	today = datetime.now()
	if today > birthdate:
		return True
	else:
		return False

def calculate_age(year, month, day):
    # write code here
	age = datetime.now() - datetime(year, month, day)
	age_in_years = age.days/365

	print("You are %d years old" % (age_in_years))

def main():
	# write main code here
	year = int(input("Enter year of birth: "))
	month = int(input("Enter month of birth: "))
	day = int(input("Enter day of birth: "))

	if check_birthdate(year, month, day):
		calculate_age(year, month, day)
	else:
		print("The birthdate is invalid")


if __name__ == '__main__':
	main()
