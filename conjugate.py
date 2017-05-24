#!/usr/local/bin/python
import requests

import sys

if len(sys.argv) == 1:
    print "conjugate v0.02"
    print "utilizes ultralingua's rest api. written by tejasprak"
    print "Usage: conjugate [pronoun] [verb]"
    print "Example: conjugate je ouvrir"
    sys.exit();
pronoun = sys.argv[1]
verb = sys.argv[2]

if pronoun == "je":
    person = "firstsingular"
elif pronoun == "tu":
    person = "secondsingular"
elif pronoun == "il":
    person = "thirdsingular"
elif pronoun == "elle":
    person = "thirdsingular"
elif pronoun == "on":
    person = "thirdsingular"
elif pronoun == "nous":
    person = "firstplural"
elif pronoun == "vous":
    person = "secondplural"
elif pronoun == "ils":
    person = "thirdplural"
elif pronoun == "elles":
    person = "thirdplural"
else:
    print "Invalid argument."
    sys.exit()

response = requests.get("http://api.ultralingua.com/api/conjugations/french/" + verb + "?tense=present&person=" + person)
print response.json()["surfaceform"]
