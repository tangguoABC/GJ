import os
 
path = r'C:\Users\TANG-GUO\Desktop\点九图转换'
docu = os.listdir(path)
print(docu)
des = input('请重命名后的输入聊天气泡描述：')
count = 0
def order(des,num):
    road = 'C:\\Users\\TANG-GUO\\Desktop\\点九图转换'
    order1 = ' & aapt s -i '+file[num] + ' -o ' + str(des) +'.png'
    enter1 = ''.join(['cd ' + road, order1])
    print(enter1)
    return(enter1)
for file in docu:
    old_dir = os.path.join(path, file)
    count += 1
    if os.path.isdir(old_dir):
        continue
    if '2x' in file:
        new_dir = os.path.join(path, des +'2x.9.png')
        os.rename(old_dir, new_dir)
    if '3x' in file:
        new_dir = os.path.join(path, des +'3x.9.png')
        os.rename(old_dir, new_dir)
print("一共重名了" + str(count) + "个文件")
 
 
file = list(os.listdir(path))
for i in file:
    print(i)
    if '2x' in i:
        m = os.popen(order(str(des)+'_2x',0), "r")
        output = m.read()
        print(output)
 
    if '3x' in i:
        n = os.popen(order(str(des)+'_3x',1), "r")
        output1 = n.read()
        print(output1)
```