import tkinter as tk

###############################################################################
#
# In this module, all of the _todo_ items will be in one comment because you
# will be modifying the same block of code as you go.
#
# DONE: 1. (1 pt)
#
#   First, create a tkinter window called window.
#
#   Make sure you call window's mainloop() method so your window will show up
#   when you run this module.
#
#   Once you have done this, then change the above _TODO_ to DONE.
#
#
# DONE: 2. (4 pts)
#
#   Now, create one frame dimensions 200 by 200.
#
#   Use the default pack() method to place it in the window.
#
#   Also, place 3 labels in the frame labeling them as Label A, Label B, and
#   Label C and give them different background colors.
#
#   Use the place() method to place each of these labels at different
#   coordinates such that they do not overlap.
#   
#   Once you have done this, then change the above _TODO_ to DONE.
#
###############################################################################
window = tk.Tk()

frame1 = tk.Frame(window, height=200, width=200)
frame1.pack()

label_a = tk.Label(frame1, text="Label A", bg="red")
label_a.place(x=20, y=20)

label_b = tk.Label(frame1, text="Label B", bg="green")
label_b.place(x=100, y=50)

label_c = tk.Label(frame1, text="Label C", bg="blue")
label_c.place(x=50, y=100)

window.mainloop()