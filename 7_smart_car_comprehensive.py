# 综合练习：智能小车综合导航程序
print("===== 自动驾驶小车导航系统 =====")
signal = input("前方交通信号灯：")

if signal == "红灯":
    print("车辆停止")
elif signal == "黄灯":
    print("缓慢减速")
elif signal == "绿灯":
    way = input("行驶方向：")
    if way == "左转":
        print("绿灯左转通行")
    elif way == "右转":
        print("绿灯右转通行")
    else:
        print("绿灯直行通过路口")
else:
    print("路况未知，暂停行驶")