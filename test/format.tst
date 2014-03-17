#!/bin/bash
# Test the format command to produce HTML

doc-format < /dev/null

doc-format <<EOF
* Test Page *
This is a test
Check out this output
**Bold text** and so much more
More plain text
 * Bullet **list** item 1
 * Bullet list item 2
 * *Italic bullet*
[[Home]]
[[book/Home]]
[[books][My books]]
http://thisandthat.com
EOF
