def palindrom_check(word):
  """funkcja sprawdza czy dany wyraz jest palindromem,
  porównuje znaki stojące na tym samym miejscu wyrazu, licząc od początku i od końca"""
  i = len(word)/2
  n = 0
  while n < i:
