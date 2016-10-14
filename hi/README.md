# [⏪ Hi There!](/README.md)

![](/assets/hi.gif)

## Table of Contents

1. [**The Usual**](#user-content--the-usual)
2. [**Prompting for Input**](#user-content--prompting-for-input)
3. [**Where is Your Assignment?**](#user-content--where-is-your-assignment)
4. [**Difference Between Functions and Procedures**](#user-content--difference-between-functions-and-procedures)
5. [**Conclusion**](#user-content--conclusion)

## [⏫ The Usual](#)

First create a new script called `hi`. Have it just print `Hi there,
what’s your name?` for now. This should be familiar to you since
we just did it in the [*Hello world*](/assets/hello/README.md)
activity. Got it?

## [⏫ Prompting for Input](#)

> Concepts: `input()`, Variables, Operators, `=`, Constants

Good. Now let’s get input from the user/player with the `input()`
function and print it immediately with an emoji as well:

```python
from emoji import smiley

name = input('> ')
print("Nice to meet you, " + name + "! " + smiley)
```

You can color it up as well if you like.

![](/assets/hi.gif)

This function causes the program to pause and wait for the user to
type something in. When the user presses enter whatever the user
typed is put into `name`.

The `name` is a ***variable***. Say that out loud a few times to
get used to the word. Think of variables as boxes that can only
hold one thing at a time. If you put something else into it, it
pushes out what was already there.  You can add something to the
thing that is in the box already, but we will talk about that later.

> 👓 The verb *to vary* means to differ or change from one form to
> another. The word *variable* comes from this and is also used in

Variables are how we get the computer and our script to remember
things. Anything we put into a variable literally goes into the
computer’s memory. 

> 💬 The opposite of a variable is a ***constant***, which never change.
> One example of a constant is Pi (π), the ratio of a circle’s
> circumference to its diameter. You can make your own constants
> in Python as well, but usually we just use a variable and remember
> not to change it by making then name be all caps.

## [⏫ Where is Your Assignment?](#)

> Concepts: Assignment, Assignment Operator, `=`, Operator, Operand

Not the kind on paper that you have to turn in to your *other*
school teacher. Truth is that symbol disguised as an equals sign
is actually not an equals sign at all, it is an ***assignment
operator***. Don’t call it ‘equals’ because that is not what it is. 

> 👓 To *assign* something means to set it aside for a specific
> purpose or to give something a specific job or duty. You
> may know the word from “assigned seating” or being “assigned”
> clean up duty or to a team.

An ***operator*** connects two things in a particular way. In the
old days a telephone *operator* would connect two people in a phone
call. 

![](/assets/phoneoperator.jpg)

Of course there is the modern day equivalent in Tank from *The Matrix*.

![](/assets/operator.jpg)

An ***operand*** is the thing being acted upon, in this case
connected. So the people being connected on the phone would be
*operands* in computer science (and math for that matter).

The *assignment operator* is the thing that connects the *variable*
with the *data*, in this case a *string*, to go into the *variable*.

## [⏫ Difference Between Functions and Procedures](#)

> Concepts: Functions, Procedures, Side Effects,
> Functional Programming Paradigm 

These days few people talk about the distinction between ***function***
and a ***procedure***, but it is still very relevant today, for
example databases still have *stored procedures* and *functions*
and enforce this distinction. A *function* gives something back,
or, another way to put that, ***returns*** something. A *procedure*
does not. A strict function does not do anything to anything outside
of itself. It only returns information. It has no ***side effects***
they say. Truly ***Functional*** programming languages only deal
with these types of *functions*. Other languages, like Python, allow
*procedures* to be defined that do stuff to things outside of itself.

> 💬 The simplest way to think of it is that if it returns something
> it is a *function*, if it does not it is a *procedure*.

Can you decide which of these two `print()` is? How about `input()`?
The second one is a little tricky.

> 💬 The truth is Python and most languages today blur the line between
> *function* and *procedure* and pretty much call everything a *function*
> to keep things simple. But now *you* understand they are really two
> different computer science concepts involved.

## [⏫ Conclusion](#)

> Concepts: REPL, Interactive Text Adventures, Stories

While most Python programs in the wild that you encounter will not
prompt for input in this way, (usually using options and [arguments][]
instead), it is fun to learn early on so you can
make your own interactive scripts and games that have their own
command line feel. This is used for programs with a ***REPL***, or 
read–eval–print loop. Congratulations, you have two more tools in your
Python coder belt.

[arguments]: /arrrgs/README.md

---
[![home](/assets/home-bw.png)](/README.md)
[![cc-by-sa](/assets/cc-by-sa.png)][cc-by-sa]
[![skilstak](/assets/skilstak-logo-bw.png)][skilstak]
[cc-by-sa]: https://creativecommons.org/licenses/by-sa/4.0/
[skilstak]: http://skilstak.io

