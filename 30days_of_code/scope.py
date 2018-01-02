class Difference(object):
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0

    def computeDifference(self):
        ar = self.__elements
        times = len(ar) - 1

        for e in ar:
            rtn = 0
            intimes = times
            while intimes > 0:
                if abs(e - ar[intimes]) > abs(self.maximumDifference):
                    self.maximumDifference = abs(e - ar[intimes])
                intimes -= 1


_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)