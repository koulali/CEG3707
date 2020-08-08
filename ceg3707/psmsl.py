import numpy as np
import pandas as pd
import os

def load_rlr(tgid):
    '''
    Read PSMSL RLR data files into a dataframe

    Args:
        * tgid  : tide guage id
    '''
    DATA_DIR = os.path.join(os.path.dirname(__file__), '..')     
    tgfile = os.path.join(DATA_DIR,'./data/'+tgid+'.rlrdata')

    df = pd.read_csv(tgfile, header=None, sep=";",na_values=-99999,
                   index_col='decyr', names=['decyr', 'msl', 'nmd', 'flag'])
    
    # remove missing data
    df = df.dropna()
    
    return df


