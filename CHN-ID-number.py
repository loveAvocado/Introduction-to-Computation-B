
id_cn = (input("输入测试身份证号前17位：")) 


last_dig = None
id_new = []

#7、9、10、5、8、4、2、1、6、3、7、9、10、5、8、4、2 ;加权相加 %11 
系数表=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
if len(id_cn)==17:
    for n in range(17):
        id_new.append(int(id_cn[n]) * 系数表[n]) 
else:
    exit()

sum_id_new = sum(id_new)

#取模
last_dig = sum_id_new % 11
last_char = ""

if last_dig == 0:
    last_char = "1"
if last_dig == 1:
    last_char = "0"
if last_dig == 2:
    last_char = "X"
if last_dig == 3:
    last_char = "9"
if last_dig == 4:
    last_char = "8"
if last_dig == 5:
    last_char = "7"
if last_dig == 6:
    last_char = "6"
if last_dig == 7:
    last_char = "5"
if last_dig == 8:
    last_char = "4"
if last_dig == 9:
    last_char = "3"
if last_dig == 10:
    last_char = "2"

id_cn =str(id_cn) 
id_cn += last_char
print(id_cn)

# mapping 

