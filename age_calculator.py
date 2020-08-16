from datetime import datetime

def check_birthdate(year, month, day):
	# write code here
	today_date = datetime.today()
	age_date = datetime(year, month, day)

	if age_date > today_date:
		return False
	else:
		return True

def calculate_age(year, month, day):
    # write code here
	d = datetime(2019, 9, 4)
	birthdate = datetime(year, month, day)
	age = d - birthdate
	age_in_years = (age.days) / 365
	print("You are %d years old" % (age_in_years))

def main():
	# write main code here
	year = int(input("Enter year of birth: "))
	month = int(input("Enter month of birth: "))
	day = int(input("Enter day of birth: "))

	if check_birthdate(year, month, day) is True:
		calculate_age(year, month, day)
	else:
		print("The birthdate is invalid")


if __name__ == '__main__':
	main()
