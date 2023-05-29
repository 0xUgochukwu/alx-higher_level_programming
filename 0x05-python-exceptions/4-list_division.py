#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            value_1 = my_list_1[i]
            value_2 = my_list_2[i]
            division = 0
            try:
                division = value_1 / value_2
            except ZeroDivisionError:
                print("division by 0")
            except (TypeError, ValueError):
                print("wrong type")
        except IndexError:
            print("out of range")
            division = 0
        finally:
            result.append(division)
    return result
