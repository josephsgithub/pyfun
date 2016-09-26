
```python
#!/usr/bin/env python3

def ask_if_likes(food):
    print("Do you like " + food + "?")
    answer = input("> ")

ask_if_likes("waffles")
ask_if_likes("pancakes")
ask_if_likes("french toast")
```


```python
#!/usr/bin/env python3

import sys

def ask_if_likes(food):
    print("Do you like " + food + "?")
    answer = input("> ")
    return answer

first_answer = ask_if_likes("waffles")

if first_answer == "no":
    print("Well fine.")
    sys.exit()

second_answer = ask_if_likes("pancakes")
third_answer = ask_if_likes("french toast")
```

```python
#!/usr/bin/env python3

import sys

def ask_if_likes(food):
    print("Do you like " + food + "?")
    answer = input("> ")
    if answer == "no":
        print("Well fine.")
        sys.exit()
    return answer

first_answer = ask_if_likes("waffles")
second_answer = ask_if_likes("pancakes")
third_answer = ask_if_likes("french toast")
```

```python
#!/usr/bin/env python3

import sys

def assert_likes(food):
    print("Do you like " + food + "?")
    answer = input("> ")
    if answer == "no":
        print("Well fine.")
        sys.exit()

assert_likes("waffles")
assert_likes("pancakes")
assert_likes("french toast")

print("♫ Doo, doo doo dupe ♫")
print("♫ Can't wait to get a mouthful! ♫")
```

```python
#!/usr/bin/env python3

import sys
import colors as c

negative = ("no", "nuhuh","i don't like")

def assert_likes(food):
    print(c.clear + c.random() + "Do you like " + food + "?" + c.x)
    answer = input(c.base00 + "> " + c.base3)
    answer = answer.lower().strip()
    if answer.startswith(negative): 
        print(c.red + "Well fine." + c.x)
        sys.exit()

assert_likes("waffles")
assert_likes("pancakes")
assert_likes("french toast")

print("♫ Doo, doo doo dupe ♫")
print("♫ Can't wait to get a mouthful! ♫")
```

```python
#!/usr/bin/env python3

import sys
import colors as c
from subprocess import call

negative = ("no", "nuhuh","i don't like")

def assert_likes(food):
    print(c.clear + c.random() + "Do you like " + food + "?" + c.x)
    call(["say", "do you like " + food + "?"])
    answer = input(c.base00 + "> " + c.base3)
    answer = answer.lower().strip()
    if answer.startswith(negative): 
        print(c.red + "Well fine." + c.x)
        sys.exit()

assert_likes("waffles")
assert_likes("pancakes")
assert_likes("french toast")

print(c.clear + "♫ Doo, doo doo doot ♫")
call(["say","Doo, doo doo doot"])

print(c.clear + "♫ Can't wait to get a mouthful! ♫")
call(["say","Can't wait to get a mouthful!"])
```

## Extras

If you are running from a local Mac computer you can add these lines
to have your computer actually say the words:

```python
from subprocess import call
call(["say", "do you like " + food + "?"])
```

Have fun experimenting with other modifications but remember not to
get too crazy since this is your reference for these concepts later.
 
---
[![home](/assets/home-bw.png)](/README.md)
[![cc-by-sa](/assets/cc-by-sa.png)][cc-by-sa]
[![skilstak](/assets/skilstak-logo-bw.png)][skilstak]
[cc-by-sa]: https://creativecommons.org/licenses/by-sa/4.0/
[skilstak]: http://skilstak.io


