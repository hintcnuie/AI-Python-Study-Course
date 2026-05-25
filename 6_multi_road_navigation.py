# if-elif-else 语句：多路况导航判断
nav = input("导航提示路况：")

if nav == "左转路口":
    print("🚗 执行左转弯操作")
elif nav == "右转路口":
    print("🚗 执行右转弯操作")
elif nav == "直行通道":
    print("🚗 匀速直线前进")
else:
    print("🚗 暂时靠边停车观察路况")