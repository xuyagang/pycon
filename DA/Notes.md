[TOC]



## 第四章 Numpy基础

- numpya是高性能科学计算和数据分析的基础包
  - ndarray:一个具有矢量计算和复杂广播能力、快速节省空间的多维数组
  - 对整组数据进行快速数学计算
  - 读写磁盘数据
  - 线性代数、随机数生成、傅里叶变换等

- 对于数据分析而言主要功能：
  - 数据整理和清洗，子集构造和过滤，矢量转换
  - 常用数组算法：排序、唯一化、结合运算
  - 高效的描述统计和数据聚类
  - 用于异构数据集的合并/连接运算的数据对齐

### 输出精度

```
np.set_printoptions(
    precision=None,
    threshold=None,
    edgeitems=None,
    linewidth=None,
    suppress=None,
    nanstr=None,
    infstr=None,
    formatter=None,
    sign=None,
    floatmode=None,
    **kwarg,
)
```



### Nympy的ndarray:一种多维数组

- 一个通用的同构数据的多维容器

- 每个数组有shape和dtype

  - ```
    data.shape
    data.dtype
    ```

- 创建ndarray

  - array(序列)

    - 嵌套序列会转换为多维数组

    - np.array会为新数组推断出合适的数据类型

    - 数据类型保存在dtype对象中

      - ```
        array.dtype
        ```

    - ![000](D:\project\pycon\DA\img\000.JPG)

    - dtype的命名方式：一个类型名+一个用于表示元素位长的数字

      - ![001](D:\project\pycon\DA\img\001.JPG)

      - ![002](D:\project\pycon\DA\img\002.JPG)

        - 可以通过astype转换其dtype

          - ==调用astype都会创建一个新的数组，即使跟原来一样==

          - ```python
            arr = np.array([1,2,3,4])
            arr.astype('float64')
            ```

          - 如果浮点数转换为整数，小数部分会被截断

            - ```python
              arr = np.array([1.34,0.55,9.345,8.245])
              arr = arr.astype('int64')
              >>>array([1, 0, 9, 8], dtype=int64)
              ```

          - 如果某字符串全是数字，astype也可将其转换为数值

          - numpy会将python类型映射到等价的dytpe上

          - 简洁的代码表示dtyep

            - `dtype = 'u4'`

### 数组与标量运算

- 数组不用编写循环即可对数据执行批量运算—矢量化

- 大小相等的数组间的算术运算都会将运算应用到元素级

- 数组与矢量的运算会将那个标量传播到各个元素

- 不同大小数组之间的运算叫做广播（broadcasting）

- 基本的索引和切片

  - 将一个标量赋值给一个切片时（arr[5:8]=12）,该值会自动传播到选区

  - 数组切片是原始数组的视图，意味着==数据不会被复制，视图上的修改会直接反应到源数组上==

  - 如果想得到的ndarray切片是副本而非视图，就需要显式的复制

    - arr[5:8].copy()

  - 二维数组中，各个位置的元素不再是标量而是一维数组

    - ```python
      arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
      # 等价方式
      print(arr[0][1])
      print(arr[0,1])
      ```

      ![003](D:\project\pycon\DA\img\003.JPG)

  - 三维数组中标量和数组都可赋值给切片

  - 切片是沿着轴选取元素

  - 可以一次传入多个索引

    ```python
    arr3d = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
    arr3d[:1,1:2]
    ```

  - 数组子集都是视图
  - ： 冒号表示选取整个轴

- 布尔型索引

  - 布尔型数组可用于数组索引

  - 布尔型数组的长度必须跟被索引的轴长度一致

  - 布尔型数组也可以和切片、整数混合使用

  - 可以通过波浪符（~）和不等号（！=）对条件进行否定

    ```python
    names = np.array(['Bob','Joe','will','Joe','Joe','Adam','hh'])
    data = np.random.randn(7,4)
    # 结果一致
    ata[~(names=='Bob')]]
    data[names!='Bob']
    ```

  - 布尔索引选取数据总是__创建数据的副本__，即使返回一模一样的数组

  - 应用多个布尔条件使用 &（和） 、|（或）

    - python的and和or再布尔数组中无效

  - 将data中所有的负值设置为0

    ```
    data[data<0]=0
    ```

- 花式索引（Fancy indexing）

  是指利用整数数组进行索引

  ```python
  arr = np.empty((8,4))
  for i in range(8):
      arr[i] = i
  # 特定顺序选取  行  子集,传入特定顺序的列表或ndarray
  arr[[3,2,1,4]]
  ```

  - 使用负数索引将会从末尾开始选取

  - 一次传入多个索引数组，将返回一个一维数组，对应各个索引元祖

    ```python
    arr = np.arange(32).reshape(8,4)
    arr[[1,5,7,2],[0,3,1,2]]
    >>> 返回arr[1][0],arr[5][3],arr[7][1],arr[2][2]
    ```

  - 选区矩形区域

    ```python
    # 方法一
    arr[[1,5,7,2]][:,[0,3,1,2]]
    # 方法二
    arr[np.ix_([1,5,7,2],[0,3,1,2])]
    ```

  - 花式索引跟切片不一样，总是将数据复制到新的数组

- 数组转置和轴对换

  - 转置返回的是源数据的视图（不会进行任何操作）

  - 不仅用transpose方法，还有特殊的T属性

    - ```python
      arr = np.arange(15).reshape((3,5))
      arr.T
      >>>array([[ 0,  5, 10],
             [ 1,  6, 11],
             [ 2,  7, 12],
             [ 3,  8, 13],
             [ 4,  9, 14]])
      ```

    - np.dot计算矩阵内积  X<sup>T</sup>X

      ```
      np.dot(arr,arr.T)
      ```

  - 对于高维的数组，transpose需要一个由轴编号组成的元祖进行转置

    ```
    arr = np.arange(16).reshape((2,2,4))
    arr.transpose((1,0,2))
    ```

  - ndarray还有一个swapaxes的方法，需要接受一对轴编号

    __返回源数据的视图__

    ```
    arr.swapaxes(1,2)
    ```

- 通用函数

  - 一元ufunc

    ![004](D:\project\pycon\DA\img\004.JPG)

    ![005](D:\project\pycon\DA\img\005.JPG)

  - 二元ufunc

    ![006](D:\project\pycon\DA\img\006.JPG)

- 利用数组进行数据处理

  - numpy可以使你将许多种数据处理任务表述为简洁的表达式

  - 用数组表达式代替循环的做法，通常被称为矢量化

  - 广播是针对矢量化计算的强大手段

    - numpy.meshgrid函数接受两个一维数组，并产生两个二维矩阵

      ```
      points = np.arange(0,5)
      xs,ys= np.meshgrid(points,points)
      print(xs)
      print(ys)
      >>>
      [[0 1 2 3 4]
       [0 1 2 3 4]
       [0 1 2 3 4]
       [0 1 2 3 4]
       [0 1 2 3 4]]
      [[0 0 0 0 0]
       [1 1 1 1 1]
       [2 2 2 2 2]
       [3 3 3 3 3]
       [4 4 4 4 4]]
      ```

- 将条件逻辑表述为数组运算

  ```python
  xarr = np.array([1.2,1.3,1.4,1.5])
  yarr = np.array([2.1,2.2,2.3,2.4,2.5])
  cond = np.array([True,False,True,True,False])
  
  result = [x if c else y
           for x,y,c in zip(xarr,yarr,cond)]
  result
  >>>[1.2, 2.2, 1.4, 1.5]
  ```

  - 以上做法的缺点：

    - 速度不快，因为是工作是纯python完成
    - 无法用于多维数组

  - numpy.where函数是三元表达式__x if condition else y__的是矢量化版本

    - 简洁操作

      ```
      numpy.where(cond,xarr,yarr)
      ```

      - numpy.where（）的第二三个参数不必是数组，可以是标量

      - 通常用于根据一个数组产生一个新的数组

        ```
        arr = np.random.randn(4,4)
        np.where(arr>0,2,-2)
        >>>array([[ 2, -2, -2, -2],
               [-2, -2,  2,  2],
               [ 2, -2, -2, -2],
               [-2, -2,  2,  2]])
        ```

      - for循环改写嵌套where表达式

        ```python
        result = []
        for i in range(n):
            if cond1[i] and cond2[i]:
                result.append(0)
            if cond1[i]:
                resuslt.append(1)
            if cond2[2]:
                result.append(2)
            else:
                result.append(3)
                
        # 等价于
        np.where(cond1 & cond2,0,
                np.where(cond1,1,
                        np.where(cond2,2,3)))
        ```

- 数学和统计方法

  - sum 对数组全部或某轴的元素求和，零长度的数组sum=0

  - mean 算术平均数,零长度的数组mans=NaN

  - std、var 标准差和方差，自由度可调（默认为n）

  - min、max 最大最小值

  - argmin、argmax 分别为==最大最小元素的索引==

  - cumsum 所有元素的累计和

    ```python
    [-1 -1 -1 -1 -1 -1  1 -1  1 -1]
    # cumsum的结果：
    [-1 -2 -3 -4 -5 -6 -5 -6 -5 -6]
    ```

    

  - cumprod 所有蒜素的累计积

- 布尔型数组方法

  - 数学和统计计算会将布尔值转换为 1（Ture) 和 0 （false）
  - any 和all对布尔型数组非常有用

- 排序

  - numpy数组也可以通过sort方法排序
  - 多维数组可以在任何一个轴向上进行排序，只需要将轴号传给sort

- 唯一化以及其他集合逻辑

  - unique(x)   计算x中的唯一元素，并返回有序结果
  - intersect1d(x,y)   计算x和y中的公共元素，并返回有序结果
  - union1d(x,y)   计算x,y的并集，并返回有序结果
  - in1d(x,y)   得到一个’x的元素是否包含与y‘ 的布尔型数组
  - setdiff1d(x,y)   集合的差，即元素在x中且不再y中
  - setxor1d(x,y)   集合的对称差，即存在与一个数组中，但不同时存在与两个数组中的元素

- 将二进制数组保存到磁盘

  - np.save()

  - np.load()

    > 默认情况下,数组是以未压缩的原始二进制格式保存在.npy文件中

    ```
    arr = np.arange(10)
    np.save('test',arr)
    np.load('test.npy')
    ```

  - np.savez可以将多个数组保存到一个压缩文件中，将数组以关键字参数传入即可

    ```python
    arr = np.arange(10)
    np.savez('test',a = arr, b = arr)
    np.load('test.npz')['a']
    ```

- 存取文本文件

  - np.loadtxt('test.txt',delimiter=',')
  - np.genfromtxt()   和loadtxt差不多，面向的是结构化数组和缺失数据处理
  - np.savetxt()    将数组以某个分隔符写入文本中

### 线性代数

线性代数（如矩阵乘法，矩阵分解，行列式以及其他）是任何数组库的组成部分

- diag   以一维数组的形式返回方阵的对角线或非对角线元素，或将一维数组转换为方阵（非对角线元素为0）
- dot   矩阵乘法
- trace   计算对角线元素的和
- det   计算矩阵行列式
- eig   计算方阵的本征值和本征向量
- inv   计算方阵的逆
- pinv   计算矩阵的moore-penrose伪逆
- qr   计算QR分解
- svd   计算奇异值分解
- solve   解线性方程Ax  = b ,其中A为一个方阵
- lstsq   计算Ax = b的最小二乘解

### 随机数生成

- seed   确定随机数生成的种子
- permutation   返回一个序列的随机排列或返回一个随机排列的范围
- shuffle    对一个序列随机的排序
- rand   产生均匀分布的样本
- randint   从给定的范围内随机选区整数   randint(low, high=None, size=None, dtype='l')
- randn   产生正态分布(平均值0，标准差为1)的样本
- binomial   产生二项分布的样本值
- beta   产生beta分布的样本值
- chisquare 产生卡方分布的样本值
- gamma   产生gamma分布的样本值
- uniform   产生在[0,1]中均匀分布的样本值

### axis的理解

