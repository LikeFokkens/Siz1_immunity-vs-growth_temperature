### Description

This repository contain the datafiles and notebooks that were used in analizing microarray data described in [URL PLoS] and create Figure 4.

Here we aimed to study the role of SUMO-signalling in thermomorphogenesis (= how growth/shape changes in response to the temperature). Both growth and immunity are affected by temperature changes. To disentangle these two processes we subjected a _pad4_ mutant (an _Arabidopsis_ line in which the gene _PAD4_, a key regulator of the immune response to temperature changes, was knocked out/knocked down) to temperature changes. We grew this line at 22 °C, and switched to 28 °C. We measured gene expression at three time points: T0 (at the temperature switch), T1 (24 after after the temperature switch) and T2 (48 hours after the temperature switch). Additionally, we used two double-mutant lines in which not only PAD4 was knocked out, but also _SIZ1_ (_siz1 pad4_), and a double knockdown of SUMO1 and SUMO2 (_1xB pad4_). Martijs Jonker determined expression levels at different timepoints and determined overexpression in time (within the same mutant, compared one time point to the other and see which genes are differentially expressed, files are in **data/reanalysisTime**) and in different mutants (in one timepoint, compared the double mutants to the single mutant: _siz1 pad4_ to _pad4_ and _1xB pad4_ to _pad4_, files are in **data/reanalysisStrains**).

In **notebooks**, we put the code that we used to analyze (differences in) expression levels for differentially expressed genes in Jupyter notebooks. By running these notebooks, you should be able to reproduce the results we presented in the paper easily.

The notebooks are in Python2 (Python 2.7.13 to be exact), we used the Anaconda2 4.3.0 distribution. To draw Venn-diagrams we used matplotlib_venn, that can be installed via easy_install or pip (https://pypi.python.org/pypi/matplotlib-venn/). We used version 0.11.4.

___
The goal of this repository is open science, so if you have any comments (bugs, bad practices, ommissions, things that are not clearly explained, positive feedback), please make an issue and we'll look at it (and learn from it). **This is very much appreciated!**
___


Description of files is in Contents.md.

