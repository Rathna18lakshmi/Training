def Check_list(numbers):
    print(numbers)
    result = numbers[0] == numbers[-1]
    if result:
        print("Result is True")
    else:
        print("Result is False")
    
numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]

Check_list(numbers_x)
Check_list(numbers_y)
