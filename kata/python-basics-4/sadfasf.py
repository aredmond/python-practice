try:
    print(sadfaf)
except NameError as e:
    print('THere was an Name error!', e)
except ValueError as e:
    print('THere was an error!', e)
finally:
    print("Do this at the end.")