[参考](<https://blog.csdn.net/xiongchengluo1129/article/details/79062991>)

```python
import numpy as np
arr=np.arange(16).reshape(2,4,2)
arr
>array([[[ 0,  1],
        [ 2,  3],
        [ 4,  5],
        [ 6,  7]],

       [[ 8,  9],
        [10, 11],
        [12, 13],
        [14, 15]]])
# arr的shape为（2,4,2），arr的shape下标为(0,1,2)
>>> arr.sum(axis=0)
array([[ 8, 10],
       [12, 14],
       [16, 18],
       [20, 22]])
>>> arr.sum(axis=1)
array([[12, 16],
       [44, 48]])
>>> arr.sum(axis=2)
array([[ 1,  5,  9, 13],
       [17, 21, 25, 29]])

# axis = i ,就是跨该轴计算
```



## 第五章   pandas 入门

pandas是基于numpy构建的，让以numpy为中心的应用变得简单

- Series和DATa Frame用的次数比较多，所以将其引入本地命名空间

`from pandas import Series,DataFrame`

`import pandas as pd`

### Series

- 类似与一维数组的对象，由一组数据以及一组与之相关的数据标签组成

- 会自动创建0到N-1的整数索引（N为数据长度）

- 如果传入的data和index都是list,则元素个数必须对应，如果传入的data是字典格式，则index可随意，结果的个数和传入的index有关系,此时使用NA表示缺失数据，自动对齐不同索引数据

  ```python
  sdata = {'ohio':35000,'texas':7100,'oregon':16000,'utah':5000}
  states={'california','texas','haha','hello','wuwu'}
  obj = pd.Series(sdata,index=states)
  obj
  >>>haha             NaN
  california       NaN
  hello            NaN
  wuwu             NaN
  texas         7100.0
  dtype: float64
  ```

- 使用NA表示缺失数据

  - isnull 和 notnull 用于检测缺失数据

- 通过Series的values 和 index 属性获取数组和索引

  ```python
  obj = Series([4,7,-5,3])
  obj.values
  >>>array([ 4,  7, -5,  3], dtype=int64)
  obj.index
  >>>RangeIndex(start=0, stop=4, step=1)
  ```

- 也可以传入数组对象作为索引

  ```python
  obj = Series([1,2,3,4],index=['a','b','c','d'])
  ```

- 可以通过字典创建Series

  `Series(dict_data)`

- Series的算术运算会自动对齐不同索引的数据

- Series和其索引都有一个name属性

  ```
  obj = Series([4,7,-5,3])
  obj.name = 'test'
  obj.index.name = 'haha'
  obj
  >>>haha
      0    4
      1    7
      2   -5
      3    3
      Name: test, dtype: int64
  ```

- Series 的索引可以通过赋值的方式就地修改，长度必须匹配

### DataFrame

DataFrame是一个表格型的数据结构，有一组有序的列，每列有不同的值类型，既有行索引也有列索引，可以看作是Series组成的字典

- 构建方法（data,columns,index）

  >构建方法有很多，最常用的是传入一个等长的列表或Numpy数组组成的字典

  ```python
  data = {'state':['a','b','c','d','d'],
         'year':[2011,2002,2001,2011,2003],
         'pop':[1.5,1.7,6.3,2.9,2.4]}
  frame = DataFrame(data)
  >>>  state  year  pop
  0     a  2011  1.5
  1     b  2002  1.7
  2     c  2001  6.3
  3     d  2011  2.9
  4     d  2003  2.4
  ```

  - DataFrame 会自动加上索引，并有序排列

  - 如果指定了列顺序，DataFrame会按顺序排列

  - 数据找不到会产生NA值

  - 可以通过列名获取列，通过==ix==获取==行==

  - 列可以通过赋值的方式修改，赋值的长度必须和原列长度匹配

  - 如果赋值的是series,则会精确匹配索引，空位填上缺失值

  - 为不存在的列赋值会创建新列，关键字==dell== 用于删除 ==列==

    `del frame1['列名']`

    > 通过索引方式返回的列是相应数据的视图（非副本），对返回的series做的修改会反应到源DataFrame上
    >
    > - 通过series 的copy方法可以显式的复制列

  - 把嵌套字典传给DATa Frame，外层的键会被作为列，内层键会被做为行索引，当然也可以对结果进行转置

    ```python
    pop = {'a':{'A':1,'B':2},
          'b':{'C':3},'D':5}
    df = pd.DataFrame(pop)
    print(df)
    print(df.T)
    
    >>>  a    b  D
    A  1.0  NaN  5
    B  2.0  NaN  5
    C  NaN  3.0  5
    
         A    B    C
    a  1.0  2.0  NaN
    b  NaN  NaN  3.0
    D  5.0  5.0  5.0
    ```

  - 可输入DataFrame的数据

    - 二维ndarray
    - 数组、列表或元组组成的字典
    - numyp的结构化数组（类似由数组组成的字典）
    - 由series组成的字典
    - 字典组成的字典
    - 字典或series的列表
    - 列表或元组的列表
    - 另外的DataFrame
    - numpy的maskedarray

  - 设置index和columns的名字

    ```python
    frame1.index.name = 'year'
    frame1.columns.name = 'state'
    df
    >>>AAA    a    b
    aaa          
    A    1.0  NaN
    B    2.0  NaN
    C    NaN  3.0
    D    NaN  5.0
    ```

  - 获取values值

    `frame1.values`

- 索引对象

  > 索引对象负责管理轴标签和轴名称等

  - index对象是不可修改的（immutable），这样才能保证index对象在多个数据结构之间安全共享

  - index对象
    - index                           将轴标签表示为一个python对象组成的Numpy数组
    - int64Index                  针对整数的特殊index
    - MultiIndex                  层次化索引对象
    - DatetiemIndex           存储纳秒级时间戳
    - PeriodIndex                时间间隔
  - index的方法和属性
    - append                        连接另一个index对象
    - diff                                计算差集
    - intersection                 计算交集
    - union                            计算并集
    - isin                                计算一个指示各值是否都包含在参数集合中的布尔型数组
    - delete                           删除索引 i 处的元素，得到新的index
    - drop                              删除传入的值，得到新的index
    - insert                            将元素插入到索引  i  处
    - is_monotonic(单调的)               当各元素均大于前一个元素时，返回True 
    - is_unique                      当index没有重复时，返回true
    - unique                           计算index中的唯一值数组

- 基本功能

  - 重新索引

    > pandas对象的一个重要方法是reindex,其作用是创建一个适应新索引的对象

    ```python
    obj = pd.Series([4.5,7.2,-5.3,3.6],index=['d','b','a','c'])
    obj
    >>>d    4.5
    b    7.2
    a   -5.3
    c    3.6
    dtype: float64
    
    # reindex 会根据索引重排，当索引值不在时引入缺失值
    obj2 = obj.reindex(['a','b','c','d','e'])
    obj2
    >>>a   -5.3
    b    7.2
    c    3.6
    d    4.5
    e    NaN
    dtype: float64
    # 给缺失值赋值
    obj.reindex(['a','b','c','d','e'],fill_value=0)
    >>>a   -5.3
    b    7.2
    c    3.6
    d    4.5
    e    0.0
    dtype: float64
    ```

  - 插值处理 method

    - ffill 或 pad                             向前填充值

    - bfill 或 backfill                      向后填充值

      ```
      obj3 = pd.Series(['blue','yellow','red'],index=[0,2,3])
      print(obj3)
      print(obj3.reindex(range(6),method='ffill'))
      >>>0      blue
      2    yellow
      3       red
      dtype: object
      0      blue
      1      blue
      2    yellow
      3       red
      4       red
      5       red
      dtype: object
      ```

    - 对于DataFrame，reindex 可修改行和列索引，如果传入一个 序列，则会重新索引行

      - 使用columns参数可重新索引列

      - 可同时对行列进行索引，而插值只能按行应用

        ```
        frame.reindex(index=['a','b','c','d'],columns=states).ffill()
        ```

      - 利用ix的标签索引功能

        ```
        frame.ix[['a','b','c','d'],states]
        ```

      - reindex的参数

        - index :索引新序列
        - method：插值方式 
        - fill_value:重新索引过程中引入缺失值时使用的替代值
        - limit:向前向后填充时的最大填充量
        - level:在multiindex的指定级别上匹配简单索引，否则选区其子集
        - copy:默认true,无论如何都复制

    - 对齐指定轴的项——drop()

      ```python
      obj = pd.Series(np.arange(5.),index=['a','b','c','d','e'])
      new_obj = obj.dorp('c')     
      >>>a    0.0
      b    1.0
      d    3.0
      e    4.0
      ```

      - 对于dataframe,可以删除任意轴上的索引

    - 索引、选取和过滤

      ```python
      # 索引选取和过滤
      obj = pd.Series(np.arange(4.),index = ['a','b','c','c'])
      print(obj['b'])
      # 必须嵌套两层
      print(obj[[1]])
      print(obj[2:4])
      print(obj[['b','a']])
      print(obj[[1,3]])
      print(obj[obj<2])
      
      # 标签的切片和python的普通切片不同，其末端是包含的
      print(obj['b':'d'])
      >>>b    1.0
      c    2.0
      d    3.0
      dtype: float64
      ```

      - 对DataFrame进行索引就是选区一个或多个==列==

        > 首先通过切片或布尔型数组选区行，这种语法源于实践
        >
        > 可通过布尔型DataFrame进行索引

        ```python
        data = pd.DataFrame(np.arange(16).reshape((4,4)),
                           index=['ohio','colorado','utah','new york'],
                           columns=['one','two','three','four'])
        data
        >one	two	three	four
        ohio	0	1	2	3
        colorado	4	5	6	7
        utah	8	9	10	11
        new york	12	13	14	15
        # 索引行——通过数字索引
        data[:2]
        # 索引列——通过列名
        data[['three','one']]
        # 布尔型
        data[data['three']<5]
        data[data['three']<5] = 0
        ```

      - 为了在DataFrame的==行==上进行标签索引，引入字段  ix 

        ```python
        # 可通过轴标签从DataFrame中选取行和列的子集
        data.ix['colorado', ['tow', 'three']]
        >tow      NaN
        three    6.0
        Name: colorado, dtype: float64
        
        data.ix[2]
        >one       8
        two       9
        three    10
        four     11
        Name: utah, dtype: int32
        ```

        loc：通过行标签索引数据

        iloc：通过行号索引行数据

        ix：通过行标签或行号索引数据（基于loc和iloc的混合）(废止函数)

    - 算术运算和数据对齐

      pandas可以对不同索引的对象进行算术运算，将对象相加时，如果有不同的索引对，则结果索引就是该索引对的并集

      ```python
      s1 = pd.Series([7.3,-2.5,3.4,1.5], index = ['a','c','d','e'])
      s2 = pd.Series([-2.1,3.6,-1.5,4,3.1], index=['a','c','e','f','g'])
      print(s1,s2,sep='\n')
      s1
      >a    7.3
      c   -2.5
      d    3.4
      e    1.5
      dtype: float64
      s2
      >a   -2.1
      c    3.6
      e   -1.5
      f    4.0
      g    3.1
      dtype: float64
      s1+s2
      >a    5.2
      c    1.1
      d    NaN
      e    0.0
      f    NaN
      g    NaN
      dtype: float64
      ```

      - 自动数据对齐在不重叠的索引处引入NA值，缺失值在 算术过程中brodcast

      - 对于dataframe对齐操作会发生在行和列上，相加后其索引和列为原来两个DataFrame的并集

      - 在算术方法中填充值

        - 在不同索引的对象进行算术运算时，你可能希望当一个对象的某个轴标签在另一个对象中找不到时填充一个特殊值（比如0)

          ```python
          df1 = pd.DataFrame(np.arange(12).reshape((3,4)), columns=list('abcd'))
          df2 = pd.DataFrame(np.arange(20).reshape((4,5)),columns=list('abcde'))
          print(df1,df2,sep='\n'+'_'*23+'\n')
          >   a  b   c   d
          0  0  1   2   3
          1  4  5   6   7
          2  8  9  10  11
          _______________________
              a   b   c   d   e
          0   0   1   2   3   4
          1   5   6   7   8   9
          2  10  11  12  13  14
          3  15  16  17  18  19
          
          # 相加时没有重叠的部分产生NA
          df1+df2
          >a	b	c	d	e
          0	0.0	2.0	4.0	6.0	NaN
          1	9.0	11.0	13.0	15.0	NaN
          2	18.0	20.0	22.0	24.0	NaN
          3	NaN	NaN	NaN	NaN	NaN
          
          # 使用add方法，并传入一个fill_value参数
          df1.add(df2, fill_value=0)
          >
          a	b	c	d	e
          0	0.0	2.0	4.0	6.0	4.0
          1	9.0	11.0	13.0	15.0	9.0
          2	18.0	20.0	22.0	24.0	14.0
          3	15.0	16.0	17.0	18.0	19.0
          ```

        - 在对Series和DataFrame重新索引时，可以指定一个填充值

          ```
          df1 = pd.DataFrame(np.arange(12).reshape((3,4)), columns=list('abcd'))
          df1
          >   a  b   c   d
          0  0  1   2   3
          1  4  5   6   7
          2  8  9  10  11
          
          # 生成新的DataFrame,而不是改变本身
          df1.reindex(columns=df2.columns, fill_value=0)
          >
          a	b	c	d	e
          0	0	1	2	3	0
          1	4	5	6	7	0
          2	8	9	10	11	0
          ```

          - add 加法
          - sub 减法
          - div 除法
          - mul 乘法

    - DataFrame和Series之间的运算

      ```python
      # 计算一个二维数组和某行的差
      arr = np.arange(12).reshape((3,4))
      arr - arr[0]
      >array([[0, 0, 0, 0],
             [4, 4, 4, 4],
             [8, 8, 8, 8]])
      ```

      这就是broadcasting，DataFrame和Series之间的运算也差不多如此

      ```python
      frame = pd.DataFrame(np.arange(12).reshape((4,3)),columns=list('bde'),
                           index=['utah','ohil','texas','oregon'])
      frame
      >	b	d	e
      utah	0	1	2
      ohil	3	4	5
      texas	6	7	8
      oregon	9	10	11
      
      series = frame.iloc[0]
      >
      b    0
      d    1
      e    2
      Name: utah, dtype: int32
      ```

      

      - 默认情况下，DataFrame和Series之间的运算会将Series的索引匹配到DataFrame的列，然后沿着行广播

        ```
        frame - series
        >
        b	d	e
        utah	0	0	0
        ohil	3	3	3
        texas	6	6	6
        oregon	9	9	9
        ```

        - 如果某个索引值在DataFrame的列或Series的索引中找不到，则参与计算的两个对象会被重新索引形成并集

          ```python
          series2 = pd.Series(range(3), index=list('bef'))
          frame + series2
          >
          b	d	e	f
          utah	0.0	NaN	3.0	NaN
          ohil	3.0	NaN	6.0	NaN
          texas	6.0	NaN	9.0	NaN
          oregon	9.0	NaN	12.0	NaN
          ```

  - 函数应用和映射

    numpy 的ufuncs(元素级数组方法)也可以用于操作pandas

    ```python
    frame = pd.DataFrame(np.random.randn(4,3), columns=list('bde'), 
                        index=['aa','cc','bb','dd'])
    frame
    >
    b	d	e
    aa	-0.484424	1.231815	0.329560
    cc	-0.276545	-0.136395	-0.228278
    bb	-0.725752	0.249103	1.876091
    dd	0.785835	1.555279	-0.884602
    
    np.abs(frame)
    >
    b	d	e
    aa	0.484424	1.231815	0.329560
    cc	0.276545	0.136395	0.228278
    bb	0.725752	0.249103	1.876091
    dd	0.785835	1.555279	0.884602
    ```

    另外一个常见的操作就是将函数应用到有各列或行组成的一维数组上，DataFrame的apply方法可实现：

    ```
    fun = lambda x: x.max() - x.min()
    frame.apply(fun)
    >b    1.511587
    d    1.691673
    e    2.760692
    dtype: float64
    
    frame.apply(fun, axis=1)
    >aa    1.716239
    cc    0.140150
    bb    2.601843
    dd    2.439880
    dtype: float64
    ```

    许多常见的数组统计功能都被实现为DataFrame的方法

    除标量值外，传递给apply的函数也可以返回多个值组成的Series

    ```python
    def f(x):
        return Series([x.min(), x.max()], index=['min', 'max'])
    frame.apply(f)
    >	b	d	e
    min	-0.725752	-0.136395	-0.884602
    max	0.785835	1.555279	1.876091
    ```

    元素即的python函数也可以，如：将frame中各个浮点数格式化字符串，使用applymap

    ```python
    # format的方法会报错
    # fm = lambda x:format(x, '.2f')
    fm = lambda x:'%.2f' %x
    frame.applymap(fm)
    >>>b	d	e
    aa	-0.48	1.23	0.33
    cc	-0.28	-0.14	-0.23
    bb	-0.73	0.25	1.88
    dd	0.79	1.56	-0.88
    ```

    Series有一个应用于元素级函数的map方法：

    > eries的map方法可以接受一个函数或含有映射关系的字典型对象
    >
    > 使用map是一种实现元素级转换以及其他数据清理工作的便捷方式
    >
    > （DataFrame中对应的是applymap()函数，当然DataFrame还有apply()函数）

    ```python
    # map accepts a dict or a Series. Values that are not found in the dict are 
    # converted to NaN, unless the dict has a default value
    s = pd.Series(['cat', 'dog', np.nan, 'rabbit'])
    s = pd.Series(['cat', 'dog', np.nan, 'rabbit'])
    >>>
    0   kitten
    1    puppy
    2      NaN
    3      NaN
    dtype: object
    ```

  - 排序和排名

    根据条件对数据集排序（sorting)也是一种重要的内置运算。要对行或列排序，可使用sort_index方法，将返回一个已排序的新对象

    `frame.sort_index(axis=0, level=None, ascending=True, inplace=False, kind='quicksort', na_position='last', sort_remaining=True, by=None)`

    ```python
    obj = pd.Series(range(4), index=list('dabc'))
    obj.sort_index()
    >>>
    a    1
    b    2
    c    3
    d    0
    dtype: int64
    ```

    对于DataFrame可根据任意一个轴上的索引进行排序

    ```python
    frame = pd.DataFrame(np.arange(8).reshape((2,4)), index=['three', 'one'], columns=list('dabc'))
    frame.sort_index()
    >>>
    d	a	b	c
    one	4	5	6	7
    three	0	1	2	3
    
    frame.sort_index(axis=1)
    >>>
    a	b	c	d
    three	1	2	3	0
    one	5	6	7	4
    ```

    默认是升序的，也可以降序排列

    ```
    frame.sort_index(axis=1, ascending=False)
    >>>
    d	c	b	a
    three	0	3	2	1
    one	4	7	6	5
    ```

    要对Series进行排序，可使用其sort_values方法

    ```python
    obj = Series([4, 7, -3, 2])
    obj.sort_values()
    >>>
    2   -3
    3    2
    0    4
    1    7
    dtype: int64
        
    # 缺失值默认放到末尾
    obj = pd.Series([4,np.nan, 7, -3,np.nan, 2])
    obj.sort_values()
    >>> 
    3   -3.0
    5    2.0
    0    4.0
    2    7.0
    1    NaN
    4    NaN
    dtype: float64
    ```

    对DataFrame根据多个列进行排序,使用sort_values

    `frame.sort_values(by, axis=0, ascending=True, inplace=False, kind='quicksort', na_position='last')`

    ```
    frame = pd.DataFrame({'b':[4,7,-3,2],'a':[0,1,0,1]})
    frame.sort_values(by='b')
    >>>
    b	a
    2	-3	0
    3	2	1
    0	4	0
    1	7	1
    
    # 根据多列排序，传入列名的列表给by
    frame.sort_values(by=['a', 'b'])
    >>>
    b	a
    2	-3	0
    0	4	0
    3	2	1
    1	7	1
    ```

    排名（ranking）跟排序关系密切，且会增设一个排名值，可以根据某种规则破环平级关系

    ```python
    obj.rank(axis=0, method='average', numeric_only=None, na_option='keep', ascending=True, pct=False)
    
    method : {'average', 'min', 'max', 'first', 'dense'}
        * average: average rank of group
        * min: lowest rank in group
        * max: highest rank in group
        * first: ranks assigned in order they appear in the array
        * dense: like 'min', but rank always increases by 1 between groups
    
    
    obj = pd.Series([7,-5,7,4,2,0,4])
    # 默认情况下是为各组分配一个平均排名
    obj.rank()
    >>>
    0    6.5
    1    1.0
    2    6.5
    3    4.5
    4    3.0
    5    2.0
    6    4.5
    dtype: float64
    
    # 根据值在原数据中出现的顺序排名
    obj.rank(method='first')
    0    6.0
    1    1.0
    2    7.0
    3    4.0
    4    3.0
    5    2.0
    6    5.0
    dtype: float64
    ```

    排名时破坏平衡关系的method选项

    - average      默认：在相等分组中，为各个值分配平均排名

    - min             相同的排名使用整个分组的最小排名

    - max            相同排名使用整个分组的最大排名

    - first             按值在原始数据中出现的顺序分配排名

      ```python
      df = pd.DataFrame(data={'Animal': ['cat', 'penguin', 'dog', 'spider', 'snake'],
                              'Number_legs': [4, 2, 4, 8, np.nan]})
      df
      >>>
      Animal	Number_legs
      0	cat	4.0
      1	penguin	2.0
      2	dog	4.0
      3	spider	8.0
      4	snake	NaN
      
      df['default_rank_average'] = df['Number_legs'].rank(method='average')
      df['max_rank'] = df['Number_legs'].rank(method='max')
      df['min_rank'] = df['Number_legs'].rank(method='min')
      df['first_rank'] = df['Number_legs'].rank(method='first')
      df['NA_botton'] = df['Number_legs'].rank(na_option='bottom')
      df['pct_rank']  = df['Number_legs'].rank(pct=True)
      df
      >>>	Animal	Number_legs	default_rank_average	max_rank	min_rank	first_rank	NA_botton	pct_rank
      0	cat	    4.0	2.5	3.0	2.0	2.0	2.5	0.625
      1	penguin	2.0	1.0	1.0	1.0	1.0	1.0	0.250
      2	dog	    4.0	2.5	3.0	2.0	3.0	2.5	0.625
      3	spider	8.0	4.0	4.0	4.0	4.0	4.0	1.000
      4	snake	NaN	NaN	NaN	NaN	NaN	5.0	NaN
      ```

  - 带有重复值的轴索引

    许多pandas函数(reindex)都要求标签唯一，但并不是强制性的

    ```python
    # 有重复索引的Series
    obj = pd.Series(range(5), index=['a','a','b','b','c'])
    obj
    >>>
    a    0
    a    1
    b    2
    b    3
    c    4
    dtype: int64
        
    # 索引的is_unique属性可告诉你是否唯一
    obj.index.is_unique
    >>>False
    ```

    带有重复索引的对象，数据选取时，索引对应多个值则返回Series,索引对应单个值则返回标量

    ```python
    obj['c']
    >>>4
    obj['a']
    >>>
    a    0
    a    1
    dtype: int64
    ```

#### 汇总和计算描述统计

pandas拥有一组常用的数学和统计方法，用于从Series中提取单个值，或从DataFrame中提取一个Series,跟对应的Numpy数组方法相比，他们都是基于没有缺乏数据的假设而构建的

```
# 按列求和
df.sum()
# 按行求和
df.sum(axis=1)
# NA值会自动被排除，除非整个切片都是NA
# skipna选项可以禁用该功能，含有NA的行或列求解为NA

obj.mean(axis=None, skipna=None, level=None, numeric_only=None, **kwargs)
```

约简方法选项

- axis 约简的轴
- skipna   排除缺失值，默认为True
- level   如果轴是层次化索引的，则根据level分组约简

有些轴是间接统计的，比如idxmin 和 idxmax

有些则是累计型的，比如 cumsum

有些既不是约简也不是累计，而是一次性产生多个汇总统计，比如describe

描述和统计汇总：

| 方法           | 说明                             |
| -------------- | -------------------------------- |
| count          | 非NA值的数量                     |
| describe       | 计算汇总统计                     |
| min、max       | 最值                             |
| idxmin、idxmax | 获取到最大、最小值的索引         |
| quantile       | 样本的分位数（0到1）             |
| sum            | 和                               |
| mean           | 均值                             |
| median         | 算术中位数（50%分位数）          |
| mad            | 根据均值计算平均绝对离差         |
| var            | 样本值的方差                     |
| std            | 样本值的标准差                   |
| skew           | 样本值的偏度(三阶矩)             |
| kurt           | 样本值的峰度（si'jie）           |
| cumsum         | 样本值的累计和                   |
| cummin、cummax | 累计值的最值                     |
| cumprod        | 样本值的累计积                   |
| diff           | 计算一阶差分（对时间序列很有用） |
| pct_change     | 计算百分数变化                   |

#### 相关系数和协方差

有些统计，比如相关系数和协方差是通过参数对计算出来的

```
pandas-datareader
# pip3 install pandas_datareader
# to download some data for a few stock tickers
import pandas_datareader.data as web
```

