#!/bin/bash
# Select a quote from a file

hammer-wiki < $pt/quote.txt | sed 's/[1-3]//'

