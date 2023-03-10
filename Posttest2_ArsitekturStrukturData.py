import math
import random
import os
os.system('cls')

def JumpSearch( arr , t , f ):
    cara = math.sqrt(f)
    r = 0
    for e in range(len(arr)):
        if type(arr[e]) == list:  
            CariData = JumpSearch(arr[int(e)],t,len(arr[int(e)]))
            if CariData == -1:
                arr[int(e)] = "z"
                print()
            else:
                print(t, "Ditemukan pada indeks ke -", {int(e)} ,"kolom" ,{CariData})
                exit()
    while arr[int(min(cara, f)-1)] < t:
                r = cara
                cara += math.sqrt(f)
                if r >= f:
                    return -1
    while arr[int(r)] < t:        
                r += 1
                if r == min(cara, f):
                    return -1
    if arr[int(r)] == t:
            return int(r)
    return -1

def SearchJump(w,o,i):
    v = JumpSearch(w,o,i)
    if v == -1:
        print(o,"Tidak ditemukan")
    else:
        print(o,"Ditemukan pada indeks ke -", v)

Array = ["Arsel","Avivah","Daiva",["Wahyu","Wibi"]]

h = len(Array)
while True:
    elemen = input("Masukan nama yang ingin dicari :")
    SearchJump(Array,elemen,h)
    break