from getdata import getDF,but1,cel,getDFLocal

# df=getDF()

# b=but1(df,'en')
#
# print(b.bt1,b.bt2,b.bt3,b.bt4,b.bt5,sep='    ')
#
# b=but1(df)
#
# print(b.bt1,b.bt2,b.bt3,b.bt4,b.bt5,sep='    ')



df=getDFLocal()

for x in range(1,13):
    for y in range(2,46):
        # cel(df,4,2)
        if str(cel(df, x, y)) != 'nan':
            print('{}  {}  {}'.format(x,y,cel(df,x,y) if str(cel(df,x,y))!='nan' else ''))

# print('t' if not True else 'f')

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
