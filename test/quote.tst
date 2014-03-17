#!/bin/bash
# Select a quote from a file

doc-format < $pt/quote.txt | sed 's/[1-3]//'

