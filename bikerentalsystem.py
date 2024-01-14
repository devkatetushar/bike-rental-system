import tkinter as tk
from tkinter import messagebox

class BikeRentalSystem:
    def __init__(self):
        self.bikes = {'Mountain Bike': 10, 'City Bike': 5, 'Road Bike': 8}
        self.rental_rates = {'Daily': 100, 'Weekly': 500, 'Monthly': 1500}
        self.discount_percentage = tk.DoubleVar(value=10.0)
        self.selected_bike = tk.StringVar()
        self.selected_rental_period = tk.StringVar()

    def update_available_bikes_label(self, label):
        label.config(text=f"Available Bikes: {sum(self.bikes.values())}")

    def rent_bike(self):
        bike = self.selected_bike.get()
        rental_period = self.selected_rental_period.get()

        if bike and rental_period:
            if self.bikes.get(bike, 0) > 0:
                cost = self.calculate_cost(bike, rental_period)
                messagebox.showinfo("Rent Bike", f"You rented a {bike} for {rental_period}. Cost: Rs.{cost:.2f}")
                self.bikes[bike] -= 1
                self.update_available_bikes_label(label_available_bikes)
            else:
                messagebox.showwarning("Rent Bike", f"Sorry, {bike} is not available for rent.")
        else:
            messagebox.showwarning("Rent Bike", "Please select a bike and rental period.")

    def return_bike(self):
        returned_bike = self.selected_bike.get()
        if returned_bike in self.bikes:
            self.bikes[returned_bike] += 1
            messagebox.showinfo("Return Bike", f"Thank you for returning the {returned_bike}.")
            self.update_available_bikes_label(label_available_bikes)
        else:
            messagebox.showwarning("Return Bike", f"{returned_bike} was not rented from this system.")

    def calculate_cost(self, bike, rental_period):
        rate = self.rental_rates.get(rental_period, 0)
        discount = (rate * self.discount_percentage.get()) / 100
        return rate - discount

# Create the GUI
class BikeRentalGUI:
    def __init__(self, root):
        self.rental_system = BikeRentalSystem()

        root.title("Bike Rental System")
        root.minsize(width="400", height="300")
        root.maxsize(width="400", height="300")
        #root.iconbitmap("bike.ico")

        global label_available_bikes
        label_available_bikes = tk.Label(root, text=f"Available Bikes: {sum(self.rental_system.bikes.values())}")
        label_available_bikes.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        label_bike = tk.Label(root, text="Select Bike:")
        label_bike.grid(row=1, column=0, padx=10, pady=10)

        label_period = tk.Label(root, text="Select Rental Period:")
        label_period.grid(row=2, column=0, padx=10, pady=10)

        label_discount = tk.Label(root, text="Enter Discount (%):")
        label_discount.grid(row=3, column=0, padx=10, pady=10)

        label_prices = tk.Label(root, text="Prices:")
        label_prices.grid(row=0, column=2, padx=10, pady=10)

        prices_text = "\n".join([f"{bike}: Rs.{rate}" for bike, rate in self.rental_system.rental_rates.items()])
        label_prices_values = tk.Label(root, text=prices_text)
        label_prices_values.grid(row=1, column=2, rowspan=3, padx=10, pady=10)

        # Dropdowns
        bikes_dropdown = tk.OptionMenu(root, self.rental_system.selected_bike, *self.rental_system.bikes.keys())
        bikes_dropdown.grid(row=1, column=1, padx=10, pady=10)

        periods_dropdown = tk.OptionMenu(root, self.rental_system.selected_rental_period,
                                         *self.rental_system.rental_rates.keys())
        periods_dropdown.grid(row=2, column=1, padx=10, pady=10)

        # Entry for discount
        entry_discount = tk.Entry(root, textvariable=self.rental_system.discount_percentage)
        entry_discount.grid(row=3, column=1, padx=10, pady=10)

        # Rent Button
        rent_button = tk.Button(root, text="Rent Bike", command=self.rental_system.rent_bike)
        rent_button.grid(row=4, column=0, columnspan=2, pady=10)

        # Return Button
        return_button = tk.Button(root, text="Return Bike", command=self.rental_system.return_bike)
        return_button.grid(row=5, column=0, columnspan=2, pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    app = BikeRentalGUI(root)
    root.mainloop()