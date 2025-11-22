
def fibonnaci(n):
    """
    Recursively returns the n-th Fibonacci number.
    Base Cases:
        F(0) = 0
        F(1) = 1
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonnaci(n - 1) + fibonnaci(n - 2)



# Part II – Euclid’s GCD Algorithm


def gcd(a, b):
    """
    Recursively returns the greatest common divisor (GCD) of two integers.
    If b == 0, return a as the base case.
    Otherwise, gcd(a, b) = gcd(b, a % b)
    """
    if b == 0:
        return a
    return gcd(b, a % b)



# Part III – Recursive String Comparison


def compareTo(s1, s2):
    """
    Recursively compares two strings.
    Returns:
        negative number if s1 < s2
        0 if s1 == s2
        positive number if s1 > s2
    """
    # Base case: both strings empty
    if len(s1) == 0 and len(s2) == 0:
        return 0
    
    # If one string is empty but the other isn't
    if len(s1) == 0:
        return -ord(s2[0])  # s1 < s2
    if len(s2) == 0:
        return ord(s1[0])   # s1 > s2

    # Compare first characters
    if s1[0] != s2[0]:
        return ord(s1[0]) - ord(s2[0])

    # Characters match → compare the rest recursively
    return compareTo(s1[1:], s2[1:])



# Optional: Quick tests

if __name__ == "__main__":
    print("Fibonacci(10):", fibonnaci(10))
    print("GCD(48, 18):", gcd(48, 18))
    print("compareTo('apple', 'banana'):", compareTo("apple", "banana"))
    print("compareTo('cat', 'cat'):", compareTo("cat", "cat"))
    print("compareTo('zebra', 'apple'):", compareTo("zebra", "apple"))
