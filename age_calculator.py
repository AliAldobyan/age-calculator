from datetime import datetime

def check_birthdate(year, month, day):
	# write code here
	d = datetime.date(2019,9,4)
	age_date = datetime.date(year,month,day)

	if age_date >= d:
		return False
	else:
		return True

def calculate_age(year, month, day):
    # write code here
	d = datetime(2019,9,4)
	birthdate = datetime.date(year,month,day)
	age = d - birthdate
	age_in_years = int((age.days) / 365)
	print("You are %d years old" % (age_in_years))

def main():
	# write main code here
	year = int(input("Enter year of birth: "))
	month = int(input("Enter month of birth: "))
	day = int(input("Enter day of birth: "))

	if check_birthdate(year,month,day) == True:
		calculate_age(year,month,day)
	else:
		print("The birthdate is invalid")


if __name__ == '__main__':
	main()
