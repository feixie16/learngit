#coding = utf-8
import pandas as pd

df = pd.read_csv('/Users/xiefei/Desktop/reject_reason', sep= '\t')
df['hit_name'] = df['hit_name'].apply(lambda x : x[len(x-3),len(x)-1])

a = df.groupby(['hit_name'])['user_id'].nunique().reset_index()
print a

def getZmscore(x):
    para = str(x)
    if len(para) > 3:
        score = para[]


