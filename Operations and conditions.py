a=20 # integer one
b=30 # integer two
if a<b: #true
    print("this is if")
elif a<b: # ture
    print("this is elif")
else: #false
    print("this is else")


srinu=28
jiddu=24

if srinu>jiddu: # this is true
    print("this is outer if")
    if srinu<jiddu: # this is flase
       print("this is inner if")
    else:
       print("this is inner else")
else:
    print("this is outer else")



while (1,10001):
    print('while')

srinu=15
while srinu<17:
    print('srinu')
    srinu+=1
else:
    print('done')



for srinu in 'writer':
    print(srinu)


for srinu in range(1,20,5):
    print('srinu')



jumping statements

for b in 'srinu':
    if b=='n':
        break
    print('b')
    print('end')


for b in range(1,21):
    for s in range(1,11):
        print(b*s, end = " ")
    print()