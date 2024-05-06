lst4 = [3,11,[20,24],200]
print(lst4[2] + [lst4[0]])
import doctest
from practical8 import print_contacts
def is_special_num(original_num):
  """The function takes a number and check if it is a special number
     :param:Original number
     :returns: special number
     >>> 89
     True
     >>> 98
     False
  """
  sums = (original_num // 10) +  (original_num % 10)
  product = (original_num // 10) * (original_num % 10)
  special_num = sums + product
  
  if original_num == special_num:
    return True
  else:
    return False
  

print(is_special_num(89)) 

for num in range(is_special_num(100)):
     print(num)
     
  