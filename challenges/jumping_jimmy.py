
import itertools as iter


def jumpingJimmy(tower, jumpHeight):
    result = 0
    for distance in tower:
        if distance <= jumpHeight:
            result += distance
        else:
            break
    return result


from functools import reduce


def jumpingJimmy2_(tower, power, poison, jumpHeight):
    if tower == []:
        return 0
    prefix_sum = []
    acc = 0
    for floor in tower:
        acc += floor
        prefix_sum.append(acc)
    print(prefix_sum)
    if prefix_sum[0] > jumpHeight:
        return 0
    index = 0

    while prefix_sum[index] <= jumpHeight:
        index += 1
    index -= 1
    print(index, "-> ", sum(tower[:index + 1]), "->", jumpHeight)
    super_power = jumpHeight
    while index < len(tower) - 1 and super_power >= prefix_sum[index]:
        if index in power:
            jumpHeight += 1
        if index in poison:
            jumpHeight -= 1
        super_power += jumpHeight
        index += 1
        print(index, "-> ", sum(tower[:index + 1]), "->", jumpHeight)
    return sum(tower[:index])


def to_floor(index):
    return index + 1


def can_up_floor(tower, index, jumpHeight):
    if jumpHeight >= tower[to_floor(index)]:
        return True
    else:
        return False


def jumpingJimmy2(tower, power, poison, jumpHeight):
    index = -1
    floor = -1
    while index < len(tower) - 1:

        aux_jump = jumpHeight
        if jumpHeight < floor:

            break
        if can_up_floor(tower, index, jumpHeight):
            index += 1
            floor = tower[index]
        else:
            if aux_jump >= floor:
                index += 1
                floor = tower[index]
        while aux_jump >= floor and index < len(tower) - 1:
            aux_jump -= floor
            if index + 1 < len(tower) and aux_jump < tower[index+1]:
                break
            else:
                index += 1
                floor = tower[index]
        if index in power:
            jumpHeight += 1
        if index in poison:
            jumpHeight -= 1
        print(index, "->", jumpHeight)
    return sum(tower[:index+1])


def main():

    tower = [1, 4, 3, 2, 2, 2, 2, 1, 4, 4, 2, 3,
             3, 4, 1, 4, 2, 1, 2, 4, 1, 2, 2, 4, 1]
    power = [1, 3, 11]
    poison = [2, 4, 5, 7, 12, 20, 22]
    jumpHeight = 4
    # tower = [32, 76, 64, 61, 31, 8, 68, 42, 68, 17, 91, 47, 12]
    # power = [2, 4, 8, 11]
    # poison = [1, 9]
    # jumpHeight = 100
    # Here is what I understood and already did in my solution. With test 1         for example:

    # tower: [1, 4, 3, 2, 2, 2, 2, 1, 4, 4, 2, 3,
    #         3, 4, 1, 4, 2, 1, 2, 4, 1, 2, 2, 4, 1]
    # power: [1, 3, 11]
    # poison: [2, 4, 5, 7, 12, 20, 22]
    # jumpHeight: 4

    # 0: tower[0], jumpHight = 4, he can't jump over tower[0] + tower[1] because 1 + 4 > 4
    # 1: tower[1], jumpHight = 5, got power[0] = 1
    # 3: tower[2] + tower[3], jumpHight = 6, got power[1] = 3
    # 6: tower[4] + tower[5] + tower[6]
    # 8: tower[7] + tower[8]
    # 10: tower[9] + tower[10]
    # 12: tower[11] + tower[12], jumpHight = 5, got poison[4] = 12
    # 14: tower[13] + tower[14]
    # 15: tower[15]
    # 18: tower[16] + tower[17] + tower[18]
    # 20: tower[19] + tower[20], jumpHight = 4, got poison[5] = 20
    # 22: tower[21] + tower[22], jumpHight = 3, got poison[] = 22
    # 23: jumpHight = 3 < tower[23] = 4: Jimmy2 can't jump anymore
    # return sum[0..22] = 56
    # tower = [1, 1, 4, 1, 3, 4, 2, 2, 2, 4, 4, 1,
    #          3, 4, 2, 4, 2, 3, 4, 3, 2, 4, 2, 4, 4]
    # power = [1, 10, 11, 17]
    # poison = [0, 2, 6, 8, 9, 13, 15, 16, 22]
    # jumpHeight = 4

    # tower = [5, 4, 5, 1, 3, 5, 4, 1, 2, 4]
    # power = []
    # poison = [1, 2, 6]
    # jumpHeight = 5
    print(jumpingJimmy2(tower, power, poison, jumpHeight))


if __name__ == '__main__':
    main()
