# 10-6 编写一个程序，提示用户输入两个数字，再将它们相加并打印结果。在用户输入的任何一个值不是数字时都捕获TypeError 异常，并打印一
# 条友好的错误消息。对你编写的程序进行测试：先输入两个数字，再输入一些文本而不是数字。（经测，是ValueError）
# 10-7 加法计算器 ：将你为完成练习10-6而编写的代码放在一个while 循环中，让用户犯错（输入的是文本而不是数字）后能够继续输入数字。
介绍 = "两个数字相加的游戏"
print(介绍.center(80))
print('(退出请填写Q)')
print('=' * 80)


while True:
    num1 = input('请输入第一个数字：')

    if num1 == 'Q':
        print('下次再来玩！')
        break
    num2 = input('请输入第二个数字：')
    if num2 == 'Q':
        print('下次再来玩！')
        break

    try:
        subtotal = int(num1) + int(num2)
        print ('%s + %s = %d' % (num1, num2, subtotal))

        # 创建一个txt文件，把正确的记录保存下来。
        with open ('sum.txt', 'a', encoding='UTF-8') as f_object:
            f_object.write ('\n\t %s + %s = %d' % (num1, num2, subtotal))

    except ValueError:
        print('您的输入有误，请重新输入！')

