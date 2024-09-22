import sys
import time
import webbrowser
from typing import TextIO
print("如遇到关卡闪退等请重启游戏后读档\n")
print("本游戏为二创，请勿抄袭与Warma视频无关的其他内容\n")
print("游戏作者：B站地灯 视频作者：Warma\n")
print("沃的厨馆\n\n")
Money_Plot = 0
def WWDX():
    print("制作者：dideng")
    S()
    print("原创视频：Warma")
    S()
    print("未完待续")
def progress_bar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█'):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    sys.stdout.write('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix)),

    # Print New Line on Complete
    if iteration == total:
        print()
def dh_W(content):
    W = "我："
    print(W + content)

def dh_MTY(content):
    W = "猫头鹰："
    print(W + content)
def dh_CSGZ(content):
    W = "我："
    print(W + content)
def dh_J(content):
    W = "鸡："
    print(W + content)
def dh_HLN(content):
    W = "火烈鸟："
    print(W + content)
def buy_plot(price):
    global Money_Plot
    if price > Money_Plot:
        print("您没有足够的钱来购买这个商品。")
    else:
        Money_Plot -= price
        print(f"购买成功！剩余金额为：{Money_Plot}")
def SJ(Sj):
    time.sleep(Sj)
Print = print
def S():
    SJ(0.9)
def Money_Plot_detection(detection):
    global Money_Plot
    if Money_Plot != detection:
        Money_Plot = Money_Plot + detection
not1ce = "你输入了不存在的选项"
begins = 0
Main_menu = input("1.开始游戏\n2.读档\n3.给制作者关注\n4.给up关注\n5.退出游戏\n")
if Main_menu == "1":
    print("开始游戏")
    begins = 2
elif Main_menu == "5":
    sys.exit()
elif Main_menu == "2":
    try:
        file: TextIO
        with open('Archive_data-Plot-S1.parma', 'r') as file:
            lines = file.read()
            if lines != "Not":
                begins = begins + int(lines)
                print("存档加载成功")
            else:
                print("存档文件为空或格式不正确")
    except FileNotFoundError:
        print("没有存档")
elif Main_menu == "3":
    webbrowser.open_new("https://space.bilibili.com/1749090711")
elif Main_menu == "4":
    webbrowser.open_new("https://space.bilibili.com/53456")
else:
    print(not1ce)
if begins == 2:
    with open('Archive_data-Plot-S1.parma', 'r') as file:
        lines = file.read()
        if lines:
            IFDF = input("你确定要放弃原存档，开启新游戏吗？y/n\n")
            if IFDF == "y":
                with open("Archive_data-Plot-S1.parma", "w") as file_write:
                    file_write.write("Not")
                    file_write.close()
    print("第一章 未知的森林")
    print("你不知为什么在一片树林里")
    choose_SL1 = input("你要？:A：北 B：南\n")
    if choose_SL1 == "A":
        print("北方没有东西")
        choose_SL1 = input("你要？:A：北 B：南\n")
        if choose_SL1 == "A":
            print("北方没有东西")
            print("You Die")
        elif choose_SL1 == "B":
            print("北方有森林！")
            begins = 3
    elif choose_SL1 == "B":
        print("北方有森林！")
        begins = 3
    else:
        print(not1ce + ",提示，是大写")
