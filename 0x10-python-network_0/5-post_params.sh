#!/bin/bash
#POST request to the passed URL and display body of response
curl -s -X POST -d "subject=I will always be here for PLD&email=test@gmail.com" "$1"
