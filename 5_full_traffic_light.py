# if-elif-else 语句：三色红绿灯完整判断
light = input("请输入信号灯颜色：")

if light == "红灯":
    print("🔴 红灯停，原地等待")
elif light == "黄灯":
    print("🟡 黄灯亮，减速慢行")
elif light == "绿灯":
    print("🟢 绿灯行，正常通行")
else:
    print("⚠️ 信号识别异常，谨慎驾驶")