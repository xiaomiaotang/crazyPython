# 10-11 喜欢的数字 ：编写一个程序，提示用户输入他喜欢的数字，并使用json.dump() 将这个数字存储到文件中。
# 再编写一个程序，从文件中读取这个值，并打印消息“I know your favorite number! It's _____.”。
# 10-12 记住喜欢的数字 ：将练习10-11中的两个程序合而为一。如果存储了用户喜欢的数字，就向用户显示它，
# 否则提示用户输入他喜欢的数字并将其存储到文件中。运行这个程序两次，看看它是否像预期的那样工作。

# 1、获取用户名
# 2、以得到用户名为名的json文件名（路径）。
# 3、尝试是否已有这样的文件，如果有，打开。
# 4、如果没有，让用户录入信息。


import json

username = input('请输入你的名字：')
filename = username + '.json'

try:
    with open(filename) as file_object:
        favorite_num = json.load(file_object)
        print('Hi, %s 我知道你喜欢的数字是 %s' % (username, favorite_num))

except FileNotFoundError:
    favorite_num = input('请输入你喜欢的数字：')
    with open(filename, 'w') as file_object:
        json.dump(favorite_num, file_object)


    



