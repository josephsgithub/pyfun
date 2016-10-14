# [⏪ Nyan, Nyan, STOP!](/README.md)

![](/assets/nyan.gif)

## [⏫ Nyan What?](#)

Unless you have been asleep for the last five years you have probably
heard of the infamous Nyan Cat. If not here is a reminder link to
the YouTube video for your enjoyment.


[![](/assets/nyan-vid.gif)](https://youtu.be/QH2-TGUlwu4)

Love it or hate it, we are gonna code it.

## [⏫ The Usual](#)

Create a script called `nyan` in the way that should be second
nature almost by now. Print your interpretation of “Nyan” but it
can be anything, within reason. Grab an 
[emoji](http://emoji.skilstak.io) for fun while you are at it
or import them, whichever you find easier.

```python
from emoji import cat
print(cat + " Nyan")
```

Add some color if you like.

> 💬 As a reminder make sure to stick with the names we say so
> that the links from your workbook will work.

## [⏫ True or False](#)

> Concepts: Booleans, Types, `True`, `False`

Before we continue let’s review what `True` and `False` actually
are. The big name for them is ***booleans***. A boolean is
something that is either `True` or `False`.

> 👓 The term Boolean comes from a English math guy name George
> Boole who was obsessed with logic and conditions.

How long is `True` `True`? How long is `False` `False`? Seems
silly to ask the question but that is exactly what we are
about to ask the computer in our script.

> 💬 The idea of true and false, on and off, 1 and 0 is found
> throughout computers and computer science because ultimately
> that is all a computer understands. Everything a computer
> does and knows can be reduced to a bunch of ons and offs.

## [⏫ Loop It](#)

> Concepts: `while`, Infinite Loops, End of the World

You may remember the `loop:` from CodeCombat. Well, that does not
exist in real Python. What you actually want is `while True:`
so let’s add that:

```python
while True:
    print(cat + " Nyan")

```
⛔ **DO NOT RUN YOUR PROGRAM YET!** First you have to learn to
stop it. Keep reading.

Here is that question, how long is `True` `True`? The answer
is forever, meaning this makes the computer print forever until
you kill it, the computer gets turned off, the power fails, or
the world we just so cordially greeted ends. Do not panic, there
are ways to stop your script besides ending the world, but we
need to go over some stuff first.

The `while` statement looks at the thing following it and will
continue to do whatever is in that *code block* as long as that
*condition* is true.

## [⏫ In Your Block](#)

> Concepts: Code Blocks, `:`

A ***code block*** is some amount of code that is grouped together.
The most common way to do this is with braces (`{}`) but Python
uses another way. The colon character (`:`) when followed by a line
return and then finding the next line after it to be indented tells
Python to use all the lines that line up with that line as a code
block. So in our script now we have only one line in our *code block*
that we could add to:

```python
while True:
    print("Nyan")
    print("Another Nyan")
```

You get the idea. These *code blocks* can be combined one within
another, which we will go over more later.

## [⏫ Indenting with `vim`](#)

> Concepts: `>>`, `<<`, `vim`

You probably just added spaces to the beginning of your `print..`
statement that you already had, which is fine. But there is another
way.

> 👓 To *indent* means to start a line of text further from the 
> edge, or margin, than the main part of text By the way, to *indent*
> when starting a new line type the `TAB` key. In `vim` this makes
> it insert four spaces. There is no need to spam the space key (as
> some noobs do).

Since we have already typed out the print line you could just move it
over with `vim`’s `>>` shortcut. From command mode this inserts
enough spaces to ***indent*** properly. To move back the other
direction `vim` has the `<<` shortcut as well. Like all `vim` commands
these can be combined with numbers to operate on more than one line.
So `5>>` indents the five next lines from where you are in the file.

![](/assets/indenting.gif)

> 💬 Be careful if you are using an editor other than the one we
> have configured using [`home-config`][] because your `vim`
> might put an actual tab character in there, which no one does
> in the world of Python despite what anyone might tell you.

## [⏫ Spaces and Tabs that Matter](#)

> Concepts: Significant White Space
> 
Proper ***indentation*** is very important because Python uses
spacing as a part of the language, or, as they say, it is a
***significant whitespace*** language.

> 💬 At one point the world found bloody battles over whether white
> space should ever be a part of any language, turns out everyone
> settled down and more than a few still use the concept today

Why does whitespace matter? Because that is how Python identifies
a *code block*.

## [⏫ Make is STOP!](#)

TODO

## [⏫ Stop From Stopping?](#)

TODO

## [⏫ Handling Interruptions Politely ](#)

TODO

## [⏫ Conclusion](#)

The infamous Nyan cat shows us about loops and what happens when
we cannot stop it. This comes up a lot when programming particularly
things that involve loops, which is pretty much every game ever
made.

> 💪 To flex those *string*, `print()`, and *join operator* skills
> see if you can create an ascii art animation of your cat flying.
> Make each frame a variable (constant) and print it after a `sleep()`
> delay, then clear the screen and print the next frame and so on.

---
[![home](/assets/home-bw.png)](/README.md)
[![cc-by-sa](/assets/cc-by-sa.png)][cc-by-sa]
[![skilstak](/assets/skilstak-logo-bw.png)][skilstak]
[cc-by-sa]: https://creativecommons.org/licenses/by-sa/4.0/
[skilstak]: http://skilstak.io

