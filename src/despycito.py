#!/usr/bin/python
# -*- coding: utf-8 -*-
# coding=utf-8
#
#Check out the code at https://github.com/campionfellin/despycito
#

from __future__ import print_function

import sys
import ast
import re

# These are the regular expressions that define the language.
k = {
    "boilerplate"   :   r"^#Despacito",
    "import"        :   r"feat (?P<libname>\w+?)\b",
    "def"           :   r"this is how we (?P<func_name>.*?) (?P<args>.*?)\n (?P<body>.*?)do it",
    "="             :   r"es (?P<left>\w*) (?P<right>.*)",
    "++"            :   r"sube (?P<value>\w*)",
    "loops"         :   r"pasito a pasito(?P<loop>.*?)otra",
    "break"         :   r"termina",
    "return"        :   r"favorito (?P<return>\w*?)",
    "print"         :   r"dime (?P<print>.+)",
    "true"          :   r"(?P<true>verdad)",
    "false"         :   r"(?P<false>falso)",
    "function"      :   r"(?P<function>\w+) despacito (?P<args>[\w ]*)\n",
}

def replace(p):

    subs = [
        (k["true"],     r"True"),
        (k["false"],    r"False"),
        (k["import"],   r"import \g<libname>"),
        (k["return"],   r"return \g<return>"),
        (k["="],        r"\g<left> = \g<right>"),
        (k["++"],       r"\g<value> = \g<value> + 1"),
        (k["function"], r"\g<function>(\g<args>)"),
        (k["print"],    r"print(\g<print>)"),
        (k["break"],    r"break"),
    ]

    for pattern, replacement in subs:
        p = re.sub(pattern, replacement, p)

        p = re.sub(k["loops"],  r"while True:\n \g<loop>", p, flags=re.DOTALL)
        p = re.sub(k["def"],    r"def \g<func_name>(\g<args>):\n \g<body>", p, flags=re.DOTALL)
    
    print(p)
    return p

def parse_v2(program):

    # check for boilerplate
    if not re.match(k["boilerplate"], program):
        raise SyntaxError("Otra vez. Empieza con #Despacito por fi")

    return ast.parse(replace(program))

def main():

    if len(sys.argv) < 2:
        raise IOError('''
            Otra vez. Pasame algo como it.o

            por ejemplo: de it.o
            ''')

    if (sys.argv[1] != "it.o"):
        raise IOError('''
            Otra vez. Pasame it.o

            ''')

    try: 
        f = open(sys.argv[1], 'r')
        program = f.read()
        exec(compile(parse_v2(program), filename="<despycito>", mode="exec")) 
    except IOError:
        print("Could not open {}. Otra vez.".format(sys.argv[1]))

if __name__ == '__main__':
  main()