if begins == 3:
    SJ(1)
    print("有钻石！")
    SJ(1)
    print("你需要一个背包！")
    SJ(0.7)
    print("有背包！")
    SJ(1.7)
    print("你的背包\n￥：0\n1.无 2.无 3.无 4.无")
    SJ(1)
    print("你获得了：钻石")
    S()
    print("你的背包\n￥：0\n1.钻石 2.无 3.无 4.无")
    SJ(0.7)
    print("你捡了一朵花")
    S()
    print("你的背包\n￥：0\n1.钻石 2.花 3.无 4.无")
    SJ(3)
    print("你捡了一些不知名物体")
    S()
    print("你的背包\n￥：0\n1.钻石 2.花 3.樱花 4.树叶")
    SJ(2)
    print("你发现了一个商人 企鹅")
    SJ(1)
    print("我：你好啊，企鹅")
    SJ(0.8)
    print("企鹅：？")
    SJ(1.1)
    print("我：请问这里是哪里？")
    SJ(0.8)
    print("企鹅：哎呀！是人类，来来来，这边请！")
    SJ(1)
    print("我：请问你是.....")
    SJ(0.6)
    Print("企鹅:我最最最喜欢跟人类打交道了！你们人类都特别特别有钱，您需要什么您尽管跟我说！")
    SJ(0.9)
    print("我：不好意思，我没带钱..我迷路了。")
    S()
    print("企鹅:什么？那你原本做什么？抢东西？抓动物？")
    S()
    Print("我：我没有坏心思，我真的只是迷路了，你能帮帮我吗？")
    S()
    Print("企鹅:那...行吧。我好歹是个商人，从不做赔本买卖。你帮我拿些东西过来，我给你个好东西。")
    S()
    Print("我:你需要什么？")
    S()
    print("企鹅：什么都行，越多越好。")
    S()
    print("你把背包里的东西都给了他！")
    S()
    Print("我：...........省略 这些可以吗？")
    S()
    print("企鹅：哦哟！这简直太...咳咳，勉强凑活吧。")
    S()
    Print("我：那我的报酬呢？")
    S()
    print("早就给你准备好啦！这个，你拿去")
    S()
    print("你获得了：砧板")
    S()
    print("企鹅：一个简单的操作台，不错吧？这可是特别昂贵的好东西！看在你给了我钻石的份上，就送你了！")
    S()
    print("我：这不是做饭用的吗？一个钻石就换个砧板，也太亏了吧？")
    S()
    print("企鹅：哎呀，你可真贪。行吧，看在你送我这么多东西，我再给你一点额外报酬。")
    S()
    Print("你获得了：￥10")
    Money_Plot = Money_Plot + 10
    S()
    print("你的背包\n￥：10\n1.无 2.无 3.无 4.无 物品栏：砧板")
    S()
    print("我：也太抵门了！才10块钱！")
    S()
    Print("爱要不要，不要拉倒！你还拿人类世界的物价水平衡量我们世界啊？\n懂不懂我们这边货币的含金量？！\n这钱你不要我就拿回去了啊")
    S()
    print("我：你骂谁呢！")
    S()
    Print("哟哟哟，想一个人饿死在荒野上那你就继续骂吧\n我头顶上的保镖可不会惯着你。")
    S()
    print("（保镖？（看向天上）啊？！）")
    S()
    print("我：对不起，请您帮帮我")
    S()
    print("企鹅：哼，那就跟我来吧")
    S()
    print("我：不要吃我！！！")
    S()
    print("企鹅：说什么呢，带你去个能自力更生的地方")
    S()
    print("我：谢谢（颤音）")
    S()
    print("第一章 完")
    text_to_save = "1"
    try:
        with open("Archive_data-Plot-S1.parma", "w") as file:
            beginsq = begins + 1
            file.write(str(begins))
            file.close()
            print("存档成功！")
            begins = begins + 1
    except FileNotFoundError:
        print("存档失败！")
