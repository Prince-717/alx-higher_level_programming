#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    fresh_list = []
    for index in range(list_length):
        try:
            answer = my_list_1[index] / my_list_2[index]
        except ZeroDivisionError:
            print("division by 0")
            answer = 0
        except TypeError:
            print("wrong type")
            answer = 0
        except IndexError:
            print("out of range")
            answer = 0
        finally:
            fresh_list.append(answer)

    return (fresh_list)
