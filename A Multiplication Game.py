
while True:
    try:
        inp = int(input())
        limit = 1
        stan_turn = True
        while limit < inp:
            if stan_turn:
                limit *= 9
            else:
                limit *= 2
            stan_turn = not stan_turn
        print("Ollie wins." if stan_turn else "Stan wins.")
    except:
        break
