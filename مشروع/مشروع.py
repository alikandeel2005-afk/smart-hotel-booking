from abc import ABC, abstractmethod


# =========================
# Abstract Class (Blueprint)
# =========================
class HotelItem(ABC):
    def __init__(self, item_id, name, price):
        self.__item_id = item_id
        self.__name = name
        self.__price = price

    def get_item_id(self):
        return self.__item_id

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def set_price(self, new_price):
        if new_price > 0:
            self.__price = new_price
        else:
            print("Invalid price!")

    @abstractmethod
    def calculate_item_cost(self):
        pass

    @abstractmethod
    def display_details(self):
        pass


# =========================
# Hotel Room Class
# =========================
class HotelRoom(HotelItem):

    CITY_TAX = 0.15

    def __init__(self, item_id, name, price, bed_size, smoking_allowed):
        super().__init__(item_id, name, price)
        self.__bed_size = bed_size
        self.__smoking_allowed = smoking_allowed

    def calculate_item_cost(self):
        return self.get_price() + (self.get_price() * HotelRoom.CITY_TAX)

    def display_details(self):
        smoking = "Yes" if self.__smoking_allowed else "No"

        print(
            f"[Room] ID: {self.get_item_id()} | "
            f"{self.get_name()} | "
            f"Bed: {self.__bed_size} | "
            f"Smoking: {smoking} | "
            f"Price: ${self.get_price():.2f}"
        )


# =========================
# Spa Service Class
# =========================
class SpaService(HotelItem):

    GRATUITY = 0.20

    def __init__(self, item_id, name, price, duration):
        super().__init__(item_id, name, price)
        self.__duration = duration

    def calculate_item_cost(self):
        return self.get_price() + (self.get_price() * SpaService.GRATUITY)

    def display_details(self):
        print(
            f"[Service] ID: {self.get_item_id()} | "
            f"{self.get_name()} | "
            f"Duration: {self.__duration} mins | "
            f"Price: ${self.get_price():.2f}"
        )


# =========================
# Reservation Class
# =========================
class CustomerReservation:

    def __init__(self):
        self.__items = []

    def add_item(self, item):
        self.__items.append(item)
        print(f"\n{item.get_name()} added successfully!\n")

    def view_reservation(self):

        if len(self.__items) == 0:
            print("\nReservation is empty.\n")
            return

        print("\n===== CURRENT RESERVATION =====")

        for item in self.__items:
            item.display_details()

        print()

    def print_final_bill(self):

        if len(self.__items) == 0:
            print("\nNo items reserved.\n")
            return

        total = 0

        print("\n========== FINAL HOTEL FOLIO ==========")

        for item in self.__items:
            cost = item.calculate_item_cost()
            print(f"{item.get_name():25} ${cost:.2f}")
            total += cost

        print("---------------------------------------")
        print(f"TOTAL AMOUNT:            ${total:.2f}")
        print("=======================================\n")


# =========================
# Create hotel items
# =========================
room1 = HotelRoom(1, "Deluxe Room", 120, "King", False)
room2 = HotelRoom(2, "Standard Room", 80, "Queen", True)

spa1 = SpaService(3, "Massage Session", 50, 60)
spa2 = SpaService(4, "Facial Treatment", 70, 45)

hotel_items = [room1, room2, spa1, spa2]

reservation = CustomerReservation()


# =========================
# Functions
# =========================
def display_menu():
    print("===== SMART HOTEL BOOKING SYSTEM =====")
    print("1. View Hotel Offerings")
    print("2. Add To Reservation")
    print("3. View Reservation")
    print("4. Print Final Bill")
    print("5. Exit")


def view_offerings():
    print("\n===== AVAILABLE HOTEL OFFERINGS =====")
    for item in hotel_items:
        item.display_details()
    print()


def add_to_reservation():
    view_offerings()

    try:
        item_id = int(input("Enter Item ID: "))

        found = False

        for item in hotel_items:
            if item.get_item_id() == item_id:
                reservation.add_item(item)
                found = True
                break

        if not found:
            print("\nInvalid ID!\n")

    except ValueError:
        print("\nPlease enter a valid number!\n")


# =========================
# Main Loop
# =========================
while True:

    display_menu()

    try:
        choice = int(input("Choose option: "))

        if choice == 1:
            view_offerings()

        elif choice == 2:
            add_to_reservation()

        elif choice == 3:
            reservation.view_reservation()

        elif choice == 4:
            reservation.print_final_bill()

        elif choice == 5:
            print("\nThank you for using the system!")
            break

        else:
            print("\nInvalid choice!\n")

    except ValueError:
        print("\nPlease enter a valid number!\n")