*This is a work in progress*

## Intro

In computing, numbers are internally represented in binary. This means, when you use an integer type for a variable, this will internally be represented as a summation or concatenation of zeros and ones.
This is also true for booleans! If you had a bit that equaled to 1 or a boolean that was equal to true, there would be no difference in the value of both variables.

As you might know, a single bit represents one 0 or one 1. A concatenation of eight of those bits represent a Byte. The maximum value of a byte is 255 which is the summation of all the bits. Each bit has a "value" and the summation of all the bits is what we call mask. For example the, the first bit value is 1, the 2nd bit value is 2 * the value of the bit to his right.




``` c++
// This is the same as saying that 2^the current bit = x, for example
2^0=1
2^1=2
2^2=4
2^3=8
2^4=16
2^5=32
2^6=64
2^7=128

// Or you could represent this concept like this:
1   = 00000001
2   = 00000010
4   = 00000100
8   = 00001000
16  = 00010000
32  = 00100000
64  = 01000000
128 = 10000000
```

When a number is 4 Bytes long, this means that your number actually uses 32 bits of the internal storage:

00000000 00000000 00000000 00000000

The 32-bit integer data type can hold integer values in the range of −2,147,483,648 to 2,147,483,647. You may also refer to this data type as signed int or unsigned. Unsigned int means that the 32-bit unsigned int data type can hold integer values in the range of 0 to 4,294,967,295.
The reason why the unsigned int will always store more positive values vs a signed is because we use the negative values of the signed int as positives and this duplicates the ammout of positive values you can store in a variable.

## What is their usage for?

Now imagine you want to create a program that holds a state, which is based on multiple values that are one(true) or zero(false). One could store these values in different variables, may they be booleans or integers. Or instead use a single integer variable and use each bit of its internal 32 bits to represent the different true and falses.

An example: 00000101. Here the the first bit (reading from right to left) is true, which represents the first variable. The 2nd is false, which represents the 2nd variable. The third true. And so on...

This is a very compact way of storing data and has many usages.

This is where bit masking comes in. It sounds complex but actually it's very simple.

Bit masking allows you to use operations that work on bit-level.

Editing particular bits in a byte(s)
Checking if particular bit values are present or not.
You actually apply a mask to a value, where in our case the value is our state 00000101 and the mask is again a binary number, which indicates the bits of interest.

By performing binary operations on the mask and the state one could achieve the following:

The AND operator extracts a subset of the bits in the state
The OR operator sets a subset of the bits in the state
The XOR operator toggles a subset of the bits in the state
If we want to set a particular value to true, we could do this by using the OR operator and the following bit mask:

Mask:   10000000b
Value:  00000101b
---- OR ---------
Result: 10000101b
Or one could select a particular value from the state by using the AND operator:

Mask:   00000100b
Value:  00000101b
---- AND ---------
Result: 00000100b
