###############################################################################
# DONE: 1. (5 pts)
#
#   For this _todo_, copy your code from your fillable form from Session 18 and
#   paste it below.
#
#   Now, use the geometry managers we have learned about and reorganize/
#   reformat your fillable form. You must use more than just the pack() method,
#   but you can still use it if it is what you need in a certain spot.
#
#   You may need to add more frames and such to move things around effectively.
#
#   Feel free to be creative on how you want your form to look.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
import tkinter as tk

window = tk.Tk()
window.title("Fillable Form")

# Googled Color:F0F0F0, tk font command, and the sticky command.

window.configure(bg="#F0F0F0")

form_frame = tk.Frame(window, bg="#F0F0F0")
button_frame = tk.Frame(window, bg="#F0F0F0")
form_frame.grid(row=0, column=0, padx=20, pady=20)
button_frame.grid(row=0, column=1, padx=20, pady=20)

header_label = tk.Label(form_frame, text="Please Fill out the Form", bg="#F0F0F0", fg="black", font=("Arial", 14, "bold"))
header_label.grid(row=0, column=0, columnspan=2, pady=10)

name_label = tk.Label(form_frame, text="Name:", bg="#F0F0F0", fg="black", font=("Arial", 10))
name_label.grid(row=1, column=0, sticky="w", padx=5, pady=5)
name_entry = tk.Entry(form_frame, width=35)
name_entry.grid(row=1, column=1, padx=5, pady=5)

address1_label = tk.Label(form_frame, text="Address Line 1:", bg="#F0F0F0", fg="black", font=("Arial", 10))
address1_label.grid(row=2, column=0, sticky="w", padx=5, pady=5)
address1_entry = tk.Entry(form_frame, width=35)
address1_entry.grid(row=2, column=1, padx=5, pady=5)

address2_label = tk.Label(form_frame, text="Address Line 2:", bg="#F0F0F0", fg="black", font=("Arial", 10))
address2_label.grid(row=3, column=0, sticky="w", padx=5, pady=5)
address2_entry = tk.Entry(form_frame, width=35)
address2_entry.grid(row=3, column=1, padx=5, pady=5)

city_label = tk.Label(form_frame, text="City:", bg="#F0F0F0", fg="black", font=("Arial", 10))
city_label.grid(row=4, column=0, sticky="w", padx=5, pady=5)
city_entry = tk.Entry(form_frame, width=35)
city_entry.grid(row=4, column=1, padx=5, pady=5)

state_label = tk.Label(form_frame, text="State:", bg="#F0F0F0", fg="black", font=("Arial", 10))
state_label.grid(row=5, column=0, sticky="w", padx=5, pady=5)
state_entry = tk.Entry(form_frame, width=35)
state_entry.grid(row=5, column=1, padx=5, pady=5)

zip_label = tk.Label(form_frame, text="Zip Code:", bg="#F0F0F0", fg="black", font=("Arial", 10))
zip_label.grid(row=6, column=0, sticky="w", padx=5, pady=5)
zip_entry = tk.Entry(form_frame, width=35)
zip_entry.grid(row=6, column=1, padx=5, pady=5)

phone_label = tk.Label(form_frame, text="Phone Number:", bg="#F0F0F0", fg="black", font=("Arial", 10))
phone_label.grid(row=7, column=0, sticky="w", padx=5, pady=5)
phone_entry = tk.Entry(form_frame, width=35)
phone_entry.grid(row=7, column=1, padx=5, pady=5)

email_label = tk.Label(form_frame, text="Email Address:", bg="#F0F0F0", fg="black", font=("Arial", 10))
email_label.grid(row=8, column=0, sticky="w", padx=5, pady=5)
email_entry = tk.Entry(form_frame, width=35)
email_entry.grid(row=8, column=1, padx=5, pady=5)

submit_button = tk.Button(button_frame, text="Submit", bg="green", fg="white", font=("Arial", 12, "bold"), padx=10, pady=5)
submit_button.pack()

window.mainloop()