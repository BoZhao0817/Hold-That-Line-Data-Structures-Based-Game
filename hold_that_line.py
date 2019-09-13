def coordinates():
    box_size = input("input maps size, for example 3,3:").split(',')
    height = int(box_size[0])
    width = int(box_size[1])
    maps = []
    for i in range(height):
        for j in range(width):
            maps.append((i, j))

    return maps

all_coordinates = coordinates()


def chance_one_only(all_coordinates):
    """
    Step 1: In this function, player one gets to choose two coordinates which will be taken as the inputs for the very first line of the
    game.
    Step 2: End A and End B of the lines would be defined.
    Step 3: A check would be performed if the line is made by overlapping any points and if so, the overlapping points would be removed.
    Step 4: Two separate lists will now be created which comprises of the possibilities of lines which can be drawn from End A and End B.
    :return:
    """

    duplicate_all_coordinates = all_coordinates

    print("List of all the possible coordinates for the selected n x m dimension matrix:\n", duplicate_all_coordinates)





    while True:
        End_A = input(print("Enter coordinate representing End A from listed coordinates:"))

        End_A = tuple(map(int, End_A.split(',')))

        if End_A in duplicate_all_coordinates:
            break
        else:
            print("Please type the coordinates from the given list only.")


    while True:
        End_B = input(print("Enter coordinate representing End B from listed coordinates:"))

        End_B = tuple(map(int, End_B.split(',')))

        if End_B in duplicate_all_coordinates:
            break
        else:
            print("Please type the x and y coordinates from the given list only and SEPERATED BY COMMA")


    # Now checking for all the overlapping points which will be removed according to the planned stratergy.


    x0 = End_A[0]
    y0 = End_A[1]

    x1 = End_B[0]
    y1 = End_B[1]


    delta_x = x1 - x0
    delta_y = y1 - y0

    print(delta_x)
    print(delta_y)


    if 0 not in [delta_x, delta_y]:
        first_line_slope = delta_y / delta_x
    else:
        first_line_slope = 0



    for i in duplicate_all_coordinates:

        if i not in [End_A, End_B]:


            x2 = i[0]
            y2 = i[1]


            delta_y_new = y2 - y0
            delta_x_new = x2 - x0

            if 0 not in [delta_x_new, delta_y_new]:

                second_line_slope = delta_y_new/delta_x_new
            else:

                second_line_slope = 0

            if second_line_slope == first_line_slope:

                duplicate_all_coordinates.remove(i)

    End_A_Possibilities = duplicate_all_coordinates
    End_B_Possibilities = duplicate_all_coordinates

    return End_A_Possibilities, End_B_Possibilities



End_A_Possibilities, End_B_Possibilities = chance_one_only(all_coordinates)
print("endA: ", End_A_Possibilities)
print("endB：", End_B_Possibilities)



'''
   method reference from https://blog.csdn.net/sizaif/article/details/79192165 which is a popular Chinese IT forum
   endA, endB, previous_endB, new_endB getting from the former function, if the player choose that his or her next step is endA,
   then endA in code below becomes endB, and other endB related point become endA related point.
'''
endA = (0, 0)  # endA
previous_endB = (3, 3)  # previous_endB
endB = (3, 2)  # endB
new_endB = (0, 3)  # new_endB

def cross(endA, previous_endB, endB):
    x1 = previous_endB[0] - endA[0]
    y1 = previous_endB[1] - endA[1]
    x2 = endB[0] - endA[0]
    y2 = endB[1] - endA[1]

    return x1 * y2 - x2 * y1


def intersection(endA, previous_endB, endB, new_endB):
    if (max(endA[0], previous_endB[0]) >= min(endB[0], new_endB[0])
            and max(endB[0], new_endB[0]) >= min(endA[0], previous_endB[0])
            and max(endA[1], previous_endB[1]) >= min(endB[1], new_endB[1])
            and max(endB[1], new_endB[1]) >= min(endA[1], previous_endB[1])):

        if (cross(endA, previous_endB, endB) * cross(endA, previous_endB, new_endB) <= 0 and cross(endB, new_endB,
                                                                                                   endA) * cross(endB,
                                                                                                                 new_endB,
                                                                                                                 previous_endB) <= 0):
            D = "invalid point, intersection!"
        else:
            D = "valid point!"
    else:
        D = "valid point!"
    return D
