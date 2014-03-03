#!/bin/bash
# Include document text

# Create a test doc
cat<<EOF | doc-put test/Include
* Include Tester *

[[INCLUDE:Included]]
[[INCLUDE:Included]]
[[INCLUDE:Included]]
[[INCLUDE:Included]]
EOF

cat<<EOF | doc-put test/Included
* Included File *
Four score and seven
years ago...

EOF


# Show the formatted test doc
doc-show test/Include

# Remove the test doc
rm $pd/test/Include*

