# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:
updated_damages = []
for damage in damages:
  if damage[-1] == 'B':
    updated_damages.append(float(damage[:-1]) * 10**9)
  elif damage[-1] == 'M':
    updated_damages.append(float(damage[:-1]) * 10**6)
  else:
    updated_damages.append(damage)

#print(updated_damages)        

# write your construct hurricane dictionary function here:
hurricane_dictionary = {}
for i in range(len(names)):
  hurricane_dictionary[names[i]] = {'Name': names[i], 'Month': months[i], 'Year': years[i], 'Max Sustained Wind': max_sustained_winds[i], 'Areas Affected': areas_affected[i], 'Damage': updated_damages[i], 'Death': deaths[i]}

#print(hurricane_dictionary)

# write your construct hurricane by year dictionary function here:
hurricane_in_year = {}
#print(hurricane_dictionary.get('Matthew').get('Year'))
for key in hurricane_dictionary.keys():
  current_year = hurricane_dictionary.get(key).get('Year')
  current_cane = hurricane_dictionary.get(key)
  if current_year in hurricane_in_year.keys():
    temp = hurricane_in_year.get(current_year)
    temp.append(current_cane)
    hurricane_in_year[current_year] = temp
  else:
    hurricane_in_year[current_year] = [current_cane]

print('=== HURRICANE IN YEAR ===')
print(hurricane_in_year.get(1932))

# write your count affected areas function here:
def count_area_affected(area):
  counter = 0
  for key in hurricane_dictionary.keys():
    if area in hurricane_dictionary.get(key).get('Areas Affected'):
      counter += 1
  return counter

print('=== COUNT AREA AFFECTED ===')
print(count_area_affected('Jamaica'))
print(count_area_affected('The Bahamas'))


# write your find most affected area function here:
def most_affected_area(dicti):
  counter_dictionary = {}
  # create dictionary
  for key in dicti.keys():
    areas = dicti.get(key).get('Areas Affected')
    for area in areas:
      if area in counter_dictionary.keys():
        counter_dictionary[area] = counter_dictionary.get(area) + 1
      else:
        counter_dictionary[area] = 1
  # find most affected area
  ma_area = None
  hit = 0
  for area in counter_dictionary.keys():
    if counter_dictionary.get(area) > hit:
      hit = counter_dictionary.get(area)
      ma_area = area

  return (ma_area, hit)    

print('=== MOST AFFECTED AREA ===')
print(most_affected_area(hurricane_dictionary))

# write your greatest number of deaths function here:
def greatest_death(dicti):
  fatal_hurricane = None
  total_death = 0
  for hurricane in dicti.keys():
    if dicti.get(hurricane).get('Death') > total_death:
      fatal_hurricane = hurricane
      total_death = dicti.get(hurricane).get('Death')
  return (fatal_hurricane, total_death)    

print('=== GREATEST DEATH ===')
print(greatest_death(hurricane_dictionary))

# write your catgeorize by mortality function here:
mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}
hurricane_mortality = {0: [], 1: [], 2: [], 3:[], 4: [], 5: []}

for hurricane in hurricane_dictionary.keys():
  current_death = hurricane_dictionary.get(hurricane).get('Death')
  hm_key = 0
  
  for scale in mortality_scale.keys():
    if current_death > mortality_scale.get(scale):
      hm_key = scale+1
  
  temp = hurricane_mortality.get(hm_key)
  temp.append(hurricane_dictionary.get(hurricane))
  hurricane_mortality[hm_key] = temp

print('=== HURRICANE MORTALITY ===')
print(hurricane_mortality.get(1))  


# write your greatest damage function here:
def greatest_damage(dicti):
  fatal_hurricane = None
  total_damage = 0
  for hurricane in dicti.keys():
    damage = dicti.get(hurricane).get('Damage')
    if damage == 'Damages not recorded':
      damage = 0.0
    if damage > total_damage:
      fatal_hurricane = hurricane
      total_damage = damage
  return (fatal_hurricane, total_damage)    

print('=== GREATEST DAMAGE HURRICANE ===')
print(greatest_damage(hurricane_dictionary))

# write your catgeorize by damage function here:
damage_scale = {0: 0.0,
                1: 100000000.0,
                2: 1000000000.0,
                3: 10000000000.0,
                4: 50000000000.0}
hurricane_damage = {0: [], 1: [], 2: [], 3:[], 4: [], 5: []}

for hurricane in hurricane_dictionary.keys():
  current_damage = hurricane_dictionary.get(hurricane).get('Damage')
  if current_damage == 'Damages not recorded':
    current_damage = 0
  hm_key = 0
  
  for scale in damage_scale.keys():
    if current_damage > damage_scale.get(scale):
      hm_key = scale+1
  
  temp = hurricane_damage.get(hm_key)
  temp.append(hurricane_dictionary.get(hurricane))
  hurricane_damage[hm_key] = temp

print('=== HURRICANE DAMAGE SCALE ===')
print(hurricane_damage.get(4))  








