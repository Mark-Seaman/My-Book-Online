#!/bin/bash
# Setup the bashrc environment


# If not running interactively, don't do anything
[ -z "$PS1" ] && return


# Enable the bash prompt 
[ -f ~/bin/bash-prompt ] && . ~/bin/bash-prompt

# Enable the bash shell completion
[ -f /etc/bash_completion ] && . /etc/bash_completion

# Load the project context
[ -f bin/bash-alias ] && . bin/bash-alias
[ -f bin/project    ] && . bin/project
