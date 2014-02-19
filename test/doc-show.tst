#!/bin/bash
# Show the doc from storage

# Usage error
doc-show

# Create test file
mkdir -p $pd/test
echo "My new doc" > $pd/test/Index
doc-show test/Index

# Remove test file
rm -r $pd/test

# Missing file
doc-show test/Index | filter-path
