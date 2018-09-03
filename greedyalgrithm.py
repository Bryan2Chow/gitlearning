d=[1,2,5,10,20,50,100]#纸币面值
d_num=[3,1,2,1,2,3,5]#纸币数量
s=0#纸币总和
for i in range(0,len(d_num)):
    s+=d[i]*d_num[i]#计算收银员钱数
sum=float(input('请输入要找的零钱：'))
if sum>s:
    print('数据有错')
else:
    while i>=0:
        if sum>=d[i]:
            n=int(sum/d[i])
            if n>=d_num[i]:
                 n=d_num[i]
            sum-=n*d[i]
            print('用了%d个%f元纸币'%(n,d[i]))
        i-=1