if begins == 4:
        try:
            with open("Archive_data-Plot-S1.parma", "w") as file:
                beginsq = begins + 1
                file.write(str(begins))
                file.close()
                print("存档成功！")
                begins = begins + 1
        except FileNotFoundError:
            print("存档失败！")
        Money_Plot_detection(10)
        print("第二章 意外成为厨师")
        print("企鹅：那么就是这里")
        S()
        print("这就是你家了")
        S()
        Print("接下来就看你的了")
        S()
        print("我先走咯")
        S()
        print("我家好空旷啊")
        SJ(0.9)
        Print("装家具中.ing")
        SJ(3)
        print("装好了！")
        S()
        print("咚咚咚")
        S()
        print("我：有人敲门？")
        S()
        print("（开门）")
        S()
        print("猫头鹰：你好，请问你是厨师吗？")
        S()
        print("我：算是吧，我有个砧板")
        S()
        print("猫头鹰：那太好了，我好饿，我想吃......")
        S()
        print("我：等一下！我这里不是餐厅啊")
        S()
        print("猫头鹰：我知道怎么做饭，我可以教你啊......等等，为什么我说话是一个程序？")
        S()
        print("猫头鹰：我就教你做个简单的吧，我想要一份【大碗消食草】")
        S()
        print("我：这是什么？")
        S()
        print("猫头鹰：长这样-[大碗消食草]")
        S()
        print("我：这......不就是一碗沙拉吗？")
        S()
        print("猫头鹰：吼吼，你们人类把这叫沙拉啊，真怪的名字")
        S()
        print("猫头鹰：不过既然来到了我们这里，你最好还是入乡随俗，按照我们的叫法来喊")
        S()
        print("我：好吧......那你能教教我怎么做吗？")
        S()
        print("猫头鹰：很简单。你去菜市场买[西兰花][萝卜]来用你的钻板就能做")
        S()
        print("我：那菜市场要怎么走？")
        S()
        print("猫头鹰：你输入：handoff(Market)即可（英文符号）")
        IFAI1 = input("输入猫头鹰给你的指令：")
        if IFAI1 == "handoff(Market)":
            print("你已来到菜市场！")
            Money_Plot_detection(10)
            try:

                with open("Archive_data-Plot-S1.parma", "w") as file:
                    beginsq = begins + 1
                    file.write(str(begins))
                    file.close()
                    print("存档成功！")

            except FileNotFoundError:
                print("存档失败！")
        elif IFAI1 != "handoff(Markat)":
            print("输入错误，我帮你进入了菜市场")
        try:
            with open("Archive_data-Plot-S1.parma", "w") as file:
                beginsq = begins + 1
                file.write(str(begins))
                file.close()
                print("存档成功！")
                begins = begins + 1
        except FileNotFoundError:
            print("存档失败！")
            begins = begins + 1
if begins == 5:
            Money_Plot_detection(10)
            print("孔雀： 咪[米]1￥\n鸽子： 咸[盐]1￥\n鸭子： 绿头[萝卜]2￥\n火烈鸟： 又烂[草莓]4￥\n老鹰： 蛋[蛋]1￥\n企鹅： 水龙头[水龙头]5￥ 操作台[砧板]10￥ 小冰箱[冰箱]10￥ 烤箱[烤箱]30￥ 锅[锅]20￥ 平底锅[平底锅]30￥ 墨镜[墨镜]10￥ 扩展背包[背包]10￥")
            IFAI2 = input("你要跟谁对话？1.孔雀 2.老鹰（其他键为跳过对话）\n")
            if IFAI2 == "1":
                S()
                print("我：你好，请问你卖的这个为什么叫做“咪”？")
                S()
                print("孔雀：哈哈，这位人类顾客，您就别开玩笑了。你们人类不也是这也称呼它的吗")
                S()
                print("孔雀：我可是专门去了趟人类的世界，跟着你们的读音学过来的～")
                S()
                Print("我：（6）")
                IFAI2 = input("你要跟谁对话？1.老鹰\n")
                if IFAI2 == "1":
                    S()
                    print("为什么你卖的商品名字和人类世界的叫法一模一样？")
                    S()
                    print("因为我经常出入人类的世界，见多了自然就知道啦")
                    S()
                    begins = begins + 1
                    try:
                        with open("Archive_data-Plot-S1.parma", "w") as file:
                            beginsq = begins + 1
                            file.write(str(begins))
                            file.close()
                            print("存档成功！")
                    except FileNotFoundError:
                        print("存档失败！")
                        begins = begins + 1
                else:
                    begins = begins + 1
            elif IFAI2 == "2":
                print("为什么你卖的商品名字和人类世界的叫法一模一样？")
                S()
                print("因为我经常出入人类的世界，见多了自然就知道啦")
                IFAI2 = input("你要跟谁对话？1.孔雀\n")
                if IFAI2 == "1":
                    S()
                    print("我：你好，请问你卖的这个为什么叫做“咪”？")
                    S()
                    print("孔雀：哈哈，这位人类顾客，您就别开玩笑了。你们人类不也是这也称呼它的吗")
                    S()
                    print("孔雀：我可是专门去了趟人类的世界，跟着你们的读音学过来的～")
                    S()
                    Print("我：（6）")
                    try:
                        with open("Archive_data-Plot-S1.parma", "w") as file:
                            beginsq = begins + 1
                            file.write(str(begins))
                            file.close()
                            print("存档成功！")
                    except FileNotFoundError:
                        print("存档失败！")
                        begins = begins + 1
                    begins = begins + 1
            else:
                begins = begins + 1
