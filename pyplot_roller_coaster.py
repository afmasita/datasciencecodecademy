import codecademylib3_seaborn
import pandas as pd
import matplotlib.pyplot as plt

# load rankings data here:

wood = pd.read_csv('Golden_Ticket_Award_Winners_Wood.csv')
steel = pd.read_csv('Golden_Ticket_Award_Winners_Steel.csv')

print(wood.head(10))

# write function to plot rankings over time for 1 roller coaster here:
def plot_rc(df, name, park_name):
  rc = df[(df.Name == name) & (df.Park == park_name)]
  year = rc['Year of Rank']
  rank = rc['Rank']

  plt.close('all')
  plt.plot(year, rank, marker='o')
  plt.title('Annual Ranking of {} Roller Coaster in {}'.format(name, park_name))
  plt.xlabel('Year')
  plt.ylabel('Rank')
  plt.show()

plot_rc(wood, 'El Toro', 'Six Flags Great Adventure')  
plt.clf()

# write function to plot rankings over time for 2 roller coasters here:
def plot_two_rc(df, name1, name2, parkname1, parkname2):
  rc1 = df[(df['Name'] == name1) & (df['Park'] == parkname1)]
  rc2 = df[(df['Name'] == name2) & (df['Park'] == parkname2)]

  year1 = rc1['Year of Rank']
  rank1 = rc1['Rank']
  year2 = rc2['Year of Rank']
  rank2 = rc2['Rank']

  plt.close('all')
  plt.plot(year1, rank1, marker='o', color='blue')
  plt.plot(year2, rank2, marker='o', color='red')
  plt.xlabel('Year')
  plt.ylabel('Rank')
  plt.title('Annual Ranking of Two Roller Coasters')
  plt.legend(['{} in {}'.format(name1, parkname1), '{} in {}'.format(name2, parkname2)])
  plt.show()

plot_two_rc(wood, 'El Toro', 'Boulder Dash', 'Six Flags Great Adventure', 'Lake Compounce')
plt.clf()

# write function to plot top n rankings over time here:
def plot_top_n(df, n):
  top_n_rankings = df[df['Rank'] <= n]

  plt.close('all')
  plt.figure(figsize=(8, 4))

  for coaster in set(top_n_rankings['Name']):
    coaster_rankings = top_n_rankings[top_n_rankings['Name'] == coaster]
    plt.plot(coaster_rankings['Year of Rank'], coaster_rankings['Rank'], label=coaster, marker='o')
  plt.title('Top {} Coaster Ranking Over Time'.format(str(n)))
  plt.xlabel('Year of Rank')
  plt.ylabel('Rank')

  ax = plt.subplot()
  ax.set_yticks(range(1,(n+1)))
  plt.legend(set(top_n_rankings['Name']))
  plt.show()

plot_top_n(wood, 5)
plt.clf()

# load roller coaster data here:
rc_stat = pd.read_csv('roller_coasters.csv')
print(rc_stat.head(10))

# write function to plot histogram of column values here:
def plot_hist(df, col):
  histdata = None
  if col == 'height':
    temp = df[df.height <= 140]
    histdata = temp.height
  else:
    histdata = df[col]  

  plt.hist(histdata.dropna())  
  plt.show()

plot_hist(rc_stat, 'speed')
plt.clf()

# write function to plot inversions by coaster at a park here:
def plot_inversion(df, park):
  dff = df[df.park == park]
  dff = dff.sort_values('num_inversions', ascending=False)
  coaster_names = dff.name
  no_inv = dff.num_inversions

  plt.bar(range(len(coaster_names)), no_inv)
  plt.title('Inversions by Coaster in ' + park)
  plt.xlabel('Coaster name')
  plt.ylabel('Number of inversions')
  ax = plt.subplot()
  ax.set_xticklabels(coaster_names)
  plt.show()

plot_inversion(rc_stat, 'Parque Warner Madrid')  
plt.clf()
    
# write function to plot pie chart of operating status here:
def plot_status(df):
  operating = df.groupby('status').name.count().reset_index()
  status_name = operating.status
  coaster_cnt = operating.name

  plt.pie(coaster_cnt, autopct='%0.1f%%')
  plt.axis('equal')
  plt.legend(status_name)
  plt.show()

plot_status(rc_stat)
plt.clf()
  
# write function to create scatter plot of any two numeric columns here:
def scatter_plot(df, col1, col2):
  df = df[df.height < 140]
  df1 = df[col1]
  df2 = df[col2]

  plt.figure(figsize=(10,10))
  plt.scatter(df1, df2, alpha=0.5)
  plt.xlabel(col1)
  plt.ylabel(col2)
  plt.title('Scatter plot between {} and {}'.format(col1, col2))
  plt.show()

scatter_plot(rc_stat, 'length', 'speed')  
plt.clf()
