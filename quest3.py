library = {
    "Python Basics": 3,
    "Data Science": 2,
    "AI Fundamentals": 1
}

book = input("Enter book to borrow: ")
if book in library:
    if library[book] > 0:
        library[book] -= 1
        print("Book issued.")
    else:
        print("Out of stock.")
else:
    print("Not found.")

with open("library.txt", "w") as file:
    for title, qty in library.items():
        file.write(f"{title}:{qty}\n")