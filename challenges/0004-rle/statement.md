# Run-length encoding

## Problem description

Run-length encoding (RLE) is a form of lossless data compression in which runs
of data (consecutive occurrences of the same value) are stored as a single
occurrence of that value and a count of its consecutive occurrences,
rather than as the original run.

In simpler terms, the goal of RLE is to compress a string by replacing
sequences of repeated characters with a single character followed (or preceded)
by the number of times it's repeated.

Here are some examples:

```txt
AAAABBBCCDAA => 4A3B2C1D2A
WWWWAAADEXXXXXXYWWW => 4W3A1D1E6X1Y3W
```

RLE is performant when the string to encode contains many runs of identical
characters. For example, the encoded version of this string uses more space
than the original.

```txt
BAD.CANDIDATE => 1B1A1D1.1C1A1N1D1I1D1A1T1E
```

The decoding process involves reconstructing the original data from the encoded
format by repeating characters according to their counts. The steps are as
follows:

- Traverse the encoded data.
- For each count-character pair, repeat the character $count$ times.
- Append these characters to the result string.

You task, for this challenge, is to write a program able to encode strings
using RLE and decode run-length encoded strings.

### Note

In the examples above, when a string is encoded, a single decimal digit is used
to represent the length of a run. When a single run contains more than nine
characters, we have to use more than one count-character pair. For example the
string "AAAAAAAAAAAAAA" is encoded as "9A5A".

To improve this, we will use base 62 digits (0-9, A-Z, a-b) to represent
characters counts. Thus the string "AAAAAAAAAAAAAA" is now encoded as "EA".

## Input

Input consists of several lines that should be processed independantly. Each
line consists of two elements separated by a space:

- a letter, D (for decode) or E (for encode), that indicates the operation
  to perform on the string that follows;
- the string to process.

## Output

For each line of input, print the result of encoding or decoding the input string.

## Sample input

```txt
E AAAABBBCCDAA
E WWWWAAADEXXXXXXYWWW
D 1B1A1D1.1C1A1N1D1I1D1A1T1E
```

## Sample output

```txt
4A3B2C1D2A
4W3A1D1E6X1Y3W
BAD.CANDIDATE
```
