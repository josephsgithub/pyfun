# [⏪ Hello World](/README.md)

![](/assets/hello.gif)

## Table of Contents

1. [**History**](#-history)
2. [**Touch and Chmod**](#-touch-and-chmod)
 1. [**Why not just start editing the file?**](#-why-not-just-start-editing-the-file)
3. [**Printing Text to the Screen**](#-printing-text-to-the-screen)
4. [**Files and `PATH`**](#-files-and-path)
 1. [**What does the `PATH` have to do with `python3`?**](#-what-does-the-path-have-to-do-with-python3)
5. [**Shuh to the Bang**](#-shuh-to-the-bang)
6. [**Color Things Up**](#-color-things-up)
 1. [**What colors can I use?**](#-what-colors-can-i-use)
 2. [**How do I activate them?**](#-how-do-i-activate-them)
 3. [**So how do we print in color to the screen?**](#-so-how-do-we-print-in-color-to-the-screen)
 4. [**What about clearing the screen and random colors?**](#-what-about-clearing-the-screen-and-random-colors)
7. [**Beads on a Necklace**](#-beads-on-a-necklace)
8. [**Action**](#-action)
9. [**Paying for Air**](#-paying-for-air)
10. [**Final Comment**](#-final-comment)
11. [**Do It Again**](#-do-it-again)
12. [**Conclusion**](#-conclusion)

## [⏫ History](#table-of-contents)

Hello world is an long-standing tradition in programming. It has been
written by billions of people soon to include you. As simple as it is,
it still gets used by professionals as a way to make sure everything
is working. In this case, if Python is installed and setup correctly
and you know how to use it. Unlike other lessons we will cover some of
those things as well as the actually programming part.

## [⏫ Touch and Chmod](#table-of-contents)

> Concepts: `touch`, `chmod +x`
> Permissions, Executable, Runnable, File, Script

![](/assets/hello-touch-chmod-ls.gif)

Sounds like a band name. As cool as they are these two commands
would have trouble getting dates, too nerdy. But they are
definitely our friends. `touch` is a simple but little known command
that started out life just to update the time stamp on a given file
showing when it was last modified but has become known as a nice
shortcut for creating an empty file.

```sh
touch hello
```

Look at the file with `ls`, or better, `ls -`. Note the color. Now
make the file into a runnable (executable) script by adding the `x`
permission with `chmod`.

```sh
chmod +x hello
```

List again with `ls -l` and you will see a different color and the `x`
in the permissions bits. At this point you can actually run the
script.

```sh
hello
```

Not very exciting, but it does run. The reason this works is because
by default the system runs the script with whatever the shell
language, in this case Bash. When you login to the command line you
are using a scripting language for every command.

> 💬 This concept of using the shell to run the file by default is
> important because we are working in Python and have to tell
> the system so.

Learning to code in Bash is fun and very useful in itself, but this is
a Python course so let’s move on to telling the system to use Python
to run our code.

```sh
python3 hello
```

Again, not very exciting, but it works! Now let’s put something in
that file.

### [⏫ Why not just start editing the file?](#table-of-contents)

You could do that and a lot of people do. But it saves a step or two
when you forget to `chmod +x` the file later and try to run it. For
some reason getting all that out of the way early on flows better for
this author.

## [⏫ Printing Text to the Screen](#table-of-contents)

> Concepts: `print()`, Strings, Quotes, `vim`, `vi`, Code Birthday

We assume you already learned the essentials of `vim`. If not go
back and read about it in [Prep][]. Open the file and add the
following simple line.

[Prep]: http://prep.skilstak.io

```python
print("Hello world!")
```

Simple enough. Now save and exit (`ctrl-[ + ZZ`). Then run the
script. Do not forget the `3` in `python3`.

```sh
python3 hello
```

Woot! Houston, we have code!! (Google it if you are too young.)

> 💬 If that was your first command line code congratulations today
> is, what we call, your ***code birthday***. Write the date down somewhere.
> Later you will be, like, “I started coding on ______.” And your adult
> friend will be like, “Woahhh.” And you will be all nodding your head
> with a sly grin.

Seems simple enough but what is going on? The script you wrote,
`hello` is actually not running. It is `python3` that is running that
opens your script, compiles it, and then runs it.

## [⏫ Files and `PATH`](#table-of-contents)

> Concepts: Files, `$PATH`, `path`, `which`, `echo`, Full Path, Fully
> Qualified Path, Root Path, `/`, `.`, `..`, `./`, `../`, `~`

![](/assets/path.gif)

You learned about creating files and directories in [Prep][] but now
we are seeing that programs (`python3`) can be located and run
from the shell without telling the computer exactly where they are.
They don’t even have to be in the same directory. That’s because when
the shell cannot find what you typed it goes looking in all the
directories listed in the `PATH`, an ***environment variable*** that
contains them all separated by a colon. We will talk more about
*variables* later. The basically contain stuff like a box that can
only hold one thing at a time. You can see your path with
this:

```sh
echo $PATH
```

The `echo` command simply prints to the screen. And if that is too
hard to read we have added a version that splits it up so you can
read it better:

```sh
path
```

All operating systems have a `PATH` of some kind. Mac and Linux are
the same. Windows does it slightly differently. 

The `which` command tells you where the program is that you want to
run, if the shell can find it at all.

```sh
which python3
```

### [⏫ What does the `PATH` have to do with `python3`?](#table-of-contents)

When you enter `python3 hello` you are telling the shell to find
`python3` using the path, run it, and then read your `hello` script
to run the code.

You could also type `/usr/bin/python3 hello` or `/usr/local/bin/python3
hello` depending on where `python3` is on your system. These longer
versions are called the ***fully qualified path*** or just ***full
path*** because they show how to get to the `python3` program 
from the base or ***root*** of the filesystem, which is the initial
slash `/`.

Now is a good time to remind you of some special filesystem symbols:

| Symbol | Meaning |
| :----: | :-------: |
| `.` or `./` | Current Directory |
| `..` or `../` | Parent Directory (One Up) |
| `~` or `~user` | User Home Directory |
| `/` | Root Directory |

You will use these a lot on the command line as well as in your
`$PATH` environment variable.

## [⏫ Shuh to the Bang](#table-of-contents)

> Concepts: Shebang Line, `#!`, `env`, File System, Path 

**Good programmers are lazy in the best way.** Nature is too.  Both go
with the simplest path that works. Typing `python3` to run your
script every time is way too much work. Let’s simplify with a thing
coder’s call ***the shebang line***, *she* for *hashtag* and *bang*
for *exclamation point*.

![](/assets/shebang.png)

These two characters tell the shell to use the rest of the line as
the command you would normally type in but there is a catch. ***The
shell does not look in the PATH for stuff on the shebang line.***
This means we have to use the *full path* of `/usr/bin/python3`
instead of just `python3`. Go ahead and try it by adding the following
to the very first line of your `hello` script file.

```python
#!/usr/bin/python3
print("Hello world!")
```

Now that we have given the shell this shebang hint and `chmod +x`-ed
our script we can just run it with the script name dropping the
`python3`.

```sh
hello
Hello world!
```

There is still a problem though. On other computers `python3` might
not be at that exact *full path* location, maybe
`/usr/local/bin/python3`. So to write a shebang line that is more
flexible we can use the special `env` program, or `/usr/bin/env`. This
program is pretty much guaranteed to be on any system at exactly that
spot. It’s job in this case is to return the full path to the first
`python3` (or whatever) it finds. Rewrite your first line as follows:

```python
#!/usr/bin/env python3
```

**This is the shebang line to memorize.** You will constantly use it
for Python development and more.

## [⏫ Color Things Up](#table-of-contents)

> Concepts: `import`, `colors`, `as`, Using Python Modules, Terminal
> Escapes, `c.random()`, `c.multi()`, `c.clear`

Now that we have done a lot of technical stuff to get our `hello`
script to run let’s have some fun coloring up the output. Terminals
have become more popular now that we can print all kinds of color
and symbols to the screen (thanks to UTF-8). We are, however, still
limited to 16 colors and have to change the theme of our terminal
to match if we want any kind of consistency. Solarized is the theme
we use in these courses and at SkilStak™. There are many other
amazing ones. This is one of the things we spent time setting up
in [Prep][] so we do not have to do it now.

### [⏫ What colors can I use?](#table-of-contents)

All these terminal screens conform to a standard that sees special,
non-printable characters as commands to change stuff about the screen.
These are called ***terminal escapes***. They are complicated little
buggers so we have put them all into a convenient package to use
simply. First let’s have a look at them by typing `colors` from the
command line.

![](/assets/colors.gif)

### [⏫ How do I activate them?](#table-of-contents)

First you have to tell `python3` to use, or ***import*** code in
another file. Add the following near the top of your code. It has
to be above any lines that might use it.

```python
import colors as c
```

This brings in all the code in the [`colors.py`](/lib/colors.py)
as if you had typed it at that exact spot. Anything in that code
can be used by putting a `c.` in front of it. The `as c` allows us
to not have to type `colors.` every time.

### [⏫ So how do we print in color to the screen?](#table-of-contents)

Now we just print the color *escapes* before the text. Change your
code to use `c.red` for example:

```python
print(c.red + "Hello world!" + c.x)
```

Don’t forget to put the `c.reset` or `c.x` at the end. This *escape*
turns off coloring setting it back. Sometimes if this is forgotten it
can leave your command line stuck in a given color causing you to
logout and back in to get it back.

### [⏫ What about clearing the screen and random colors?](#table-of-contents)

Everyone wants to know about these immediately.  Notice there are
some special entries in the list:

| Command | Action |
| :-----: | :----: |
| `c.clear` | Clears the Screen |
| `c.random()` | Sets Random Color of Text to Follow |
| `c.multi("MULTI")` | Sets Characters to Random Colors |

These are fun and convenient. Try them out.

## [⏫ Beads on a Necklace](#table-of-contents)

> Concepts: Strings, Quotes, `Join Operator`, `+`

Now that we have had a break printing crazy strings let’s take a
moment to talk about what strings are and how to join them together.
**A string is a sequence of characters like beads on a necklace strung
together with quotes on the ends as nots holding them on.** Leave off
a quote and the characters spill off causing errors.

![](/assets/string.png)

The ***join operator*** that looks like a plus `+` sign joins together
the character beads of the string necklace.

Without help see if you can chop your `"Hello world!"` string in half
and make each a different color by joining in another color code. Keep
in mind you only need one `print()`. Everything should change inside
of the parentheses `()`.

## [⏫ Action](#table-of-contents)

> Concepts: Actions, Functions, Function Call

To get a computer to perform an ***action*** we usually need to use
a ***function***, (also sometimes called ***procedures*** but we’ll
get into that another day). To use the *function* we *call* it. In
Python3 `print()` is one of these. We will go into functions in
much more detail later, but it is good to understand the idea now.
For now just know that `print()` is a ***function call***.

## [⏫ Paying for Air](#table-of-contents)

> Concepts: Arguments, Parameters

![](/assets/pump.jpg)

Remember those old air pumps that you did not have to put money in?
Neither do I. But the new ones that require a coin are a good way to
think about ***parameters*** and ***arguments***.

> 💬 At this point you might be like, “make it stop!” but understanding
> these terms will help us talk intelligently about this stuff as we go.

Simply put, *parameters* are like the slots that you put the money in.
*Arguments* are like the coins that go into the slots. When you put
money in something happens. In this case, you get air.

The `print("Hello world!")` *function call* is like this. The `"Hello
world!"` string is an *argument*. For now we can’t see the *parameter*
but can say that we know the `print()` function accepts, or takes,
at least one.

We’ll return to this concept soon.

## [⏫ Final Comment](#table-of-contents)

> Concepts: Comments, `'''`, `"""`, `pydoc3`, `pydoc`

As simple as our program is it is not complete without a descriptive
comment. One of Python’s greatest strengths is the ability to create
amazing documentation right in the code that can be read using the
`pydoc3` tool. In fact, you can try it now without anything added to
the code:

```sh
pydoc3 hello
```

![](/assets/comment.gif)

Now add something like the following line after the shebang line.

```python
#!/usr/bin/env python3

'''Hello prints a colorful greeting to the screen.'''
```

When you run `pydoc3` again note the change. We will learn more about
this as we add more complicated code to other scripts but you can
never start to early to create good, well-documented code. **Good code
documentation separates good programmers from great programmers.** It
might not seem like it now, but programmers spend way more time
reading other people’s code than writing new code. Never forget that
even if you are sure you thing no one will ever see your code. The you
of a year from now will appreciate the you now who takes this extra
effort.

## [⏫ Do It Again](#table-of-contents)

> Concepts: Repetition, Athletic Software Engineering

Philip Johnson coined the term [Athletic Software Engineering][]
in 2013 after realizing many of the skills from athletics are not
always considered when learning to program. Indeed, today’s hackathons
and timed interviews where potential employers have you code solutions
sometimes on paper have reminded everyone that programming well
includes programming *quickly*. The less you have to look up, the less
time it takes and the better you have mastered the syntax and
structure of the language. So let’s do it again.

[Athletic Software Engineering]: http://philipmjohnson.org/essays/athletic-software-engineering.html  

After you finish all this you should have about five lines of code.
Not much, but a good start. **Now either delete or rename those script
and write it all again, and again, and again. Begin to time yourself
and write your best time in your workbook.** A program like this for
someone with 30 wpm typing speed should be way under a minute to
complete. Work hard to get there and not have to look up
anything—particularly the shebang line.

## [⏫ Conclusion](#table-of-contents)

*Hello World* is a simple program but we’ve used this opportunity to
learn all the stuff you need to do to get a script to run from the
command line and understand how that works. As you master the exercise
of writing it don’t forget to remember reviewing this stuff so you
could explain it to someone you were teaching it to. If you can’t
explain it, you don’t know it.

---
[![home](/assets/home-bw.png)](/README.md)
[![cc-by-sa](/assets/cc-by-sa.png)][cc-by-sa]
[![skilstak](/assets/skilstak-logo-bw.png)][skilstak]
[cc-by-sa]: https://creativecommons.org/licenses/by-sa/4.0/
[skilstak]: http://skilstak.io

