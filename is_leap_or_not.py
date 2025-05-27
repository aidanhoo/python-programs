def askUser() -> int:
    return int(input("What year is it? "))

def defineLeapYear(year) -> bool:
    """
    It's a leap year if the year is divisible by 4
    It's NOT a leap year if the year is divisible by 100 (with the exception of 400)
    """
    
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False

def main():
    currentYear = askUser()
    leapYearStatus = defineLeapYear(currentYear)
    print("It's a leap year." if leapYearStatus else "It's not a leap year.")

if __name__ == "__main__":
    main()