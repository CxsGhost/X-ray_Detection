import pandas as pd

data = pd.read_csv('./workdata.txt', sep='\t', header=None, index_col=None)
col = 'province:String, city:String, code:String, acc_number:String, tel:String, date:String, rep_disoe:Int, overtime:Int, receipt:Int, descr:String, exp_empid:String, fault_1:String, fault_2:String, fault_type:String, acs_way:String, address:String'
col = col.replace(',','')
col = col.split(' ')
col = list(map(lambda x: x[:x.find(':')], col))
print(col)
#%%
data = data.drop(columns=[16])
data.columns = col

data = data[['province', 'address', 'fault_1', 'fault_2', 'fault_type', 'acs_way']]
data['num'] = data.groupby(['province', 'address', 'fault_1', 'fault_2', 'fault_type', 'acs_way'])['acs_way'].transform('count')
data.to_csv('./bda.csv')