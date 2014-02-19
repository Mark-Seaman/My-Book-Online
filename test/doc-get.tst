#!/bin/bash
# Get the doc from storage


doc-get
doc-get test/TestDoc | filter-path

mkdir -p $pd/test
echo "My new doc" > $pd/test/TestDoc

doc-get test/TestDoc

rm  $pd/test/TestDoc
