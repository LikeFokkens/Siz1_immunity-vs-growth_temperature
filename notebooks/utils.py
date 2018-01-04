'''
Set of functions for selecting probes, mapping probeIDs to transcript ids etc., used in several notebooks
''' 


def select_probes(fname, qvalue_cutoff):
    '''Select probes that are differentially expressed. 
    Store them as integers for further analyses:
    pandas imports the column with probeIDs as intergers.
    Returns a set of integers that are the differentially expressed probeIDs.'''
    
    selection = set([])
    
    #fileheader:
    #probeset_id     transcript_id   logFC   AveExpr t       P.Value adj.P.Val       B       qvalues
    for line in open(fname).readlines()[1:]: #skip header
        data = line.strip().split('\t')
        if float(data[-1]) <= qvalue_cutoff:
            selection.add(int(data[0]))
            
    return selection




'''
#mapping from transcripts to probes (copied to 2.scatterplot_DEGs_mutant_vs_bkgr):
import glob
import pickle

def homogenize_geneID(string):
    return string.strip().upper().split('.')[0]


# make dict with transcript_id --> probeset_id mapping
def update_transcript2probe(fname, t2p, all_probes):
    lines = open(fname).readlines()[1:]
    for line in lines:
        #print line
        data        = line.strip().split('\t')
        probe       = int(data[0])
        transcripts = [homogenize_geneID(x) for x in data[1].split(';')]
        
        for t in transcripts:
            t2p[t] = probe
            all_probes.add(probe)
            
    return t2p, all_probes

dirnameStrains = 'data/reanalysisStrains/'
transcript2probe = {}
all_probes = set([])
for fname in glob.glob(dirnameStrains+'*_vs_*.txt'):
    transcript2probe, all_probes = update_transcript2probe(fname, transcript2probe, all_probes)
    print len(transcript2probe.keys())
    pickle.dump(transcript2probe, open('util/pickles/transcript2probes.pickled', 'w'))
    pickle.dump(all_probes, open('util/pickles/all_probes_set.pickled', 'w'))
'''