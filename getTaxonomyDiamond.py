#!/usr/bin/env python3

# 9 JAN 2018 #

########################################################################################
# NOTE: THIS HAS BEEN MODIFIED TO WORK WITH DIAMOND OUTPUT FORMAT 102 (taxonomy mode). #
# FOR BLASTn TAXONOMY ASSIGNMENT, USE THE SCRIPT CALLED 'getTaxonomyBLASTn.py'         #
########################################################################################

##############################################################################
# USING THIS PROGRAM                                                         #
##############################################################################
# Place this script in the same folder as the file with the Diamond results. #
# Then simply type 'python getTaxonomyDiamond.py DIAMOND_OUTPUT_FILE.txt'    #
#                                                                            #
# The results of this program will be written to a tab-delimited text file   #
# with the same name as the input file, except prefixed with 'taxonomy_'.    #
# So if the input file were named 'diamond_output.txt' the output of this    # 
# program would be 'taxonomy_diamond_output.txt'.                            #
##############################################################################


# This program will take a tab delimited file with the following columns:
# sequence_name	taxon_id e-value

# The output will be a tab-delimited file with the following format
# sequence_name  e-value  superkindom  kingdom  phylum class order  family genus species  taxon_id

# I am going to use the Joint Genome Institute Taxonomy platform obtain taxonomy information for each
# DIAMOND hit.

# Using the url 'http://taxonomy.jgi-psf.org/sc/simple/id/<taxon_id>' I will get the taxonomy
# information in the following format:
#
# 'sk:$superkingdom;k:$kingdom;p:$phylum;o:$order;f:$family;g:$genus;s:$species'

import sys
import os
import requests

# Make sure the program is called correctly
if len(sys.argv) < 2:
	print("Usage: %s %s" % (sys.argv[0], fileWithTaxonIDs.txt))
	exit(1)

# Initialize the inputs and outputs.
inf = sys.argv[1]
#outf = "taxonomy_" + inf
outf = inf.split(".")[-2] + "_taxonomy" + inf.split(".")[-1]   # If I put 'taxonomy_' in front of the input file name,
                                                               # then the program would break if the input file is in diff directory

output = open(outf, 'w')	# The output is invoked this way so if the program fails, you will still get a results file.

# Write a header  line, detailing what each column is.
output.write('#query_name' + '\t' + 'e_value' + '\t' + 'superkindgom' + '\t' + 'kingdom' + '\t' +\
             'phylum' + '\t' + 'class' + '\t' + 'order' + '\t' + 'family' + '\t' + 'genus' + '\t' +\
             'species' + '\t' + 'taxon_id#' + '\n')

# Open the DIAMOND results file, read each line (representing one sequence/hit) and retrieve the taxonomical information from JGI.
with open(inf, "r") as input:
	for line in input:
		line = line.strip()
		if not line:
			pass

		# For each sequence, split it into an array and name each item
		array = line.split("\t")
		query_name = array[0]
		taxon_id = array[1]
		e_value = array[2]

		# Take the TaxonID and query it against the JGI-PSF taxonomy database
		url = 'http://taxonomy.jgi-psf.org/sc/simple/id/' + taxon_id
		t = requests.get(url)
		taxonomy = str(t.text)

		# Split the taxonomy result by rank
		tax = {}
		tax_array = taxonomy.split(";")
		for pair in tax_array:		# pair would be like " 'superkindgdom':'bacteria' "
			rank = pair.split(":")
			level = rank[0]		# level would be 'superkingdom'
			try:
				taxon = rank[1]	# if there's an entry for superkingdom, taxon would be 'bacteria'
			except:
				taxon = 'N/A'
			tax[level] = taxon	# add this taxonomic level to the taxonomy dictionary object

		# Try to assign a taxon for each taxonomical rank. If there isn't an entry for that rank, write "N/A" and move on.
		try:
			superkingdom = tax['sk']
		except:
			superkingdom = 'N/A'
		
		try:
			kingdom = tax['k']
		except:
			kingdom = 'N/A'
		
		try:
			phylum = tax['p']
		except:
			phylum = 'N/A'

		try:
			clas = tax['c']
		except:
			clas = 'N/A'

		try:
			order = tax['o']
		except:
			order = 'N/A'

		try:
			family = tax['f']
		except:
			family = 'N/A'

		try:
			genus = tax['g']
		except:
			genus = 'N/A'

		try:
			species = tax['s']
		except:
			species = 'N/A'

		# Write the results to the output file
		output.write(query_name + '\t')
		output.write(e_value + '\t')
		output.write(superkingdom + '\t')
		output.write(kingdom + '\t')
		output.write(phylum + '\t')
		output.write(clas + '\t')
		output.write(order + '\t')
		output.write(family + '\t')
		output.write(genus + '\t')
		output.write(species + '\t')
		output.write(taxon_id + '\n')
	
		print('wrote taxonomy for %s' % query_name)
output.close()
