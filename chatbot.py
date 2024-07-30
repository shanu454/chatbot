from tkinter import *

root = Tk()
root.title("Chatbot")

BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"
FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

def send():
    user_input = e.get().lower()
    txt.insert(END, f"\nYou -> {user_input}")

    if user_input == "hello":
        txt.insert(END, "\nBot -> Hi there, how can I help?")
    elif user_input in ["hi", "hii", "hiiii"]:
        txt.insert(END, "\nBot -> Hi there, what can I do for you?")
    elif user_input == "how are you":
        txt.insert(END, "\nBot -> Fine! And you?")
    # Add more responses here based on your chatbot's functionality

    else:
        txt.insert(END, "\nBot -> Sorry! I didn't understand that")

    e.delete(0, END)

label1 = Label(root, bg=BG_COLOR, fg=TEXT_COLOR, text="Welcome", font=FONT_BOLD, pady=10, width=20, height=1)
label1.grid(row=0)

txt = Text(root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=60)
txt.grid(row=1, column=0, columnspan=2)

scrollbar = Scrollbar(txt)
scrollbar.place(relheight=1, relx=0.974)

e = Entry(root, bg="#2C3E50", fg=TEXT_COLOR, font=FONT, width=55)
e.grid(row=2, column=0)

send_button = Button(root, text="Send", font=FONT_BOLD, bg=BG_GRAY, command=send)
send_button.grid(row=2, column=1)

root.mainloop()