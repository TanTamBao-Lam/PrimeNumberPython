# Function to verify if a number is a prime number
def is_prime(number_to_check):
    for factor in range(2, number_to_check):
        # Prime number can only be divided by 1 or itself.
        if number_to_check % factor == 0:
            return False

        return True


# Find all the primes up to input number
def all_primes_number_up_to(num):
    # 0 and 1 are not prime number, and 2 is always a prime number.
    prime_numbers_list = [2]
    for number in range(3, num):
        # 2 is always a prime number.
        if is_prime(number):
            prime_numbers_list.append(number)

    print(f"the prime numbers up to {num} is {prime_numbers_list}")


# Print all primes up to 100.
all_primes_number_up_to(50)
