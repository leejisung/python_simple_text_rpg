import spot_maker
import item
import hero

hero = hero.hero_make('me')
inv = item.inv_make()

def hp_potion_effect():
    hero.hp = max(hero.max_hp, hero.hp+50)
hp_potion = item.item_make("HP포션",hp_potion_effect)
def mp_potion_effect():
    hero.hp = max(hero.max_hp, hero.hp+50)
mp_potion = item.item_make("MP포션",mp_potion_effect)

inv.gain_item(hp_potion)
inv.gain_item(mp_potion)

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

def item_view():
    def view():
        if len(inv.item_list)==0:
            print("아이템이 없습니다.")
            return;
        print("아이템 목록")
        for i in range(len(inv.item_list)):
            print(i+1, inv.item_list[i].name)
    print("1 = 아이템 보기")
    print("2 = 아이템 버리기")
    print("3 = 아이템 사용")
    print("다른 키 = 나가기")
    while(1):
        xxx = input()
        if xxx == "1":
            view()
        elif xxx =="2":
            print("버릴 아이템의 번호는?")
            view()
            try:
                d_num = int(input())
                del inv.item_list[d_num-1]
            except:
                print("잘못된 접근입니다.")
        else:
            break
        

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
            elif command =="능력치":
                print("레벨", hero.level)
                print("공격력",hero.attack)
                print("HP",hero.max_hp,"/",hero.hp)
                print("MP",hero.max_mp,"/",hero.mp)
                print("EXP",hero.level*10,"/",hero.exp)
            elif command == "아이템":
                item_view()
            else:
                print("잘못된 명령이다.")
    
