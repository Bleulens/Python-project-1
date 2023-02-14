import tkinter as tk

root = tk.Tk()


#create window
canvas = tk.Canvas(root, width=600, height=300)
canvas.pack()
#Name of application
lable = tk.Label(root, text='Password Generator')
lable.place(
    relx=0.4,
    rely=0.01
    )
#first frame
frame = tk.Frame(root, bg='blue', bd=5)
frame.place(relx=0.05,
    rely=0.1,
    relwidth=0.75,
    relheight=0.1
    )

#create button
button = tk.Button(frame,
    text="Click me!")
button.place(
    relx=0.7,
    relwidth=0.3,
    relheight=1
)

root.mainloop()
