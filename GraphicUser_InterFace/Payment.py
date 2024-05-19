import tkinter as tk
from tkinter  import messagebox

# Create the main application window
root = tk.Tk()
root.title("Payment Window")
root.geometry("500x550") # Adjust window size as needed
root.configure(bg="#f0f0f0")

# Title label
title_label = tk.Label(
    root, text="Payment Details", font=("Arial", 18), bg="#f0f0f0", padx=20, pady=20
)
title_label.pack()

# Frame for name and email fields
name_email_frame = tk.Frame(root, bg="#f0f0f0", pady=10)
name_email_frame.pack()

# Name label and entry
tk.Label(name_email_frame, text="Name:", bg="#f0f0f0", font=("Arial", 14)).grid(row=0, column=0, sticky="w", padx=10)
name_entry = tk.Entry(name_email_frame, font=("Arial", 14))
name_entry.grid(row=0, column=1, padx=10)

# Email label and entry
tk.Label(name_email_frame, text="Email:", bg="#f0f0f0", font=("Arial", 14)).grid(row=1, column=0, sticky="w", padx=10)
email_entry = tk.Entry(name_email_frame, font=("Arial", 14))
email_entry.grid(row=1, column=1, padx=10)

# Frame for amount and payment method fields
amount_method_frame = tk.Frame(root, bg="#f0f0f0", pady=10)
amount_method_frame.pack()

# Amount label and entry
tk.Label(amount_method_frame, text="Amount (Rs):", bg="#f0f0f0", font=("Arial", 14)).grid(row=0, column=0, sticky="w", padx=10)
amount_entry = tk.Entry(amount_method_frame, font=("Arial", 14))
amount_entry.grid(row=0, column=1, padx=10)

# Payment method label and option menu
tk.Label(amount_method_frame, text="Payment Method:", bg="#f0f0f0", font=("Arial", 14)).grid(row=1, column=0, sticky="w", padx=10)
payment_method_var = tk.StringVar(root)
payment_method_var.set("Credit Card")
payment_method_optionmenu = tk.OptionMenu(amount_method_frame, payment_method_var, "Credit Card", "Debit Card")
payment_method_optionmenu.config(font=("Arial", 14))
payment_method_optionmenu.grid(row=1, column=1, padx=10)

# Card details label
card_label = tk.Label(root, text="Card Details", font=("Arial", 16), bg="#f0f0f0", padx=20, pady=15)
card_label.pack()

# Frame for card details fields
card_details_frame = tk.Frame(root, bg="#f0f0f0", pady=10)
card_details_frame.pack()


# Card number label and entry
tk.Label(card_details_frame, text="Card Number:", bg="#f0f0f0", font=("Arial", 14)).grid(row=0, column=0, sticky="w", padx=10)
card_number_entry = tk.Entry(card_details_frame, font=("Arial", 14), show="*")
card_number_entry.grid(row=0, column=1, padx=10)

# Expiry date label and entry
tk.Label(card_details_frame, text="Expiry Date (MM/YY):", bg="#f0f0f0", font=("Arial", 14)).grid(row=1, column=0, sticky="w", padx=10)
expiry_date_entry = tk.Entry(card_details_frame, font=("Arial", 14))
expiry_date_entry.grid(row=1, column=1, padx=10)

# CVV label and entry
tk.Label(card_details_frame, text="CVV:", bg="#f0f0f0", font=("Arial", 14)).grid(row=2, column=0, sticky="w", padx=10)
cvv_entry = tk.Entry(card_details_frame, font=("Arial", 14), show="*")
cvv_entry.grid(row=2, column=1, padx=10)

def process_payment():
    """Process the payment details provided by the user."""
    # Retrieve the values from the input fields
    name = name_entry.get()
    email = email_entry.get()
    amount = amount_entry.get()
    payment_method = payment_method_var.get()
    card_number = card_number_entry.get()
    expiry_date = expiry_date_entry.get()
    cvv = cvv_entry.get()

    # Check if all required fields are filled
    if not name or not email or not amount or not card_number or not expiry_date or not cvv:
        messagebox.showerror("Error", "Please fill in all required fields.")
        return

    # Generate a receipt with the payment details
    receipt = f"Name: {name}\nEmail: {email}\nAmount: {amount}\nPayment Method: {payment_method}\nCard Number: {card_number}\nExpiry Date: {expiry_date}\nCVV: {cvv}"
    messagebox.showinfo("Payment Details", f"Payment submitted successfully!\n\n{receipt}")

    # Clear the input fields after successful submission
    clear_entries()

def clear_entries():
    """Clear all the input fields."""
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)
    card_number_entry.delete(0, tk.END)
    expiry_date_entry.delete(0, tk.END)
    cvv_entry.delete(0, tk.END)

# Submit button to process the payment
submit_button = tk.Button(root, text="Submit Payment", font=("Arial", 14), command=process_payment, bg="#4CAF50", fg="white", padx=20, pady=10)
submit_button.pack(pady=20)

# Run the main event loop
root.mainloop()
