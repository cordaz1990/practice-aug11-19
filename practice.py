#Reverse Lookup
def reverse_lookup(d,v):
    for k in d:
      if d[k] == v:
          return k
        
    raise lookupError()
    
#Dictionary
def invert_dict(d):
    inverse = dict()
    for key in d:
      val = d[key]
      if val not in inverse:
         inverse[val] = [key]
      else:
        inverse[val].append(key)
    return inverse
