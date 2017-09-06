#include "stdafx.h"
#include "PrimeFactorizer.h"

using namespace std;

int main()
{
    cout << "Please enter a number: ";

    int number;

    cin >> number;

    PrimeFactorizer factorizer;

    factorizer.factorize(number);

    cout << "\n\r";

    return 1;
}

void PrimeFactorizer::factorize(int number)
{
    cout << number << " = 1 x ";

    if (isPrime(number))
    {
        // Factors for a prime number are 1 and the number itself.
        cout << number;

        return;
    }

    // Start factorization at 2 and go all the way up to half of the specified
    // number as no number is divisible by any other number higher than half
    // its value.
    int factors = 1;
    for (int divisor = 2; factors < number; ++divisor)
    {
        if (number % divisor == 0)
        {
            // The specified number is exactly divisible by the current
            // divisor.
            if (isPrime(divisor))
            {
                if (factors > 1)
                {
                    cout << " x ";
                }

                cout << divisor;

                factors *= divisor;
            }
            // It is possible that the current divisor itself has factors
            // that have already been discovered, so check if any new
            // factors can be found from the current divisor.
            else if (divisor / factors > 1)
            {
                if (factors > 1)
                {
                    cout << " x ";
                }

                if (divisor % factors == 0)
                {
                    // If the current divisor contains factors that have
                    // been already encountered, skip those.
                    cout << (divisor / factors);

                    factors *= (divisor / factors);
                }
                else
                {
                    cout << divisor;

                    factors *= divisor;
                }
            }
        }
    }
}

bool PrimeFactorizer::isPrime(int number)
{
    if (number < 4)
    {
        // Numbers less than 4 are treated as prime for the purposes of
        // factorization since they cannot be factorized further.
        return true;
    }

    // Check if the specified number is divisible by any number greater than
    // 1 but less than half its value.
    for (int divisor = number / 2; divisor > 1; --divisor)
    {
        if (number % divisor == 0)
        {
            // The specified number is exactly divisible by a number other than
            // 1 and itself. It cannot be a prime number.
            return false;
        }
    }

    // The specified number is not divisible by any number other than 1 and
    // itself. It is therefore a prime number.
    return true;
}
