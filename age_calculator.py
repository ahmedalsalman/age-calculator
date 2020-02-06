from datetime import datetime

def check_birthdate(year, month, day):
	birthdate = datetime(year, month, day)
	today = datetime.now()
	if birthdate > today:
		return False
	else:
		return True


def calculate_age(year, month, day):
	birthdate = datetime(year, month, day)
	today = datetime.now()
	age = (today - birthdate).days


	print(f"You are {age/365} years old")

def main():
	day = int(input("What day were you born?  "))
	month = int(input("On which month?  "))
	year = int(input("In which year?  "))

	if check_birthdate(year, month, day):
		calculate_age(year, month, day)
	else:
		print("The birthdate you entered is invalid")


if __name__ == '__main__':
	main()
