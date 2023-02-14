#Password Generator
#Creat list to store all characters for Password
import string
import random
#Using tkinter for GUI
import tkinter as tk

root =tk.Tk()

alphabet = list(string.ascii_letters)
digits = list(string.digits)
special_characters = list("!@#$%^&*()")
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

#user choose length of password
# def generate():
    # length = int(input('Enter length of password: '))
    #
    # #Enter number of each character type
    # alphabet_count = int(input("Enter alphabet count in password: "))
    # digit_count = int(input("Enter digit count in password: "))
    # special_character_count = int(input("Enter special character count in password: "))
    #
    # character_count = alphabet_count + digit_count + special_character_count
    #If character_count is greater than length then false
    # if character_count > length:
    #     print("Character total is greater than chosen password length")
    #     return
    #
    # #Create empty list for password
    # password = []
    #
    # for i in range(alphabet_count):
    #     password.append(random.choice(alphabet))
    #
    # for i in range(digit_count):
    #     password.append(random.choice(digits))
    #
    # for i in range(special_character_count):
    #     password.append(random.choice(special_characters))
    #
    # if character_count < length:
    #     random.shuffle(characters)
    #     for i in range(length - character_count):
    #         password.append(random.choice(characters))
    # random.shuffle(password)
    #
    # print("".join(password))
#generate()


#create window
root.title('Password Generator')
canvas = tk.Canvas(root, width=600, height=300)
canvas['bg'] = 'ghost white'
canvas.grid(rowspan=5, columnspan=2)

#Tell user what information to input

#Labels and entry widgits
label_1 = tk.Label(text='Enter amount of letters')
label_1.grid(row=0, column=0)
letter_count = tk.Entry()
letter_count.grid(row=0, column=1)

label_2 = tk.Label(text='Enter amount of numbers')
label_2.grid(row=1, column=0)
num_count = tk.Entry()
num_count.grid(row=1, column=1)

label_3 = tk.Label(text='Enter amount of special characters')
label_3.grid(row=2, column=0)
spec_char_count = tk.Entry()
spec_char_count.grid(row=2, column=1)

label_4 = tk.Label(text='Enter length of password')
label_4.grid(row=3, column=0)
len_password = tk.Entry()
len_password.grid(row=3, column=1)

# label_4 = tk.Label(text='Enter total amount of characters')
# label_4.grid(row=4, column=0)
# total_char_count = tk.Entry()
# total_char_count.grid(row=4, column=1)
label_5 = tk.Label()

def generate():
#retrieving entries in integers
    letter = int(letter_count.get())
    num = int(num_count.get())
    special = int(spec_char_count.get())
    len = int(len_password.get())
    sum = letter+num+special

    global label_5
    label_5.destroy()

    if sum > len:
        label_5 = tk.Label(text="Charater total is greater than chosen password length")
        label_5.grid(row=4, column=1)

    #Create empty list for password
    password = []

    for i in range(letter):
        password.append(random.choice(alphabet))

    for i in range(num):
        password.append(random.choice(digits))

    for i in range(special):
        password.append(random.choice(special_characters))

    if sum < len:
        random.shuffle(characters)
        for i in range(len - sum):
            password.append(random.choice(characters))
    random.shuffle(password)
    password = "".join(password)
    for i in range(len):
        label_5 =tk.Label(text=str(password))
        label_5.grid(row=4, column=1, pady=10)

    # print("".join(password))

#Button to generate password

button = tk.Button(text='Click here', command=generate)
button.grid(row=4, column=0)

#first frame
# frame = tk.Frame(root, bg='blue', bd=5)
# frame.place(relx=0.05,
#     rely=0.1,
#     relwidth=0.75,
#     relheight=0.1
#     )
#
# #create button
# button = tk.Button(frame,
#     text="Click me!")
# button.place(
#     relx=0.7,
#     relwidth=0.3,
#     relheight=1
# )

root.mainloop()
