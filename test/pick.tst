#!/bin/bash
# Pick some file content to insert into a page

mkdir -p $pd/Public/test

echo $pd/Public/test/Pick

cat <<EOF > $pd/Public/test/Pick
* Pick File *
This is a random content selector

[[PICK]]
EOF


doc-show ./Public/test/Pick

