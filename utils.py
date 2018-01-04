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
            selection.add(int(data[0]))  # convert probes to integers for cross-compatibility with a file read by pandas:
                                         # pandas automatically converts the probeID column to integers
            
    return selection


# make dict with probeset_id --> transcript_id mapping
def probe2transcripts(fname):
    ''' Map probeIDs to transcript IDs, returns a dictionary'''
    p2t   = {}
    lines = open(fname).readlines()[1:]
    for line in lines:
        data        = line.strip().split('\t')
        probe       = int(data[0])
        transcripts = data[1].split(';')

        p2t[probe] = transcripts
        
    if not len(p2t.keys()) == len(lines):
        print 'WARNING: keys in probe2transcript dict is not the number of lines in the file'
    
    return p2t


def homogenize_geneID(string):
    ''' The arabidopsis gene IDs are written in different formats, 
    e.g. At12345 and AT12345 or At12345.1 and At12345. This function homogenizes different formats, 
    to allow mapping between different gene lists
    '''
    return string.strip().upper().split('.')[0]


# make dict with transcript_id --> probeset_id mapping
def update_transcript2probe(fname, t2p, all_probes):
    ''' Map probeIDs to transcript IDs, returns an updated dictionary'''
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


