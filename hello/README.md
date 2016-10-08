# [⏪ Hello World](/README.md)

![](/assets/hello.gif)

## Table of Contents

1. [**History**](#history)
2. [**Touch and Chmod**](#touch-and-chmod)
 1. [**Why not just start editing the file?**](#why-not-just-start-editing-the-file)
3. [**Printing Text to the Screen**](#printing-text-to-the-screen)
4. [**Shuh to the Bang**](#shuh-to-the-bang)

## [⏫ History](#table-of-contents)

Hello world is an long-standing tradition in programming. It has been
written by billions of people soon to include you. As simple as it is,
it still gets used by professionals as a way to make sure everything
is working. In this case, if Python is installed and setup correctly
and you know how to use it. Unlike other lessons we will cover some of
those things as well as the actually programming part.

## [⏫ Touch and Chmod](#table-of-contents)

> Concepts: `touch`, `chmod +x`, Shell, Bash, Command Line,
> Permissions, Executable, Runnable, File, Script

![](/assets/hello-touch-chmod-ls.gif)

Sounds like a band name. As cool as they are these two commands are
they would have trouble getting gigs, too nerdy. But they are
definitely our friends. `touch` is a simple but little known command
that started out life just to update the time stamp on a give file
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

> This concept of using the shell to run the file by default is
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

We assume you already learned the essentials of `vim`. If not go back
and read about it in [Prep](http://prep.skilstak.io). Open the file
and add the following simple line.

```python
print("Hello world!")
```

Simple enough. Now save and exit (`ctrl-[ + ZZ`). Then run the
script. Do not forget the `3` in `python3`.

```sh
python3 hello
```

Woot! Houston, we have code!! (Google it if you are too young.)

> If that was your first command line code congratulations today
> is, what we call, your ***code birthday***. Write the date down somewhere.
> Later you will be, like, “I started coding on ______.” And your adult
> friend will be like, “Woahhh.” And you will be all nodding your head
> with a sly grin.

## [⏫ Shuh to the Bang](#table-of-contents)

> Concept: Shebang Line, `#!`, `env`

TODO

---
[![home](/assets/home-bw.png)](/README.md)
[![cc-by-sa](/assets/cc-by-sa.png)][cc-by-sa]
[![skilstak](/assets/skilstak-logo-bw.png)][skilstak]
[cc-by-sa]: https://creativecommons.org/licenses/by-sa/4.0/
[skilstak]: http://skilstak.io

