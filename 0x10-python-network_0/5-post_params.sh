#!/bin/bash
# script that shows body of response after sending POST request
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
