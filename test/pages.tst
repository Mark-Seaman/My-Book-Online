#!/bin/bash
# Get pages from the remote web server

cd $pt/pages

# Remove old results
rm *.out

# Get new pages
page-grab  < $pt/page_list

# Loop over all of the tests
for f in *.diff
do 
    [ -s "$f" ]                                                 &&
    lc $f
done

