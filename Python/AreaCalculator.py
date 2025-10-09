# Easier to complete with function
def calculate(choice):

    print('');
    area = 0;

    # First we check if we got and Integer as an argument
    try:

        # We try to go from smth to integer e.g. "12" --> 12, then yes we can continue, but if 'asgas' --> Can't be an Integer, so we have an exception
        choice = int(choice);

        # Switch case
        match choice:
            case 1:
                base = float(input("Base: "));
                height = float(input("Height: "));
                area = (height * base) / 2;
            case 2:
                length = float(input("Length: "));
                width = float(input("Width: "));
                area = (length * width);
            case 3:
                side = float(input("Side: "));
                area = side ** 2;
            case 4:
                pi = 3.14;
                radius = float(input("Radius: "));
                area = pi * (radius ** 2);
            case 5:
                return 0;
            case _:
                print("Invalid number");
                return 0;

        # Printing area
        print("\nThe area is " + str(area));

    # If not, we have to try again
    except ValueError:
        print("Must be a Number!")

# Printing the GUI and then activating our function
print('==================\nArea Calculator 📐\n==================\n1) Triangle\n2) Rectangle\n3) Square\n4) Circle\n5) Quit\n');
calculate(input("Choose number --> "));