- corr计算相关系数

  > 相关关系是一种非确定性的关系，相关系数是研究变量之间[线性相关](https://baike.baidu.com/item/%E7%BA%BF%E6%80%A7%E7%9B%B8%E5%85%B3)程度的量。由于研究对象的不同

- cov 计算协方差

  > 协方差用于衡量两个变量的总体误差

dataframe的这两个方法将以DataFrame的形式返回完整的相关系数或协方差矩阵

```
returns.corr()
>	AAPL	IBM	MSFT	GOOG
AAPL	1.000000	0.379356	0.452113	0.457141
IBM	0.379356	1.000000	0.487115	0.400139
MSFT	0.452113	0.487115	1.000000	0.534055
GOOG	0.457141	0.400139	0.534055	1.000000
```

利用DataFrame的corrwith方法，计算其列或行跟另外一个Series或DataFrame之间的相关系数

- 传入Series将会返回一个相关系数值Series
- 传入一个DataFrame则会计算按列名称配对的相关系数

#### 唯一值、值计数以及成员资格

还有一类方法可以从一维Series的值中抽取信息

- unique:得到Series中的唯一值数组

  ```python
  obj = pd.Series(['c', 'a', 'd', 'a', 'a', 'b', 'b', 'c', 'c'])
  uniques = obj.unique()
  >array(['c', 'a', 'd', 'b'], dtype=object)
  # 返回值是未排序的，如果需要排序可以
  uniques.sort()
  > array(['a', 'b', 'c', 'd'], dtype=object)
  ```

- ==values_counts==:用于计算一个Series中==各值出现的频率==

  ```python
  # obj.value_counts(normalize=False, sort=True, ascending=False, bins=None, dropna=True)
  obj.value_counts()
  >a    3
  c    3
  b    2
  d    1
  dtype: int64
  ```

- isin:用于判断矢量化集合的成员资格

  ```python
  obj.isin(['b','c'])
  0     True
  1    False
  2    False
  3    False
  4    False
  5     True
  6     True
  7     True
  8     True
  dtype: bool
  ```

- ```python
  apply(func, axis=0, broadcast=None, raw=False, reduce=None, result_type=None, args=(), **kwds) method of pandas.core.frame.DataFrame instance
  # Apply a function along an axis of the DataFrame.
  ```

#### 处理缺失值

python中的None也会被当作NA处理

- dropna:根据各标签的值是是否存在缺失数据对轴标签进行过滤，可通过阈值调整对缺失值的容忍度
- fillna：用指定值或插值方法ffill或bfill填充缺失数据
- isnall:返回一个含有布尔值的对象
- notnull:isnull的否定形式

##### 滤掉缺失数据

```python
# 对于DataFrame,dropna默认丢弃任何含有缺失值的行
data.dropna()
# 或
data[data.notnull()]

# 传入how='all'将只丢弃全为NA的行
# 要丢弃列，只需传入axis=1

# 对于时间序列数据，只想留下部分数据，可以用thresh
df.dropna(thresh=3)
```

##### 填充缺失数据

不想过滤掉缺失信息，而是希望通过其他方式填补它，fillna方法是最主要的函数（将缺失值替换为常数）

```python
df
>Animal	Number_legs	default_rank_average	max_rank	min_rank	first_rank	NA_botton	pct_rank
0	cat	4.0	2.5	3.0	2.0	2.0	2.5	0.625
1	penguin	2.0	1.0	1.0	1.0	1.0	1.0	0.250
2	dog	4.0	2.5	3.0	2.0	3.0	2.5	0.625
3	spider	8.0	4.0	4.0	4.0	4.0	4.0	1.000
4	snake	NaN	NaN	NaN	NaN	NaN	5.0	NaN
df.fillna(0)
>Animal	Number_legs	default_rank_average	max_rank	min_rank	first_rank	NA_botton	pct_rank
0	cat	4.0	2.5	3.0	2.0	2.0	2.5	0.625
1	penguin	2.0	1.0	1.0	1.0	1.0	1.0	0.250
2	dog	4.0	2.5	3.0	2.0	3.0	2.5	0.625
3	spider	8.0	4.0	4.0	4.0	4.0	4.0	1.000
4	snake	0.0	0.0	0.0	0.0	0.0	5.0	0.000
```

- 通过一个字典调用fillna,就可以实现对不同列填充不同值

```
df.fillna({1:0.5, 3:-1})
df.fillna({'default_rank_average':0.5, 'first_rank':-1})
```

- fillna默认返回新的对象，也可以对现有对象进行就地修改: inplace

```
df.fillna(0, inplace=True)
```

- 对reindex有效的那些插值方式也可用于fillna

```
df.fillna(method='ffill')
df.fillna(method='ffill', limit=3)  # 限制修改个数
```

- fillna参数
  - value  用于填充的标量值或字典对象
  - method  插值方式，默认ffill,还有bfill
  - axis  待填充的轴，默认axis=0
  - inplace  修改调用对象是否产生副本
  - limit  可以连续填充的最大数量

#### 层次化索引

可以使你在一个轴上拥有多个索引级别（以低维度处理高维度数据）

```python
data = pd.Series(np.random.randn(10),
                index = [['a','a','a','b','b','b','c','c','d','d'],[1,2,3,1,2,3,1,5,8,3]])
data
>a  1    0.859286
   2   -0.110505
   3   -0.791249
b  1   -2.142436
   2   -0.019902
   3   -0.676113
c  1   -0.691733
   5    0.061846
d  8   -0.069086
   3    0.107944
dtype: float64
```

这是带有MultiIndex索引的Series,索引间的间隔表示使用上面的标签

```
data.index
>MultiIndex(levels=[['a', 'b', 'c', 'd'], [1, 2, 3, 5, 8]],
           labels=[[0, 0, 0, 1, 1, 1, 2, 2, 3, 3], [0, 1, 2, 0, 1, 2, 0, 3, 4, 2]])
```

选取子集

```python
data.b
data['b']
>1   -2.142436
2   -0.019902
3   -0.676113
dtype: float64

data['b':'c']
>b  1   -2.142436
   2   -0.019902
   3   -0.676113
c  1   -0.691733
   5    0.061846
dtype: float64

# 在内层选取
data[:,1]
>
a    0.859286
b   -2.142436
c   -0.691733
dtype: float64

# 将数据安排到dataframe中
data.unstack()
>	1	2	3	5	8
a	0.859286	-0.110505	-0.791249	NaN	NaN
b	-2.142436	-0.019902	-0.676113	NaN	NaN
c	-0.691733	NaN	NaN	0.061846	NaN
d	NaN	NaN	0.107944	NaN	-0.069086

# unstack的逆运算
data.unstack().stack()
>a  1    0.859286
   2   -0.110505
   3   -0.791249
b  1   -2.142436
   2   -0.019902
   3   -0.676113
c  1   -0.691733
   5    0.061846
d  3    0.107944
   8   -0.069086
dtype: float64
```

对于dataframe没条轴都可以有分层索引

```python
frame = pd.DataFrame(np.arange(12).reshape((4,3)),
                    index = [['a','a','b','b'],[1,2,1,2]],
                    columns = [['Ohio', 'Ohio', 'Colorado'],['Green', 'Red', 'Green']])
frame
>
Ohio	Colorado
Green	Red	Green
a	1	0	1	2
2	3	4	5
b	1	6	7	8
2	9	10	11
```

各层都可以有名字

```
frame.index.names = ['big','small']
frame.columns.names =['high','low']
frame
>
high	Ohio	Colorado
low	Green	Red	Green
big	small			
    a	1	0	1	2
    2	3	4	5
    b	1	6	7	8
    2	9	10	11
```

由于有了分部的列索引，可以轻松选取分组

```
frame['Ohio']
# 或
frame.Ohio
> 
low	Green	Red
big	small		
a	1	0	1
2	3	4
b	1	6	7
2	9	10
```

可以单独的创建MultiIndex然后复用

```
MultiIndex.from_arrays([['Ohio', 'Ohio', 'Colorado'], ['Green', 'Red', 'Green']],                       names=['state', 'color']) 
# pd.MultiIndex.from_arrays()
```

#### 重排分级顺序

有时需要重新调整某条轴上各级别的顺序，或根据指定级别上的值对数据进行排序

swaplevel接受两个级别编号或名称，返回 一个互换了级别的新对象（数据不会变化）

```python
frame
> 	high	Ohio	Colorado
low	Green	Red	Green
big	small			
a	1	0	1	2
2	3	4	5
b	1	6	7	8
2	9	10	11

frame.swaplevel('big','small')
>high	Ohio	Colorado
low	Green	Red	Green
small	big			
1	a	0	1	2
2	a	3	4	5
1	b	6	7	8
2	b	9	10	11
```

sortlevel根据单个级别中的值对数据进行排序

```
frame.sort_index(level=1)
>
high	Ohio	Colorado
low	Green	Red	Green
big	small			
a	1	0	1	2
b	1	6	7	8
a	2	3	4	5
b	2	9	10	11
```

#### 根据级别汇总统计

许多对dataframe和series的描述和汇总统计都有一个level选项，用于指定某条轴上求和的level

```python
# 求和
frame.sum(level='big')
>high	Ohio	Colorado
low	Green	Red	Green
big			
a	3	5	7
b	15	17	19

frame.sum(level='small')
>high	Ohio	Colorado
low	Green	Red	Green
small			
1	6	8	10
2	12	14	16
```

#### 使用dataframe的列

```python
 frame = pd.DataFrame({'a': range(7), 'b': range(7, 0, -1),
                       'c': ['one', 'one', 'one', 'two', 'two','two', 'two'],
                       'd': [0, 1, 2, 0, 1, 2, 3]})
frame
>   a	b	c	d
0	0	7	one	0
1	1	6	one	1
2	2	5	one	2
3	3	4	two	0
4	4	3	two	1
5	5	2	two	2
6	6	1	two	3

# dataframe的set_index函数会将其一个或多个列转换为行索引，创建一个新的dataframe
frame2 = frame.set_index(['c', 'd'])
>      a	b
c	d		
one	0	0	7
    1	1	6
    2	2	5
two	0	3	4
    1	4	3
    2	5	2
    3	6	1
# 默认情况下被修改的列会从dataframe中删除，也可将其保留下来
frame.set_index(['c','d'], drop=False)
> 	   a	b	c	d
c	d				
one	0	0	7	one	0
    1	1	6	one	1
    2	2	5	one	2
two	0	3	4	two	0
    1	4	3	two	1
    2	5	2	two	2
    3	6	1	two	3

# reset_index的功能和set_index刚好相反，层次化索引的级别会被转移到列里面
frame2.reset_index()
> 	c	d	a	b
0	one	0	0	7
1	one	1	1	6
2	one	2	2	5
3	two	0	3	4
4	two	1	4	3
5	two	2	5	2
6	two	3	6	1
```

#### 其他有关pandas的话题

##### 整数索引

```python
ser = pd.Series(np.arange(3.))
ser
>
0    0.0
1    1.0
2    2.0
dtype: float64
# 该操作会报错，很难判断出用户想要基于标签还是位置的索引
ser[-1]
```

对于非整数的索引，就没有这样的歧义

```
ser2 = pd.Series(np.arange(3,), index=['a','b','c'])
ser2
>
a    0
b    1
c    2
dtype: int32
ser2[-1]
> 2
```

如果需要可靠的、不考虑索引类型的、基于位置的索引，可以使用 loc 和 iloc

- loc使用行名

- iloc使用行序号

  ```python
  frame = pd.DataFrame(np.arange(6).reshape(3,2),index=[2,0,1])
  frame
  >
  	0	1
  2	0	1
  0	2	3
  1	4	5
  
  frame.iloc[1]
  >
  0    2
  1    3
  Name: 0, dtype: int32
          
  frame.loc[1]
  >
  0    4
  1    5
  Name: 1, dtype: int32
  ```

##### 面板数据





## 第六章 数据加载、存储与文件格式

输入输出通常分为几个大类：读取文本文件和其他更高效的磁盘存储格式、加载数据库中的数据、利用web API 操作网络资源

### 读写文本格式的数据

pandas中的解析函数：

- read_csv	从文件、URL或类文件对象加载带分隔符的数据;逗号作为默认分隔符
- read_table     从文件、URL或类似文件的对象加载带分隔符的数据;使用tab ('\t')作为默认分隔符
- read_fwf        读取固定宽度列格式的数据(即,没有分隔符)
- read_clipboard    从剪贴板读取数据的read_table版本;用于从web页面转换表
- read_excel      从Excel XLS或XLSX文件中读取表格数据
- read_hdf        读取pandas编写的HDF5文件
- read_html      读取给定HTML文档中的所有表
- read_json       从JSON (JavaScript对象表示法)字符串表示中读取数据
- read_msgpack     读取使用MessagePack二进制格式编码的panda数据
- read_pickle     读取以Python pickle格式存储的任意对象
- read_sas     读取以SAS系统的自定义存储格式之一存储的SAS数据集
- read_sql      将SQL查询的结果(使用SQLAlchemy)作为panda的dataframe数据
- read_stata    从Stata文件格式中读取数据集
- read_feather     Read the Feather binary file format

这些函数可以分为几类：

- 索引
- 类型推断和数据转换
- 日期解析
- 迭代（对大文件逐块迭代）
- 不规整数据问题（跳过一些行、页脚、注释等）

类型推断(type inference)是这些函数最重要的功能之一，无需指定类型是数值、整数、布尔还是字符串，日期和其他自定义类型需要多花点功夫

```python
pd.read_csv('./examples/ex1.csv')
>
	a	b	c	d	message
0	1	2	3	4	hello
1	5	6	7	8	world
2	9	10	11	12	foo

# 利用read_table读取需要加分隔符
pd.read_table('./examples/ex1.csv',sep=',')
>
	a	b	c	d	message
0	1	2	3	4	hello
1	5	6	7	8	world
2	9	10	11	12	foo

# 对于没有列名的数据读取
pd.read_csv('./examples/ex2.csv',header=None)
> 
	0	1	2	3	4
0	1	2	3	4	hello
1	5	6	7	8	world
2	9	10	11	12	foo

# names用于指定列名
pd.read_csv('./examples/ex2.csv',names=['a','b','c','d','message'])
>
a	b	c	d	message
0	1	2	3	4	hello
1	5	6	7	8	world
2	9	10	11	12	foo

# 用列做index使用 index_clo
names=['a','b','c','d','message']
pd.read_csv('./examples/ex2.csv',names=names,index_col='message')
> 
	a	b	c	d
message				
hello	1	2	3	4
world	5	6	7	8
foo	9	10	11	12

# 如果需要将多个列坐车一个层次化索引，之需传入由列编号或列名组成的列表即可
pd.read_csv('./examples/csv_mindex.csv',index_col=['key1','key2'])
pd.read_csv('./examples/csv_mindex.csv',index_col=[0,1])
>
		 value1	value2
key1	key2		
    one	a	1	2
        b	3	4
        c	5	6
        d	7	8
    two	a	9	10
        b	11	12
        c	13	14
        d	15	16
        
# 对于没有使用固定分隔符的，可以使用正则表达式作为分隔符
pd.read_csv('./examples/ex3.txt',sep='\s+')
pd.read_table('./examples/ex3.txt',sep='\s+')
>
       A	      B	          C
aaa	-0.264438	-1.026059	-0.619500
bbb	0.927272	0.302904	-0.032399
ccc	-0.264273	-0.386314	-0.217601
ddd	-0.871858	-0.348382	1.100491
```

- read_csv和read_table的参数解析

  | 参数             | 说明                                                         |
  | ---------------- | ------------------------------------------------------------ |
  | path             | 文件系统位置、url、文件类型对象的字符串                      |
  | sep or delimiter | 对字段进行拆分的字符序列或正则表达式                         |
  | header           | 用作列名的行号，默认为0（第一行），如果没有header行就设为None |
  | index_col        | 用作行索引的列编号或列名，可以是单个名称/数字/或由多个名称/数字组成（层次化索引） |
  | names            | 用于结果的列表名称，结合header=None                          |
  | skiprows         | 需要忽略的行数（从开始算起），或需要跳过的行号列表           |
  | na_values        | 一组用于替换NA的值                                           |
  | commend          | 用于将注释信息从行尾拆分出去的字符（一个或多个）             |
  | parse_dates      | 尝试将数据解析为日期，默认为False,如果为True,则尝试解析所有列，也可以指定需要解析的一组列号或列名，如果列表的元素为列表或元组，就会将多个列组合到一起再进行日期解析工作（例如日期和时间位于两个列中） |
  | keep_data_col    | 如果连接多列解析日期，则保持参与连接的列，默认False          |
  | converters       | 由列号/列名跟函数之间的映射关系组成的字典例如，{‘foo’:f}会对foo列的所有值应用函数f |
  | dayfirst         | 当解析有歧义的日期时，将其看作国际格式（7/6/2012—June 7,2012),默认为false |
  | date_parse       | 用于解析日期的函数                                           |
  | nrows            | 需要读取的行数（从开始算起）                                 |
  | iterator         | 返回一个TextParser以便逐块读取文件                           |
  | chunksize        | 文件块的大小,用于分段读取（每几行一个块）                    |
  | skip_footer      | 需要忽略的行数（从末尾算起）                                 |
  | verbose          | 打印各种解析器输出信息，比如“非数值列中缺失值的数量”等       |
  | encoding         | 用于unicode的文本编码格式，例如，’utf-8'表示用UTF-8编码的文本 |
  | squeeze          | 如果数据经解析后仅含一列，则返回Series                       |
  | thousands        | 千分位分隔符，如“，“或“.''                                   |

#### 逐块读取文本文件

在处理很大的文件时，或找出大文件中的参数以便后续处理，需要逐块读取

```python
# 可通过nrows读取前几行
pd.read_csv('./examples/ex6.csv',nrows=7)
>
one	two	three	four	key
0	0.467976	-0.038649	-0.295344	-1.824726	L
1	-0.358893	1.404453	0.704965	-0.200638	B
2	-0.501840	0.659254	-0.421691	-0.057688	G
3	0.204886	1.074134	1.388361	-0.982404	R
4	0.354628	-0.133116	0.283763	-0.837063	Q
5	1.817480	0.742273	0.419395	-2.251035	Q
6	-0.776764	0.935518	-0.332872	-1.875641	U

# 分段读取,每1000行一个块
chunker = pd.read_csv('./examples/ex6.csv',chunksize=1000)

# 将分段读取的数据聚合到key列
tot = pd.Series([])
for piece in chunker:
    tot = tot.add(piece['key'].value_counts(),fill_value=0)
    
tot = tot.sort_values(ascending = False)
tot[:10]
>
E    368.0
X    364.0
L    346.0
O    343.0
Q    340.0
M    338.0
J    337.0
F    335.0
K    334.0
H    330.0
dtype: float64
```

#### 将数据写出到文本

数据可输出为分隔符格式的文本，利用dataframe的to_csv方法可以将数据写到一个以逗号分隔的文件

```python
data.to_csv('./to_csv.csv')

# 利用其他分隔符,(sys.stdout的输出，所以仅仅是打印出文本，缺失值会表示为空字符串)
import sys
data.to_csv(sys.stdout,sep='|')
>
|something|a|b|c|d|message
0|one|1|2|3.0|4|
1|two|5|6||8|world
2|three|9|10|11.0|12|foo

# sys.stdout输出，将空字符串表示为其他字符
data.to_csv(sys.stdout, na_rep='NULL')
>
,something,a,b,c,d,message
0,one,1,2,3.0,4,NULL
1,two,5,6,NULL,8,world
2,three,9,10,11.0,12,foo

# 禁用行列标签
data.to_csv(sys.stdout, index=False, header=False)
>
one,1,2,3.0,4,
two,5,6,,8,world
three,9,10,11.0,12,foo

# 写出一部分的列，并以指定列序排列
data.to_csv(sys.stdout, index=False, columns=['a','b','c'],na_rep='NULL')
>
a,b,c
1,2,3.0
5,6,NULL
9,10,11.0

# Series的to_csv方法
dates = pd.date_range('1/1/2000',periods=7)
dates
>
DatetimeIndex(['2000-01-01', '2000-01-02', '2000-01-03', '2000-01-04',
               '2000-01-05', '2000-01-06', '2000-01-07'],
              dtype='datetime64[ns]', freq='D')
ts = pd.Series(np.arange(7), index=dates)
ts
>
2000-01-01    0
2000-01-02    1
2000-01-03    2
2000-01-04    3
2000-01-05    4
2000-01-06    5
2000-01-07    6
Freq: D, dtype: int32
        
ts.to_csv('series_to_csv.csv')
```

#### 手工处理分隔符格式

大部分存储在磁盘上的表格型数据都能使用pandas.read_table进行加载，然而有时还是需要做一些处理

对于任何单字符分隔的文件，可以直接使用python内置的csv模块，将任意已打开的文件或文件对象传给csv.reader

```python
import csv
f = open('./examples/ex7.csv')
reader = csv.reader(f)
for line in reader:
    print(line)
>
['a', 'b', 'c']
['1', '2', '3']
['1', '2', '3']

lines = list(csv.reader(open('./examples/ex7.csv')))
header,values = lines[0],lines[1:]
data_dict = {k:v for k,v in zip(header,zip(*values))}
data_dict
>{'a': ('1', '1'), 'b': ('2', '2'), 'c': ('3', '3')}

# zip用法注意事项
print(values)
> [['1', '2', '3'], ['1', '2', '3']]
for i in zip(values):
    print(i)
>(['1', '2', '3'],)
(['1', '2', '3'],)

for i in zip(*values):
    print(i)
> ('1', '1')
('2', '2')
('3', '3')

#  当zip只传入一个list的时候，会为其中的每项匹配一个空值
for i in zip([1,2,3,4]):
    print(i)
>
(1,)
(2,)
(3,)
(4,)
```

csv文件的形式有很多，只需要定义csv.Dialect的一个子类即可定义新的格式（专门的分隔符，字符串引用约定、行结束符等）

```python
class my_dialect(csv.Dialect):
    lineterminator = '\n'
    delimiter = ';'
    quotechar = '"'
reader = csv.reader(f,dialect=my_dialect)
```

csv.Dialect的属性：

| 参数             | 说明                                                         |
| ---------------- | ------------------------------------------------------------ |
| delimiter        | 用于分隔字段的但字符字符串，默认为 ‘，’                      |
| lineterminator   | 用于写操作的行结束符，默认为‘\r\n’,读操作将忽略此选项，它能认出跨平台的结束符 |
| quotechar        | 用于带有特殊字符的字段的引用符号，默认为‘ “ ’                |
| quoting          | 引用约定，可选值包括csv.QUOTE_ALL(引用所有字段)、csv.QUOTE_MINIMAL(只引用带有诸如分隔符之类特殊字符的字段)、csv.QUOTE_NONNUMERIC以及csv.QUOTE_NON(不引用)，默认为QUOTE_MINIMAL |
| skipinitialspace | 忽略分隔符后面的空白内容，默认为False                        |
| doublequote      | 如何处理字段内的引用符号，如果为True,则双写                  |
| escapechar       | 用于对分隔符进行转义的字符串（如果quoting被设置为csv.QUOTE_NONE的话），默认禁用 |

要手工输出分隔符文件，可以使用csv.write，它接受一个已经打开且可写的文件对象以及跟csv.reader相同的语支和格式化选项

