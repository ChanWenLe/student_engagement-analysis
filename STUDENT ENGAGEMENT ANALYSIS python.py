# Import relevant libraries
import re
import pandas as pd
import pymysql
from sqlalchemy import create_engine

# -- set up regular expressions patterns ----
INIT_regex = re.compile(r'^WEBVTT\s*$')
SNo_regex = re.compile(r'^(\d+)\s*$')
Time_regex= re.compile(r'^(\d{2}:\d{2}:\d{2}\.\d{3}) --> (\d{2}:\d{2}:\d{2}\.\d{3})\s*$')
NameUtt_regex = re.compile(r'^([^:]+):\s?(.*)$')
UttOnly_regex = re.compile(r'^([^:]+)$')

# -- read in vtt file ---- 
vttpath = 'captured_dialogue.vtt'
vtt = open(vttpath)
all_lines = vtt.readlines()
vtt.close()

# -- create an empty DataFrame with five columns ----
colnames = ['SNo','TimeFrom','TimeTo','RegName','Utterance']
df = pd.DataFrame(columns=colnames)

lookingFor = 'INIT'

for i, current_line in enumerate(all_lines):
    if lookingFor == 'INIT':
        mo = INIT_regex.search(current_line)
        if mo!= None:
            lookingFor = 'SNo'
    elif lookingFor == 'SNo':
        mo = SNo_regex.match(current_line)
        if mo:
            SNo = mo.group(1)
            lookingFor = 'Time'
    elif lookingFor == 'Time':
        mo = Time_regex.match(current_line)
        if mo:
            TimeFrom = mo.group(1)
            TimeTo = mo.group(2)
            lookingFor = 'NameUtt_or_UttOnly'
    elif lookingFor == 'NameUtt_or_UttOnly':
        mo_nameutt = NameUtt_regex.match(current_line)
        mo_utt_only = UttOnly_regex.match(current_line)
        if mo_nameutt:
            RegName = mo_nameutt.group(1)
            Utterance = mo_nameutt.group(2)
            df.loc[len(df)] = [SNo, TimeFrom, TimeTo, RegName, Utterance]
            lookingFor = 'SNo'
        elif mo_utt_only:
            RegName = None  # Assign None or a default speaker name
            Utterance = mo_utt_only.group(1)
            df.loc[len(df)] = [SNo, TimeFrom, TimeTo, RegName, Utterance]
            lookingFor = 'SNo'



print(df)


from sqlalchemy import create_engine
engine = create_engine('mysql+pymysql://root:111111@localhost/anl503')


df.to_sql('vtt', con=engine,  index=False,if_exists='replace')

