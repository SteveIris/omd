def change_color(color, c):
    cl = -256 * (1 - c)
    f = 259 * (cl + 255) / (255 * (259 - cl))
    return int(f*(color-128)+128)


class Color:
    END = '\033[0'
    START = '\033[1;38;2'
    MOD = 'm'

    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    def __repr__(self):
        return f'{Color.START};{self.red};{self.green};{self.blue}{Color.MOD}●{Color.END}{Color.MOD}'

    def __eq__(self, other):
        return self.red == other.red and self.blue == other.blue and self.green == other.green

    def __add__(self, other):
        return Color(min(self.red+other.red, 255), min(self.green+other.green, 255), min(self.blue+other.blue, 255))

    def __mul__(self, c: float):
        new_red = change_color(self.red, c)
        new_green = change_color(self.green, c)
        new_blue = change_color(self.blue, c)
        return Color(new_red, new_green, new_blue)

    __rmul__ = __mul__

    def __hash__(self):
        return hash((self.red, self.green, self.blue))


def main():
    red = Color(255, 0, 0)
    green = Color(0, 255, 0)
    blue = Color(0, 1, 255)
    white = Color(240, 240, 240)
    greenish = Color(0, 255, 0)
    print(white)
    print(blue+green)
    assert not (blue == green)
    assert greenish == green
    print({greenish, white, blue, green})
    print(0.5*white)


if __name__ == '__main__':
    main()
