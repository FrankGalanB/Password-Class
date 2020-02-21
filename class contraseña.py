class contraseña:  
  import string
  import hashlib
  import random 
  def a():
    simb = str.ascii_letters+str.punctuation+str.digits
    res = "".join(choice(simb) for x in range(randint(8,12)))
    
    return res
#
  def final(conversor):
    conversor_no = hashlib.new("sha256", res)
    print(conversor.digest())