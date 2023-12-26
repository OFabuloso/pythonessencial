#!/usr/bin/env
"""
Hello World Multi Language.
the LAng in use the ambient for developer "env"
the message is usual env language

usage:
have a LANG var config sucesffuly in your env
EX:

    export LANG=pt_BR
Execution:

    python3 hello.py
    or
    ./hello.py
"""
__version__ = "0.0.1"
__author__ = "OFabuloso"
 
import os 


# tem o shebang aprender mais sobre

current_language = os.getenv("LANG")[:5]
msg = "Hello, World"

if current_language == "pt_BR":
    msg = "E ae Zé Bunda"
elif current_language == "it_IT":
    msg = "la mafia del pizza"
else:
    msg = "E deu ruim"


print(msg)


