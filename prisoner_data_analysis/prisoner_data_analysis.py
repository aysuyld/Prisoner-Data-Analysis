#%%
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

df = pd.read_csv("prisoner.csv")
ax = plt.gca()
df.head()

df.columns=['Year','Total Prisoners','Male Prisoners','Female Prisoners']
data = []
new_row = {'Year':1998,'Total Prisoners':66096,'Male Prisoners':63576,'Female Prisoners':2520}
data.insert(0,new_row)

df = pd.concat([pd.DataFrame(data), df], ignore_index=True)
#print(df)

df.plot(x='Total Prisoners', y='Year', kind='line', label='Total',ax=ax)
df.plot(x='Male Prisoners', y='Year', kind='line', label='Male',ax=ax)
df.plot(x='Female Prisoners', y='Year', kind='line', label='Female',ax=ax)

plt.title('Year by Prisoners')
plt.xlabel('Prisoners')
plt.ylabel('Year')
plt.show()
#sns.lineplot(x='Year',y='Total Prisoners',data=df)

# %%
