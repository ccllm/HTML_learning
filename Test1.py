#获取用户输入长宽高
length = float(input("请输入长方体长度："))
width = float(input("请输入长方体宽度："))
high = float(input("请输入长方体高度："))

#计算长方体体积和面积
area = 2*(length*width + length*high + width*high)
v = length*width*high

#输出结果
print(f"长方体表面积为：{area:.2f}")
print(f"长方体体积为：{v:.2f}")