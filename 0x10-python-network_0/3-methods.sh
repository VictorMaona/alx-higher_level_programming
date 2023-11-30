#!/bin/bash
# displays all HTTP methods that server will accept after receiving URL.
curl -Is "$1" | grep "Allow:" | cut -d ":" -f 2 | cut -c 2- | rev | cut -c 2- | rev
