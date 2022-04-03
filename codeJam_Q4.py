num_cases = int(input())
for x in range(num_cases):
    num_modules = int(input())
    fun_factor = list(map(int, input().strip().split(" ")))
    list_position = list(map(int, input().strip().split(" ")))
    max_position = max(list_position)
    index_max = list_position.index(max_position)
    position_1 = []
    position_2 = []
    position_3 = []
    total = 0
    for i in range(len(list_position)):
        if list_position[i] == 1:
            position_1.append(fun_factor[i])
        elif list_position[i] == 2:
            position_2.append(fun_factor[i])
        elif list_position[i] == 3:
            position_3.append(fun_factor[i])
        else:
            total += list_position[i]
    print(position_1, position_2, position_3)
    print(total)
    position_1.sort()
    position_2.sort()
    position_3.sort()
    total_1 = 0
    total_2 = 0
    total_3 = 0
    len_1 = len(position_1)
    len_2 = len(position_2)
    len_3 = len(position_3)
    for i in range(0, len_1, -1):
        total_1 += position_1[-i]
    print(total_1)
    # for i in range(len_2):
    #     total_2 += position_2[(-len_2)+1:]
    # for i in range(len_3):
    #     total_3 += position_3[(-len_3)+1:]
    # print(total_1, total_2, total_3)
    # for i in range(total_1):
    #     total += total_1[i]
    # for i in range(total_2):
    #     total += total_2[i]
    # for i in range(total_3):
    #     total += total_3[i]:
    # print(total)
    print("Case #{}: {}".format(x+1,total))