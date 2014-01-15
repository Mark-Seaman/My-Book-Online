#!/bin/bash
# Setup the bashrc environment

# If not running interactively, don't do anything
[ -z "$PS1" ] && return
echo 'Running bashrc'

# Enable the bash prompt 
[ -f ~/bin/bash-prompt ] && . ~/bin/bash-prompt

# Enable the bash shell completion
[ -f /etc/bash_completion ] && . /etc/bash_completion

# Alias definitions.
[ -f ~/bin/bash-alias ] && . ~/bin/bash-alias

# Load the project vars
[ 'web126.webfaction.com' == `hostname` ] && return

. bin/project
