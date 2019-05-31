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





















