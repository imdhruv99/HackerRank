class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0

    def computeDifference(self):
        for i in range(0, len(a)):
            for j in range(i+1, len(a)):
                diff = abs(a[i] - a[j])
                self.maximumDifference = max(diff, self.maximumDifference)


_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)