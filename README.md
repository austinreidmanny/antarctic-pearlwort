# nibert-lab
Code written for research in the laboratory of Max Nibert, MD, PhD at Harvard.

For the work on Antarctic pearlwort (Colobanthus quitensis):

Citation: Nibert ML, Manny AR, Debat HJ, Firth AE, Bertini L, Caruso C. (2018). A barnavirus sequence mined from a transcriptome of the Antarctic pearlwort Colobanthus quitensis. Archives of Virol. doi: 10.1007/s00705-018-3794-x. PMID: 29516246.

To assess the extent of fungal reads in the C. quitensis transcriptome, Diamond was run to assign a taxon ID for each contig.

These taxon IDs were then run on the Joint Genome Institute's taxonomy platform (https://taxonomy.jgi-psf.org) in order to transfrom the taxon ID into a full lineage readout. These phylogenies were analyzed manually to evaluate the proportion of transcriptome belonging to various taxa.

Code layout:
`pipeline.sh` is a two-step script that first runs Diamond on the C. quitensis transcriptome (`launchDiamond.sh`), followed by taxonID deconstruction (`getTaxonomyDiamond.py`).

Running the code:
With Diamond installed and its dependencies gathered (see Diamond manual for full requirements when involving taxnomic analysis), simply run `./pipeline.sh`.
