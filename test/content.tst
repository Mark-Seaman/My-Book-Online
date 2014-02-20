#!/bin/bash
# Format a document as HTML

# Create test files
cat <<EOF > /tmp/t1
* Test Document *

This is a test.

EOF
cat <<EOF > /tmp/t2
* Test User Home *
This is a test page for the test user.

**Tab 1**
 This is some text

**Tab 2**

This is some more text
EOF

echo 
echo 'Create files'
echo '------------------'
doc-put Public/test/Index < /tmp/t2
doc-put Public/test/TestDoc1 < /tmp/t1
doc-put Public/test/TestDoc2 < /tmp/t2


# Show docs as HTML
echo 
echo 'Redirect to Index'
echo '------------------'
doc-show localhost:8052/Public/test

echo 
echo 'Index'
echo '------------------'
doc-show localhost:8052/Public/test/Index

echo 
echo 'Formatted output'
echo '------------------'
doc-show localhost:8052/Public/test/TestDoc1

echo 
echo 'Test missing file'
echo '------------------'
doc-show localhost:8052/Public/test/xxx

# Clean up after test
rm $pd/Public/test/*
