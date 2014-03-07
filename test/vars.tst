#!/bin/bash
# Test the var storage mechanism

# Set single variables
var-clear
var-set pipe-num 50
var-get pipe-num
var-list

# Create global list
var-save  <<EOF    

    scan_path=2014/CNE-Creative/02-19/20140219
    scan_path
    scan_pipeID =            89
    scan_scanID =            65
    scan_notes =             No notes
    scan_is_double =         true
    client_company =         Company Name
    equipment_truck =        Truck Name

EOF

# Test the JSON formatting
var-read | var-write $p/xxx
var-read $p/xxx | python -mjson.tool
rm $p/xxx

# Look for vars
var-list | grep pipeID
var-get scan_pipeID
var-set scan_pipeID 42
var-list | grep pipeID
