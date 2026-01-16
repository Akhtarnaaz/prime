def prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
if __name__ =="__main__":
    import sys
    isprime =  prime(int(sys.argv[1]))
    if isprime:
      print("number is prime")
    else:
        print("number is not prime")  