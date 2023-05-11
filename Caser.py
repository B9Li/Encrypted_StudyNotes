#!/user/bin/env python3
# -*- coding: utf-8 -*-

#在密码本上，用特定的方式替换字符所在的位置
#这里需要两个东西，1、密码本 2、特定的方式


#版本一
unicode = ''
for i in range(0,55296):
    unicode = unicode + chr(i)
def caesarCipher(dict,message,mode,key): #密码本，密文，密匙，模式
    '可输入密码本的凯撒挪移式密码机'
    outmessage = ''
    for i in message:
        if i in dict:
            x = dict.find(i)
            if mode == 'encode':
                outmessageIndex = x + key
                if outmessageIndex >= len(dict):
                    outmessageIndexback = outmessageIndex - len(dict)
                    outmessage = outmessage + dict[outmessageIndexback]
                else:
                    outmessage = outmessage + dict[outmessageIndex]
            elif mode == 'decode':
                outmessageIndex = x - key
                if outmessageIndex < 0:
                    outmessageIndexback = outmessageIndex + len(dict)
                    outmessage = outmessage + dict[outmessageIndexback]
                else:
                    outmessage = outmessage + dict[outmessageIndex]
        else:
            outmessage = outmessage + i
    return outmessage #



#密文输入，密钥
#版本二
def caesarCipher(message,mode,key):
    '用unicode变换的凯撒挪移密码机'
    if mode == 'encode':
        ciphertext = ''
        for i in message:
            numtext = int(ord(i))+key
            try:
                ciphertext = ciphertext + chr(numtext)
            except:
                ciphertext = ciphertext + i
        return ciphertext
    if mode == 'decode':
        original = ''
        for i in message:
            numtext = int(ord(i))-key
            try:
                original = original + chr(numtext)
            except:
                original = original + i
        return original

#测试
banane = caesarCipher('一二三','encode',358)
print(banane)
b = caesarCipher('佦俲佯','decode',358)
print(b)
