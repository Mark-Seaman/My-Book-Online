#!/bin/bash
# Show the doc from storage

doc-show
doc-show test/Index

mkdir -p test
echo "My new doc" > $pd/test/Index
doc-show test/Index
rm  $pd/test/Index