if begins == 6:
    Money_Plot_detection(10)
    try:
        with open("Archive_data-Plot-S1.parma", "w") as file:
            beginsq = begins + 1
            file.write(str(begins))
            file.close()
            print("存档成功！")
    except FileNotFoundError:
        print("存档失败！")
        begins = begins + 1
    print("我：对了，不是要买[西兰花]和[萝卜]吗？")
    SJ(1.2)
    print("孔雀： 咪[米]1￥\n鸽子： 咸[盐]1￥\n鸭子： 绿头[萝卜]2￥\n火烈鸟： 又烂[草莓]4￥\n老鹰： 蛋[蛋]1￥\n企鹅： 水龙头[水龙头]5￥ 操作台[砧板]10￥ 小冰箱[冰箱]10￥ 烤箱["
          "烤箱]30￥ 锅[锅]20￥ 平底锅[平底锅]30￥ 墨镜[墨镜]10￥ 扩展背包[背包]10￥")
    S()
    print("你的背包\n￥：10\n1.无 2.无 3.无 4.无\n 物品栏：砧板")
    S()
    Print("我：你好，请问这个：“绿头怎么卖？”")
    S()
    print("鸭子：嘘——！小声点。你要买少绿头？赶紧拿了就走人，别让人看见了。去去去，快走快走")
    S()
    print("我：你为什么怎么紧张？")
    S()
    print("鸭子：别问了，留下钱走人。")
    S()
    print("输入buy('商品')即可购买商品")
    IFAI3 = input("输入buy(radish)即可购买萝卜\n")
    if IFAI3 == "buy(radish)":
         buy_plot(2)
         print(f"你的背包\n￥：{Money_Plot}\n1.萝卜 2.无 3.无 4.无\n")
    else:
        print("作者帮你买了")
        buy_plot(2)
        print(f"你的背包\n￥：{Money_Plot}\n1.萝卜 2.无 3.无 4.无\n")
    S()
    Money_Plot_detection(8)
    print("我：奇怪，为什么没人卖西兰花呢？")
    SJ(1.5)
    print("我：请问你知道在哪里买吗？")
    S()
    print("猫头鹰：菜市场就可以买到，你去找[天鹅]")
    S()
    print("我：可是我菜市场没找到[天鹅]，真的有这个商贩吗？")
    S()
    print("猫头鹰：你自己想想办法吧")
    S()
    print("我:好吧......总之谢谢你，我再想想办法找")
    SJ(1.3)
    print("我：你好，请问你认识天鹅吗？")
    S()
    print("鸽子：当然认识！但她最近不在这边，请问有什么事")
    S()
    print("我：我听说她出售西兰花，想找她买一点")
    S()
    print("鸽子：西栏...花.....那是什么东西？")
    S()
    print("我：长这样的[西兰花]")
    S()
    print("鸽子：噢～迷你树啊，这个我有一点，我给你吧")
    S()
    print("谢谢你啊，请问多少钱？")
    S()
    print("鸽子：哎呀算啦，一个迷你树又没什么，拿着拿着。")
    S()
    Print(f"你的背包\n￥：{Money_Plot}\n1.萝卜 2.西兰花 3.无 4.无\n")
    S()
    print("我：这多不好意思啊，真的谢谢你啊，我新开了个餐馆，下次有空来我这吃饭啊。")
    S()
    print("鸽子：好！那我先失陪了，我急着回去给孩子搭窝呢，两个孩子冷得一直叫唤")
    SJ(1.4)
    print("我：我凌齐材料啦！接下来要怎么做呢？")
    S()
    print("猫头鹰：把材料放到你的钻板上，处理一下就行了")
    S()
    items = list(range(0, 57))  # 假设有57个项
    l = len(items)

    for i, item in enumerate(items):
        # 模拟一些耗时的操作
        time.sleep(0.3)
        # 更新进度条
        progress_bar(i + 1, l, prefix='做菜中:', suffix='完成', length=100)
    S()
    print("我：做好啦！怎样？是你说的那个大碗消食草吗？")
    S()
    print("猫头鹰：没错没错！太棒了！我就爱这个！")
    S()
    print("我：谢谢你教我做法，现在我可以开餐厅自力更生了")
    S()
    print("猫头鹰：不客气！还有这个，￥6，我结账咯")
    S()
    Money_Plot = Money_Plot + 6
    Money_Plot_detection(14)
    print(f"你的背包\n￥：{Money_Plot}\n1.无 2.无 3.无 4.无\n")
    S()
    print("我：这……怎么还好意思收你的钱，你都教了我这么宝贵的谋生方式")
    S()
    print("猫头鹰：收下吧，之后你还要买更多食材，做更多饭呢")
    S()
    print("猫头鹰：之后你还要买更多食材，做更多饭呢。等会儿估计就会有更多顾客来咯")
    S()
    print("我：谢谢！那我的餐厅随时欢迎您！")
    S()
    print("猫头鹰：等等，我想要一杯葡萄九[葡萄酒]")
    S()
    Print("我：这个叫法......该不会是里面有9粒葡萄吧？")
    S()
    Print("猫头鹰：对，用9粒葡萄榨成的葡萄汁")
    S()
    try:
        with open("Archive_data-Plot-S1.parma", "w") as file:
            beginsq = begins + 1
            file.write(str(begins))
            file.close()
            begins = begins + 1
            print("存档成功！")
    except FileNotFoundError:
        print("存档失败！")
