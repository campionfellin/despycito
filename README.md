`#DesPYcito`

Check it out! DesPYcito is based on Python, but using lyrics from the song Despacito by Luis Fonsi

## Hola Todas
```
dime "Hola Todas"
```

## FizzBuzz

```
this is how we fizzbuzz n

  es i 0

  pasito a pasito
    if i % 3 == 0 & i % 5 == 0:
      dime "FizzBuzz"
    elif i % 3 == 0:
      dime "Fizz"
    elif i % 5 == 0:
      dime "Buzz"
    else:
      dime i

    if i >= n:
      termina

    sube i
    otra

  favorito verdad
do it
```

## How to run:

You have to add an alias for it to work.
```
alias de="PATH_TO_DIRECTORY/bin/despycito"
```

When you run the program you must type:

```
de it.o
```

Thus, whatever file you make must be named 'it.o'

## Name
This language is called desPYcito because it's the slow way to write Python (also it's a dope song).

## Syntax

#### Boilerplate
All desPYcito programs must begin with the following comment:

```
#Despacito
```

#### Built-in types
desPYcito supports integers, floats, and strings. Booleans are `verdad` (true) and `falso` (false).

desPYcito accepts all standard operators, `+`, `-`, `*`, `\`, `%`, `**`, etc. (It's basically python)

```
69
verdad
"hola"
```

#### Printing
To print a value, say: dime "hola"

```
dime 69
dime "hola"
```


#### Assigning variables
desPYcito uses the following notation for assigning variable values:

```
es x 1
```

This essentially assigns 1 to x, like `x = 1`

You can also use "sube" to add 1 to a value, like this:

```
sube x
```
which roughly translates to `x = x + 1`

#### Functions
Function definitions begin with `this is how we [name] [args]` and are closed with `do it`. To specify the return value, use `favorito [optional value]`. desPYcito does not yet support anonymous functions.

Examples are included in the /examples directory.

#### Loops
To make a loop, start it with: pasito a pasito and end it with: otra
```
pasito a pasito
  ...
otra
```

####
To make a loop go slowly (despacito), you can do this:

```
feat time
pasito a pasito
   ...
   despacito 1
otra
```
This will slow down each loop by 1 second. Make sure you feat time before using despacito to slow it down

#### Breaks
To exit a loop use the command `termina`. Thus we can write a while loop as follows:

```
pasito a pasito
	[...]
	if [condition]:
		termina
otra
```

#### Importing modules
You can access other Python libraries by featuring them on the track using: `feat [libname]`.

## Author

Campion Fellin. Shoutout to https://github.com/rrshaban/keyplusplus for the inspiration
