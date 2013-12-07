#!/bin/bash
# Format random content as HTML

# Run these to proof the output
echo  doc-random Public/SpiritualGrowth/Prayers
doc-random Public/SpiritualGrowth/Prayers | range 

# Run these to proof the output
echo  doc-show ./Public/SpiritualGrowth/Prayers/Index
doc-show ./Public/SpiritualGrowth/Prayers/Index  | range 
