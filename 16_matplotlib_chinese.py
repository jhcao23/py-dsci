# -*- coding: utf-8 -*-

__author__ = 'John'
__date__ = '2019-09-13'
__product__ = 'PyCharm'
__filename__ = '16_matplotlib_chinese'

"""
16 彻底解决matplotlib中文显示问题, 画箱形图及数据分析_笔记
http://www.ai111.vip/thread-232-1-1.html
"""

"""
设置中文和负号正常显示import matplotlib as mpl
mpl.rcParams['font.family'] = 'sans-serif'
mpl.rcParams['font.sans-serif'] = 'SimHei'
mpl.rcParams['axes.unicode_minus'] = False


如果是windwos系统 这样就可以生效了, 但是mac并不起作用, 或许也会有windows系统不起作用的, 那就可以尝试下面的方法, 
可以彻底解决matplotlib中文显示问题, 包括windows与mac系统
1 找到matplotlib 安装的目录, 修改matplotlibrc文件
删除font.family和font.sans-serif两行前的#, 并在font.sans-serif后添加对应的中文字体. 这里我们用的是中文简体 SimHei
print(mpl.matplotlib_fname())
2 将对应的字体SimHei.tff拷贝到matplotlib/mpl-data/fonts/ttf目录下
3 清空缓存文件
这一步很重要! 否则其他几步都是白忙活. 一定要清空matlibplot加载字体的缓存, 因为加载字体的时候要读取FontList文件, 
我们新加入的字体不在这个文件的列表, 加载时必然会报找不到字体的错: 
UserWarning: findfont: Font family [u'sans-serif'] not found. Falling back to Bitstream Vera Sans
  (prop.get_family(), self.defaultFamily[fontext]))
所以我们要前进到这个坑爹的文件夹下.  Windows和centos Ubuntu的一些清除缓存的命令, 可能并不适用于Mac系统! 
所以很多博客提供的命令, 直接不起作用啊! 所以稳妥起见, 还是手动删除缓存. 
有些博客上写的是FontList.cache, 但是我的机器上没有FontList.cache文件,但是有一个FontList.json文件, 
打开后发现, 这个文件详细记录了matplotlib加载字体的名称 路径. 
文件目路径是: /Users/lqhk/.matplotlib/FontList.json, 删除即可. 
下次调用matplotlib时, 会自动生成一个新的json文件. 

4 重启python与项目

设置图形的显示风格
plt.style.use('ggplot')
"""

"""
用pandas自带的画图工具更快
df1.boxplot()
plt.show()
"""

"""
箱形图的参数解析: 
x: 指定要绘制箱线图的数据；
notch: 是否是凹口的形式展现箱线图, 默认非凹口；
sym: 指定异常点的形状, 默认为+号显示；
vert: 是否需要将箱线图垂直摆放, 默认垂直摆放；
whis: 指定上下须与上下四分位的距离, 默认为1.5倍的四分位差；
positions: 指定箱线图的位置, 默认为[0,1,2…]；
widths: 指定箱线图的宽度, 默认为0.5；
patch_artist: 是否填充箱体的颜色；
meanline: 是否用线的形式表示均值, 默认用点来表示；
showmeans: 是否显示均值, 默认不显示；
showcaps: 是否显示箱线图顶端和末端的两条线, 默认显示；
showbox: 是否显示箱线图的箱体, 默认显示；
showfliers: 是否显示异常值, 默认显示；
boxprops: 设置箱体的属性, 如边框色, 填充色等；
labels: 为箱线图添加标签, 类似于图例的作用；
filerprops: 设置异常值的属性, 如异常点的形状 大小 填充色等；
medianprops: 设置中位数的属性, 如线的类型 粗细等；
meanprops: 设置均值的属性, 如点的大小 颜色等；
capprops: 设置箱线图顶端和末端线条的属性, 如颜色 粗细等；
whiskerprops: 设置须的属性, 如颜色 粗细 线的类型等；
"""

import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd

mpl.rcParams['font.family'] = 'sans-serif'
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False

print(mpl.matplotlib_fname())

df1 = pd.DataFrame({
    u'计算机应用基础': [85, 78, 81, 95, 70, 67, 82, 72, 80, 81, 77],
    u'西方经济学': [93, 81, 76, 88, 66, 79, 83, 92, 78, 86, 78],
    u'Math': [65, 95, 51, 74, 78, 63, 91, 82, 75, 71, 55],
    u'英语': [76, 90, 97, 71, 70, 93, 86, 83, 78, 85, 81],
})
print(df1)
# print(df1.describe())
# df1.boxplot()
# plt.show()
# plt.style.use('ggplot')
plt.boxplot(x=df1.values, labels=df1.columns, whis=1.5, showmeans=True)
# plt.ylim(0, 85)

plt.show()


"""
箱形图的数据分析: 

箱形图有5个参数: 
下边缘, 表示下边界；
下四分位数 (Q1) , 又称“第一四分位数”, 等于该样本中所有数值由小到大排列后第25%的数字；
中位数 (Q2) , 又称“第二四分位数”等于该样本中所有数值由小到大排列后第50%的数字；
上四分位数 (Q3) , 又称“第三四分位数”等于该样本中所有数值由小到大排列后第75%的数字；
上边缘, 表述上边界. 
上四分位数与下四分位数的差距又称四分位间距IQR=Q3-Q1
箱型图无需对数据进行正态分布要求. 适用范围广.  (判断异常的其他方法比如3西伽马,z分数方法都要求数据服从正态分布. 
箱形图可以用来观察数据整体的分布情况, 利用中位数, 25%分位数, 75%分位数, 
通过计算这些统计量, 生成一个箱体图, 箱体包含了大部分的正常数据, 而在箱体上边界和下边界之外的, 就是异常数据. 
其中上下边界的计算公式如下: 
UpperLimit=Q3+1.5IQR=75%分位数+ (75%分位数-25%分位数) *1.5, 
LowerLimit=Q1－1.5IQR=25%分位数- (75%分位数-25%分位数) *1.5
IQR表示上下四分位差, 系数1.5是一种经过大量分析和经验积累起来的标准, 一般情况下不做调整. 

那为什么要引入箱形图呢? 
1.为了反映原始数据的分布情况, 比如数据的聚散情况和偏态. 
2.箱型图有个功能就是可以检测这组数据是否存在异常值. 异常值在哪里呢? 就是在上边缘和下边缘的范围之外. 
3.可以直观地比较多组数据的情况. 
http://www.ai111.vip/forum.php?mod=attachment&aid=MTV8NTNjMmM5YzJ8MTU2ODQxNTY4Nnw0OHwyMzI%3D&nothumb=yes
"""


