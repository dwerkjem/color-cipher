import random
from random import seed
from src import tableOfValues

TABLE_OF_VALUES = tableOfValues.get_table_of_values()

if __name__ == '__main__':
    for i in range(len(TABLE_OF_VALUES)):
        print(TABLE_OF_VALUES[i])