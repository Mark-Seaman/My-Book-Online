#!/bin/bash
# Format a document as HTML

# Test the mapping from URL to DOC
doc-file localhost:8052/Public
doc-file localhost:8052/Public/Index
doc-file localhost:8052/seaman
doc-file localhost:8052/seaman/Index
doc-file localhost:8052/Public/test/TestDoc

doc-file shrinking-world.org/Public
doc-file shrinking-world.org/Public/Index
doc-file shrinking-world.org/seaman
doc-file shrinking-world.org/seaman/Index
doc-file shrinking-world.org/Public/test/TestDoc

doc-file sxhrinking-world.org/Public
doc-file sxhrinking-world.org/Public/Index
doc-file sxhrinking-world.org/seaman
doc-file sxhrinking-world.org/seaman/Index
doc-file sxhrinking-world.org/Public/test/TestDoc

doc-file mybookonline.org/Public
doc-file mybookonline.org/Public/Index
doc-file mybookonline.org/seaman
doc-file mybookonline.org/seaman/Index
doc-file mybookonline.org/Public/test/TestDoc
