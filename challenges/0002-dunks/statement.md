# Dunks

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
to determine if we can create a video that gives the expression of an infinite
loop. An infinite loop means that the player that ends the clip should be
the one that get dunked on at the start.

For simplicity, we add a restriction on the number of times a player can
appear in the video. A player can appear only twice in the video: in the clip
where he performed the dunk, and in the next clip where he gets dunked on.

## Input

You input consist of several testcases, but no more than $100$.

The first line of input contains an integer $N$, the number of testcases
in the file. Each testcase starts with a line that contains an integer
$H \le 1000$, the number of clips available. $H$ lines that describe the
available clips follow. Each clip consists of two strings separated by an
space: the name of the player that made the dunk and the name of his "victim".
Each name will consist of letters, underscores, and digits with no space
between.

## Output

For each testcase, output the length of the longest loop, i.e. the number
of clips in the longest video that can be created.

If it is not possible to create an infinite loop, output the number $0$.

## Sample input

```txt
3
11
Jason_Tatum LeBron_James
Chris_Paul Dwight_Howard
Russel_Westbrook Rudy_Gobert
Kobe_Bryant Chris_Paul
John_Collins Joel_Embiid
Joel_Embiid Russel_Westbrook
LeBron_James Jason_Terry
Jason_Terry Jason_Tatum
Anthony_Edwards John_Collins
John_Collins Anthony_Edwards
Dwight_Howard Chris_Paul
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
3
2
0
```

## Explanations

In the first testcase, the longest video we can create uses the clips of:

- LeBron_James dunking on Jason_Terry,
- Jason_Tatum dunking on LeBron_James,
- and Jason_Terry dunking on Jason_Tatum.

Since there are $3$ clips, the answer to this testcase is $3$.
We can create other videos. For example we can use the clip of Chris_Paul
dunking on Dwight_Howard, and the clip of Dwight_Howard dunking on Chris_Paul
later. But the video will contain only two clips.

In the second testcase, we can create only one video by using the dunk of
Aomine_Daiki over Kagami_Taiga and the dunk of Kagami_Taiga on Aomine_Daiki.
So the answer for this testcase is $2$.

For the last testcase, it is not possible to create a video from the clips
available, so the answer is $0$.
