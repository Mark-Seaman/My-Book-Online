#!/bin/bash
# Test the var storage mechanism

var-clear
var-set pipe-num 50
var-get pipe-num
var-list


var-save  <<EOF    

    scan_path=2014/CNE-Creative/02-19/20140219
    scan_path
    scan_pipeID =            0
    scan_scanID =            0
    scan_notes =             No notes
    scan_is_double =         true
    scan_grade_1 =           0
    scan_grade_2 =           0

    calibration_scale_flaw = 50
    calibration_scale_wall = -80
    calibration_good =       2014/CNE-Creative/02-19/20140219
    calibration_bad =        2014/CNE-Creative/02-19/20140219
    calibration_badness =    36

    client_company =         Company Name
    client_invoice =         Invoice Name
    client_well =            Well name
    client_on_location =     2013-12-25
    client_start =           2013-12-25
    client_end =             2013-12-25

    equipment_truck =        Truck Name
    equipment_operator =     Operator Name
    equipment_hand =         Hand Name
    equipment_shoe =         12345
    equipment_stack =        12345
    equipment_tube =         12345
    equipment_computer =     12345

    pipe_grade_yellow =      15
    pipe_grade_blue =        30
    pipe_grade_green =       50 

    pipe_is_pitting =        true
    pipe_size =              2 3/8
    pipe_type =              unknown
    pipe_weight =            42

EOF


var-read | var-write

var-list

vars-show
vars-edit
