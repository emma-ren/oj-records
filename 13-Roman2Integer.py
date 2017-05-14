class Solution:
    def romanToInt(self, s):
        z = 0
        roman = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
        for i in range(0, len(s) - 1):
            if roman[s[i]] < roman[s[i+1]]:
                z = z - roman[s[i]]
            else:
                z = z + roman[s[i]]
        z = z + roman[s[-1]]
        print z
        return z


def main():
    while True:
        try:
            s = raw_input("Enter Roman num: ")
            inst = Solution()
            inst.romanToInt(s)
        except EOFError:
            break

if __name__ == "__main__":
    main()
