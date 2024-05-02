def custom_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def is_prime(n):
    # Check if the number is less than 2
    if n < 2:
        return False
    
    # Check for factors from 2 to the square root of the number
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def RSA():
    p = int(input("Enter a prime number (p): "))
    q = int(input("Enter a prime number (q): "))
    message = int(input("Enter the message: "))

    if not is_prime(p) or not is_prime(q):
        print("Both p and q should be prime numbers.")
        return

    n = p * q

    t = (p - 1) * (q - 1)
    e = None
    for i in range(2, t):
        if custom_gcd(i, t) == 1:
            e = i
            break
    print("Encryption exponent ",e)    
    if e is None:
        print("No valid public key found")
        return

    j = 0
    while True:
        if (j * e) % t == 1:
            d = j
            break
        j += 1
        if j >= t:  
            print("No valid private key found")
            return
    print("Decryption exponent ",d)
    ct = (message **e) % n
    print(f"Encrypted message is {ct}")

    mes = (ct ** d) % n
    print(f"Decrypted message is {mes}")

RSA()
