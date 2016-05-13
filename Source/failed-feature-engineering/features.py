import numpy as np
import pandas as pd

h = open('kc.txt','w')

def main():
    file_name = input('file name: ')
    df = None
    if file_name[-4:] == '.txt':
        df = pd.read_csv(file_name, sep='\t')
    else:
        df = pd.read_csv(file_name)


    print('Cleaning up NaN fields...')
    df['Correct Step Duration (sec)'] = df['Correct Step Duration (sec)'].replace(np.nan, 0)
    df['Error Step Duration (sec)'] = df['Error Step Duration (sec)'].replace(np.nan, 0)
    df['KC(Default)'] = df['KC(Default)'].replace(np.nan, '')
    df['Opportunity(Default)'] = df['Opportunity(Default)'].replace(np.nan, '')
    df = df.replace(np.nan, 0)  # any NaN's missed will now be 0

    # feature engineering: transforming KC(Default) to a cleaner string
    print("KC feature string transformation...")
    kc_label = 'KC(Default)'
    kc_new_label = 'KC(Simple)'
    kc_simple = pd.DataFrame(columns=[kc_new_label])
    for i, kc in enumerate(df[kc_label].iteritems()):
        #kc[0] is index, kc[1] is value
        start = kc[1].find(':')
        if start != -1:
            start += 2
            end = kc[1].find(';', start)
            if end == -1:
                kc_simple.loc[i] = kc[1][start:]
            else:
                kc_simple.loc[i] = kc[1][start:end]
        else:
            kc_simple.loc[i] = kc[1]

        df[kc_new_label] = kc_simple[kc_new_label]
    
    # build map of KC strings to unique int IDs
    print("Build dictionary of KC strings to int IDs...")
    kcmap = dict()
    for kc in df[kc_new_label].iteritems():
        if kc[1] not in kcmap:
            kcID = np.random.random() # [0.0, 1.0)
            while kcID in kcmap.values():
                kcID = np.random.random()
            kcmap[kc[1]] = kcID
        o = str(kc) + '\n'
        h.write(o)        
            
    
    
'''
    # build column of kcIDs for dataframe
    print("Build kcIDs data frame...")
    kcIDlabel = 'KC(IDs)'
    kc_ids = pd.DataFrame(columns=[kcIDlabel])
    for i, kc in enumerate(df[kc_new_label].iteritems()):
        kc_ids.loc[i] = kcmap[kc[1]]

    print("Append kcIDs to original data frame...")
    df[kcIDlabel] = kc_ids

    print("KC feature engineering complete.")


    # separating Problem Hierarchy into UNIT and SECTION
    print("Splitting problem hierarchy string into Unit and Section strings")
    ph_label = 'Problem Hierarchy'
    u_label = 'Hierarchy Unit'
    s_label = 'Hierarchy Section'
    new_frame = pd.DataFrame(columns=[u_label, s_label])
    for i, ph in enumerate(df[ph_label].iteritems()):
        arr = ph[1].split(', ')
        new_frame.loc[i] = arr

    print("Appending Unit and Section string columns to original data frame")
    df[u_label] = new_frame[u_label]
    df[s_label] = new_frame[s_label]

    # build map of UNIT/SECTION strings to unique int IDs
    print("Build dictionary of UNIT strings to int IDs...")
    umap = dict()
    for u in df[u_label].iteritems():
        if u[1] not in umap:
            uID = np.random.random() # [0.0, 1.0)
            while uID in umap.values():
                uID = np.random.random()
            umap[u[1]] = uID

    print("Build dictionary of SECTION strings to int IDs...")
    smap = dict()
    for s in df[s_label].iteritems():
        if s[1] not in smap:
            sID = np.random.random() # [0.0, 1.0)
            while sID in smap.values():
                sID = np.random.random()
            smap[s[1]] = sID

    # build columns of uIDs/sIDs for dataframe
    print("Build uIDs/sIDs data frame...")
    uIDlabel = 'Unit(IDs)'
    sIDlabel = 'Section(IDs)'
    u_ids = pd.DataFrame(columns=[uIDlabel])
    s_ids = pd.DataFrame(columns=[sIDlabel])
    for i, u in enumerate(df[u_label].iteritems()):
        u_ids.loc[i] = umap[u[1]]
    for i, s in enumerate(df[s_label].iteritems()):
        s_ids.loc[i] = smap[s[1]]

    df[uIDlabel] = u_ids[uIDlabel]
    df[sIDlabel] = s_ids[sIDlabel]

    print("outputting dataframe to file: features_output.csv")
    df.to_csv("features_output.csv", index=False)
'''
if __name__ == '__main__':
    main()
