#John Rick Santillan #1910045

def selection_sort_descend_trace(int_list):
    for i in range(len(int_list)-1):
        index = i
        for j in range(i + 1, len(int_list)):
            if int_list[index] < int_list[j]:
                index = j
        int_list[i], int_list[index] = int_list[index], int_list[i]
        new_string = ''
        for i in int_list:
            new_string += str(i)+' '
        print(new_string)


if __name__ == '__main__':
    input_list = input().split()
    for i in range(len(input_list)):
        input_list[i] = int(input_list[i])
    selection_sort_descend_trace(input_list)