"""Every day you rent the car costs $40. If you rent the car for 7 or more days, you get $50 off your total. Alternatively, if you rent the car for 3 or more days, you get $20 off your total.
Write a code that gives out the total amount for different days(d)."""

def rental_car_cost(d):
    if d < 4:
        return (d*40)
    elif d >= 4 and d < 7:
        return ((d*40)-20)
    elif d >= 7:
        return ((d*40)-50)
