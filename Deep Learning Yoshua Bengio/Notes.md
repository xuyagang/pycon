## 2.1 标量，向量，矩阵，张量
- 标量:scalar_一个单独的数
    - 斜体小写表示
- 向量:vector_一列数
    - 有顺序，可索引，带负号表示补集索引
    - 粗体小写表示
    - **s**<sub>i</sub> : i可为数字
    - 集合**s** <sub>-i</sub> 表示除i外的

- 矩阵:matrix_二维数组，元素被两个索引确定
    - 粗体大写斜体表示
    - f(A)i,j 表示函数f 作用在 A 上输出的矩阵的第 i 行第 j 列元素
    - : 表示行的所有元素
- 张量_tensor:某些情况下我们会讨论坐标超过两维的数组，一个数组中的元素分布在若干维的规则网格中，将其称为张量
    - 粗体大写表示
    - A<sub>ijk</sub>用来取对应位置的值
    - 转置_transpose:把矩阵以对角线为轴的镜像
        - 左上到右下为主对角线_main diagonal
        - A的转置是A<sup>T</sup>
        - (A<sup>T</sup>)<sub>ji</sub>=A<sub>ij</sub>
        - 向量可当做只有一行矩阵，转置可变为列向量
        - 标量是单个元素的矩阵，==转置是本身==
            - a<sup>T</sup>=a
    - 两个矩阵形状一样，可以进行相加(对应位置元素相加)
        - 向量加矩阵会广播
## 2.2 矩阵向量相乘
- 矩阵A和矩阵B相乘，矩阵A的列数必须和矩阵B的==行数相等==
  - ___A___的形状是m*n,___B___的形状是n\*p，结果___C___等于m\*p

- 两个矩阵的标准积不是对应元素的乘积

- 连个矩阵对应元素的乘积是__元素对应乘积__（Hadamard product）

  ![001](D:\project\pycon\Deep Learning Yoshua Bengio\img\001.JPG)

- 两个维数相同的向量__x__和__y__的点积（dot product）可看作是矩阵__x__<sup>T</sup>__y__

  - 两个向量a = [a1, a2,…, an]和b = [b1, b2,…, bn]的点积定义为：

    __a·b=a1b1+a2b2+……+anbn__

- 矩阵乘积服从分配律、集合律

  - 矩阵加法就是相同位置的数字加一下,矩阵减法也类似

  - 矩阵乘以一个常数，就是所有位置都乘以这个数

  - 矩阵乘法

    - [参考](https://nolaymanleftbehind.wordpress.com/2011/07/10/linear-algebra-what-matrices-actually-are/)，[参考](https://www.cnblogs.com/alantu2018/p/8528299.html)
    - 结果矩阵第m行与第n列交叉位置的那个值，等于第一个矩阵第m行与第二个矩阵第n列，对应位置的每个值的乘积之和

    ![002](D:\project\pycon\Deep Learning Yoshua Bengio\img\002.jpg)

    - **矩阵的本质就是线性方程式，两者是一一对应关系**

      - 线性方程式

        ![003](D:\project\pycon\Deep Learning Yoshua Bengio\img\003.jpg)

      - 矩阵的最初目的，只是为线性方程组提供一个简写形式

        ![004](D:\project\pycon\Deep Learning Yoshua Bengio\img\004.jpg)

    - 内积与外积

      - 一个行向量乘以一个列向量称作向量的内积，又叫作点积，结果是一个数；
      - 一个列向量乘以一个行向量称作向量的外积，外积是一种特殊的[克罗内克积](http://zh.wikipedia.org/wiki/%E5%85%8B%E7%BD%97%E5%86%85%E5%85%8B%E7%A7%AF)，结果是一个矩阵

  - 矩阵乘积不满足交换律（___AB___=___BA___并非总是满足）

    - 两个向量的点积（dot product)满足交换律

      > x<sup>T</sup>y = y<sup>T</sup>x

  - 矩阵乘积的转置

    > (___AB___)<sup>T</sup> = ___B___<sup>T</sup>___A___<sup>T</sup>

  - 向量乘积是标量，标量转置是自身

## 2.3 单位矩阵和逆矩阵



















