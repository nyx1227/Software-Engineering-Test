f = open("yq_in.txt", "r")  # 以只读方式打开文件
fo = open("yq_out.txt", 'w')  # 只写模式打开文件；若文件已存在则打开文件，并从头开始编辑。若文件不存在，创建新文件。
lines = f.readlines()  # 读取所有行
province = []  # 省份列表
sole_province = []  # 去除了重复省份值的列表
city = []  # 城市列表
num = []  # 新增人数列表
for line in lines:
    items = line.strip().split("\t")
    province.append(items[0])  # 把文件的第1列添加进省份列表
    city.append(items[1])  # 把文件的第2列添加进城市列表
    num.append(items[2])  # 把文件的第3列添加进人数列表

for x in province:
    if x not in sole_province:
        sole_province.append(x)  # 去除省份列表重复值，不重复元素添加进sole_province

for i in sole_province:
    print(i, file=fo)  # 把省份先写进yq_out.txt
    for j in range(len(province)):
        if i == province[j]:
            print(city[j]+"\t"+num[j], file=fo)  # 如果省份值相等的，就把对应的城市和人数写进yq_out.txt
f.close()
fo.close()
