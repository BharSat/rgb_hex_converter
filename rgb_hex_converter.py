def hex_to_rgb(hexadecimal=('#', 'F', 'F', '0', '6', 'A', 'a')):
    # convert a hexadecimal code to rgb code
    hexadecimal = list(hexadecimal)
    hexadecimal = hexadecimal[1:]
    count = 0

    dict1 = {
        'a': 10,
        'b': 11,
        'c': 12,
        'd': 13,
        'e': 14,
        'f': 15
    }

    for i in hexadecimal:
        hexadecimal[count] = dict1.get(i.lower(), i)
        count += 1
    r, r1, g, g1, b, b1 = list(hexadecimal)
    r = (int(r)*16) + int(r1)
    b = (int(b)*16) + int(b1)
    g = (int(g)*16) + int(g1)
    return r, g, b


def rgb_to_hex(rgb=(200, 19, 255)):
    # conver an rgb code to hexadecimal code
    final = []
    for i in rgb:
        py_hex = hex(i)
        hex_ = py_hex.replace('0x', '')
        final.append(hex_)
    return '#' + final[0] + final[1] + final[2]


if __name__ == '__main__':
    print(rgb_to_hex(hex_to_rgb(hexadecimal=tuple('#FA23DE'))))
