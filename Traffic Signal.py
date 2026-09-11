input_color = input("Enter your traffic color: ")

match input_color.lower():
    case "red":
        print("Stop")
    case "yellow":
        print("Get Ready")
    case "green":
        print("Go")
    case _:
        print("Invalid color")