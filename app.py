import sys


class Colorz:
    def __init__(self, string):
        self.string = string

    def display_color_range(self):
        for i in range(0, 16):
            for j in range(0, 16):
                code = str(i * 16 + j)
                sys.stdout.write(u"\u001b[38;5;" + code + "m" + code.ljust(4))
            print(u'\u001b[0m]')

    def black(self):
        return f"\033[30m{self.string}\033[0m"

    def red(self, string):
        return f"\033[31m{string}\033[0m"

    def green(self):
        return f"\033[32m{self.string}\033[0m"

    def yellow(self):
        return f"\033[33m{self.string}\033[0m"

    def blue(self):
        return f"\033[34m{self.string}\033[0m"

    def magenta(self):
        return f"\033[35m{self.string}\033[0m"

    def cyan(self):
        return f"\033[36m{self.string}\033[0m"

