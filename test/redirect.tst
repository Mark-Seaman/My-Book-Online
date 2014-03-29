#!/bin/bash
# Format a document as HTML

mkdir -p $pd/test/xxx

# Test the doc redirection
doc-redirect ''
doc-redirect Index
doc-redirect test
doc-redirect test/xxx
doc-redirect test/yyy

# Test the automatic mapping to Index file for directories
echo 
echo 'directories:'
page-redirect localhost:8052 Public ''
page-redirect localhost:8052 seaman ''
page-redirect shrinking-world.org Public ''
page-redirect shrinking-world.org seaman ''
page-redirect sxhrinking-world.org Public ''
page-redirect sxhrinking-world.org seaman ''
page-redirect mybookonline.org Public ''
page-redirect mybookonline.org seaman ''

# Test the missing file detector
echo
echo 'missing:'
page-redirect localhost:8052 Public test/TestDoc
page-redirect shrinking-world.org test xxx
page-redirect shrinking-world.org Public test/TestDoc
page-redirect sxhrinking-world.org Public test/TestDoc
page-redirect mybookonline.org Public test/TestDoc

# Test the good files
echo
echo 'ok:'
page-redirect localhost:8052 Public Index
page-redirect localhost:8052 seaman Index
page-redirect shrinking-world.org Public Index
page-redirect shrinking-world.org seaman Index
page-redirect sxhrinking-world.org Public Index
page-redirect sxhrinking-world.org seaman Index
page-redirect mybookonline.org Public Index
page-redirect mybookonline.org seaman Index






