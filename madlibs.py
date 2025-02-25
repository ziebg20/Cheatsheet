import tkinter as tk
from tkinter import messagebox

# Function to generate the story
def generate_story():
    words = {key: entries[key].get() for key in entries}
    story = f"""
    The {words['adjective1']} and {words['adjective2']} {words['firstName1']} has {words['pastTenseVerb']} 
    {words['firstName2']}'s {words['adjective3']} sibling and plans to steal their {words['adjective4']} 
    {words['pluralNoun1']}! What are a {words['largeAnimal']} and a backpacking {words['smallAnimal']} to do? 
    Before you can help {words['firstName2']}, you'll have to collect the {words['adjective5']} {words['pluralNoun2']} 
    and {words['adjective6']} {words['pluralNoun3']} that open up the {words['numberOneToFifty']} worlds connected 
    to {words['firstName1']}'s lair. There are {words['number1']} {words['pluralNoun4']} and {words['number2']} 
    {words['pluralNoun5']} in the game, along with hundreds of other goodies for you to find.
    """ 
    
    messagebox.showinfo("Your Video Game Story", story)

# Ensure the window opens correctly
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Mad Libs Video Game Generator")
    root.geometry("600x700")

    # Create input fields
    entries = {}
    labels = [
        "adjective1", "adjective2", "adjective3", "adjective4", "adjective5", "adjective6",
        "pastTenseVerb", "pluralNoun1", "pluralNoun2", "pluralNoun3", "pluralNoun4", "pluralNoun5",
        "largeAnimal", "smallAnimal", "firstName1", "firstName2",
        "numberOneToFifty", "number1", "number2"
    ]

    for i, label in enumerate(labels):
        tk.Label(root, text=label.replace("_", " ").title()).grid(row=i, column=0, padx=10, pady=5, sticky="w")
        entry = tk.Entry(root)
        entry.grid(row=i, column=1, padx=10, pady=5)
        entries[label] = entry

    # Create button to generate story
    tk.Button(root, text="SHOW ME", command=generate_story).grid(row=len(labels), column=0, columnspan=2, pady=20)

    # Run the application (Ensures GUI window actually appears)
    root.mainloop()
