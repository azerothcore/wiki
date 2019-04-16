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

/*
 * You can represent a byte as a sequence of zeros and ones accordingly.
 * Reading like this, the order of the bits is read
 * from right to left 
 * <-----
*/
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

Now imagine you want to create a program that holds a state, which is based on multiple values. We can

``` c++
// Store the current state of this program
bool firstValue = true;
bool secondValue = false;

```

We can store these values in different variables, may they be booleans or integers. Or instead use a single integer variable and use each bit of its internal 32 bits to represent the different true and falses.

``` c++
// 00000101
int maskValue = 5;
```

Above, the the first bit is true, which represents the first variable. The 2nd is false, which represents the 2nd variable. The third true. And so on...

This is a very compact way of storing data and has many usages.

This is where bit masking comes in. It sounds complex but actually it's very simple.

Bitmasking allows the user to:
1. Editing particular bits in a byte(s)
2. Checking if particular bit values are present or not.
3. Apply a mask to a value, where in our case the value is our state 00000101 and the mask is again a binary number, which indicates the bits of interest. In this case our mask is the number 5.

## Binary operations

Operating with bits is pretty similar to setting up conditions between two variables. Lets say we have, for example:

``` C++
if (1 && !0)
  printf('This condition is true');
```

Any value that is not 0 will always be the same as true. This means that:

- 1 is true
- !0 is the same as saying not false, which means that !0 is true
- true and true confirms the condition

This way we can compare 2 bits values and if they are both true, we can keep the bit's value and get an end result likewise:

``` C++
255 &= 1

// This will result in 255 becoming 1 due to 
// F - False and T - True to compare the bits from 255 and 1
(255) -> 1 1 1 1 1 1 1 1
(1)   -> 0 0 0 0 0 0 0 1
(1)   -> F F F F F F F T
         0 0 0 0 0 0 0 1
         
// Another example:
Value:  00000101
Mask:   00000100
---- AND ---------
Result: 00000100

// In this case we have the value 5
int MyState = 5;

// And we want to remove 1 state from that value
MyState &= 4;

/* This will turn our 00000101 (5)
 * into a 00000100 (4)
 */
```
Resuming: The AND operator extracts a subset of the bits in the state
Or one could select a particular value from the state by using the AND operator.

--- 

If we want to set a particular value to true, we could do this by using the OR operator and the following bit mask:
The OR operator sets a subset of the bits in the state.

``` C++
Mask:   10000000
Value:  00000101
---- OR ---------
Result: 10000101

// Here we initialize MyState with 5
// This is the same as saying that MyState is equal to 00000101
int MyState = 5;

// Then we can add a value to it with the following syntax
// This will turn the mask from 00000101 to 10000000
MyState |= 128;

// Our end result will turn 5 into 133
```
