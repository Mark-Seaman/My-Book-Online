#!/bin/bash
# Format a document as HTML

# Test the mapping from URL to DOC
page-redirect localhost:8052/Public
page-redirect localhost:8052/Public/Index
page-redirect localhost:8052/seaman
page-redirect localhost:8052/seaman/Index
page-redirect localhost:8052/Public/test/TestDoc

page-redirect shrinking-world.org/Public
page-redirect shrinking-world.org/Public/Index
page-redirect shrinking-world.org/seaman
page-redirect shrinking-world.org/seaman/Index
page-redirect shrinking-world.org/Public/test/TestDoc

page-redirect sxhrinking-world.org/Public
page-redirect sxhrinking-world.org/Public/Index
page-redirect sxhrinking-world.org/seaman
page-redirect sxhrinking-world.org/seaman/Index
page-redirect sxhrinking-world.org/Public/test/TestDoc

page-redirect mybookonline.org/Public
page-redirect mybookonline.org/Public/Index
page-redirect mybookonline.org/seaman
page-redirect mybookonline.org/seaman/Index
page-redirect mybookonline.org/Public/test/TestDoc

