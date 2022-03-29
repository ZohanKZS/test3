from getdata import getDF,but1

df=getDF()

b=but1(df,'en')

print(b.bt1,b.bt2,b.bt3,b.bt4,b.bt5,sep='    ')

b=but1(df)

print(b.bt1,b.bt2,b.bt3,b.bt4,b.bt5,sep='    ')

# fg = 45
#
#
# def dfg():
#     global fg
#     fg = 5
#     print(fg)
#
#
# # print(dfg())
# dfg()
# print(fg)
