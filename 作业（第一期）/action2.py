import pandas as pd
d = pd.read_csv('testresult.csv')
df = pd.DataFrame(d)
pd.set_option('display.unicode.east_asian_width', True)
s = df.mean()
df = df.append(s, ignore_index=True)
df.iloc[5,0]='平均成绩'
min_test = df.min()
df = df.append(min_test, ignore_index=True)
df.iloc[6,0]='最低成绩'
max_test=df.max()
df = df.append(max_test, ignore_index=True)
df.iloc[7,0]='最高成绩'
fangcha = df.iloc[0:5, 1:4].var()
df = df.append(fangcha, ignore_index=True)
df.iloc[8,0]='方差'
biaozhuncha =  df.iloc[0:5, 1:4].std()
df = df.append(biaozhuncha, ignore_index=True)
df.iloc[9,0]='标准差'
zcj = df.iloc[0:5,1:4].sum(axis=1)

df['总成绩']=zcj
result=df.sort_values(by='总成绩',ascending=True)
print(result)
