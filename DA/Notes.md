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

pg88