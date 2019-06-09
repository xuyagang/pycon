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
- randint   从给定的范围内随机选区整数
- randn   产生正态分布(平均值0，标准差为1)的样本
- binomial   产生二项分布的样本值
- beta   产生beta分布的样本值
- chisquare 产生卡方分布的样本值
- gamma   产生gamma分布的样本值
- uniform   产生在[0,1]中均匀分布的样本值

pg123













