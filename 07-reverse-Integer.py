class Solution(object):
    def reverse(self,x):
        sign = 1
        if x < 0:
            sign = -1
        x = abs(x)
        rev = 0L
        while x != 0:
            rev = rev * 10 + x % 10
            x = x / 10
        if rev > (pow(2,31) - 1):
            rev = 0
        rev = rev * sign
        return rev

def main():
    while True:
        try:
            x = int(raw_input("Enter a 32 Integar: "))
            inst = Solution()
            inst.reverse(x)
        except EOFError:
            break

if __name__ == "__main__":
    main()
