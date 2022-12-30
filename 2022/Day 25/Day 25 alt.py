lines = [l.rstrip() for l in open("input.txt", "r", encoding="utf-8").readlines()]


class Snafu:
    dec_snafu = lambda self, i: "=" if i == -2 else "-" if i == -1 else str(i)
    snafu_dec = lambda self, i: -2 if i == "=" else -1 if i == "-" else int(i)

    def __init__(self, input):
        if type(input) == int:
            s = []
            while input:
                s += [input % 5]
                input //= 5

            s = self.do_carry(s)

            self.s = "".join([self.dec_snafu(c) for c in s[::-1]])
        elif type(input) == str:
            if all([c in ["=", "-", "0", "1", "2"] for c in input]):
                if len(input) > 1 and input[0] == "0":
                    nz = [i != "0" for i in input]
                    if any(nz):
                        self.s = input[nz.index(True) :]
                    else:
                        self.s = "0"
                else:
                    self.s = input
            else:
                raise Exception("Invalid SNAFU number")
        else:
            raise Exception("Invalid type for SNAFU conversion")

    def __repr__(self):
        return self.s

    def __int__(self):
        s = [self.snafu_dec(i) for i in self.s[::-1]]
        return int(sum([5**i * s[i] for i in range(len(s))]))

    def place_values(self, pad=0):
        return [self.snafu_dec(i) for i in self.s[::-1]] + [0] * pad

    def check_carry(self, c):
        if c > 2:
            return c - 5, 1
        elif c < -2:
            return c + 5, -1
        else:
            return c, 0

    def do_carry(self, c):
        for i in range(len(c)):
            digit, carry = self.check_carry(c[i])
            c[i] = digit
            if carry:
                if i + 1 in range(len(c)):
                    c[i + 1] += carry
                else:
                    c.append(carry)

        return c

    def __add__(self, other):
        a = self.place_values(len(other.s) - len(self.s))
        b = other.place_values(len(self.s) - len(other.s))
        c = self.do_carry([a[i] + b[i] for i in range(len(a))])

        return Snafu("".join([self.dec_snafu(i) for i in c[::-1]]))


print(f"Part 1: {sum([Snafu(l) for l in lines], Snafu('0'))}")