```python
with open('mydata.csv', 'w') as f:
    writer = csv.writer(f, dialect=my_dialect)    
    writer.writerow(('one', 'two', 'three'))    
    writer.writerow(('1', '2', '3'))    
    writer.writerow(('4', '5', '6'))    
    writer.writerow(('7', '8', '9')) 
```

#### JSON数据

JSON（JavaScript Object Notation的简称），以及成为通过http请求在web浏览器和其他应用程序之间发送数据的标准格式之一。是一种比表格文本格式灵活的数据格式

```python
obj = """ 
{"name": "Wes", 
"places_lived": ["United States", "Spain", "Germany"], 
"pet": null, 
"siblings": [{"name": "Scott", "age": 30, "pets": ["Zeus", "Zuko"]},
			{"name": "Katie", "age": 38,
			"pets": ["Sixes", "Stache", "Cisco"]}] 
} 
""" 
```

除其空值null和一些细微差别外，json非常接近于有效的python代码，基本类型有对象（字典），数组（列表），字符串，数值，布尔值以及null，对象中所有键必须是字符串

- json.loads可将字符串转为python格式
- json.dumps可将python对象转为json格式

如何将json对象转换为dataframe或其他便于分析的数据结构，最简单的方式就是向dataframe构造器传入一组json对象，并选取数据字段的子集

```
siblings = pd.DataFrame(result['siblings'],columns=['name','age'])
siblings
>
name	age
0	Scott	30
1	Katie	38
```

pandas.==read_json==能自动转换json数据集为Series和dataframe

==to_json==能将pandas数据转为json

```python
data = pd.read_json('./examples/example.json')
data
>
a	b	c
0	1	2	3
1	4	5	6
2	7	8	9

#  export data from pandas to JSON
print(data.to_json())
>
{"a":{"0":1,"1":4,"2":7},"b":{"0":2,"1":5,"2":8},"c":{"0":3,"1":6,"2":9}}
```

#### XML和HTML：web信息收集

- python有许多库可用于读写html和xml格式数据，比如lxml,beautiful soup、html5lib,虽然lxml通常要快得多，但是其他库可以更好地处理格式错误的HTML或XML文件

- panda有一个内置函数==read_html==，它使用lxml和Beautiful Soup等库自动将HTML文件中的表解析为DataFrame对象。

  - 需要安装的附加库

    ```python
    conda install lxml
    pip install beautifulsoup4 html5lib 
    ```

  - read_html有许多选项，默认会搜索并尝试解析标记中包含的所有表格数据。结果是一个DataFrame==对象列表==

  - ```python
    tables = pd.read_html('./examples/fdic_failed_bank_list.html')
    len(tables)
    >
    1
    tables[0].head()
    >
    Bank Name	City	ST	CERT	Acquiring Institution	Closing Date	Updated Date
    0	Allied Bank	Mulberry	AR	91	Today's Bank	September 23, 2016	November 17, 2016
    1	The Woodbury Banking Company	Woodbury	GA	11297	United Bank	August 19, 2016	November 17, 2016
    2	First CornerStone Bank	King of Prussia	PA	35312	First-Citizens Bank & Trust Company	May 6, 2016	September 6, 2016
    3	Trust Company Bank	Memphis	TN	9956	The Bank of Fayette County	April 29, 2016	September 6, 2016
    4	North Milwaukee State Bank	Milwaukee	WI	20364	First-Citizens Bank & Trust Company	March 11, 2016	June 16, 2016
    ```

##### 利用 lxml.objectify解析xml

对于xml的数据，首先用lxml.objectify解析该文件，然后通过getroot得到该xml文件的根节点的引用

```python
from lxml import objectify

path = './datasets/mta_perf/Performance_MNR.xml'
parsed = objectify.parse(open(path))
# 根节点的引用
root = parsed.getroot()

# root.INDICATOR 返回一个用于产生各个<INDICATOR>xml元素的生成器
data = []
skip_fields = ['PARENT_SEQ', 'INDICATOR_SEQ','DESIRED_CHANGE', 'DECIMAL_PLACES']
for elt in root.INDICATOR:
    el_data = {} 
    for child in elt.getchildren():
        if child.tag in skip_fields:
            continue
            
        el_data[child.tag] = child.pyval
    data.append(el_data) 
data
>[{'AGENCY_NAME': 'Metro-North Railroad',
  'INDICATOR_NAME': 'On-Time Performance (West of Hudson)',
  'DESCRIPTION': 'Percent of commuter trains that arrive at their destinations within 5 minutes and 59 seconds of the scheduled time. West of Hudson services include the Pascack Valley and Port Jervis lines. Metro-North Railroad contracts with New Jersey Transit to operate service on these lines.\n',
  'PERIOD_YEAR': 2008,
  'PERIOD_MONTH': 1,
  'CATEGORY': 'Service Indicators',
  'FREQUENCY': 'M',
  'INDICATOR_UNIT': '%',
  'YTD_TARGET': 95.0,
  'YTD_ACTUAL': 96.9,
  'MONTHLY_TARGET': 95.0,
  'MONTHLY_ACTUAL': 96.9},......]

# 将字典转为一个dataframe
perf = pd.DataFrame(data)
```

xml数据可以比本例复杂的多，每个标记都可以有元数据,下面看这个html的链接标记（算是一段有效的xml）

```python
from io import StringIO
tag = '<a href="http://www.google.com">Google</a>'
root = objectify.parse(StringIO(tag)).getroot()
root
><Element a at 0x1bef9cbcd88>
root.get('href')
>'http://www.google.com'
root.text
>'Google'
```

#### 二进制数据格式

实现二进制格式存储最简单的方式就是用内置的pickle序列化，为了使用方便，pandas 有一个`to_pickle`方法将数据保存到磁盘上

```python
frame = pd.read_csv('./examples/ex1.csv')
frame
>a	b	c	d	message
0	1	2	3	4	hello
1	5	6	7	8	world
2	9	10	11	12	foo

# 保存
frame.to_pickle('./to_pickle')
# 读取
pd.read_pickle('./to_pickle')
```

 Some other storage formats for pandas or NumPy data include: 

- bcolz 

  A compressable column-oriented binary format based on the Blosc compression library.

- Feather 

  A cross-language column-oriented file format I designed with the R programming community’s Hadley Wickham. Feather uses the Apache Arrow columnar memory format

#### Using HDF5 Format

hierachical data format,有很多高效读写磁盘上二进制数据工具，hdf5就是其中一个流行的工业级库

HDF5支持多种压缩模式的实时压缩，使具有重复模式的数据能够更有效地存储。HDF5对于处理不适合内存的非常大的数据集是一个很好的选择，因为您可以高效地读写大得多的数组的小段

可以使用PyTables or h5py库来访问hdf5文件，但pandas提供了高级接口，简化了存储Series和DataFrame对象

```python
frame = pd.DataFrame({'a':np.random.randn(100)})
frame.head()
>
a
0	0.500469
1	0.338317
2	0.482018
3	-1.690491
4	-1.009748

store = pd.HDFStore('hdf5_store.h5')
store['obj1'] = frame
store['obj1_clo']=frame['a']
store
><class 'pandas.io.pytables.HDFStore'>
File path: hdf5_store.h5

# HDF5文件中包含的对象可以使用相同的dict-like API检索:
store['obj1']

# HDFStore支持两种存储模式，“fixed”和“table”。后者通常较慢，但它支持使用特殊语法的查询操作:
store.put('obj2',frame,format='table')
store.select('obj2',where=['index>=10 and index <=15'])
>a
10	-0.204815
11	-0.005680
12	0.113166
13	2.704010
14	0.582593
15	-0.479058

# put 操作是 store['obj2'] = frame 的显式版本，但允许我们设置其他选项
frame.to_hdf('mydata.h5','obj3',format='table')
pd.read_hdf('mydata.h5', 'obj3', where=['index < 5']) 
>   a
0	0.623734
1	0.832671
2	0.294341
3	-1.472452
4	0.084376
```

#### Reading  Microsoft Excel Files

pandas支持使用ExcelFile类或pandas.read_excel读取excel数据。由于他们在内部使用了xlrd和openpyxl来读取XLS和XLSX文件，需要先安装他们

通过传入一个xls或xlsx文件的路径即可创建一个excelFile实例

```python
# pd.read_excel(io, sheet_name=0, header=0, names=None, index_col=None, usecols=None, 
# squeeze=False, dtype=None, engine=None, converters=None, true_values=None, 
# false_values=None, skiprows=None, nrows=None, na_values=None, parse_dates=False, 
# date_parser=None, thousands=None, comment=None, skipfooter=0, convert_float=True, **kwds)
# 创建一个excelFile实例
xlsx = pd.ExcelFile('./examples/ex1.xlsx')
# 读取某个sheet的数
pd.read_excel(xlsx,'Sheet1')
> 
a	b	c	d	message
0	1	2	3	4	hello
1	5	6	7	8	world
2	9	10	11	12	foo

# 也可以不创建excelfile实例，简化方式
frame = pd.read_excel('./examples/ex1.xlsx','Sheet1')
```

将pandas数据写入excel

```python
# To write pandas data to excel format. you must first create an excelwriter ，then write data 
# to it using pandas object's to_excel method
writer = pd.ExcelWriter('./write_to_excel.xlsx')
frame.to_excel(writer,'Sheet3')
writer.save()

# you can also pass a file path to to_excel and avoid the ExcelWriter
frame.to_excel('./write_to_excel.xlsx','Sheet4')
```

- 总结

  - 读excel

    ```python
    frame = pd.read_excel('./examples/ex1.xlsx','Sheet1')
    ```

  - 写excel

    ```python
    frame.to_excel('./write_to_excel.xlsx','Sheet4')
    ```

#### Interacting with web APIs

many websites hava public APIs providing data feeds via JSON or some other format,there are a number of ways to access thest APIs from python,one easy-to-use method that i recommend is the __requests__ package

To find the last 30 GitHub issues for pandas on GitHub, we can make a GET HTTP request using the add-on requests library

```python
import requests
url = 'https://api.github.com/repos/pandas-dev/pandas/issues'
resp = requests.get(url)
resp
>
<Response [200]>
```

the response object's __json__ methon will return a __dictionary__ containing json parsed into native python objects

```python
data = resp.json()
data[0]['title']
>'Period does not round down for frequencies less that 1 hour' 
```

我们可以将数据传给dataframe,提取出感兴趣的字段( We can pass data directly to DataFrame and extract fields of interest:)

```python
issues = pd.DataFrame(data,columns=['number', 'title','labels', 'state'])
issues
>
number	title	labels	state
0	28123	Doc: Fix RangeIndex and other docstrings for m...	[]	open
1	28122	Performance regression uint64 groupby().min() ...	[]	open
2	28121	CLN: change regex try/except to checks	[]	open
3	28120	to_datetime errors='ignore' unexpected behavior	[]	open
```

#### Interacting with Datasets

In a business setting, most data may not be stored in text or Excel files. SQL-based relational databases (such as SQL Server, PostgreSQL, and MySQL) are in wide use, and many alternative databases have become quite popular. The choice of database is usually dependent on the performance, data integrity, and scalability needs of an application. (应用程序的性能、数据完整性和可伸缩性需求)

loading data from SQL into a DataFrame is fairly straightforward, and pandas has some function to simplify the process, create a SQLite database using python's built-in sqlite3 driver:

```python
import sqlite3
query = '''
CREATE TABLE test
(a VARCHAR(20), b VARCHAR(20),
c REAL,        d INTEGER
);'''

con = sqlite3.connect('mydata.sqlite')
con.execute(query)
con.commit()
```

the data saved is ==persistent and is available== in subsequent sessions

```python
cursor = con.execute('select * from test')
rows = cursor.fetchall()
rows
>
[('Atlanta', 'Georgia', 1.25, 6),
 ('Tallahassee', 'Florida', 2.6, 3),
 ('Sacramento', 'California', 1.7, 5),
 ('Atlanta', 'Georgia', 1.25, 6),
 ('Tallahassee', 'Florida', 2.6, 3),
 ('Sacramento', 'California', 1.7, 5)]
```

column names, contained in the cursor’s description attribute

```python
cursor.description
>
(('a', None, None, None, None, None, None),
 ('b', None, None, None, None, None, None),
 ('c', None, None, None, None, None, None),
 ('d', None, None, None, None, None, None))
```

You can pass the list of tuples to the dataframe constructor

```python
pd.DataFrame(rows, columns =[i[0] for i in cursor.discription])
>
a	b	c	d
0	Atlanta	Georgia	1.25	6
1	Tallahassee	Florida	2.60	3
2	Sacramento	California	1.70	5
3	Atlanta	Georgia	1.25	6
```



## 第七章 数据规整化：清理、转换、合并、重塑

### 合并数据集

Data contained in pandas objects can be combined together in a number of ways:

-  ==pandas.merge== connects rows in DataFrames based on one or more keys, as it implements database join operations.
- ==pandas.concat== concatenates or “stacks” together objects along an axis
- The ==combine_first== instance method enables splicing together overlapping data to fill in missing values in one object with values from another

#### Database-Style DataFrame joins

