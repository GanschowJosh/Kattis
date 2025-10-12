while True:
  try:
    line = input().split(",")
    line = map(lambda l: float(l.replace(" ", "")), (l for l in line))
    print(sum(line))
  except Exception as e:
    print(e)
    break