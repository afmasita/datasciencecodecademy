premium_ground_shipping_cost = 125.0

def ground_shipping_cost(weight):
  flat_charge = 20.0
  cost = flat_charge

  if weight <= 2:
    cost += (1.50 * weight)
  elif weight <= 6:
    cost += (3.00 * weight)
  elif weight <= 10:
    cost += (4.00 * weight)
  else:
    cost += (4.75 * weight)

  return cost

def drone_shipping_cost(weight):
  flat_charge = 0.0
  cost = flat_charge

  if weight <= 2:
    cost += (4.50 * weight)
  elif weight <= 6:
    cost += (9.00 * weight)
  elif weight <= 10:
    cost += (12.00 * weight)
  else:
    cost += (14.25 * weight)

  return cost

print(ground_shipping_cost(8.4))        

print(drone_shipping_cost(1.5))

def cheapest_shipping_cost(weight):
  gs = ground_shipping_cost(weight)
  ds = drone_shipping_cost(weight)
  pgs = premium_ground_shipping_cost
  cheapest = 0.0
  method = "none"

  if gs < ds:
    if pgs < gs:
      cheapest = pgs
      method = "Premium Ground Shipping"
    else:
      cheapest = gs
      method = "Ground Shipping"
  else:
    if pgs < ds:
      cheapest = pgs      
      method = "Premium Ground Shipping"
    else:
      cheapest = ds
      method = "Drone Shipping"

  return ("The cheapest method is " + method + " with price " + str(cheapest))

print(cheapest_shipping_cost(4.8))       
