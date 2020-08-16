from datetime import datetime

def check_birthdate(year, month, day):
	# write code here
	today = datetime(2019,9,4)
	age_date = datetime(year,month,day)

	if age_date > today:
		return False
	else:
		return True

def calculate_age(year, month, day):
    # write code here
	d = datetime(2019,9,4)
	birthdate = datetime(year,month,day)
	age = d - birthdate
	age_in_years = float(((age.days) / 365))
	print("You are %d years old" % (age_in_years))

def main():
	# write main code here
	birthdate_year = int(input("Enter year of birth: "))
	birthdate_month = int(input("Enter month of birth: "))
	birthdate_day = int(input("Enter day of birth: "))

	if check_birthdate(birthdate_year,birthdate_month,birthdate_day) == True:
		calculate_age(birthdate_year,birthdate_month,birthdate_day)
	else:
		print("The birthdate is invalid")


if __name__ == '__main__':
	main()
