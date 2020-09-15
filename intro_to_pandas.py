import codecademylib
import pandas as pd

orders = pd.read_csv('shoefly.csv')

orders['shoe_source'] = orders.shoe_material.apply(lambda x: 'animal' if x == 'leather' else 'vegan')

print(orders.head())

orders['salutation'] = orders.apply(lambda row: 'Dear Mr. {}'.format(row.last_name)  if row.gender == 'male' else 'Dear Ms. {}'.format(row.last_name), axis=1)
