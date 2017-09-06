#pragma once

/*
    Factorizes a number into its prime factors.
*/
class PrimeFactorizer
{
public:
    /*
        Factorizes a number into its prime factors.

        @param number The number to factorize.
    */
    void factorize(int number);

private:
    /*
        Determines if a number is prime, that is, it is divisible only by
        1 or itself.

        @param number The number to check.
        @return "true" if "number" is prime, "false" otherwise.
    */
    bool isPrime(int number);
};

