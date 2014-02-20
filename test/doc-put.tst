#!/bin/bash
# Put the doc in storage

# Look for a missing file
doc-get test/TestDoc | filter-path


# Create two test files

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

doc-put test/TestDoc < /tmp/t2
doc-get test/TestDoc

echo "My new doc" | doc-put test/TestDoc

doc-put Public/test/TestDoc1 < /tmp/t1
doc-put Public/test/TestDoc2 < /tmp/t2


# Display the test files
doc-show localhost:8052/Public/test/TestDoc1
doc-show localhost:8052/Public/test/TestDoc2


# Clean up
rm  $pd/test/TestDoc
rm $pd/Public/test/TestDoc*


