def show_hotels():
    print("Available hotels:")
    print("1. Hotel Royal")
    print("2. Hotel El Djazair")


def choose_hotel():
    hotel = input("Choose a hotel (1 or 2): ")
    return hotel


def make_booking():
    name = input("Enter your name: ")
    print("Booking confirmed for", name)


def main():
    show_hotels()
    choose_hotel()
    make_booking()


if __name__ == "__main__":
    main()