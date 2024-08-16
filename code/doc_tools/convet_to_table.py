import pandas as pd

# List of values
values = [
    " ",
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
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
    "START OF NUMBER",
    "END OF NUMBER",
    "START OF TEXT",
    "END OF TEXT",
    "START OF NEW KEY",
    "END OF NEW KEY",
    "START OF SYMBOL",
    "END OF SYMBOL",
    "BLANK",
    ".",
    ",",
]



# Create binary representation for each value
binary_representation = [format(i, "06b") for i in range(len(values))]

# Create DataFrame
binary_table = pd.DataFrame({"Value": values, "Binary": binary_representation})

print(binary_table.to_string(index=False))
