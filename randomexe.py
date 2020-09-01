class asending:
    def __init__(self, x):
        self.ascen = x

    def a(self):
        print(self.a)
        for i in range(len(self.ascen)):
            for i in range(len(self.ascen)-1):
                if self.ascen[i] > self.ascen[i + 1]:
                    self.ascen[i], self.ascen[i + 1] = self.ascen[i + 1], self.ascen[i]
        return self.ascen


if __name__ == "__main__":
    print(1)
    x = [int(i) for i in input("enter the random no's with ,").split(",")]
    print(x)
    asc = asending(x)
    z = asc.a()
    print(f"the ascending order is {z}")
