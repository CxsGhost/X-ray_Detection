#%%

import pandas as pd
import re

#%%

data = pd.read_csv('./workdata.txt', sep='\t', header=None, index_col=None)
col = 'province:String, city:String, code:String, acc_number:String, tel:String, date:String, rep_disoe:Int, overtime:Int, receipt:Int, descr:String, exp_empid:String, fault_1:String, fault_2:String, fault_type:String, acs_way:String, address:String'
col = col.replace(',','')
col = col.split(' ')
col = list(map(lambda x: x[:x.find(':')], col))
print(col)
#%%
data = data.drop(columns=[16])
data.columns = col
print(data)
#%%
data = data[['province', 'date', 'exp_empid']]


#%%

def f(x):
    return x[:-2]+'01'
data['date'] = data['date'].apply(f)
data['num'] = data.groupby(['province', 'date'])['exp_empid'].transform(lambda x: len(x))

#%%

data['exp_num'] = data.groupby(['province', 'date'])['exp_empid'].transform(lambda x: len(x.unique()))
#%%

data['effic'] = data['num'] / data['exp_num']
data.to_csv('./nengxioa.csv', header=None)