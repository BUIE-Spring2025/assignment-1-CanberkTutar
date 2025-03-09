def int_to_roman(num):
    final_roman_list = []
    total_decimal_count = 0
    zero_detected = False
    if num >= 1000:
        total_decimal_count = 4
    elif num >= 100:
        total_decimal_count = 3
    elif num >= 10:
        total_decimal_count = 2
    elif num >= 1:
        total_decimal_count = 1
    # returning list içinde [0]->which_decimal, [1]->ten, [2]->five, [3]->one
    def find_which_decimal (num):
        if num/1000 >= 1:
            return [4,"","","M"]
        elif num/100 >= 1:
            return [3,"M","D","C"]
        elif num/10 >= 1:
            return [2,"C","L","X"]
        elif num >= 1:
            return [1,"X","V","I"]

    def find_num_on_decimal (num,which_decimal):
        if which_decimal == 4:
            return int(num/1000)
        elif which_decimal == 3:
            return int(num/100)
        elif which_decimal == 2:
            return int(num/10) 
        elif which_decimal == 1:
            return int(num)

    def find_current_roman_decimal(num_on_decimal,one,five,ten):
        current_roman_decimal_list = [] 
        if num_on_decimal < 4:
            for i in range(num_on_decimal):
                current_roman_decimal_list.append(one)
            return current_roman_decimal_list

        elif num_on_decimal == 4:
            current_roman_decimal_list += [one,five]
            return current_roman_decimal_list

        elif (num_on_decimal > 4) and (num_on_decimal < 9):
            current_roman_decimal_list += [five]
            for i in range(num_on_decimal-5):
                current_roman_decimal_list.append(one)
            return current_roman_decimal_list

        elif num_on_decimal == 9:
            current_roman_decimal_list += [one,ten]
            return current_roman_decimal_list

    for i in range(total_decimal_count):
        if zero_detected == True:
            zero_detected = False
            continue
        find_which_decimal_info_list = find_which_decimal(num)   
        which_decimal = find_which_decimal_info_list[0]
        ten = find_which_decimal_info_list[1]
        five = find_which_decimal_info_list[2]
        one = find_which_decimal_info_list[3]
        num_on_decimal = find_num_on_decimal(num,which_decimal)
        current_roman_decimal = find_current_roman_decimal(num_on_decimal,one,five,ten)
        final_roman_list += current_roman_decimal
        del find_which_decimal_info_list
        num -= num_on_decimal*pow(10,which_decimal-1)
        if num < pow(10,which_decimal-2):
            zero_detected = True
    roman_string = "".join(final_roman_list)
    print(roman_string)