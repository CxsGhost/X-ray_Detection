import pandas as pd

#%%

data = pd.read_csv('../data/TrainingSet.csv')
#%%

tmp_data = data[['EndDay', 'QuantitySold']]
suc_num = tmp_data.groupby('EndDay').sum()
suc_num.to_csv('./成功数量.csv')
suc_rate = suc_num / tmp_data.groupby('EndDay').count() * 100
suc_rate.to_csv('./成功率.csv')
final_f = pd.merge(suc_num, suc_rate, on='EndDay')
print(final_f)
# suc_data = data[data['IsHOF'] == 1][['SellerName', 'QuantitySold']]
# success_rate = suc_data.groupby('SellerName').count()['QuantitySold']
# success_rate = suc_data.groupby('SellerName')['QuantitySold'].sum() / success_rate * 100
# success_rate = success_rate.sort_values(ascending=False)
# success_rate.to_csv('./金牌买家成功率.csv')
# #%%
#
# train = data[['EbayID', 'QuantitySold']]
# train.to_csv('./train_label.csv', index=False)
# test_data = pd.read_csv('../data/TestSet.csv')
# test = test_data[['EbayID', 'QuantitySold']]
# test.to_csv('./test_label.csv', index=False)
# #%%
#
# train = data.drop(columns=['SellerName', 'QuantitySold', 'EndDay'])
# train.to_csv('./train_data.csv', index=False)
# test_data = test_data.drop(columns=['SellerName', 'QuantitySold', 'EndDay'])
# test_data.to_csv('./test_data.csv', index=False)