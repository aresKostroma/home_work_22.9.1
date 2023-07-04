spisok = [int(x) for x in input("Введите числа от 1 до 999 через пробел: ").split()]

def sortirovka(spisok):
    if len(spisok) < 2:
        return spisok[:]
    else:
        middle = len(spisok) // 2
        left = sortirovka(spisok[:middle])
        right = sortirovka(spisok[middle:])
        return fun(left, right)


def fun(left, right):
    result = []
    a, b = 0, 0

    while a < len(left) and b < len(right):
        if left[a] < right[b]:
            result.append(left[a])
            a += 1
        else:
            result.append(right[b])
            b += 1

    while a < len(left):
        result.append(left[a])
        a += 1

    while b < len(right):
        result.append(right[b])
        b += 1

    return result

print(sortirovka(spisok))


def binary_search(spisok, element, left, right):
    if left > right:
        return False

    middle = (right + left) // 2
    if spisok[middle] == element:
        return middle
    elif element < spisok[middle]:

        return binary_search(spisok, element, left, middle - 1)
    else:
        return binary_search(spisok, element, middle + 1, right)


while True:
    try:
        element = int(input("Введите число от 1 до 999: "))
        if element < 0 or element > 999:
            raise Exception
        break
    except ValueError:
        print("Введите число ")
    except Exception:
        print("Неправильный диапазон")


print(binary_search(spisok, element, 0,  len(spisok)))