#!/bin/bash
# Format random content as HTML

# Run these to proof the output
echo  doc-random Public/SpiritualGrowth/Prayers
doc-random Public/SpiritualGrowth/Prayers | range 1 50

# Run these to proof the output
echo  doc-show ./Public/SpiritualGrowth/Prayers/Index
doc-show ./Public/SpiritualGrowth/Prayers/Index  | range 1 40