[参考1](https://mp.weixin.qq.com/s/686SKGkIrlaYdtGfX0uKEQ)

合并和连接运算是通过一个或多个键将行链接起来，这些运算是关系型数据库的核心

默认情况下，merge做的是‘inner'连接，结果中键是求交集，其他链接方式还有’left','right','outer'

外链接求的是键的并集，组合了左链接和右链接

| 参数        | 说明                                                         |
| ----------- | ------------------------------------------------------------ |
| left        | DataFrame to be merged on the left side                      |
| right       |                                                              |
| how         | One of 'inner', 'outer', 'left', or 'right'; defaults to 'inner'. |
| on          | Column names to join on. Must be found in both DataFrame objects. If not specified and no other join keys given, will use the intersection of the column names in left and right as the join keys |
| left_on     | Columns in left DataFrame to use as join keys                |
| right_on    |                                                              |
| left_index  | Use row index in left as its join key (or keys, if a MultiIndex). |
| right_index |                                                              |
| sort        | Sort merged data lexicographically by join keys; True by default (disable to get better performance in some cases on large datasets). |
| suffixes    | Tuple of string values to append to column names in case of overlap; defaults to ('\_x', '\_y') (e.g., if 'data' in both DataFrame objects, would appear as 'data_x' and 'data_y' in result). |
| copy        | If False, avoid copying data into resulting data structure in some exceptional cases; by default always copies. |
| indicator   | Adds a special column _merge that indicates the source of each row; values will be 'left_only', 'right_only', or 'both' based on the origin of the joined data in each row |



- 内连接,取共同列alpha值的交集进行连接:`df3 = pd.merge(df1,df2,how='inner',on='alpha')`

![007](D:\project\pycon\DA\img\007.jpg)

- 外连接,参数on设置连接的共有列名:`df4 = pd.merge(df1,df2,how='outer',on='alpha')`

![008](D:\project\pycon\DA\img\008.jpg)

- 左连接，我们可以理解基于左边位置dataframe的列进行连接

`f5 = pd.merge(df1,df2,how='left',on='alpha')`

![009](D:\project\pycon\DA\img\009.jpg)

- 右连接，可以理解基于右边位置dataframe的列进行连接

`df6 = pd.merge(df1,df2,how='right',on='alpha')`

![010](D:\project\pycon\DA\img\010.jpg)

- 多列连接的算法与单列连接一致

  多列的内连接`df7 = pd.merge(df1,df2,on=['alpha','beta'],how='inner')`

![011](D:\project\pycon\DA\img\011.jpg)

​	多列的右连接:`df8 = pd.merge(df1,df2,on=['alpha','beta'],how='right')`

![012](D:\project\pycon\DA\img\012.jpg)

- 基于index的连接方法

  基于df1的beta列和df2的index连接

  `df9 = pd.merge(df1,df2,how='inner',left_on='beta',right_index=True)`

![013](D:\project\pycon\DA\img\013.jpg)

- 设置参数suffixes以修改除连接列外相同列的后缀名

```python
df1 = pd.DataFrame({'alpha':['A','B','B','C','D','E'],'beta':['a','a','b','c','c','e'],
                    'feature1':[1,1,2,3,3,1],'feature2'
                    ['low','medium','medium','high','low','high']})
df1
>alpha	beta	feature1	feature2
0	A	a	1	low
1	B	a	1	medium
2	B	b	2	medium
3	C	c	3	high
4	D	c	3	low
5	E	e	1	high

df2 = pd.DataFrame({'alpha':['A','A','B','F'],'pazham':['apple','orange','pine','pear'],
                        'kilo'
                    ['high','low','high','medium'],'price':np.array([5,6,5,7])},index=
                   ['d','d','b','f'])
df2
>	alpha	pazham	kilo	price
d	A	apple	high	5
d	A	orange	low	6
b	B	pine	high	5
f	F	pear	medium	7

# 设置参数suffixes以修改 除连接列外 相同列的后缀名
df9 = pd.merge(df1,df2,how='inner',left_on='beta',right_index=True,suffixes=('_000','_999'))
df9
>alpha_000	beta	feature1	feature2	alpha_999	pazham	kilo	price
2	B	b	2	medium	B	pine	high	5
```

- join方法

  join方法是基于==index==连接dataframe，merge方法是基于column连接，连接方法有内连接，外连接，左连接和右连接，与merge一致
  - lsuffix和rsuffix设置相同连接列名的后缀名,有同名的列名没指定会报错

    ```python
    caller = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3', 'K4', 'K5'], 'A': ['A0', 'A1', 'A2', 'A3', 'A4', 'A5']})
    caller
    >key	A
    0	K0	A0
    1	K1	A1
    2	K2	A2
    3	K3	A3
    4	K4	A4
    5	K5	A5
    
    other = pd.DataFrame({'key': ['K0', 'K1', 'K2'],'B': ['B0', 'B1', 'B2']})
    > key	B
    0	K0	B0
    1	K1	B1
    2	K2	B2
    
    caller.join(other,lsuffix='left__',rsuffix='right__',how='inner')
    >keyleft__	A	keyright__	B
    0	K0	A0	K0	B0
    1	K1	A1	K1	B1
    2	K2	A2	K2	B2 
    ```

  - 要使用join连接列，需要把dataframe需要连接的列设置为index

    ```
    caller.set_index('key').join(other.set_index('key'),how='inner')
    >A	B
    key		
    K0	A0	B0
    K1	A1	B1
    K2	A2	B2
    ```

- concat方法

  concat方法是拼接函数，有行拼接和列拼接，==默认是行拼接==，拼接方法默认是外拼接（并集），拼接的对象是pandas数据类型

  ` pd.concat(objs, axis=0, join='outer', join_axes=None, ignore_index=False, keys=None, levels=None, names=None, verify_integrity=False, sort=None, copy=True)`

  | 参数             | 说明                                                 |
  | ---------------- | ---------------------------------------------------- |
  | objs             | pandas对象的列表或字典，唯一必须的参数               |
  | axis             | 指明连接的轴向，默认为0                              |
  | join             | outer-并集，inner-交集                               |
  | join_axes        | 指明其他n-1条轴的索引，不执行交并运算                |
  | keys             | 与连接对象相关的值，用于形成连接轴上的层次化索引，   |
  | levels           | 指定用作层次化索引各级别上的索引，如果设置了keys的话 |
  | names            | 用于创建分层级别的名称，如果设置了keys和levels的话   |
  | verify_integrity | 检测结果对象新轴上的重复情况，如果有重复则引发异常   |
  | ignore_index     | 不保留连接轴上的索引，产生一组新索引                 |

  - series的拼接

    默认是在axis=0上工作，产生一个series,如果传入axis=1,结果会变为dataframe 

    要在轴上创建一个层次化索引，使用keys参数

    ```python
    df1 = pd.Series([1.1,2.2,3.3],index=['i1','i2','i3'])
    df2 = pd.Series([4.4,5.5,6.6],index=['i2','i3','i4'])
    
    # 行拼接
    pd.concat([df1,df2])
    >i1    1.1
    i2    2.2
    i3    3.3
    i2    4.4
    i3    5.5
    i4    6.6
    dtype: float64
        
    # 行拼接若有相同的索引，为了区分索引，我们在最外层定义了分组情况
    pd.concat([df1,df2],keys=['aaa','bbb'])
    >aaa  i1    1.1
         i2    2.2
         i3    3.3
    bbb  i2    4.4
         i3    5.5
         i4    6.6
    dtype: float64
    # 如果传入字典，字典的键则会被当作keys
    pd.concat({'aa':df1,'bb':df2})
    >aa  i1    1.1
        i2    2.2
        i3    3.3
    bb  i2    4.4
        i3    5.5
        i4    6.6
    dtype: float64
       
        
    # 列拼接，默认是并集
    pd.concat([df1,df2],axis=1)
    >0	1
    i1	1.1	NaN
    i2	2.2	4.4
    i3	3.3	5.5
    i4	NaN	6.6
    
    # 设置列拼接的列名
    pd.concat([df1,df2],axis=1,join='inner',keys=['aaa','bbb'])
    >aaa	bbb
    i2	2.2	4.4
    i3	3.3	5.5
    
    # 对指定的索引拼接
    pd.concat([df1,df2],axis=1,join_axes=[['i2','i3']])
    ```

  - dataframe类型的拼接方法

    ```python
    df1 = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3', 'K4', 'K5'],
                        'A': ['A0', 'A1', 'A2', 'A3', 'A4', 'A5']})
    df1
    >key	A
    0	K0	A0
    1	K1	A1
    2	K2	A2
    3	K3	A3
    4	K4	A4
    5	K5	A5
    
    df2 = pd.DataFrame({'key': ['K0', 'K1', 'K2'],'B': ['B0', 'B1', 'B2']})
    df2
    >key	B
    0	K0	B0
    1	K1	B1
    2	K2	B2
    
    # 行拼接
    pd.concat([df1,df2],sort=True)
    >A	B	key
    0	A0	NaN	K0
    1	A1	NaN	K1
    2	A2	NaN	K2
    3	A3	NaN	K3
    4	A4	NaN	K4
    5	A5	NaN	K5
    0	NaN	B0	K0
    1	NaN	B1	K1
    2	NaN	B2	K2
    
    # 列拼接
    pd.concat([df1,df2],axis=1)
    >key	A	key	B
    0	K0	A0	K0	B0
    1	K1	A1	K1	B1
    2	K2	A2	K2	B2
    3	K3	A3	NaN	NaN
    4	K4	A4	NaN	NaN
    5	K5	A5	NaN	NaN
    
    # 若行列拼接有重复名则报错
    pd.concat([df1,df2],axis=1,verify_integrity=True)
    >ValueError: Indexes have overlapping values: Index(['key'], dtype='object')
    ```

##### 轴向连接

另外一种合并运算也被称为连接（concatenate）、绑定（binding）或堆叠（stacking），numpy有一个合并原始nympy数组的concatenation函数

```python
arr = np.arange(12).reshape(3,4)
arr
>array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])

np.concatenate([arr,arr],axis=1)
>array([[ 0,  1,  2,  3,  0,  1,  2,  3],
       [ 4,  5,  6,  7,  4,  5,  6,  7],
       [ 8,  9, 10, 11,  8,  9, 10, 11]])
       
np.concatenate([arr,arr],axis=0)
>array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11],
       [ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])
```

##### 合并重叠数据

有一类数据组合问题不能用简单的合并和连接运算来处理，比如可能有索引全部或部分重叠的两个数据集

用numpy的where实现

```python
a = pd.Series([np.nan, 2.5, np.nan, 3.5, 4.5, np.nan],
              index=['f', 'e', 'd', 'c', 'b', 'a'])
a
>f    NaN
e    2.5
d    NaN
c    3.5
b    4.5
a    NaN
dtype: float64

b = pd.Series(np.arange(len(a), dtype=np.float64),
              index=['f', 'e', 'd', 'c', 'b', 'a'])
b[-1] = np.NAN
b
>f    0.0
e    1.0
d    2.0
c    3.0
b    4.0
a    NaN
dtype: float64

np.where(np.isnan(a),b,a)
>array([0. , 2.5, 2. , 3.5, 4.5, nan])
```

series有一个combine_first的方法，实现同样的功能，会对齐数据

```
b[:-2].combine_first(a[2:])
>a    NaN
b    4.5
c    3.0
d    2.0
e    1.0
f    0.0
dtype: float64
```

对于DataFrame，combine_first会在列上做同样的事情，可将其看作用参数对象中的数据为调用者对象的缺失数据打补丁

```python
df1 = pd.DataFrame({'a':[1., np.nan, 5., np.nan],
                   'b':[np.nan, 2., np.nan, 6.],
                   'c': range(2, 18, 4)})
df1
>a	b	c
0	1.0	NaN	2
1	NaN	2.0	6
2	5.0	NaN	10
3	NaN	6.0	14


df2 = pd.DataFrame({'a': [5., 4., np.nan, 3., 7.],'b': [np.nan, 3., 4., 6., 8.]})
df2
>a	b
0	5.0	NaN
1	4.0	3.0
2	NaN	4.0
3	3.0	6.0
4	7.0	8.0

df1.combine_first(df2)
>a	b	c
0	1.0	NaN	2.0
1	4.0	2.0	6.0
2	5.0	4.0	10.0
3	3.0	6.0	14.0
4	7.0	8.0	NaN

df2.combine_first(df1)
>a	b	c
0	5.0	NaN	2.0
1	4.0	3.0	6.0
2	5.0	4.0	10.0
3	3.0	6.0	14.0
4	7.0	8.0	NaN
```

#### Reshape and Pivoting(重塑和轴向旋转)

##### reshaping with hierarchical indexing

层次化索引为dataframe提供了一致性的方式

- stack:将数据的==列旋转为行==
- unstack:将数据的==行旋转为列==

```
data = pd.DataFrame(np.arange(6).reshape((2, 3)),
                    index=pd.Index(['Ohio', 'Colorado'], name='state'),
                    columns=pd.Index(['one', 'two', 'three'],name='number'))
data
>>>
number	one	two	three
state			
Ohio	0	1	2
Colorado	3	4	5

result = data.stack()
result
>>>
state     number
Ohio      one       0
          two       1
          three     2
Colorado  one       3
          two       4
          three     5
dtype: int32

type(result)
>>>pandas.core.series.Series

# result.unstack()
number	one	two	three
state			
Ohio	0	1	2
Colorado	3	4	5
```

stack 将列转换为行，得到一个series,对于一个层次化索引的Series，可以使用ustack将其重排为dataframe

两个操作默认操作最内层，传入分层级的编号或名称可对其他级别操作

```
result.unstack(0)
# 等价
result.unstack('state')
>>>
state	Ohio	Colorado
number		
one	0	3
two	1	4
three	2	5
```

当某个级别有值找不到时，unstack操作回引入缺失数据

```
s1 = pd.Series([0,1,2,3],index=['a','b','c','d'])
s2 = pd.Series([4,5,6],index=['c','d','e'])
data2 = pd.concat([s1,s2],keys=['one','two'])
data2
>>>
one  a    0
     b    1
     c    2
     d    3
two  c    4
     d    5
     e    6
dtype: int64

data2.unstack()
>>>

	a	b	c	d	e
one	0.0	1.0	2.0	3.0	NaN
two	NaN	NaN	4.0	5.0	6.0
```

stack默认过滤缺失数据，因此该运算可逆

```
data2.unstack().stack()
>>>
one  a    0.0
     b    1.0
     c    2.0
     d    3.0
two  c    4.0
     d    5.0
     e    6.0
dtype: float64

data2.unstack().stack(dropna=False)
>>>
one  a    0.0
     b    1.0
     c    2.0
     d    3.0
     e    NaN
two  a    NaN
     b    NaN
     c    4.0
     d    5.0
     e    6.0
dtype: float64
```

对dataframe进行unstack操作时，作为旋转轴的级别是最低级别（会被满铺的那个项）

```python
df = pd.DataFrame({'left': result, 'right': result + 5},
                   columns=pd.Index(['left', 'right'], name='side'))

print(df)
>>>
side             left  right
state    number             
Ohio     one        0      5
         two        1      6
         three      2      7
Colorado one        3      8
         two        4      9
         three      5     10
         
df.unstack('state')
>>>
side	left	right
state	Ohio	Colorado	Ohio	Colorado
number				
one	0	3	5	8
two	1	4	6	9
three	2	5	7	10

# 两个操作都可以指定旋转轴的名字
df.unstack('state').stack('side')
```

### 将“长格式”转为“宽格式”

时间序列通常是所谓的“长格式”（long）或“堆叠格式”（stacked）存储在数据库和csv中

![014](D:\project\pycon\DA\img\014.JPG)

关系型数据库中的数据经常是这样存储的

- 固定架构有一个好处：随着表中数据的增加或删除，item列中的值的种类能够增加或减少

- 缺点:长格式数据操作起来不那么轻松

  ```
  pivoted = ldata.pivot('date', 'item', 'value')
  ```

  

## 数据转换

### 移除重复数据

- duplicated方法返回一个布尔型Series，表示各行是否是空行
- drop_duplicates()用于移除重复行的dataframe
  - 默认保留的是第一个，take_last = True 则保留最后一个

### 利用函数或映射进行数据转换

- 将大写的字符变小写  ==str.lower()==

  ````
  data = pd.DataFrame({'food': ['bacon', 'pulled pork', 'bacon',
                                'Pastrami', 'corned beef', 'Bacon',
                                'pastrami', 'honey ham', 'nova lox'],
                       'ounces': [4, 3, 12, 6, 7.5, 8, 3, 5, 6]})
  lowercased = data['food'].str.lower()
  
  meat_to_animal = {  'bacon': 'pig',  'pulled pork': 'pig',  'pastrami': 'cow',  'corned beef': 'cow',  'honey ham': 'pig',  'nova lox': 'salmon' } 
  ````

- series的map方法接收一个函数或含有映射关系的字典对象

  ``` 
  data.['anamal'] = lowercased.map(meat_to_animal)
  # 等价
  data['food'].map(lambda x:meat_to_animal[x.lower()])
  ```

### 替换值

- fillna填充缺失数据可以看作一种特殊情况

- replace方法可用于修改数据子集，比map灵活方便

  ```
  data = pd.Series([1., -999., 2., -999., -1000., 3.])
  data.replace(-999, np.nan) 
  ```

- 传入一个由待替换值组成的列表和一个替换值

  ```
   data.replace([-999, -1000], np.nan) 
  ```

- To use a different replacement for each value, pass a list of substitutes

  ```
  data.replace([-999, -1000], [np.nan, 0])
  ```

- 也可以传入字典

  ```
  data.replace({-999: np.nan, -1000: 0}) 
  ```

### 重命名轴索引

轴标签可以通过函数或映射进行转换，，轴还可以就地更改

```python
 data = pd.DataFrame(np.arange(12).reshape((3, 4)),
                     index=['Ohio', 'Colorado', 'New York'],
                     columns=['one', 'two', 'three', 'four']) 
# the axis indexes have a map method
transform = lambda x: x[:4].upper()
data.index.map(transform)
# columns 同理
# 需要将值赋值给dataframe才能完成更改
data.index = data.index.map(transform)
data.columns = data.columns.map(transform)
```

如果要创建数据集的转换版（而不是修改原始数据），可以使用rename

rename帮我们实现了：复制dataframe并对其索引和列标签进行赋值，如果希望就地更改某个数据，传入==inplace=True==

```python
# rename 可以结合字典型对象对轴标签更新,生成一个新的df
data.rename(index={'OHIO':'test'},
           columns={'TWO':'222'})
# 就地更改,修改原始df
data.rename(index={'OHIO': 'INDIANA'}, inplace=True)
```

### 离散化和面元划分

为了便于分析，连续数据常常被离散化或拆分为“面元”（bin）

离散化和面元划分 ：就是分组，进行相应的计算

1. 对于数据进行离散化和面元划分的前提条件是：连续变化的数据
2. 例如下面是一组人的年龄数据，现在要按照年龄划分为不同年龄的4组,需要使用pandas的==cut==函数

```python
pd.value_counts(cats)
# 将一组人员数据分为不同的年龄组
ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]
#  divide these into bins of 18 to 25, 26 to 35, 36 to 60, and finally 61 and older
bins = [18, 25, 35, 60, 100]
# cut 函数
cats = pd.cut(ages,bins)
cats
>>>[(18, 25], (18, 25], (18, 25], (25, 35], (18, 25], ..., (25, 35], (60, 100], (35, 60], (35, 60], (25, 35]]
Length: 12
Categories (4, interval[int64]): [(18, 25] < (25, 35] < (35, 60] < (60, 100]]

# pandas返回了一个表示每个元素区间的列表
# treat it like an array of strings indicating the bin name
cats.codes
>>>array([0, 0, 0, 1, 0, 0, 2, 1, 3, 2, 2, 1], dtype=int8)
cats.categories
>>>IntervalIndex([(18, 25], (25, 35], (35, 60], (60, 100]]
              closed='right',
              dtype='interval[int64]')
pd.value_counts(cats)
>>>
(18, 25]     5
(35, 60]     3
(25, 35]     3
(60, 100]    1
dtype: int64
```

和区间类似，圆括号表示开端，方括号表示闭端，可通过right = False修改

```python
pd.cut(ages,[18,26,36,61,100],right=False)
>>>
[[18, 26), [18, 26), [18, 26), [26, 36), [18, 26), ..., [26, 36), [61, 100), [36, 61), [36, 61), [26, 36)]
Length: 12
Categories (4, interval[int64]): [[18, 26) < [26, 36) < [36, 61) < [61, 100)]
```

可设置自己的面元名称

```
group_names = ['Youth', 'YoungAdult', 'MiddleAged', 'Senior']
 pd.cut(ages, bins, labels=group_names) 
```

如果传入面元数量而不是面元边界值，它会根据最大和 最小值计算等长面元

```python
data = np.random.randn(1000)
cats = pd.qcut(data, 4) 
```

qcut 类似于cut函数，可根据样本分位数对数据进行划分，根据数据分布情况，cut无法使各个面元含有相同数量的数据点，而qcut使用的是样本分位数，可以得到大小基本相等的面元

> 分位数：**分位数**（Quantile），亦称**分位点**，是指将一个[随机变量](https://baike.baidu.com/item/%E9%9A%8F%E6%9C%BA%E5%8F%98%E9%87%8F/828980)的[概率分布](https://baike.baidu.com/item/%E6%A6%82%E7%8E%87%E5%88%86%E5%B8%83/828907)范围分为几个等份的数值点，常用的有[中位数](https://baike.baidu.com/item/%E4%B8%AD%E4%BD%8D%E6%95%B0/3087401)（即二分位数）、[四分位数](https://baike.baidu.com/item/%E5%9B%9B%E5%88%86%E4%BD%8D%E6%95%B0/5040599)、[百分位数](https://baike.baidu.com/item/%E7%99%BE%E5%88%86%E4%BD%8D%E6%95%B0/10064171)等

### 检测和过滤异常值

异常值的过滤或变换在很大程度上其实就是数组运算，来看一个含有正态分布的dataframe

```
np.array.any()是或操作，任意一个元素为True，输出为True。
np.array.all()是与操作，所有元素为True，输出为True
```

- sign()是Python的Numpy中的取数字符号（数字前的正负号）的函数

  ![012](D:\project\pycon\Python_学习手册\img\012.JPG)

```
np.random.seed(1024)
data = pd.DataFrame(np.random.randn(1000,4))

# 选出含有“超过3或者-3”的行
# 可以利用布尔型和any
data[(np.abs(data) > 3).any(1)]
# 将值限制在区间-3到3
data[np.abs(data) > 3] = np.sign(data) * 3
```

#### 排列和随机采样

利用numpy.random.permutation函数可以轻松实现对Series和DataFrame的列的排列工作，通过需要排列的轴的长度调用permutation,生成一个新顺序的数组

- permutation：

  ```
  # 产生0到n-1的所有整数的随机排列
  sampler = np.random.permutation(3)
  # 行随机排列
  df.take(sampler)
  # 列随机排列
  df.take(sampler,axis=1)
  ```

- 随机采样

  ```
  沿着某个维度，按照给定的索引取回所有的元素,给定的索引必须要是一个由整数组成的列表或者ndarray，用以指明在索引中的位置
  take 也可以接受负整数，作为相对于结尾的相对位置
  take 方法处理的是一个范围更窄的输入，因此会比话实索引（fancy indexing）的速度快很多
  ```

  ```
  # 随机选取列的子集
  df = pd.DataFrame(np.arange(5 * 4).reshape((5, 4)))
  df.sample()
  >>>
  	0	1	2	3
  2	8	9	10	11
  4	16	17	18	19
  1	4	5	6	7
  ```

  #### 计算指标/哑变量

  常用于机器学习或统计建模的转换方式是：将分类变量转换为“哑变量矩阵”（dummy matrix）或“指标矩阵”（indicator matrix）

  也叫虚拟变量，引入哑变量的目的是，将不能够定量处理的变量量化，如职业、性别对收入的影响，战争、自然灾害对GDP的影响

  ```
  # 如果dataframe的某一列含有k个不同的值，则可以派生出一个k列矩阵或dataframe(其值全为1和0)
  # pandas有一个get_dummies的函数可实现该功能
  df = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'b'],'data1': range(6)})
  print(df)
  pd.get_dummies(df['key'])
  >>>
  key  data1
  0   b      0
  1   b      1
  2   a      2
  3   c      3
  4   a      4
  5   b      5
  >>>
  	a	b	c
  0	0	1	0
  1	0	1	0
  2	1	0	0
  3	0	0	1
  4	1	0	0
  5	0	1	0
  # 给指标dataframe列加上一个前缀
  pd.get_dummies(df['key'],prefix='hh')
  >>>
  hh_a	hh_b	hh_c
  0	0	1	0
  1	0	1	0
  2	1	0	0
  3	0	0	1
  4	1	0	0
  5	0	1	0
  ```

  ```
  mnames = ['movie_id','title','tenres']
  movies = pd.read_table(r'./datasets/movielens/movies.dat',sep='::',header=None,names=mnames)
  movies[:10]
  >>>
  	movie_id	title	tenres
  0	1	Toy Story (1995)	Animation|Children's|Comedy
  1	2	Jumanji (1995)	Adventure|Children's|Fantasy
  2	3	Grumpier Old Men (1995)	Comedy|Romance
  3	4	Waiting to Exhale (1995)	Comedy|Drama
  4	5	Father of the Bride Part II (1995)	Comedy
  5	6	Heat (1995)	Action|Crime|Thriller
  6	7	Sabrina (1995)	Comedy|Romance
  7	8	Tom and Huck (1995)	Adventure|Children's
  8	9	Sudden Death (1995)	Action
  9	10	GoldenEye (1995)	Action|Adventure|Thriller
  
  # dataframe中的行同属多个分类的情况下添加指标变量
  genres = pd.unique(all_genres)
  genres
  >>>array(['Animation', "Children's", 'Comedy', 'Adventure', 'Fantasy',
         'Romance', 'Drama', 'Action', 'Crime', 'Thriller', 'Horror',
         'Sci-Fi', 'Documentary', 'War', 'Musical', 'Mystery', 'Film-Noir',
         'Western'], dtype=object)
         
  # 创建0矩阵
  zero_matrix = np.zeros((len(movies),len(genres)))
  # 将指标名赋予0矩阵
  dummies = pd.DataFrame(zero_matrix,columns=genres)
  # 使用get_indexer添加指标变量
  for i,gen in enumerate(movies.tenres):
      indices = dummies.columns.get_indexer(gen.split('|'))
      dummies.iloc[i,indices] = 1
  >>>
  	Animation	Children's	Comedy	Adventure	Fantasy	Romance	Drama	Action	Crime	Thriller	Horror	Sci-Fi	Documentary	War	Musical	Mystery	Film-Noir	Western
  0	1.0	1.0	1.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0
  1	0.0	1.0	0.0	1.0	1.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0
  2	0.0	0.0	1.0	0.0	0.0	1.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0
  3	0.0	0.0	1.0	0.0	0.0	0.0	1.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0
  4	0.0	0.0	1.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0
  ```

  ```
  index.get_indexer() 
  # 创建新索引的索引列表，缺失值返回 -1
  >>> index = pd.Index(['c', 'a', 'b'])
  >>> index.get_indexer(['a', 'b', 'x'])
  array([ 1,  2, -1])
  ```

  对于统计应用程序，一个有用的方法是将get_dummies与一个离散化函数(如cut)结合起来

  ```
  np.random.seed(123)
  values = np.random.rand(10)
  bins = [0, 0.2, 0.4, 0.6, 0.8, 1]
  pd.get_dummies(pd.cut(values,bins))
  >>>
  (0.0, 0.2]	(0.2, 0.4]	(0.4, 0.6]	(0.6, 0.8]	(0.8, 1.0]
  0	0	0	0	1	0
  1	0	1	0	0	0
  2	0	1	0	0	0
  3	0	0	1	0	0
  4	0	0	0	1	0
  5	0	0	1	0	0
  6	0	0	0	0	1
  7	0	0	0	1	0
  8	0	0	1	0	0
  9	0	1	0	0	0
  ```

### 字符串操作

#### 字符串对象方法

对于大部分字符串处理，内置字符串已经够用了

- split常常和strip(修剪空白)一起使用

  `[x.strip() for x in val.split(',')]`

- 可以使用加法连接字符和符号

- 也可以使用join方法

  `'::'.join(['a','b','c'])`

- 检测子串定位最佳方式是字符串的  in  方法 ，index  和 find  方法
  - find和index的区别：如果找不到字符串，index会引发一个异常而不是返回-1
  - 还有一个count,可以返回指定子串的出现次数
- replace用于替换或删除（传入空值）

字符串方法：

| 方法                 | 说明                                                        |
| -------------------- | ----------------------------------------------------------- |
| strip\rstrip\lstrip  | 去除空字符串                                                |
| split                | 分割为一组字串                                              |
| lower、upper         | 转换为大小写                                                |
| ljust、rjust         | 用空格或字符填充空白返回符合最低宽度的字符串                |
| count                | 返回出现次数                                                |
| endswith、startswith | 如果字符串包含某个后缀或前缀，怎返回True                    |
| join                 | 拼接字符串                                                  |
| index                | 找到子串，返回第一个发现字串的位置，没找到则引发 ValueError |
| find                 | 找到子串，返回第一个发现字串的位置，没找到返回-1            |
| rfind                | 找到子串，返回最后一个发现字串的位置，没找到返回-1          |
| replace              | 替换子字符串                                                |

#### 正则表达式（regex）

提供了灵活的文本中搜索匹配字符串模式的方法。

内置re模块负责对字符串应用正则表达式

re模块函数可分为三个大类，模式匹配、替换、拆分

```
import re
text = 'huihui shi ge sha   dan'
# 描述一个或多个空白符的模式  \s+
re.split('\s+',text)
>>>
['huihui', 'shi', 'ge', 'sha', 'dan']
```

调用re.split('\s+',text)时，正则表达式会先被编译，然后在text上调用其split方法，你可以使用re.compile自己编译一个可以重用的对象

```
# 编译
regex = re.compile('\s+')
# 分割
regex.split((text))
```

如果只希望得到匹配regex 的所有模式，则可以使用findall方法

```
regex.findall(text)
>>>
[' ', ' ', ' ', '   ']
```

- 如果想避免正则表达式中不需要的转义 \ ,则可以使用原始字符串字面量如（r'C:\x'）,也可以编写其等价模式 'C:\\x'
- 如果打算对许多字符串应用同一条正则表达式，建议使用re.compile创建对象，可节省cpu时间
- match和search跟findall功能类似
  - findall返回的是字符串中所有的匹配项
  - search则只返回第一个匹配项
  - match更加严格，只匹配字符串的首部

```
text = """Dave dave@google.com Steve steve@gmail.com Rob rob@gmail.com Ryan ryan@yahoo.com """ 
pattern = r'[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}'
# re.IGNORECASE的作用是使正则表达式对大小写不敏感
regex = re.compile(pattern,flags=re.IGNORECASE)
regex.findall(text)
>>>
['dave@google.com', 'steve@gmail.com', 'rob@gmail.com', 'ryan@yahoo.com']

# search返回的是第一个电子邮件，以特殊的匹配项对象形式返回，匹配项告诉我们模式在原字符串中的起始和结束的位置
m = regex.search(text)
m
>>>
<re.Match object; span=(5, 20), match='dave@google.com'>
print(m.start(),m.end())
>>> 5 20

# regex.match 返回None，因为它只匹配出现在字符串开头的模式
print(regex.match(text))
>>>None
```

还有一个sub方法，会将匹配到的模式替换为指定字符串，返回得到的新字符串

```
print(regex.sub('ABC___',text))
>>>
Dave ABC___ Steve ABC___ Rob ABC___ Ryan ABC___ 
```

如果你不仅想找到电子邮件，还想将其分为三部分：用户名、域名、以及后缀，要实现次功能，指需将待分段的模式各部分用==圆括号==包起来

```
pattern = r'([A-Z0-9._%+-]+)@([A-Z0-9.-]+)\.([A-Z]{2,4})'
regex = re.compile(pattern,flags=re.IGNORECASE)
m = regex.match('dave@google.com')
m.groups()
>>>
('dave', 'google', 'com')

#  findal会返回一个分组列表
regex.findall(text)
>>>
[('dave', 'google', 'com'),
 ('steve', 'gmail', 'com'),
 ('rob', 'gmail', 'com'),
 ('ryan', 'yahoo', 'com')]
```

sub还能通过诸如 \1 \2 之类的特殊符号访问各匹配项中的分组

```
regex.sub(r'Username: \1, Domain: \2, Suffix: \3', text)
>>>
Dave Username: dave, Domain: google, Suffix: com Steve Username: steve, Domain: gmail, Suffix: com Rob Username: rob, Domain: gmail, Suffix: com Ryan Username: ryan, Domain: yahoo, Suffix: com 
```

- 正则表达式方法

  | 函数              | 方法                                                         |
  | ----------------- | ------------------------------------------------------------ |
  | findall、finditer | 返回字符串中所有的非重叠匹配模式，findall返回的是由所有模式组成的列表，finditer通过一个迭代器逐个返回 |
  | match             | 从字符串起始位置匹配，可对模式各部分进行分组，如果找到则返回一个匹配模式，否则返回None |
  | search            | 扫描整个字符串以匹配，找到则返回，不仅仅是起初处             |
  | split             | 根据模式拆分                                                 |
  | sub、subn         | 将字符串中的所有（sub）或 前n个（subn）模式替换为指定表达式，在替换字符串中可以通过 \1  \2 等符号表示 各分组项 |

  #### pandas中矢量化的字符串函数

  data.map 所有字符串和正则表达式都能被应用于各个值，如果存在NA就会报错，为了解决这个问题，Series有一些能跳过NA值的操作方法，

  - Series 的 str 属性即可访问这些方法

    ```
    data.isnull()
    
    # 检查字符串是否含有某个字符串
    data.str.contains('gmail')
    # 使用正则表达式，加上任意re选项（IGNORECASE）
    ```

  - 实现矢量化的元素获取操作，要么使用str.get,要么在str属性上使用索引

    ```
    data.str.findall(pattern, flags=re.IGNORECASE) 
     
    matches = data.str.match(pattern, flags=re.IGNORECASE)
    
    matches.str.get(1)
    matches.str[0] 
    data.str[:5]
    ```

#### 矢量化字符串方法

| 函数        | 方法                                                         |
| ----------- | ------------------------------------------------------------ |
| cat         | 元素级的字符串连接操作，可指定分隔符                         |
| contains    | 返回各个字符串中是否含有指定模式的布尔型数组                 |
| count       | 模式出现的次数                                               |
| ==extract== | Use a regular expression with groups to extract one or more strings from a Series of strings; the result will be a DataFrame with one column per group |
| endswith    |                                                              |
| startswith  |                                                              |
| findall     | 匹配字符列表                                                 |
| get         | 获取第 i 个字符                                              |
| isalnum     |                                                              |
| isdecimal   |                                                              |
| isdigit     |                                                              |
| islower     |                                                              |
| isnumeric   |                                                              |
| isupper     |                                                              |
| join        | 根据指定字符拼接                                             |
| len         |                                                              |
| lower,upper |                                                              |
| match       |                                                              |
| pad         |                                                              |
| center      |                                                              |
| repeat      |                                                              |
| replace     |                                                              |
| slice       |                                                              |
| split       |                                                              |
| strip       |                                                              |
| rstrip      |                                                              |
| lstrip      |                                                              |



## 第八章 绘图和可视化

绘图是分析过程中重要的任务之一，是探索的过程，找出异常值，必要的数据转换，得出有关模型的idea等

matplotlib 是一个用于创建出版质量的桌面绘图包，项目由John Hunter 于2002年启动，目的是为python构建一个Matlab式的绘图接口，不仅支持各种操作系统上许多不同的GUI后端，还能将图片导出为各种常见的矢量（vector）和光栅（raster）:pdf,svg,jpg,png,bmp,gif等

还有许多插件工作集，如用于3D图形的mplot3d以及用于地图和投影的basemap

### maplotlib入门

```
import matplotlib.pyplot as plt
```

虽然pandas的的绘图函数能处理许多普通的绘图任务，如果需要自定义一些高级功能的话，就必须学习matplitlib API 

#### Figure 和 Subplot

matplot的图像位于==Figure==对象中，你可以使用plt.figure创建一个新的figure:

```
fig = plt.figure()
```

- 当前的图表和子图可以使用plt.gcf()和plt.gca()获得，分别表示Get Current Figure和Get Current Axes

- figure有一些选项，figsize 大小和纵横比

figure不能直接绘图，绘图需要用add_subplot创建一个或多个subplot才行在两行两列的四个ax中，选中第一个（变号从1开始）

```
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
# 此时发出绘图命令，就会在最后一个用过的subplot中绘图
# k-- 是一个线性选项，告诉plt 绘制黑色虚线
plt.plot(np.random.randn(50).cumsum(),'k--')
plt.plot([1,2,3],[1,2,3])
```

fig.add_subplot返回的是axessubplot对象,直接调用其实例方法就可以在其表示的格子中画图了

```
ax2.scatter(np.arange(30),np.arange(30)+3*np.random.randn(30))
```

根据特定的布局创建figure 和 subplot 是一个非常常见的任务，于是出现了一个更为方便的方法 plt.subplts,可以创建一个新的figure，返回一个还有已创建的subplot对象的numpy数组

```
fig,axes = plt.subplots(2,3)
axes
>>> 
array([[<matplotlib.axes._subplots.AxesSubplot object at 0x0000024FF5A91CC0>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x0000024FF5ABE198>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x0000024FF5AE8128>],
       [<matplotlib.axes._subplots.AxesSubplot object at 0x0000024FF5B0F7B8>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x0000024FF5B36E80>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x0000024FF5B67518>]],
      dtype=object)

# 可通过axes[i,j]获取目标axes
axes[1,1]
```

![015](D:\project\pycon\DA\img\015.JPG)

- pylot.subplots的选项
  - nrows 		行数
  - ncols		   列数
  - sharex                所有subplot应该使用的相同的x轴的刻度（调节xlim将会影响所有的subplot）
  - sharey                同sharex
  - subplot_kw        用于创建各subplot的关键字字典
  - ** fig_kw            创建figure时的其他关键字，如plt.subplots(2,3,figsize=(8,6))

#### 调整subplot周围的间距

默认情况下，会在subplot外围留下一定的距离，并在subplot之间留下一定的间距，间距和图像的高度和宽度有关，因此调整了图像的大小（不管是编程还是手工）间距会自动调整，利用figure的==subplots_adjust==方法可以修改间距，此外它是个顶级函数

```
subplots_adjust(left=None, bottom=None,right=None, top=None, wspace=None,hspace=None)
```

- wspach和hspace是控制高度和宽度的百分比，用作subplot之间的间距

  开始的效果:![016](D:\project\pycon\DA\img\016.JPG)

  ```
  # 下面将间距收到0
  fig, axes = plt.subplots(2,2, sharex=True, sharey=True)
  for i in range(2):
      for j in range(2):
          axes[i,j].hist(np.random.randn(500),bins=50,color='k',alpha=0.5)
  plt.subplots_adjust(wspace=0,hspace=0)
  ```

  ![017](D:\project\pycon\DA\img\017.JPG)

#### 颜色、标记和线型

绘图函数plot接收x和y坐标，还接收一个表示颜色和线型的字符串缩写，

```
ax.plot(x,y,'g--')
# 更明确的方式
ax.plot(x,y,linestyle='--',color='g')
```

常用的颜色都有一个 缩写词，要使用其他颜色则可以通过指定其rgb值形式使用（例：’#CECECE’）

线型图还可以加上一些标记，以强调实际的数据点

标记也可以放到格式字符串中，但==标记类型和线型必须放在颜色后面==

线型图中，非实际数据点默认是按==线性方式插值==的，可以通过drawstyle选项修改：

```
data = np.random.randn(30).cumsum()
plt.plot(data,'k--')
```

![018](D:\project\pycon\DA\img\018.JPG)

```
plt.plot(data,'k-', drawstyle='steps-post')
```

![019](D:\project\pycon\DA\img\019.JPG)

#### 刻度、标签和图例

对于大多数的图表装饰项，实现方式有二：使用过程性的pyplot接口，以及面向对象的原生api

pyplot接口设计的目的就是交互使用，有类似 xlim, xticks 和 xticklabels等方法，使用方法有两种：

- 调用时不带参数，则返回当前参数  `plt.xlim()`

- 调用待参数，则设置参数   `plt.xlim([0,10])`

  > 这些方法都是对当前或最近创建的AxesSubplot 起作用，各自对应subplot的两个方法，`ax.get_xlim`和`ax.set_xlim`

##### 设置标题，轴标签，刻度和刻度标签

```python
# 创建一个随机漫步
# 创建画板
fig = plt.figure()
# 创建绘图区
ax = fig.add_subplot(1,1,1)
# 设置刻度值
ticks = ax.set_xticks([0,250,500,750,1000])
# 设置刻度值对应表示
labels = ax.set_xticklabels(['one', 'two', 'three', 'four', 'five'],
                           rotation=30, fontsize='small')
# 设置标题
ax.set_title('my first matplotlib plot')
# 设置x轴标签
ax.set_xlabel('Stages')
# label是对应图线的标签，后面需要添加legend函数才能显示出来
ax.plot(np.random.randn(1000).cumsum(),'k',label='random walk')
# ax.legend()或plt.legend()
ax.legend()
```

![020](D:\project\pycon\DA\img\020.JPG)

```python
# 不同线型图的三种效果对比
ax.plot(np.random.randn(1000).cumsum(),'k',label='random walk')

ax.plot(np.random.randn(1000).cumsum(),'k--',label='two')

ax.plot(np.random.randn(1000).cumsum(),'k.',label='three')
```

![021](D:\project\pycon\DA\img\021.JPG)

##### 添加图例 legend

用于表示图表元素的工具，添加图例方法有二：

- 在添加subplot的时候传入label参数

  ```
  fig = plt.figure();ax = fig.add_subplot(1,1,1)
  ax.plot(np.random.randn(1000).cumsum(),'k',label='one')
  ```

  之后你可以调用`ax.legend()` 或 `plt.legend()`来自动创建图例

  ```
  # loc 告诉plt 要将图例放在哪，如果不是吹毛求疵，‘best'是不错的选择（选择最不碍事的地方）
  ax.legend(loc='best')
  ```

  要从图例中去除一个或多个元素，不传入label或传入`label='_nolegend_'`

#### 添加注解及在subplot上绘图

除了标准图像外，你可能希望绘制一些子定义的注解（文本、箭头、或其他）

注解可以通过 text 、arrow、annotate 等添加

- text可以将文本绘制在指定的位置，还可以加自定格式

  `ax.text(x,y,'hello world',family='monospace',fontsize=10)`

- 注解实例

  ```python
  ![022](D:\project\pycon\DA\img\022.JPG)from datetime import datetime
  import pandas as pd
  
  # 创建绘图区
  fig = plt.figure()
  ax = fig.add_subplot(111)
  # 读取数据
  data = pd.read_csv('./spx.csv',index_col=0,parse_dates=True)
  spx = data['SPX']
  # 要注解的时间点
  crisis_data = [(datetime(2007, 10, 11), 'Peak of bull market'),
                 (datetime(2008, 3, 12), 'Bear Stearns Fails'),
                 (datetime(2008, 9, 15), 'Lehman Bankruptcy') ]
  # 添加注解
  for date, label in crisis_data:
      ax.annotate(label, xy=(date, spx.asof(date) + 75),
                  xytext=(date, spx.asof(date) + 225),
                  arrowprops=dict(facecolor='black', headwidth=4, width=2,headlength=4),
                  horizontalalignment='left', verticalalignment='top')
  # 绘图
  spx.plot(ax=ax,style='k-')
  
  # 轴的缩放需放在绘图函数之后
  # Zoom in on 2007-2010 
  ax.set_xlim(['1/1/2007', '1/1/2011']) 
  ax.set_ylim([600, 1800])
  ```

![022](D:\project\pycon\DA\img\022.JPG)

图形注解的绘制要麻烦一些，matplotlib 有一些常见的图形的对象，这些对象被称为patch,有些可以在matplotlib.pyplot中找到，完整集合位于matplotlib.patches

- 要在图表中添加一个图形，需要创建一个块对象shp,然后通过`ax.add_patch(shp)`将其添加到subplot中

  ```
  fig = plt.figure() 
  ax = fig.add_subplot(1, 1, 1)
  
  rect = plt.Rectangle((0.2, 0.75), 0.4, 0.15, color='k', alpha=0.3) 
  circ = plt.Circle((0.7, 0.2), 0.15, color='b', alpha=0.3)
  pgon = plt.Polygon([[0.15, 0.15], [0.35, 0.4], [0.2, 0.6]],color='g', alpha=0.5)
  
  ax.add_patch(rect) 
  ax.add_patch(circ) 
  ax.add_patch(pgon)
  ```

  ![023](D:\project\pycon\DA\img\023.JPG)

#### 将图表保存到文件

- 注意：

  使用plt.savefig时，经常得到的时一片空白

  > 产生这个现象的原因很简单：在 `plt.show()` 后调用了 `plt.savefig()` ，在 `plt.show()` 后实际上已经创建了一个新的空白的图片（坐标轴），这时候你再 `plt.savefig()` 就会保存这个新生成的空白图片

  解决方式：

  - 在 `plt.show()` 之前调用 `plt.savefig()`

  - 画图的时候获取当前图像

    ```
    fig = plt.gcf()
    plt.show()
    fig1.savefig('tessstttyyy.png', dpi=100)
    ```

- 发布图片时经常用到两个重要的选项时dpi和bbox_inches

  - dpi:分辨率（没英寸的点数）
  - bbox_inches:剪除当前图表周围的空白部分

  ```
  # 得到一个有最小白边和400dpi的图片
  plt.savefig('figpath.png', dpi=400, bbox_inches='tight')
  ```

- savefig并不是一定写入磁盘，可以写入任何文件对象，比如 StringIO

  ```
  from io import StringIO
  buffer = StringIO()
  plt.savefig(buffer)
  plot_data = buffer.getvalue()
  # 这对在web上提供动态生成的图片很实用
  ```

- savefig的选项

  | 选项                 | 用法                                                       |
  | -------------------- | ---------------------------------------------------------- |
  | fname                | 文件路径的字符串或python文件对象                           |
  | dpi                  | 分辨率，默认100                                            |
  | facecolor、edgecolor | 背景颜色，默认’w' 白色                                     |
  | format               | 文件格式：png\|pdf\|svg\|ps\|eps...                        |
  | bbox_inches          | 图表需要保留的部分，如果设置‘tight',则尝试剪除图表周边空白 |

#### matplotlib配置

matplotlib自带一些配色方案，以及生成出版质量的图片而设定的默认配置信息

几乎所有的默认行为都能通过一组全局参数自定义，可管理图形大小，subplot边距，配色方案，字体大小，网格类型等

操作matplotlib的配置系统方式主要有两种：

- python编程方式，即利用rc方法

  ```
  # 如将全局的图形大小设置为10*10
  plt.rc('figure', figsize=(10,10))
  ```

  rc的第一个参数是希望自定义的对象：figure,axes,xtick,ytick,grid,legend,其后跟上一系列关键字参数，最简单的方式是将其写成一个字典：

  ```python
  font_options = {'family' : 'monospace',
                  'weight' : 'bold',
                  'size'   : 'small'}
  plt.rc('font', **font_options) 
  ```

  要了解全部的自定义选项，请查阅matplotlib的配置文件matplotlibrc

### pandas绘图函数

matplotlib实际是一种低级的工具，要组装一张表，你得用它的各种基础组件才行，包括：

数据展示（线型图，柱状图，盒形图，散布图，等值线图等），图例，标题，刻度标签以及其他注解型信息

在pandas中，我们有行标签，列标签以及分组信息，要制作图表会简单很多，pandas有许多能利用DataFrame对象数据组织特点来创建标准图表的高级绘图方法（这些函数的数量在不断增加）

Another library is seaborn, a statistical graphics library created by Michael Waskom. Seaborn simplifies creating many common visualization types.

#### Line Plots

__Series __and __DataFrame__ each have a ==plot== attribute for making some basic plot types. By default, plot() makes ==line plots==

```
s = pd.Series(np.random.randn(10).cumsum(), index=np.arange(0,100,10))
s.plot()
```

![024](D:\project\pycon\DA\img\024.JPG)

Series object’s __index__ is passed to matplotlib for plotting on the __x-axis__

disable this by passing __use_index=False__

![025](D:\project\pycon\DA\img\025.JPG)

Most of pandas’s plotting methods accept an optional ==ax== parameter, which can be a ==matplotlib subplot object==

DataFrame’s plot method plots each of its __columns__ as a different __line__ on the same subplot

```python
df = pd.DataFrame(np.random.randn(10,4).cumsum(0),
                 columns=['A','B','C','D'],
                 index=np.arange(0,100,10))
df.plot()
```

![026](D:\project\pycon\DA\img\026.JPG)

plot属性包含用于不同plot类型的方法的“家族”。例如，df.plot()等同于df.plot.line()

- Series.plot method arguments 

| 参数      | 说明                                                         |
| --------- | ------------------------------------------------------------ |
| label     | 图例的标签                                                   |
| ax        | 要在其上绘制的matplotlib subplot 对象，如果没有设置，则使用当前matplotlib subplot |
| style     | 将要传给matplotlib的风格字符串（如‘ko--）                    |
| alpha     | 不透明度（0-1）                                              |
| kind      | 可以是 line,bar，barh,kde                                    |
| logy      | 在y轴使用对数标尺                                            |
| use_index | 是否将对象的索引用于刻度标签                                 |
| rot       | 旋转刻度标签（0-360）                                        |
| xticks    | 用作x轴刻度的值                                              |
| yticks    | 用作y轴刻度的值                                              |
| xlim      | x轴的界限                                                    |
| ylim      | y轴的界限                                                    |
| grid      | 显示轴网格线（默认打开）                                     |

DataFrame-specific plot arguments 

| Argument     | Description                                                  |
| ------------ | ------------------------------------------------------------ |
| subplots     | 将各个DataFrame列绘制到单独的subplot中                       |
| sharex       | If subplots=True, share the same x-axis, linking ticks and limits |
| sharey       | If subplots=True, share the same y-axis                      |
| figsize      | Size of figure to create as tuple                            |
| title        | Plot title as string                                         |
| legend       | Add a subplot legend (True by default)                       |
| sort_columns | Plot columns in ==alphabetical order==; by default uses ==existing column order== |

#### Bar Plots

The plot.bar() and plot.barh() make ==vertical and horizontal== bar plots,In this case, the Series or DataFrame index will be used as the ==x (bar) or y (barh) ticks== 

- series数据

```python
fig,axes = plt.subplots(2,1)
data = pd.Series(np.random.rand(16),index=list('abcdefghijklmnop'))
>>>
a    0.258936
b    0.778937
c    0.947043
d    0.664408
e    0.084629
f    0.491530
g    0.103769
h    0.478309
i    0.529022
j    0.279143
k    0.648734
l    0.125838
m    0.421898
n    0.908906
o    0.742911
p    0.308533
dtype: float64
    
data.plot.bar(ax = axes[0], color='k', alpha=0.7)
data.plot.barh(ax = axes[1], color='k', alpha=0.5)
```

![027](D:\project\pycon\DA\img\027.JPG)

- dataframe数据

With a DataFrame, bar plots group the values in each ==row== together in a group in bars, side by side, for each value

```python
df = pd.DataFrame(np.random.rand(6,4),
                 index = ['one', 'two', 'three', 'four', 'five', 'six'],
                 columns=pd.Index(['A', 'B', 'C', 'D'], name='Genus'))
df
>>>
Genus	A	B	C	D
one	0.654920	0.266255	0.240536	0.728566
two	0.133819	0.587877	0.739531	0.813920
three	0.052354	0.683215	0.275638	0.272895
four	0.669792	0.955640	0.651783	0.637709
five	0.483585	0.563594	0.531367	0.912491
six	0.715706	0.581392	0.808408	0.566735
# 显示条形图
df.plot.bar()
```

dataframe的列名 Genus 被用作了图例的标题

![028](D:\project\pycon\DA\img\028.JPG)

- 设置 stacked = True即可为dataframe 生成堆积柱状图，这样每行的图会被堆积在一起

  `df.plot.barh(stacked=True,alpha=0.5)`

  ![029](D:\project\pycon\DA\img\029.JPG)

- 柱状图有个不错的用法：用value_counts图形化显示Series中各值出现的频率

  `s.value_counts().plot(kind='bar')`

- 利用小费相关的数据集展示聚会规模的数据点的百分比

  ```python
  tips = pd.read_csv('./tips.csv')
  tips.head()
  >>>
  total_bill	tip	smoker	day	time	size
  0	16.99	1.01	No	Sun	Dinner	2
  1	10.34	1.66	No	Sun	Dinner	3
  2	21.01	3.50	No	Sun	Dinner	3
  3	23.68	3.31	No	Sun	Dinner	2
  4	24.59	3.61	No	Sun	Dinner	4
  
  party_counts = pd.crosstab(tips['day'],tips['size'])
  party_counts = party_counts.loc[:,2:5]
  party_pcts = party_counts.div(party_counts.sum(1),axis=0)
  party_pcts.plot.bar(grid=True)
  ```

  ![030](D:\project\pycon\DA\img\030.JPG)

- seaborn的使用

  ```python
  import seaborn as sns
  
  # 加载小费数据集
  tips = pd.read_csv('./tips.csv')
  # 计算小费百分比
  tips['tip_pct'] = tips['tip']/(tips['total_bill']-tips['tip'])
  tips.head()
  >>>
  total_bill	tip	smoker	day	time	size	tip_pct
  0	16.99	1.01	No	Sun	Dinner	2	0.063204
  1	10.34	1.66	No	Sun	Dinner	3	0.191244
  2	21.01	3.50	No	Sun	Dinner	3	0.199886
  3	23.68	3.31	No	Sun	Dinner	2	0.162494
  4	24.59	3.61	No	Sun	Dinner	4	0.172069
  
  # 绘图
  sns.barplot(x='tip_pct', y='day', data=tips, orient='h')
  ```

![031](D:\project\pycon\DA\img\031.JPG)

```python
# You can switch between different plot appearances using seaborn.set
sns.set(style='whitegrid')


# seaborn.barplot has a hue option that enables us to split by an additional categorical value
sns.barplot(x='tip_pct', y='day', hue='time', data=tips, orient='h')
```

![032](D:\project\pycon\DA\img\032.JPG)

#### Histograms and Density Plots (直方图和密度图)

==直方图==是一种可以对值频率进行离散化显示的柱状图，数据点被拆分到离散的、间隔均匀的面元中，绘制的是各面元中数据点的数量

```python
tips
>>>
total_bill	tip	smoker	day	time	size	tip_pct
0	16.99	1.01	No	Sun	Dinner	2	0.063204
1	10.34	1.66	No	Sun	Dinner	3	0.191244
2	21.01	3.50	No	Sun	Dinner	3	0.199886
3	23.68	3.31	No	Sun	Dinner	2	0.162494
4	24.59	3.61	No	Sun	Dinner	4	0.172069
5	25.29	4.71	No	Sun	Dinner	4	0.228863
6	8.77	2.00	No	Sun	Dinner	2	0.295421
```

```
tips['tip_pct'] = tips['tip']/tips['total_bill']
tips['tip_pct'].hist(bins=50)
```

![033](D:\project\pycon\DA\img\033.JPG)

==密度图==是通过计算“__可能会产生观测数据的连续概率分布的估计__”而产生的，一般的过程是将该分布近似为一组核（诸如正态分布之类的较为简单的分布）

因此密度图也被称为KDE图（Kernel Density Estimate 核密度估计）

调用plot时加上kind='kde'即可生成一张密度图（标准混合正态分布KDE）

```python
tips['tip_pct'].plot(kind='kde')
```

![034](D:\project\pycon\DA\img\034.JPG)

这两种图常常会被画在一起，直方图以规格化形式给出，然后再在其上绘制和密度估计

```python
# (Gaussian) distribution
# 参数1 Mean ("centre") of the distribution.
# 参数2 Standard deviation (spread or "width") of the distribution

comp1 = np.random.normal(0,1,size=200)
comp2 = np.random.normal(10,2,size=200)

values = pd.Series(np.concatenate([comp1,comp2]))
values.hist(bins=100,alpha=0.3,color='k',normed=True)
values.plot(kind='kde',style='k--')
```

s![035](D:\project\pycon\DA\img\035.JPG)

```
pd.Series.hist(self, by=None, ax=None, grid=True, xlabelsize=None, xrot=None, ylabelsize=None, yrot=None, figsize=None, bins=10, **kwds)
```

#### Scatter or Point Plots （散布图）

散布图是观察两个一维数据序列之间的关系的有效方法 matplotlib的scatter方法是绘制散布图的主要方法

```python
# 加载statsmodels项目的macrodata 数据集，然后计算对数差
macro = pd.read_csv('./macrodata.csv')
macro.head()
>>>
year	quarter	realgdp	realcons	realinv	realgovt	realdpi	cpi	m1	tbilrate	unemp	pop	infl	realint
0	1959.0	1.0	2710.349	1707.4	286.898	470.045	1886.9	28.98	139.7	2.82	5.8	177.146	0.00	0.00
1	1959.0	2.0	2778.801	1733.7	310.859	481.301	1919.7	29.15	141.7	3.08	5.1	177.830	2.34	0.74
2	1959.0	3.0	2775.488	1751.8	289.226	491.260	1916.4	29.35	140.5	3.82	5.3	178.657	2.74	1.09
3	1959.0	4.0	2785.204	1753.7	299.356	484.052	1931.3	29.37	140.0	4.33	5.6	179.386	0.27	4.06
4	1960.0	1.0	2847.699	1770.5	331.722	462.199	1955.5	29.54	139.6	3.50	5.2	180.007	2.31	1.19


data = macro[['cpi', 'm1','tbilrate', 'unemp']]
trans_data = np.log(data).diff().dropna()
trans_data[-5:]
>>>
cpi	m1	tbilrate	unemp
198	-0.007904	0.045361	-0.396881	0.105361
199	-0.021979	0.066753	-2.277267	0.139762
200	0.002340	0.010286	0.606136	0.160343
201	0.008419	0.037461	-0.200671	0.127339
202	0.008894	0.012202	-0.405465	0.042560

plt.scatter(trans_data['m1'],trans_data['unemp'])
plt.title('Changes in log %s vs.log %s' %('m1','unemp'))
```

![036](D:\project\pycon\DA\img\036.JPG)

### 绘制地图：图形化显示海地地震危机数据

Ushahidi是一家非营利软件公司，人们可以通过短信向其提供自然灾害和地缘政治事件信息，数据会发布在他们的网站（http://communty.ushahidi.com/research/datasets/）上以供分析与图形化

- [ ] 下面用pandas来实现==后续研究==

```

```

























## 第九章 数据聚合与分组运算

### GroupBy技术

一个用于表示分组运算的术语“split-apply-combine"(拆分-应用-合并)

分组运算的第一个阶段，pandas对象中的数据会根据提供的键被拆分（split）为分组，拆分操作是在对象的特定轴上执行的（dataframe可以在其行或列上进行分组），然后将一个函数应用（apply）到各个分组并产生一个新值,最后，所有这些函数的执行结果会被合并（combine）到最终的结果对象中

![037](D:\project\pycon\DA\img\037.JPG)

- 分组键可以有多种形式，类型不必相同

  - 列表或数组，其长度与待分组的轴一样
  - 表示dataframe某个列名的值
  - 字典或series,给出待分组轴上的值与分组名之间的对应关系
  - 函数，用于处理轴索引或索引中的标签

  > 后三种只是快捷方式而已，最终目的仍然是产生一组用于拆分对象的值

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 利用列名和数据构建dataframe
df = pd.DataFrame({
    'key1':['a', 'a', 'b', 'b', 'a'],
    'key2' : ['one', 'two', 'one', 'two', 'one'],
    'data1' : np.random.randn(5),
    'data2' : np.random.randn(5)
})
df
>>>
	key1	key2	data1	data2
0	a	one	-0.223888	0.114470
1	a	two	0.624460	-1.265352
2	b	one	0.371178	1.426521
3	b	two	-1.663985	0.810567
4	a	one	-0.570321	-0.005611
```

利用key1进行分组，并计算data1列的均值

- 方式：访问data1,并根据key1调用groupby

  ```python
  grouped = df['data1'].groupby(df['key1'])
  grouped
  >>>
  <pandas.core.groupby.groupby.SeriesGroupBy object at 0x000002AC8FF30FD0>
  ```

变量grouped是一个groupby对象，它实际上还没有进行计算，只是含有一些分组键df['key1']的中间数据

简言之该对象有了对各分组执行运算的所有信息

```
grouped.mean()
>>>
key1
a   -0.056583
b   -0.646404
Name: data1, dtype: float64
```

数据根据  分组键  进行了聚合，产生了一个新的series,其索引为key1列中的唯一值

一次传入多个数组,通过多个键对数据进行分组，得到具有层次化索引的series

```
means = df['data1'].groupby([df['key1'],df['key2']]).mean()
means
>>>
key1  key2
a     one    -0.397105
      two     0.624460
b     one     0.371178
      two    -1.663985
Name: data1, dtype: float64
```

分组可以是任何长度适当的数组

```
states = np.array(['Ohio', 'California', 'California', 'Ohio', 'Ohio'])
years = np.array([2005, 2005, 2006, 2005, 2006])
df['data1'].groupby([states,years]).mean()
>>>
California  2005    0.624460
            2006    0.371178
Ohio        2005   -0.943936
            2006   -0.570321
Name: data1, dtype: float64
```

还可以将列名(可以是字符，数字等)作为分组建

```
df.groupby('key1').mean()
>>>
		data1	data2
key1		
a	-0.056583	-0.385498
b	-0.646404	1.118544

df.groupby(['key1','key2']).mean()
>>>
		data1	data2
key1	key2		
a	one	-0.397105	0.054429
two	0.624460	-1.265352
b	one	0.371178	1.426521
two	-1.663985	0.810567
```

groupby进行分组时对非数据列（麻烦列）进行了排除，默认情况下所有数值都会被聚合

size方法返回分组大小

```
df.groupby(['key1','key2']).size()
>>>
key1  key2
a     one     2
      two     1
b     one     1
      two     1
dtype: int64
```

#### 对分组进行迭代

groupby对象==支持迭代==，可以产生一组二元元组，由分组名和数据块组成

对于未进行计算的groupby对象，使用list操作可以让其显示结果

```python
df.groupby('key1')
>>>
<pandas.core.groupby.groupby.DataFrameGroupBy object at 0x000002AC92BAA2E8>
list(df.groupby('key1'))
>>>
[('a',   key1 key2     data1     data2
  0    a  one -0.223888  0.114470
  1    a  two  0.624460 -1.265352
  4    a  one -0.570321 -0.005611), ('b',   key1 key2     data1     data2
  2    b  one  0.371178  1.426521
  3    b  two -1.663985  0.810567)]
```

可以对数据片段做任何操作，一个很有用的操作是将其做成字典

```python
pieces = dict(list(df.groupby('key1')))
pieces
>>>
{'a':   key1 key2     data1     data2
 0    a  one -0.223888  0.114470
 1    a  two  0.624460 -1.265352
 4    a  one -0.570321 -0.005611, 'b':   key1 key2     data1     data2
 2    b  one  0.371178  1.426521
 3    b  two -1.663985  0.810567}
type(pieces['b'])
>>>
pandas.core.frame.DataFrame
```

groupby默认在axis=0上进行分组，通过设置可以对任何轴进行分组

```
list(df.groupby(df.dtypes,axis=1))
>>>
[(dtype('float64'),       data1     data2
  0 -0.223888  0.114470
  1  0.624460 -1.265352
  2  0.371178  1.426521
  3 -1.663985  0.810567
  4 -0.570321 -0.005611), (dtype('O'),   key1 key2
  0    a  one
  1    a  two
  2    b  one
  3    b  two
  4    a  one)]
```

#### 选取一个或一组列

对于由dataFrame产生的groupby对象，如果用一个或一组列名对其进行索引，就能实现选取部分列进行聚合的目的

```python
df.groupby('key1')['data1']
df.groupby('key1')[['data2']]
# 以上是以下的语法糖
df['data1'].groupby(df['key1'])
df[['data2']].groupby(df['key1']) 
```

对于大数据集，很可能只对部分列进行聚合，对于之前数据集只求data2列的平均值并以dataframe形式得到结果

```python
df.groupby(['key1','key2'])[['data2']].mean()
>>>
data2
key1	key2	
a	one	0.054429
two	-1.265352
b	one	1.426521
two	0.810567
```

这种索引操作返回的对象是一个已分组的DataFrame或Series

```python
s_grouped = df.groupby(['key1', 'key2'])['data2']
s_grouped
>>>
<pandas.core.groupby.SeriesGroupBy object at 0x7faa30c78da0>
s_grouped.mean() 
>>>
key1  key2
a     one     0.054429
      two    -1.265352
b     one     1.426521
      two     0.810567
Name: data2, dtype: float64
```

#### 通过字典或Series进行分组

```python
people = pd.DataFrame(
    np.random.randn(5,5),
    index=['Joe', 'Steve', 'Wes', 'Jim', 'Travis'],
    columns=['a', 'b', 'c', 'd', 'e']
)
people
>>>
a	b	c	d	e
Joe	-1.530118	-0.355276	-1.780145	-0.060734	0.870525
Steve	1.228132	1.974597	1.269202	0.691717	0.099211
Wes	-0.556833	-1.178751	0.856106	0.129820	0.329898
Jim	-1.141639	-0.019510	-0.939034	-0.369156	-0.496966
Travis	1.149363	1.781469	-0.463331	0.280201	-0.407344
# 插入空值  df.iloc[行，列] = np.nan
people.iloc[2:3, [1,2]] = np.nan
people
>>>
a	b	c	d	e
Joe	-1.530118	-0.355276	-1.780145	-0.060734	0.870525
Steve	1.228132	1.974597	1.269202	0.691717	0.099211
Wes	-0.556833	NaN	NaN	0.129820	0.329898
Jim	-1.141639	-0.019510	-0.939034	-0.369156	-0.496966
Travis	1.149363	1.781469	-0.463331	0.280201	-0.407344

mapping = {'a': 'red', 'b': 'red', 'c': 'blue',
           'd': 'blue', 'e': 'red', 'f' : 'orange'} 
by_column = people.groupby(mapping,axis=1)
by_column.sum()
>>>
blue	red
Joe	-1.840878	-1.014868
Steve	1.960920	3.301940
Wes	0.129820	-0.226935
Jim	-1.308190	-1.658116
Travis	-0.183130	2.523488
```

series作为分组键，pandas会检查series以确保其索引跟分组轴是对齐的

```
map_series = pd.Series(mapping)
map_series
>>>
a       red
b       red
c      blue
d      blue
e       red
f    orange
dtype: object

people.groupby(map_series,axis=1).sum()
>>>
	blue	red
Joe	-1.840878	-1.014868
Steve	1.960920	3.301940
Wes	0.129820	-0.226935
Jim	-1.308190	-1.658116
Travis	-0.183130	2.523488
```

#### 通过函数进行分组

相较与字典、series，python函数在定义分组映射关系时可以更有创意且更为抽象，任何被当作分组键的函数都会在各个索引值上被调用一次

```python
# 例如希望根据人名的长度来分组，仅仅需要传入len函数
people.groupby(len).sum()
>>>
	a	b	c	d	e
3	-3.228590	-0.374786	-2.719178	-0.300070	0.703458
5	1.228132	1.974597	1.269202	0.691717	0.099211
6	1.149363	1.781469	-0.463331	0.280201	-0.407344
```

将函数、列表、字典、Series混合使用也没问题，因为任何东西最终都会被转换为数组

```python
# 只需将各个项放入一个列表即可
key_list = ['one', 'one', 'one', 'two', 'two']
people.groupby([len, key_list]).min()
```

#### 根据索引级别分组

层次化索引数据集最方便的地方就在于它能够根据==索引级别==进行聚合，通过==level==关键字传入级别编号或名称

```python
columns = pd.MultiIndex.from_arrays(
    # 第一层级
    [['US', 'US', 'US', 'JP', 'JP'],
    # 第二层级
     [1, 3, 5, 1, 3]],
    # 层级的名字集合
    names=['cty', 'tenor'])
columns
>>>
MultiIndex(levels=[['JP', 'US'], [1, 3, 5]],
           labels=[[1, 1, 1, 0, 0], [0, 1, 2, 0, 1]],
           names=['cty', 'tenor'])
hier_df = pd.DataFrame(np.random.randn(4,5), columns=columns)
hier_df
>>>
cty	US	JP
tenor	1	3	5	1	3
0	0.744874	-0.024091	-1.149179	0.267842	-1.054643
1	-0.929076	-0.933683	-0.011677	-0.910201	0.431937
2	0.520172	-1.494227	1.454167	0.488063	2.434893
3	-0.055138	-0.040540	0.790086	-0.458118	-2.125981
hier_df.groupby(level='cty', axis=1).count()
>>>
cty	JP	US
0	2	3
1	2	3
2	2	3
3	2	3
```



### 数据聚合

对于聚合指的是任何能够从数组产生标量值的数据转换

许多聚合运算都有就地计算数据集统计信息的优化实现，也可以调用分组对象上定义好的方法

```python
# 利用quantile可计算series和dataframe的样本分位数
grouped = df.groupby['key1']
grouped['data1'].quantile(0.9)
>>>
key1
a    0.454790
b    0.167661
Name: data1, dtype: float64
```

quantile并没有实现与groupby，是一个series方法，这里也能使用

如果要使用自己的聚合函数，只需将其传入==aggregate(集合)==或agg方法即可：

```python
def peak_to_peak(arr):
    return arr.max() - arr.min()

grouped.agg(peak_to_peak)
```

describe严格来说不是聚合运算

- groupby的方法

  | 函数        | 说明                          |
  | ----------- | ----------------------------- |
  | count       | 分组中非NA值的数量            |
  | sum         | 非NA值的和                    |
  | mean        | 非ＮA 的平均值                |
  | median      | 算术平均数                    |
  | std、var    | 无偏（分母为n-1）标准差和方差 |
  | min、max    | 非NA值的最小最大值            |
  | prod        | 非NA的积                      |
  | first、last | 第一个和最后一个非ＮＡ值      |

#### 面向列的多函数应用

对series和dataframe的列的聚合其实就是使用aggregate或调用mean、std方法

```python
grouped = tips.groupby(['day', 'smoker'])
grouped_pct = grouped['tip_pct']
grouped_pct.agg('mean')
>>>
day   smoker
Fri   No        0.151650
      Yes       0.174783
Sat   No        0.158048
      Yes       0.147906
Sun   No        0.160113
      Yes       0.187250
Thur  No        0.160298
      Yes       0.163863
Name: tip_pct, dtype: float64
```

统计方法可以传入一组，得到dataframe的列，就会以相应的函数命名

```
grouped_pct.agg(['mean','std',peak_to_peak])
>>>
	mean	std	peak_to_peak
day	smoker			
Fri	No	0.151650	0.028123	0.067349
Yes	0.174783	0.051293	0.159925
Sat	No	0.158048	0.039767	0.235193
Yes	0.147906	0.061375	0.290095
Sun	No	0.160113	0.042347	0.193226
Yes	0.187250	0.154134	0.644685
Thur	No	0.160298	0.038774	0.193350
Yes	0.163863	0.039389	0.151240
```

并不一定要接收自动给出的列名，特别是lambda，它的名称是<lambda>,这样辨识度就很低

如果传入的是一个由==（name,function）==元组组成的列表，则各个元组的第一个元素会被用作列名

```python
grouped_pct.agg([('foo','mean'),('bar',np.std)])
>>>

         foo	bar
day	smoker		
Fri	No	0.151650	0.028123
Yes	0.174783	0.051293
Sat	No	0.158048	0.039767
Yes	0.147906	0.061375
Sun	No	0.160113	0.042347
Yes	0.187250	0.154134
Thur	No	0.160298	0.038774
Yes	0.163863	0.039389
```

对于dataframe定义一组应用于全部列的函数，或不同的列应用不同的函数

```python
functions = ['count','mean','max']
result = grouped['tip_pct','total_bill'].agg(functions)
result
>>>
tip_pct	total_bill
count	mean	max	count	mean	max
day	smoker						
Fri	No	4	0.151650	0.187735	4	18.420000	22.75
Yes	15	0.174783	0.263480	15	16.813333	40.17
Sat	No	45	0.158048	0.291990	45	19.661778	48.33
Yes	42	0.147906	0.325733	42	21.276667	50.81
Sun	No	57	0.160113	0.252672	57	20.506667	48.17
Yes	19	0.187250	0.710345	19	24.120000	45.35
Thur	No	45	0.160298	0.266312	45	17.113111	41.19
Yes	17	0.163863	0.241255	17	19.190588	43.11
```

可以传入自定的名称的元组列表

```python
ftuples = [('durchschnitt','mean'),('abweichung',np.var)]
grouped['tip_pct','total_bill'].agg(ftuples)
>>>
tip_pct	total_bill
durchschnitt	abweichung	durchschnitt	abweichung
day	smoker				
Fri	No	0.151650	0.000791	18.420000	25.596333
Yes	0.174783	0.002631	16.813333	82.562438
Sat	No	0.158048	0.001581	19.661778	79.908965
Yes	0.147906	0.003767	21.276667	101.387535
Sun	No	0.160113	0.001793	20.506667	66.099980
Yes	0.187250	0.023757	24.120000	109.046044
Thur	No	0.160298	0.001503	17.113111	59.625081
Yes	0.163863	0.001551	19.190588	69.808518
```

```python
对不同的列应用不同的函数，向agg传入一个从列名映射函数的字典
grouped.agg({'tip':np.max,'size':'sum'})
>>>
		tip	size
day	smoker		
Fri	No	3.50	9
Yes	4.73	31
Sat	No	9.00	115
Yes	10.00	104
Sun	No	6.00	167
Yes	6.50	49
Thur	No	6.70	112
Yes	5.00	40

grouped.agg({'tip_pct':['min','max','mean','std'],
            'size':'sum'})
>>>
		tip_pct	   size
min	max	mean	std	sum
day	smoker					
Fri	No	0.120385	0.187735	0.151650	0.028123	9
Yes	0.103555	0.263480	0.174783	0.051293	31
Sat	No	0.056797	0.291990	0.158048	0.039767	115
Yes	0.035638	0.325733	0.147906	0.061375	104
Sun	No	0.059447	0.252672	0.160113	0.042347	167
Yes	0.065660	0.710345	0.187250	0.154134	49
Thur	No	0.072961	0.266312	0.160298	0.038774	112
Yes	0.090014	0.241255	0.163863	0.039389	40
```

#### 以“无索引”的形式返回聚合数据

目前所示例的聚合数据都有由唯一的分组键组成的索引，由于并不总是需要如此，所以你可以向groupby传入as_index=False以禁止该功能

```python
tips.groupby(['day','smoker']).mean()
>>>
total_bill	tip	size	tip_pct
day	smoker		
Fri	No	18.420000	2.812500	2.250000	0.151650
Yes	16.813333	2.714000	2.066667	0.174783
Sat	No	19.661778	3.102889	2.555556	0.158048
Yes	21.276667	2.875476	2.476190	0.147906
Sun	No	20.506667	3.167895	2.929825	0.160113
Yes	24.120000	3.516842	2.578947	0.187250
Thur	No	17.113111	2.673778	2.488889	0.160298
Yes	19.190588	3.030000	2.352941	0.163863

tips.groupby(['day','smoker'],as_index=False).mean()
>>>
day	smoker	total_bill	tip	size	tip_pct
0	Fri	No	18.420000	2.812500	2.250000	0.151650
1	Fri	Yes	16.813333	2.714000	2.066667	0.174783
2	Sat	No	19.661778	3.102889	2.555556	0.158048
3	Sat	Yes	21.276667	2.875476	2.476190	0.147906
4	Sun	No	20.506667	3.167895	2.929825	0.160113
5	Sun	Yes	24.120000	3.516842	2.578947	0.187250
6	Thur	No	17.113111	2.673778	2.488889	0.160298
7	Thur	Yes	19.190588	3.030000	2.352941	0.163863
```



### 分组级运算与转换

聚合只不过是分组运算的其中一种，是数据转换的一个特例

接收能将一维数据简化为标量值的函数

transform和apply方法能够执行更多的分组运算

#### apply:一般性的“拆分-应用-合并”

和aggregate一样，transform也是一个有着严格条件的特殊函数，传入的函数只能产生两种结果，要么产生一个可以广播的标量值，要么产生一个相同大小的数组

apply会将待处理的对象拆分成多段，对各段调用函数，最后将各片段组合到一起

```python
# 根据分组选出最高的5个tip_pct
# 编写一个选取指定列具有最大值的行的函数
def top(df,n=5, column='tip_pct'):
    return df.sort_values(by=column)[-n:]
top(tips,n=6)
>>>
total_bill	tip	smoker	day	time	size	tip_pct
109	14.31	4.00	Yes	Sat	Dinner	2	0.279525
183	23.17	6.50	Yes	Sun	Dinner	4	0.280535
232	11.61	3.39	No	Sat	Dinner	2	0.291990
67	3.07	1.00	Yes	Sat	Dinner	1	0.325733
178	9.60	4.00	Yes	Sun	Dinner	2	0.416667
172	7.25	5.15	Yes	Sun	Dinner	2	0.710345
```

```python
tips.groupby('smoker').apply(top)
>>>
	total_bill	tip	smoker	day	time	size	tip_pct
smoker								
No	88	24.71	5.85	No	Thur	Lunch	2	0.236746
    185	20.69	5.00	No	Sun	Dinner	5	0.241663
    51	10.29	2.60	No	Sun	Dinner	2	0.252672
    149	7.51	2.00	No	Thur	Lunch	2	0.266312
    232	11.61	3.39	No	Sat	Dinner	2	0.291990
Yes	109	14.31	4.00	Yes	Sat	Dinner	2	0.279525
    183	23.17	6.50	Yes	Sun	Dinner	4	0.280535
    67	3.07	1.00	Yes	Sat	Dinner	1	0.325733
    178	9.60	4.00	Yes	Sun	Dinner	2	0.416667
    172	7.25	5.15	Yes	Sun	Dinner	2	0.710345
```

```python
# 传给apply的函数能够接收其他参数或关键字，则可以将这些内容放在函数名后面传入
tips.groupby(['smoker', 'day']).apply(top, n=1, column='total_bill') 
>>>
total_bill	tip	smoker	day	time	size	tip_pct
smoker	day								
No	Fri	94	22.75	3.25	No	Fri	Dinner	2	0.142857
Sat	212	48.33	9.00	No	Sat	Dinner	4	0.186220
Sun	156	48.17	5.00	No	Sun	Dinner	6	0.103799
Thur	142	41.19	5.00	No	Thur	Lunch	5	0.121389
Yes	Fri	95	40.17	4.73	Yes	Fri	Dinner	4	0.117750
Sat	170	50.81	10.00	Yes	Sat	Dinner	3	0.196812
Sun	182	45.35	3.50	Yes	Sun	Dinner	3	0.077178
Thur	197	43.11	5.00	Yes	Thur	Lunch	4	0.115982
```

#### 禁止分组键

分组键会跟原始对象的索引共同构成结果对象中的层次化索引，将group_keys=False 传入groupby即可禁止

```python
# 禁止分组键
tips.groupby('smoker').apply(top)
>>>
total_bill	tip	smoker	day	time	size	tip_pct
smoker								
 No	88	24.71	5.85	No	Thur	Lunch	2	0.236746
    185	20.69	5.00	No	Sun	Dinner	5	0.241663
    51	10.29	2.60	No	Sun	Dinner	2	0.252672
    149	7.51	2.00	No	Thur	Lunch	2	0.266312
    232	11.61	3.39	No	Sat	Dinner	2	0.291990
Yes	109	14.31	4.00	Yes	Sat	Dinner	2	0.279525
    183	23.17	6.50	Yes	Sun	Dinner	4	0.280535
    67	3.07	1.00	Yes	Sat	Dinner	1	0.325733
    178	9.60	4.00	Yes	Sun	Dinner	2	0.416667
    172	7.25	5.15	Yes	Sun	Dinner	2	0.710345
    
tips.groupby('smoker',group_keys=False).apply(top)
>>>
	total_bill	tip	smoker	day	time	size	tip_pct
88	24.71	5.85	No	Thur	Lunch	2	0.236746
185	20.69	5.00	No	Sun	Dinner	5	0.241663
51	10.29	2.60	No	Sun	Dinner	2	0.252672
149	7.51	2.00	No	Thur	Lunch	2	0.266312
232	11.61	3.39	No	Sat	Dinner	2	0.291990
109	14.31	4.00	Yes	Sat	Dinner	2	0.279525
183	23.17	6.50	Yes	Sun	Dinner	4	0.280535
67	3.07	1.00	Yes	Sat	Dinner	1	0.325733
178	9.60	4.00	Yes	Sun	Dinner	2	0.416667
172	7.25	5.15	Yes	Sun	Dinner	2	0.710345
```

#### 分位数和桶分析

pandas有一些能根据指定面元或样本分位数将数据拆分成多块的工具（比如cut或qcut）

```python
frame = pd.DataFrame({'data1':np.random.randn(1000),
                     'data2':np.random.randn(1000)})
quartiles = pd.cut(frame.data1,4)
quartiles[:10]
# cut返回的Factor对象可以直接用于groupby
>>>
0    (-1.275, 0.3]
1    (-1.275, 0.3]
2     (0.3, 1.875]
3    (-1.275, 0.3]
4     (0.3, 1.875]
5    (-1.275, 0.3]
6    (-1.275, 0.3]
7    (-1.275, 0.3]
8     (0.3, 1.875]
9     (0.3, 1.875]
Name: data1, dtype: category
Categories (4, interval[float64]): [(-2.857, -1.275] < (-1.275, 0.3] < (0.3, 1.875] < (1.875, 3.449]]
  
def get_stats(group):
    return {'min':group.min(),'max':group.max(),
           'count':group.count(),'mean':group.mean()}
grouped = frame.data2.groupby(quartiles)                                                                                                                                   grouped.apply(get_stats).unstack()
>>>                                                                                    count	max	mean	min
data1				
(-2.857, -1.275]	102.0	2.834342	-0.065788	-2.523687
(-1.275, 0.3]	537.0	3.065880	0.052920	-2.949736
(0.3, 1.875]	337.0	2.488922	0.109874	-2.402608
(1.875, 3.449]	24.0	2.009093	-0.209980	-2.739957
```

长度相等的桶：区间大小相等

大小相等的桶：数据点数量相等

- 对不同的分组填充不同的值

  ```python
  states = ['Ohio', 'New York', 'Vermont', 'Florida','Oregon', 'Nevada', 'California', 'Idaho']
  group_key = ['East'] * 4 + ['West'] * 4
  group_key
  >>>
  ['East', 'East', 'East', 'East', 'West', 'West', 'West', 'West']
  
  data=pd.Series(np.random.randn(8), index=states)
  data[['Vermont', 'Nevada', 'Idaho']] = np.nan
  data
  >>>
  Ohio          0.592806
  New York     -0.115530
  Vermont            NaN
  Florida       1.495049
  Oregon       -0.225957
  Nevada             NaN
  California    0.923421
  Idaho              NaN
  dtype: float64
  >>>
  fill_mean = lambda x:x.fillna(x.mean())
  data.groupby(group_key).apply(fill_mean)
  >>>
  Ohio          0.592806
  New York     -0.115530
  Vermont       0.657442
  Florida       1.495049
  Oregon       -0.225957
  Nevada        0.348732
  California    0.923421
  Idaho         0.348732
  dtype: float64
  ```

  #### 随机采样和排列

  抽取的方式有很多，其中一些的效率会比其他的高很多，一个办法是选取np.random.peimutation(N)的前k个元素，其中N为完整数据的大小，k为期望的样本大小

  ```python
  # 
  ```

  pg285

  #### 分组加权平均数和相关系数

  

  #### 面向分组的线性回归

  

  

  



### 透视表和交叉表

透视表（povit table）是各种电子表格程序和其他数据分析软件中一种常见的数据汇总工具，根据一个或多个键对数据进行聚合，并根据行和列上的分组键将数据分配到各个矩形区域中

可以通过groupby功能以及重塑运算制作透视表

Dataframe有一个povit_table的方法，此外还有一个顶级的pandas.povit_table函数

``pivot_table`(*self*, *values=None*, *index=None*, *columns=None*, *aggfunc='mean'*, *fill_value=None*, *margins=False*, *dropna=True*, *margins_name='All'*, *observed=False*)`

| pivot_table  | 说明                                            |                                                              |
| ------------ | ----------------------------------------------- | ------------------------------------------------------------ |
| data         | DataFrame                                       |                                                              |
| values       | column to aggregate, optional                   | 聚合的列                                                     |
| index        | column, Grouper, array, or list of the previous | 如果使Array，则长度需要与data相同；<br/>list内可以包含除list之外的其他各种类型；
在透视表索引上分组的键，如果传入的是array，用法与列值一样 |
| columns      |                                                 | 如果传入array，长度需与data相同                              |
| aggfunc      |                                                 | 如果是list of functions，得到的透视表具有分层的列，他们的最高级别是函数名称；<br/>如果是dict，key是需要聚合的列，value是函数或函数列 |
| fill_value   |                                                 | 填充缺失值                                                   |
| margins      |                                                 | 添加所有row/columns                                          |
| dropna       |                                                 | 不包括全是NaN的列                                            |
| margins_name |                                                 | 当margins是True，包含总数的行/列名字                         |
| observed     |                                                 |                                                              |



[案例](<https://www.cnblogs.com/onemorepoint/p/8425300.html>)

#### 交叉表：crosstab

交叉表是一种用于计算分组频率的透视表

![038](D:\project\pycon\DA\img\038.jpg)



### 示例：2012联邦选举委员会数据库







































## 第十章 时间序列

很多时间序列是固定频率的，时间序列也可以不固定频率

时间序列数据的意义取决于具体的应用场景

- 时间戳，特定的时刻
- 固定时期
- 时间间隔（由起使和结束时间表示），时期是时间间隔的特例
- 实验或过程时间

pandas提供了一组标准的时间序列处理工具和数据 算法，可以高效处理非常大的时间序列，轻松切片，聚合，采样

### 日期和时间数据类型及工具

我们会用到datetime，time，calendar模块，datetime.datetime是用的最多的数据类型



### 时间序列基础

### 日期的范围、频率以及移动

### 时区处理

### 时期及其算术运算

### 重采样及频率转换

### 时间序列绘图

### 移动窗口函数

### 性能和内存使用方面的注意事项



## 第十一章 金融和经济数据应用

### 数据规整化方面的问题

### 分组变换和分析

### 更多示例应用



## 第十二章 Numpy高级应用

### ndarray对象的内部机制

### 高级数组操作

### 广播

### ufunc高级应用

### 结构化和记录式数组

### 排序话题

### numpy的matrix类

### 高级数组输入输出

### 性能建议

 