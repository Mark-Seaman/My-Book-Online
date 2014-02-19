#!/bin/bash
# Put the doc in storage

doc-get test/TestDoc | filter-path

mkdir -p $pd/test
echo "My new doc" | doc-put test/TestDoc

doc-get test/TestDoc

rm  $pd/test/TestDoc
