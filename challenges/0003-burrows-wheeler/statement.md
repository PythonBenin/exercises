# Burrows-Wheeler

## Problem description

The Burrows-Wheeler transform is a technique for transforming a text message
so that it responds well to compression techniques. Under this transform,
we consider all cyclic shifts of an input string. For example, if our text was
the string "arbitrary string", then the string "rbitrary stringa" would be the
result of cyclicly shifting the string one character to the left. The first
character is moved to the end of the string, and all of the other characters
are moved one index earlier. If a string has $n$ characters, then there are
$n$ cyclic shifts of the string. The text on the left lists all cyclic shifts
of the string "arbitrary string", one per line.

```txt
arbitrary string             stringarbitrary
rbitrary stringa            arbitrary string
bitrary stringar            ary stringarbitr
itrary stringarb            bitrary stringar
trary stringarbi            garbitrary strin
rary stringarbit            ingarbitrary str
ary stringarbitr            itrary stringarb
ry stringarbitra            ngarbitrary stri
y stringarbitrar            rary stringarbit
 stringarbitrary            rbitrary stringa
stringarbitrary             ringarbitrary st
tringarbitrary s            ry stringarbitra
ringarbitrary st            stringarbitrary 
ingarbitrary str            trary stringarbi
ngarbitrary stri            tringarbitrary s
garbitrary strin            y stringarbitrar
```

Under the Burrows-Wheeler transform, we imagine that we lexicographically
sorted all these lines. The figure on the right illustrates what this would
yield for the text “arbitrary string”. The original message is encoded as the
right-hand column of this sorted list of cyclicly shifted copies of the input
string. For example, "arbitrary string" would be encoded as "ygrrnrbitata isr".

For this problem, you are expected to compute the Burrows-Wheeler transform for
an arbitrary line of text. Of course, the transform is invertible, but we’ll let
some other programmer worry about recovering the original message from your
encoding.

## Sample input

```txt
arbitrary·string
this·is·the·thing·I·was·talking·about
```

## Sample output

```txt
ygrrnrbitata·isr
ggssseI··twahnnttthkh·laiibiai···tuo·
```

## Note

In the samples above, the middle dot (·) is used instead of space for the sake
of clarity. Trailing spaces at the end of the encoded string should not be
ignored.

## Source

This challenge is based on the Burrows-Wheeler problem from
[Kattis](https://open.kattis.com/problems/burrowswheeler).
