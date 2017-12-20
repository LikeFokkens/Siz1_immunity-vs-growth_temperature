### Contents

**README.md**. 
Description of repository

  
**data**  
The files as provided by Martijs Jonker: INPUT for the notebooks  

**data/design.txt**  
design of the microarray: which cells belong to which mutant   

**data/rmadata.txt**  
Average expression values per gene, per cell

**data/reanalysisTime/**  
log2-transformed expression ratio's: same strain compared accross different timepoints. Adjusted (for multiple testing) P-values < 0.01 are considered differentially expressed.

**data/reanalysisStrains/**  
log2-transformed expression ratio's: per timepoint comparison of the two double-mutant strains against the pad4 backrgound. Adjusted (for multiple testing) P-values < 0.01 are considered differentially expressed.


**gene_lists**
We intersect differentially expressed genes with genes that are under control of transcription factors PIF4, BZR1, ARF6 and Hy5. We also look at SAUR genes, known to be involved in growth.

  
**notebooks**
Contains the notebooks (code and comments) that were used to analyze the data. They were changed a bit to allow you to download this repository and reproduce the figures out of the box, the original notebooks contained local paths to files, etc. We've also added a few extra comments in the code to make it easier to understand. We removed a few spurious analyses that were just extra confirmations or visualizations that did not make it into the paper. 

Notebooks also contain lines of reasoning etc., to enhance communication between a bioinformatician that is not deeply into the subject (Like Fokkens) and the PI that is (Harrold van den Burg). 


**pickles**
Contains pickled Python objects generated and reused in the notebooks.   


**results**
Plots are shown in the notebook, but also saved in different file-formats in this directory. These files were imported in Adobe Illustrator to make the Figures as they appear in the paper.



