def find(search_list, value):
    
    sorted_list = sorted(search_list)

    list_length = len(sorted_list)
    while list_length >= 1:
        # uneven list
        if list_length % 2 == 1:
            middle_element = sorted_list[ list_length // 2]
        else:
            middle_element = sorted_list[ ( list_length - 1 ) // 2 ]
    
        if middle_element == value:
            return search_list.index( value )
        # if the middle_element is larger than the value, we want to get rid of everything including that element
        elif middle_element > value:
            sorted_list = sorted_list[ : sorted_list.index( middle_element ) - 1 : 1 ]
        elif middle_element < value:
            sorted_list = sorted_list[sorted_list.index( middle_element ) + 1 : : 1]

        list_length = len(sorted_list)

    raise ValueError("value not in array")
    
    
