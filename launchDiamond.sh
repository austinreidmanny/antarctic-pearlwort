#!/bin/bash

# Runs DIAMOND using the whole NR database, with your input file as query.
# 10 JAN 2018

################################################################################################################
# CUSTOMIZE THIS SECTION, CHANGING THE NAMES ON THE RIGHT SIDE OF THE EQUAL SIGN, BUT LEAVE THE QUOTATION MARKS 
# FOR TIPS, LOOKS AT THE "NOTES" SECTION BELOW

PATH_TO_DATABASE="nr"        # leave the nr, change the directories. example: "~/Desktop/nr"
PATH_TO_QUERY_FILE="c_quitensis_transcriptome.fasta"   # example: "~/Desktop/input_query.fasta"
OUTPUT_FILE="diamond_results.txt"
PATH_TO_TAXONMAP="prot.accession2taxid.gz"
PATH_TO_TAXON_NODES="nodes.dmp"
E_VALUE="10"
BLOCK_SIZE="1.7"

#################################################################################################################

# NOTES:
# To run DIAMOND in taxonomy mode, you will need the following:
# 1. DIAMOND database file
# 2. Query file, as a FASTA
# 3. Taxon Map file, from NCBI.
# 4. Taxon Nodes file, from NCBI

# TO MAKE IT EASIER: you can place all of those files in the same folder and launch this program from that folder.
# Example: Place all of these files on the desktop. Change current directory (with Terminal command 'cd') to '~/Desktop/'.
#          Then replace all 'path/to/___' with './' That notation means current directory.

# Details on parameters used here:
# --sensitive is best used for transcriptome contigs and/or long reads. If using short reads (like Illumina) erase this parameter.
# --top 0 ensures that only sequences that are identical to the best match will be factored into the Lowest Common Ancestor algorithm .
# RAM usage: --block-size determines RAM usage. DIAMOND will fail if it runs out of RAM. The block-size used here should run with 8 GB RAM.
# If DIAMOND fails because of insufficient memory, change to --block-size 1.5    or lower.

date > diamond.log
diamond blastx --sensitive -d $PATH_TO_DATABASE -q $PATH_TO_QUERY_FILE -o $OUTPUT_FILE -f 102 --taxonmap $PATH_TO_TAXONMAP \
--taxonnodes $PATH_TO_TAXON_NODES --max-target-seqs 1 --max-hsps 1 --top 0 --block-size $BLOCK_SIZE -e $E_VALUE
date >> diamond.log
