import pandas as pd

# List of values
values = [
    " ",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "0",
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "END OF LINE",
    "END OF TEXT",
    "START OF TEXT",
    "blank",
    "START OF NEW KEY",
    "END OF NEW KEY",
    "UPPERCASE",
    "START OF SYMBOL",
    "END OF SYMBOL",
]

# Create binary representation for each value
binary_representation = [format(i, "06b") for i in range(len(values))]

# Create DataFrame
binary_table = pd.DataFrame({"Value": values, "Binary": binary_representation})

print(binary_table)