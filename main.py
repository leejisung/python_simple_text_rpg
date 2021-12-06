import spot_maker
import item
import hero
import random as rd

hero = hero.hero_make('me')
inv = item.inv_make()

GOLD = 20
#### 아이템 설정
def hp_potion_effect():
    hero.hp = min(hero.max_hp, hero.hp+50)
hp_potion = item.item_make("HP포션",hp_potion_effect, 10)
def mp_potion_effect():
    hero.mp = min(hero.max_mp, hero.mp+50)
mp_potion = item.item_make("MP포션",mp_potion_effect, 10)

orc_teeth = item.item_make("오크이빨",None, 10)
goblin_teeth = item.item_make("고블린이빨",None, 5)
slime_mass = item.item_make("슬라임덩어리",None, 1)


inv.start_item(hp_potion)
inv.start_item(mp_potion)
##############

#### 몬스터 설정
orc = spot_maker.monster("오크", 10, 100, 10, orc_teeth)
goblin = spot_maker.monster("고블린", 2, 30, 5, goblin_teeth)
slime = spot_maker.monster("슬라임", 2, 30, 1, slime_mass)



####맵 설정 
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

east_spot.monster_append(slime)
east_spot.regen_change(10)
west_spot.monster_append(slime)
west_spot.regen_change(10)
north_spot1.monster_append(goblin)
north_spot1.regen_change(5)
north_spot2.monster_append(goblin)
north_spot2.regen_change(5)
north_spot3.monster_append(orc)
north_spot3.regen_change(5)





start_spot.set_explain("시작점이다")
east_spot.set_explain("풀숲이다.")
west_spot.set_explain("풀숲이다.")
north_spot1.set_explain("우거진 풀숲이다.")
north_spot2.set_explain("우거진 풀숲이다.")
north_spot3.set_explain("벼락이 떨어진것 같다.")

my_location = start_spot

###################

def item_view():
    def view():
        if len(inv.item_list)==0:
            print("아이템이 없습니다.")
            return;
        print("아이템 목록")
        for i in range(len(inv.item_list)):
            print(i+1, inv.item_list[i].name)
    while(1):
        print("1 = 아이템 보기")
        print("2 = 아이템 버리기")
        print("3 = 아이템 사용")
        print("다른 키 = 나가기")
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
        elif xxx == "3":
            print("사용할 아이템의 번호는?")
            view()
            try:
                u = int(input())
                inv.use_item(u-1)
            except:
                print("잘못된 접근입니다.")
            
        else:
            break

def battle(spot):
    d = rd.randrange(10)
    if d>= spot.regen:
        return;
    monster_list = spot.monster
    monster = rd.choice(monster_list)
    monster_hp = monster.hp
    name = monster.name
    print("야생의 {} 이(가) 나타났다.".format(name))
    while(1):
        if hero.hp<=0:
            return;
        if monster_hp<=0:
            level = hero.level
            hero.gain_exp(monster.exp)
            if level != hero.level:
                print("레벨업을 하였습니다.")
            return;
        while(1):
            print("내 HP {}, 내 MP {}".format(hero.hp, hero.mp))
            print("적 HP {}".format(monster_hp))
            print("1 공격(mp가 많을수록 명중률 증가), 2 스킬(mp 10 소모)")
            command = input()
            if command == "1":
                dice = rd.randrange(max(hero.mp,int(hero.max_mp/2)))
                if dice*3 <hero.max_mp:
                    print("빚맞췄다.")
                else:
                    damage = hero.attack
                    monster_hp-=damage
                    print("{} 데미지".format(damage))
            elif command == "2":
                if hero.mp>=10:
                    hero.mp-=10
                else:
                    print("mp가 부족하다")
                    continue
                damage = hero.attack*2
                monster_hp-=damage
                print("{} 데미지".format(damage))
            else:
                print("잘못된 입력입니다.")
                continue
            if monster_hp<=0:
                print("이겼다.")
                hero.gain_exp(monster.exp)
                x = inv.gain_item(monster.item)
                return;
            damage = monster.atk
            damage -= hero.defend
            if damage<=0:
                print("근육으로 튕겨냈다")
            else:
                hero.hp -=damage
            if hero.hp<=0:
                print("졌다.")
                return;

def cell():
    global GOLD
    def view():
        if len(inv.item_list)==0:
            print("아이템이 없습니다.")
            return 0
        print("아이템 목록")
        for i in range(len(inv.item_list)):
            print(i+1, inv.item_list[i].name)
        return 1
    x = view()
    if x==0:
        return
    print("팔 아이템의 번호는?")
    try:
        d_num = int(input())
        price = inv.item_list[d_num-1].price
        name = inv.item_list[d_num-1].name
        GOLD += price
        del inv.item_list[d_num-1]
        print(name +" 를 팔았다.")
        print(str(price) +"골드를 벌었다.")
    except:
        print("잘못된 접근입니다.")
def buy(item_list):
    global GOLD
    if len(inv.item_list)>10:
        print("가방이 가득 차 보이네.")
        return;
    price_list = {}
    garget_list = {}
    for i in range(len(item_list)):
        print(i+1, item_list[i].name ,item_list[i].price*2, "골드")
        price_list[str(i+1)] = (item_list[i].price*2)
        garget_list[str(i+1)] = item_list[i]
    print("어떤 물거을 살 거야?")
    xxx = input()
    if xxx in price_list:
        if price_list[xxx]<=GOLD:
            GOLD-=price_list[xxx]
            inv.gain_item(garget_list[xxx])
        else:
            print("돈이 모잘라.")
    else:
        print("안녕.")
    
        
        
#### npc 설정
fairy = spot_maker.npc("요정", "안녕 난 요정이야.")
fairy.cell = cell
fairy.trade_list = [hp_potion, mp_potion]
fairy.buy = buy
start_spot.set_npc(fairy)

while(1):
    if hero.hp<=0:
        print("죽었다.")
        break
    four_dir = {'동' : my_location.east, '서': my_location.west, '남' : my_location.south, '북' : my_location.north}
    print(my_location.explain)
    npc_list = list(map(lambda x: x.name, my_location.npc))
    while(1):
        command = input()
        if command in four_dir and four_dir[command]!= None:
            my_location = four_dir[command]
            battle(my_location)
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
            elif command == "가진돈":
                print("가진돈 :", GOLD, "골드")
            elif command == "아이템":
                item_view()
            elif command in npc_list:
                ind = npc_list.index(command)
                my_location.npc[ind].talk()
            else:
                print("잘못된 명령이다.")


