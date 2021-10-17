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

start_spot.set_explain("시작점이다")
east_spot.set_explain("풀숲이다.")
west_spot.set_explain("풀숲이다.")
north_spot1.set_explain("우거진 풀숲이다.")
north_spot2.set_explain("우거진 풀숲이다.")
north_spot3.set_explain("벼락이 떨어진것 같다.")

my_location = start_spot

while(1):
    four_dir = {'동' : my_location.east, '서': my_location.west, '남' : my_location.south, '북' : my_location.north}
    print(my_location.explain)
    while(1):
        command = input()
        if command in four_dir and four_dir[command]!= None:
            my_location = four_dir[command]
            break
        else:
            if command in four_dir:
                print("갈 수 없는 방향이다.")
            else:
                print("잘못된 명령이다.")
    
