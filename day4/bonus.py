#  tables between starting and ending ranges

#  ============= STEPS
# first lets take ranges from user -- DONE
# lets loop through the range -- DONE
# in each loop lets print the table  -- DONE


starting_range = int(input("Enter the starting range for the tables : "))
ending_range = int(input("Enter the ending range for the tables : "))

for table in range(starting_range, ending_range + 1):
    print('START OF TABLE ', table)
    for value in range(1, 21):
        print(table, 'x', value, '=', table * value)
    print('END OF TABLE ', table)
