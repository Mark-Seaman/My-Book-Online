#!/bin/bash
# Test the doc-show command

# Page without domains
doc-show
doc-show path
doc-show domain/user/app/dir/file


# Public pages
doc-show localhost:8054/Anonymous
doc-show localhost:8054/Anonymous/Brain/Index

doc-show shrinking-world.org/Anonymous
doc-show shrinking-world.org/Anonymous/app/dir/file

doc-show exteriorbrain.com/Anonymous
doc-show exteriorbrain.com/Anonymous/Index


# Private pages
doc-show localhost:8054/user
doc-show localhost:8054/user/Brain/Index

doc-show shrinking-world.org/user
doc-show shrinking-world.org/user/app/dir/file

doc-show exteriorbrain.com/user
doc-show exteriorbrain.com/user/Index

# Selective execution
cat <<EOF >/dev/null
EOF

