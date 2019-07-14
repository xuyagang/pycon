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
- inv   计算方针的逆
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
        # 索引行
        data[:2]
        # 索引列
        data[['three','one']]
        # 布尔型
        data[data['three']<5]
        data[data['three']<5] = 0
        ```

      - 为了在DataFrame的==行==上进行标签索引，引入字段  ix 

        ```
        
        ```

        

        

      

    









