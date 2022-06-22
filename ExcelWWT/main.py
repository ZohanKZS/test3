from getData import getDF, but1, cel, getDFLocal

# df = getDFLocal()
df = getDF()

listData = []
listD = []

for x in range(1, 13):
    for y in range(2, 46):
        # cel(df,4,2)
        if str(cel(df, x, y)) != 'nan':
            # print('{}  {}  {}'.format(x, y, cel(df, x, y) if str(cel(df, x, y)) != 'nan' else ''))
            listD.append(x)
            listD.append(y)
            listD.append(cel(df, x, y) if str(cel(df, x, y)) != 'nan' else '')
            listData.append(listD)
            listD=[]

for it in listData:
    print(it)