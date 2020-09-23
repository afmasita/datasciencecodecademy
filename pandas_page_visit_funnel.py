import codecademylib
import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])
print(visits.head(5))
print(cart.head(5))
print(checkout.head(5))                       
print(purchase.head(5))

visit_cart = pd.merge(visits, cart, how='left')
visit_no_cart = len(visit_cart[visit_cart.cart_time.isnull()])
all_visit = len(visit_cart)
visit_no_cart_percentage = visit_no_cart / float(all_visit)
print('visit but did not atc: ' + str(visit_no_cart_percentage))

cart_checkout = pd.merge(cart, checkout, how='left')
cart_no_co = len(cart_checkout[cart_checkout.checkout_time.isnull()])
all_cart = len(cart_checkout)
cart_no_co_pct = cart_no_co / float(all_cart)
print('add to cart but did not checkout: ' + str(cart_no_co_pct))

all_data = visits.merge(cart, how='left').merge(checkout, how='left').merge(purchase, how='left')
#print(all_data.head(5))

co_no_purchase = len(all_data[(all_data.purchase_time.isnull()) & (all_data.checkout_time.notnull())]) / float(len(all_data[all_data.checkout_time.notnull()]))
print('checkout but did not purchase: ' + str(co_no_purchase))

# visit but did not atc: 0.826
# add to cart but did not checkout: 0.253112033195
# checkout but did not purchase: 0.16889632107
# ATC was the weakest link. suggestion: investigate user flow from visit to ATC to make process easier OR make PDP more interesting

all_data['time_to_purchase'] = \
    all_data.purchase_time - \
    all_data.visit_time
print(all_data[all_data.time_to_purchase.notnull()]) 

print(all_data.time_to_purchase.mean())


