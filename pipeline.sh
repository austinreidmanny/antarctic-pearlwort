#!/bin/bash

# Complete pipeline for discovering taxonomy classification from transcriptome contigs or raw sequencing reads.
# 10 JAN 2018 

#############################################################################################################
# Before beginning, customize the settings in "./launchDiamond.sh"
# Also, ensure that the name of the DIAMOND results file is the same there as it is on the single line below.

DIAMOND_RESULTS_FILE = "./diamond_results.txt"
#############################################################################################################

./launchDiamond.sh
./getTaxonomyDiamond.py $DIAMOND_RESULTS_FILE