if begins == 7:
    Money_Plot_detection(14)
    try:
        with open("Archive_data-Plot-S1.parma", "w") as file:
            beginsq = begins + 1
            file.write(str(begins))
            file.close()
            print("存档成功")
    except FileNotFoundError:
        print("存档失败！")
    input("输入前往菜市场的代码\n如忘记请到帮助文件夹的：1.前往代码\n")
    print("你来到了：菜市场")
    S()
    print("我：奇怪，怎么没人卖葡萄呢？")
    S()
    dh_W("火烈鸟卖草莓？他应该知道谁卖葡萄吧？")
    S()
    dh_W("你好！请问你卖葡萄吗？")
    S()
    dh_HLN("葡萄？......哦，你说树卵吧？这年头除了些老古董，都没人喊它葡萄啦")
    S()
    dh_W("对对对，树卵。你这里有卖吗？")
    S()
    dh_HLN("我不负责这个的呀，你去问问其他商人吧")
    S()
    dh_W("具体问谁啊？")
    XP_BBC = input("请输入您的性别（不保存）男/女\n")
    if XP_BBC not in ["男", "女"]:
        print("默认你为男！")
        XP_BBC = "男"
    elif XP_BBC == "男":
        XPCH = "小伙子"
    else:
        XPCH = "小姑娘"
    dh_HLN(f"哎呀......{XPCH}，这同行都是死对头，我要怎么给你推荐嘛")
    S()
    dh_W("那我卖你一个又烂？")
    S()
    buy_plot(4)
    dh_HLN("哎呀太好了！感谢惠顾！跟您说啊，您去野外捡点什么吃的，往地上一丢，那家伙就能出现啦")
    WWDX()