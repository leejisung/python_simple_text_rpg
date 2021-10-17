import spot_maker
spot = spot_maker.spot
start_spot = spot('start')
east_spot = spot('east_spot')
west_spot = spot('west_spot')
north_spot1 = spot('north_spot1')
north_spot2 = spot('north_spot2')
north_spot3 = spot('north_spot3')

start_spot.set_east(east_spot)
west_spot.set_east(start_spot)
start_spot.set_north(north_spot1)
north_spot1.set_north(north_spot2)
north_spot2.set_north(north_spot3)
