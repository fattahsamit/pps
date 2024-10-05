# 13. pH Levels

ph = int(input("Enter a value between 0-14: "))

if ph > 7:
  print('Basic')
elif ph < 7:
  print('Acidic')
else:
  print('Neutral')