color = input("Enter a traffic light color (Red / Yellow / Green) : ").lower()

match color:
    case 'red':
        print("STOP")
    case 'yellow':
        print("WAIT")
    case 'green':
        print("GO")
    case _:
        print("Invalid Input! Try Again.")
