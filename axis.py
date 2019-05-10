def get_boxes(crate_x, crate_y, box_x, box_y):
    
    i = 1
    x_solved = 0
    y_solved = 0
    while x_solved == 0:
        temp = box_x * i
        if temp == crate_x:
            x_solved = i
        if temp > crate_x:
            x_solved = i - 1
        i += 1
    i = 1

    while y_solved == 0:
        temp = box_y * i
        if temp == crate_y:
            y_solved = i
        if temp > crate_y:
            y_solved = i - 1
        i += 1
    return x_solved * y_solved





print(get_boxes(10, 10, 1, 1))