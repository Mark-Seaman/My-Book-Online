#!/bin/bash
# Add script execution to widgets

# Create a test doc
cat<<EOF | doc-put test/Script
* Include Tester *

[[SCRIPT:today]]

EOF


# Show the formatted test doc
doc-show test/Script

# Remove the test doc
rm $pd/test/Script

