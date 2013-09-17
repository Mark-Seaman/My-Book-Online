#!/bin/bash
# Setup the bash environment for new shell

# If not running interactively, don't do anything
[ -z "$PS1" ] && return

# Start in home directory
cd

# Update the rc files
bin/rc

# Enable the bash prompt 
if [ -f ~/bin/bash-prompt ]; then
    . ~/bin/bash-prompt
fi

# Enable the bash shell completion
if [ -f /etc/bash_completion ]; then
    . /etc/bash_completion
fi

# Variables
if [ -f ~/bin/bash-vars ]; then
    . ~/bin/bash-vars
fi

# Alias definitions.
if [ -f ~/bin/bash-alias ]; then
    . ~/bin/bash-alias
fi

# Web faction
if [ `hostname` == 'web126.webfaction.com' ]; then
	PS1='${debian_chroot:+($debian_chroot)}\u@\h:\w\$ ' 
    export PATH=/home/seaman/webapps/mybook:/home/seaman/webapps/mybook/lib/python2.6:$PATH
    alias ls='ls'
    alias grep='grep'
    cd webapps/mybook
    ls
fi

# Mill Server
if [ `hostname` == 'millserver' ]; then
	PS1='${debian_chroot:+($debian_chroot)}\u@\h:\w\$ ' 
    alias ls='ls'
    alias grep='grep'
fi

# Mill Server
if [ `id -un` == 'mill' ]; then
    cd git
    export PATH=~/git/support:~/git/scripts:$PATH
fi

# Give a short life lesson
[[ -x ~/bin/life-lesson ]] && life-lesson


### Added by the Heroku Toolbelt
#export PATH="/usr/local/heroku/bin:$PATH"
