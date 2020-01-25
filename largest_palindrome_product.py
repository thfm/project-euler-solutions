def is_palindrome(num):
    digits = str(num)
    for i in range(int(len(digits) / 2)):
        if digits[i] != digits[-i - 1]:
            return False

    return True

palindromes = []

for i in range(100, 1000):
    for j in range(100, 1000):
        product = i * j
        if is_palindrome(product):
            palindromes.append(product)

print(max(palindromes))
