import pandas as pd
df = pd.read_csv(r"C:\Users\gurua\Downloads\mckinsey.csv")
print (df)
print ('')

print(df.shape)
print('')
print (df.info())
print ('')
print (df.describe())
print('')

print(df.head(10))
print ('')
print (df.tail(10))
print ('')

# To check how any unique countries are present
print (df['country'].unique())
print ('')
print ('no. of countries are: ', len(df['country'].unique()))
print ('')

# To know the min. and max. life expectancy for the data set
print('the minimum life expectancy is: ', df['life_exp'].min())
print('the maximun life expectancy is: ', df['life_exp'].max())
print ('')

# To fetch all the details of a specific country (for ex. 'India')
df_india = df[df['country'] == 'India']
print (df_india)
print('')

# To fina year on year relation with life expectancy for country = India
import matplotlib.pyplot as plt
df_year = df_india['year']
print (df_year)
print ('')
df_exp = df_india ['life_exp']
print (df_exp)
#The plot
plt.plot(df_year, df_exp) #(x,y)
plt.show()