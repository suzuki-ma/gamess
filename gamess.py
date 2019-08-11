# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 20:58:40 2019

@author: suzukimasato
"""

import os
import time
import glob
import subprocess
import shutil

path = os.getcwd() #現在のディレクトリを取得
print("-----------Currennt directry-------")  
print(path)        #現在のディレクトリを表示
print("-----------input directry----ex C:\\Users\\suzukimasato\\Documents\\company\\gamess_home---")
gamessdir = input()
#gamess = "C:\\Users\\suzukimasato\\Documents\\company\\gamess_home"
os.chdir(gamessdir) #gamessのあるディレクトリまで移動
path = os.getcwd() #現在のディレクトリを取得
print("--------------Moved in Gamess directry-------------")       #現在’のディレクトリを表示
print(path) 
file_names = glob.glob(path + "\\*")        #ディレクトリ内のファイル名を取得


shutil.rmtree("restart")    #restartファイルの消去
os.mkdir("restart")

sub_test = subprocess.getoutput("create-parameters.bat")

#inputfileの入力
print("--------------input file-------ex H2O------")   
inputfile = input()
#inputfile = "H2Ogeo"

#gamessの実行
print("--------------Now calculation-------------")   
cmd = "rungms " + inputfile + " 2018-R1-pgi-mkl 1> " + inputfile + ".log &"
subprocess.getoutput(cmd)
print("finish")

#outputfileの読み取り
outputfile = inputfile + ".log"
for line in open(outputfile,"r"):
    print(line.rstrip("\n"))  #改行を削除して一行ずつ表示

