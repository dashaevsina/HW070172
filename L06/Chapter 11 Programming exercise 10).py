# Chapter 11, programming exercise 10
# This program uses the Sieve of Eratosthenes
# algorithm to find all the primes less than
# or equal to n. 

def main():
    print("\nThis program will use the Sieve of Eratosthenes algorithm to \n find all the primes less than or equal to n.\n")
    n = int(input("Enter a whole number for the value n: "))

    listOfNumbers = list(range(2, n + 1))
    listOfPrimes = []

    while listOfNumbers != []:
        firstNumber = listOfNumbers.pop(0)
        listOfPrimes.append(firstNumber)

        for number in listOfNumbers:
            if number % firstNumber == 0:
                listOfNumbers.remove(number)

    print("The primes less than or equal to", n, "are the following:")
    print(listOfPrimes, ".")

if __name__ == '__main__':
    main()