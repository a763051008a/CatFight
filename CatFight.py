from random import randint
from time import sleep
from progressbar import *
import knowledge_data
import json
#游戏设置
list_place=['猫猫谷','幻光森林']
list_weapon=['毛线球','猫蹄铁','猫法树枝']
list_accomplishment=['崽猫的出生证明','旋风崽猫','崽猫的第一次施法']

class CatGame(object):
    """猫咪历险记游戏类"""

    def __init__(self):
        #游戏初始化
        print('你好，小猫。欢迎来到猫咪的魔法世界。')
        sleep(1)
        print('这是一个奇幻美妙，却又充满危险的地方。你准备好了吗？')
        comeinto = 'what'
        while comeinto != 'yes':
            comeinto = input('请输入‘yes’或‘no’:\n')
            if comeinto == 'no':
                print('欢迎下次光临。')
                while True:
                    pass
        #读取存档
        self.role_values = [1, 100, 1, 0, 5]
        self.now_record_name = ['自定义存档名称']
        self.load_record()
        print('欢迎进入猫猫谷')
        self.jindutiao(1)
        # 定义出生属性与游戏设置
        self.role_values_name = ['等级', '生命值', '攻击力', '当前经验值', '金钱']
        self.now_place = ['猫猫谷']
        self.now_weapon = []
        self.now_accomplishment = []
        self.monster_random = [['萤火虫','大黄蜂','骷髅蝴蝶'],['小松鼠','树袋熊','小狐狸'],['啄木鸟','猫头鹰','鹫鹰'],['大饿狼','大饿狼','大饿狼']]
        self.enemy = {1: '昆虫系', 2: '小型哺乳类动物', 3: '飞禽系', 4: '大饿狼'}
        self.enemy_attack = {1: 5, 2: 8, 3: 12, 4: 20}
        self.enemy_health = {1: 6, 2: 15, 3: 20, 4: 100}
        self.wolf_hp = [100]
        self.hp_max = [100]
        self.exp_panding = [0,2,7,15,25,40,60,85,115,150]
        self.give_exp = [1,3,10]

    # 写入存档
    def write_to_record(self):
        io = 'record.json'
        with open(io, 'r') as f:
            data = json.load(f)
            data[self.now_record_name] = self.role_values
        with open(io, 'w') as f:
            json.dump(data, f)
            print("存档完成......")

    # 新建存档与载入存档
    def load_record(self):
        io = 'record.json'
        print('1.创建新的存档   2.读取存档\n')
        x = self.game_input()
        if x == 1:
            self.now_record_name = input('请输入新的存档的名称：\n')
            with open(io,'r') as f:
                data = json.load(f)
                new_values = {self.now_record_name: [1, 100, 1, 0, 5]}
                data.update(new_values)
            with open(io, "w") as f:
                json.dump(data, f)
                print('新建存档完成......')
        if x == 2:
            with open(io,'r') as f:
                data = json.load(f)
            i = 1
            for key in data:
                print(i, key)
                i += 1
            print('请输入您想载入的存档序号：')
            m = self.game_input()
            i = 1
            for key in data:
                if i == m:
                    print('正在载入您的存档：', key)
                    self.now_record_name = key
                    self.role_values = data[key]
                    break
                i += 1
            print('载入存档完成......')
    #进度条
    def jindutiao(self,time_done):
        chengxu_time = 100*time_done
        progress = ProgressBar()
        for i in progress(range(chengxu_time)):
            time.sleep(0.01)

    #升级系统
    def level_up(self,exp_value):
        self.role_values[3] += exp_value
        print('您获得',exp_value,'点经验')
        if self.role_values[0] >= 10:
            print('您已达等级上限')
        else:
            if self.role_values[3] >= self.exp_panding[self.role_values[0]]:
                self.role_values[0] += 1
                self.role_values[1] += 10 #提升属性
                self.role_values[2] += 1
                self.hp_max[0] +=10
                print("恭喜升级！！！！！！！")

    #开始游戏循环
    def start_game(self):
        '''开启游戏循环'''
        while True:
            self.place_action()
            self.write_to_record()

    # 动作选择_不同场景
    def place_action(self):
        print('————————————————')
        print('请选择你想做的事情：')
        if self.now_place[0] == '猫猫谷':
            print('1.出门觅食   2.玩猫抓板(已修改削弱）   3.查看属性   4.在猫窝休息   5.学习百科知识')
            action = self.game_input()
            self.action_response_mmg(action)
        if self.now_place[0] == '幻光森林':
            print('1.采蘑菇（已修改削弱）   2.捕猎小怪物   3.回猫猫谷   4.挑战大饿狼')
            action = self.game_input()
            self.action_response_hgsl(action)

    # 动作回应-猫猫谷
    def action_response_mmg(self,action):
        if action == 1:
            false1 = 0
            for place in list_place:
                false1 += 1
                print(false1, place)
            print('————————————————')
            print('请选择你想去的地点：')
            choose_place_number = self.game_input()
            if choose_place_number == 1:
                self.now_place[0] = '猫猫谷'
                print('进入猫猫谷')
            if choose_place_number == 2:
                self.now_place[0] = '幻光森林'
                print('进入幻光森林')
        if action == 2:
            lucky_of_game = randint(1, 3)
            if lucky_of_game > 2:
                print('训练成功')
                self.level_up(1)
            else:
                print('训练失败')
        if action == 3:
            i = 0
            for value in self.role_values:
                print(self.role_values_name[i], ':', value)
                i += 1
        if action == 4:
            if self.role_values[4] >= 5:
                if self.role_values[1] >= 90:
                    if self.role_values[1] == 100:
                        print('您的生命值已满，不需要休息')
                    else:
                        self.role_values[1] += 10
                        if self.role_values[1] > 100:
                            self.role_values[1] = 100
                            self.role_values[4] -= 5
                            print('金钱-5，休息完成，生命值+10')
                        else:
                            self.role_values[4] -= 5
                            print('金钱-5，休息完成，生命值+10')
                else:
                    self.role_values[4] -= 5
                    self.role_values[1] += 10
                    print('金钱-5，休息完成，生命值+10')
            else:
                print('您的金钱不足')
        if action == 5:
            w = knowledge_data.choose_que()
            if w == '正确':
                gain = randint(1, 3)
                self.role_values[4] += gain
                print('金钱+', gain)

    # 动作回应-幻光森林
    def action_response_hgsl(self,action):
        if action == 1:
            type = randint(1, 3)
            gain = randint(1, 2)
            print('辛苦的找蘑菇中')
            self.jindutiao(2)
            if type == 1:
                self.role_values[4] += gain
                print('捡了一个红蘑菇！金钱+', gain)
            if type == 2:
                self.role_values[4] += gain
                print('捡了一个蓝蘑菇！金钱+', gain)
            if type == 3:
                self.role_values[1] -= 5
                print('捡了一个绿蘑菇！生命值-', 5)
        if action == 2:
            print('请选择你想要捕猎的怪物类型:\n1.昆虫系（推荐等级1-3）\n2.小型哺乳类动物（推荐等级4-6）\n3.飞禽系（推荐等级7-9）')
            monster_type = self.game_input() - 1
            self.monster(monster_type)
        if action == 3:
            self.now_place[0] = '猫猫谷'
            print('进入猫猫谷')
        if action == 4:
            enemy_number = 4
            print('遭遇大饿狼')
            self.wolf_hp[0] = self.fight(enemy_number,1)
            if self.wolf_hp[0] <= 0:
                print('恭喜通关')
                while True:
                    pass
        self.wolf_hp[0] = 100

    #捕猎小怪物
    def monster(self,monster_type):
        self.jindutiao(1)
        lucky = randint(1,10)
        if lucky > 3:
            monster_random = randint(0,2)
            print('遭遇', self.monster_random[monster_type][monster_random], '！')
            print('你现在迎战的是', self.monster_random[monster_type][monster_random])
            self.fight(monster_type,monster_random)
        else:
            print('捕猎失败，你没有任何收获')

    #战斗界面
    def fight(self,enemy_number,monster_random):
        enemy_number += 1
        enemy_hp = self.enemy_health[enemy_number]
        while True:
            check_dead = self.check_hp()
            if check_dead == 0:
                self.role_values[1] = 1
                print('你受伤过重，即将强制返回猫猫谷')
                break
            enemy_hp1 = enemy_hp
            enemy_hp = self.fight_action(enemy_hp)
            print(self.monster_random[enemy_number-1][monster_random], '现在的血量为', enemy_hp)
            print('你现在的血量为',self.role_values[1])
            if enemy_hp == enemy_hp1:
                break
            if enemy_hp <= 0:
                print('恭喜你击败了', self.monster_random[enemy_number-1][monster_random])
                print('您获得',self.give_exp[enemy_number-1],'点经验值')
                self.level_up(self.give_exp[enemy_number-1])
                break
            self.role_values[1] -= self.enemy_attack[enemy_number]
            sleep(1)
            print(self.monster_random[enemy_number-1][monster_random], '对你造成了', self.enemy_attack[enemy_number], '点伤害')
            sleep(1)
        print('战斗结束')
        return enemy_hp

    # 战斗动作
    def fight_action(self,enemy_hp):
        print('————————————————')
        print('请选择你的动作：')
        print('1.攻击   2.诱捕(未开发)   3.逃跑')
        fight_number = self.game_input()
        if fight_number == 1:
            print('你使用【抓挠】成功造成了', self.role_values[2], '点物理伤害')
            enemy_hp -= self.role_values[2]
        if fight_number == 2:
            print('暂时没有任何效果，视同攻击选项')
            enemy_hp -= self.role_values[2]
        if fight_number == 3:
            self.hp_max[0] -= 10
            if self.hp_max[0] < self.role_values[1]:
                self.role_values[1] = self.hp_max[0]
            print('成功逃跑,但是你的生命值上限减少10点')
        return enemy_hp

    # 角色死亡检测
    def check_hp(self):
        if self.role_values[1] > 0:
            return 1
        else:
            return 0

    # 输入检测
    def game_input(self):
        while True:
            try:
                str_num = input('请输入对应的序号:')
                num = int(str_num)
                break
            except:
                print('您输入的内容不规范，请重新输入：')
        return num

if __name__ == '__main__':
    # 开始游戏
    CatGame().start_game()