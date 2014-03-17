#!/bin/bash
# Format a document as HTML

mkdir -p $pd/Public $pd/test $pd/Public/test $p/logs  $p/logs/user 
touch $pd/Domains

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
doc-put Public/test/Index    < /tmp/t2
doc-put Public/test/TestDoc2 < /tmp/t2
page-redirect localhost:8052 Public test/TestDoc
page-put localhost:8052 Public test/TestDoc1 < /tmp/t1

echo 
echo 'Get files'
echo '------------------'
doc-get Public/test/Missing
doc-get Public/test/Index
doc-get Public/test/TestDoc1
doc-get Public/test/TestDoc2


# Show docs as HTML
echo 
echo 'Redirect to Index'
echo '------------------'
doc-show Public/test
page-redirect localhost:8052 Public test
page-show     localhost:8052 Public test

echo 
echo 'Index'
echo '------------------'
doc-show Public/test/Index
page-redirect localhost:8052 Public test/Index
page-show    localhost:8052 Public test/Index
page-get     localhost:8052 Public test/Index

echo 
echo 'Formatted output'
echo '------------------'
doc-show     Public/test/TestDoc1
doc-redirect Public/test/TestDoc1
page-show    localhost:8052 Public test/TestDoc1

echo 
echo 'Test missing file'
echo '------------------'
doc-show     Public/test/xxx
page-redirect localhost:8052 Public test/xxx
page-show    localhost:8052 Public test/xxx
page-get     localhost:8052 Public test/xxx

echo 
echo 'Private files'
echo '------------------'
page-put localhost:8052 test TestPrivateDoc1 < /tmp/t1
page-get localhost:8052 test TestPrivateDoc1

echo 
echo 'Public/Private files'
echo '---------------------'
page-put localhost:8052 test TestIndex   < /tmp/t2
page-put localhost:8052 Public TestIndex < /tmp/t1
page-get localhost:8052 test TestIndex 
#page-get localhost:8052/Public/TestIndex 


# Clean up after test
rm $pd/Public/test/*
