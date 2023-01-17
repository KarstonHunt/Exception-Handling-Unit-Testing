class OutOfRangeError(Exception):
    """Exception for number out of range"""
    pass


def main():

    def name_the_number():
        user_number = int(input("Please enter an integer: "))
        if user_number == 1:
            print("one")
        elif user_number == 2:
            print("two")
        elif user_number == 3:
            print("three")
        else:
            raise OutOfRangeError

    try:
        name_the_number()
    except OutOfRangeError:
        print("That's not one of the allowed values!")


if __name__ == '__main__':
    main()

