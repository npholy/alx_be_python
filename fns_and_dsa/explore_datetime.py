from datetime import datetime, timedelta

def display_current_datetime():
    """Displays current date and time in YYYY-MM-DD HH:MM:SS format"""
    current_date = datetime.now()
    print(f"Current date and time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")
    return current_date

def calculate_future_date(days):
    """Calculates and displays future date after adding days to current date"""
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")
    return future_date

if __name__ == "__main__":
    # Part 1: Display current datetime
    display_current_datetime()
    
    # Part 2: Calculate future date
    try:
        days = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(days)
    except ValueError:
        print("Please enter a valid integer number of days.")