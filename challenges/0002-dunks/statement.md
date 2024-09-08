# Dunk

## Problem description

First, you should watch this [video](https://youtu.be/7KC_UwJ81RU).
It is about basketball. You don't really have to watch it to understand
the problem, but it can help. :grin:

The video shows highlights of players making spectacular dunks on other
players, but in the next clip getting dunked on in turn. The video ended
by showing M. Jordan dunking on P. Ewing. Pretty cool, but it left us with
a taste of unfinished business. As a comment suggests, "the video should
have ended on the guy getting dunked on in the first clip so the video is
like an infinite loop".

Your task will be the following: given a list of dunk highlights, you need
to determine if we can create an infine loop by using all or a subset of the
clips. An infinite loop means that the player that ends the clip should be
the one that get dunked on at the start.

## Input

You input consist of several testcases, but no more than $100$.

The first line of input contains an integer $N$, the number of testcases
in the file. Each testcase starts with a line that contains an integer
$H \le 1000$ which the number of clips available. $H$ lines that represent
the available clips follow. Each clip consists of with two strings separated
by an space: the name of the player that made the dunk and the name of his
"victim". Each name will consist of letters and digits, with no space.

## Output

For each testcase, output the length of the longest loop that can be created,
i.e. the number of clips in the longest video that can be created.

If it is not possible to create an infinite loop, output the number $0$.

## Sample input

```txt
3
15
Jason_Tatum Lebon_James
5
Murasakibara_Atsushi Kiyoshi_Teppei
Aomine_Daiki Kagami_Taiga
Kagami_Taiga Aomine_Daiki
Ryota_Kise Jason_Silver
Nash_Gold Kagami_Taiga
3
Blake_Griffin Pau_Gasol
LeBron_James Kevin_Garnett
Scottie_Pippen Patrick_Ewing
```

## Sample ouptut

```txt
x
2
0
```
