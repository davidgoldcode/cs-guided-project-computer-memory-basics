"""
Given an unsigned integer, write a function that returns the number of '1' bits
that the integer contains (the
[Hamming weight](https://en.wikipedia.org/wiki/Hamming_weight))

Examples:

- `hamming_weight(n = 00000000000000000000001000000011) -> 3`
- `hamming_weight(n = 00000000000000000000000000001000) -> 1`
- `hamming_weight(n = 11111111111111111111111111111011) -> 31`

Notes:

- "Unsigned Integers (often called "uints") are just like integers (whole
numbers) but have the property that they don't have a + or - sign associated
with them. Thus they are always non-negative (zero or positive). We use uint's
when we know the value we are counting will always be non-negative."
"""

# you get normal number then convert it


def hamming_weight(n: int) -> int:
    # return the number of 1s in the bitwise representation of the number
    # if we're given a normal unsized integer, how do we convert it
    # to a bitwise representation?
    # bitwise logical operators: '&', '|'
    # the left & right shift operations
    # '<<' or '>>'
    # the '>>' allows us to shift one over to the right

    # using & we have a way to check the rightmost bit of n to see if it equals 1

    # FIRST EXAMPLE
    # count = 0
    # while n != 0:
    #     if n & 1 == 1:
    #         count += 1
    #     n = n >> 1
    # return count

    # SECOND
    # bin_representation = bin(n)
    # counter = 0
    # for i in range(len(bin_representation)):
    #     if bin_representation[i] == '1':
    #         counter += 1
    # return counter

    # THIRD
    return bin(n).count('1')


print(hamming_weight(10))
print(hamming_weight(20))
print(hamming_weight(211))
print(hamming_weight(8))
