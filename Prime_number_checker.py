print()
print(" "*20 + "!!!! WELCOME TO PRIME NUMBER CHECKER !!!!")
print()

def prime_check(num):
    for i in range(2, num//2 +1):
        if num % i == 0:
            return "Not a Prime Number"
    return "It's a Prime Number"        


if __name__ == '__main__':
    print(prime_check(int(input("Enter the number: "))))