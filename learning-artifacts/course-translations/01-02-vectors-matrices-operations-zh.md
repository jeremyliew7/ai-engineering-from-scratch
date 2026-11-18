---
source_path: phases/01-math-foundations/02-vectors-matrices-operations/docs/en.md
source_commit: e6014b07fd44bc36f2a8e21ca9f64ce9d9309cf9
---

# 向量、矩阵与运算

> 每个神经网络都不过是矩阵乘法，再加上一些步骤。

**类型：** 构建
**语言：** Python、Julia
**先修课程：** 阶段 1，第 01 课（线性代数直觉）
**时间：** 约 60 分钟

## 学习目标

- 构建一个 Matrix 类，支持逐元素运算、矩阵乘法、转置、行列式和求逆。
- 区分逐元素乘法与矩阵乘法，并解释各自适用的场景。
- 仅使用从零实现的 Matrix 类，实现一个全连接神经网络层：`relu(W @ x + b)`。
- 解释广播规则，以及神经网络框架如何进行偏置相加。

## 问题

你想构建一个神经网络。阅读代码时，你看到了这一行：

```text
output = activation(weights @ input + bias)
```

这里的 `@` 是矩阵乘法。`weights` 是一个矩阵，`input` 是一个向量。如果你不知道这些运算在做什么，这行代码就像魔法。如果你知道，它就是用三个运算完成一层的整个前向传播。

模型处理的每张图像都是由像素值组成的矩阵。每个词嵌入都是一个向量。每个神经网络的每一层都是一次矩阵变换。要构建 AI 系统，你必须熟练掌握矩阵运算，就像写代码必须理解变量一样。

本课从零培养这种熟练程度。

> 校注：以上是原文的概括性表述。彩色图像通常表示为含通道维的张量；神经网络也包含激活、归一化等运算，不能把每一层都严格等同于矩阵线性变换。

## 核心概念

### 向量：有序的数字列表

向量是一组具有方向和大小的数字。在 AI 中，向量表示数据点、特征或参数。

```text
v = [3, 4]        -- a 2D vector
w = [1, 0, -2]    -- a 3D vector
```

二维向量 `[3, 4]` 指向平面上的坐标 (3, 4)。它的长度（模）是 5，对应 3-4-5 直角三角形。

### 矩阵：数字网格

矩阵是一个由行和列组成的二维网格。一个 $m \times n$ 矩阵有 $m$ 行、$n$ 列。

```math
A = \begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{bmatrix} \quad \text{2x3 matrix (2 rows, 3 columns)}
```

上述矩阵为 2×3，即两行三列。在神经网络中，权重矩阵把输入向量变换成输出向量。具有 784 个输入、128 个输出的一层使用一个 128×784 的权重矩阵。

### 为什么形状很重要

矩阵乘法有一条严格的规则：`(m x n) @ (n x p) = (m x p)`。中间两个维度必须相同。

```text
(128 x 784) @ (784 x 1) = (128 x 1)
  weights       input       output

Inner dimensions: 784 = 784  -- valid
```

这里 weights、input、output 分别表示权重、输入、输出。中间维度都是 784，因此乘法有效。

如果你在 PyTorch 中遇到形状不匹配错误，这就是原因。

> 校注：这里针对矩阵乘法的形状错误；PyTorch 的形状错误也可能来自广播、拼接等其他操作。

### 运算概览

| 运算 | 做什么 | 神经网络中的用途 |
|---|---|---|
| 加法 | 对对应元素相加 | 给输出加偏置 |
| 标量乘法 | 缩放每个元素 | 学习率乘以梯度 |
| 矩阵乘法 | 变换向量 | 一层的前向传播 |
| 转置 | 交换行与列 | 反向传播 |
| 行列式 | 用一个数概括矩阵 | 检查可逆性 |
| 逆矩阵 | 撤销一次变换 | 求解线性方程组 |
| 单位矩阵 | 不改变输入的矩阵 | 初始化、残差连接 |

### 逐元素乘法与矩阵乘法

这个区别经常让初学者困惑。

逐元素乘法：将对应位置的元素相乘。两个矩阵必须具有相同形状。

```math
\begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix} * \begin{bmatrix} 5 & 6 \\ 7 & 8 \end{bmatrix} = \begin{bmatrix} 5 & 12 \\ 21 & 32 \end{bmatrix}
```

矩阵乘法：对行与列做点积。中间维度必须匹配。

```math
\begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix} @ \begin{bmatrix} 5 & 6 \\ 7 & 8 \end{bmatrix} = \begin{bmatrix} 1 \cdot 5 + 2 \cdot 7 & 1 \cdot 6 + 2 \cdot 8 \\ 3 \cdot 5 + 4 \cdot 7 & 3 \cdot 6 + 4 \cdot 8 \end{bmatrix} = \begin{bmatrix} 19 & 22 \\ 43 & 50 \end{bmatrix}
```

不同的运算，有不同的结果，也遵循不同的规则。

> 校注：上述逐元素乘法先讨论相同形状的情况；支持广播的库也允许形状不同但可广播的数组做逐元素乘法。

### 广播

把偏置向量加到输出矩阵上时，两者的形状并不一致。广播会把较小的数组扩展到适合运算的形状。

```text
| 1  2  3 |   +   [10, 20, 30]
| 4  5  6 |

Broadcasting stretches the vector across rows:

| 1  2  3 |   | 10  20  30 |   | 11  22  33 |
| 4  5  6 | + | 10  20  30 | = | 14  25  36 |
```

上图表示：把向量沿着各行扩展，再与矩阵相加。现代框架都会自动完成这项操作。理解广播，可以避免“形状看起来不对，代码却能运行”带来的困惑。

> 校注：广播并不是任意调整形状。从最后一个维度向前比较，对应维度必须相等，或者其中一个为 1；缺失维度按 1 处理。“扩展”是概念描述，通常不需要实际复制数据。

```figure
vector-projection
```

上面是课程注册的“向量投影”交互图标识。

## 从零构建

### 第 1 步：Vector 类

```python
class Vector:
    def __init__(self, data):
        self.data = list(data)
        self.size = len(self.data)

    def __repr__(self):
        return f"Vector({self.data})"

    def __add__(self, other):
        return Vector([a + b for a, b in zip(self.data, other.data)])

    def __sub__(self, other):
        return Vector([a - b for a, b in zip(self.data, other.data)])

    def __mul__(self, scalar):
        return Vector([x * scalar for x in self.data])

    def dot(self, other):
        return sum(a * b for a, b in zip(self.data, other.data))

    def magnitude(self):
        return sum(x ** 2 for x in self.data) ** 0.5
```

代码说明：构造函数保存向量数据和长度；`__repr__` 控制显示；加减法逐元素执行；`__mul__` 实现标量乘法；`dot` 计算点积；`magnitude` 计算欧几里得长度。

> 校注：这段原始示例没有检查向量长度。`zip` 遇到不同长度会按较短者截断，因此不能把不报错当作维度正确。

### 第 2 步：实现核心运算的 Matrix 类

```python
class Matrix:
    def __init__(self, data):
        self.data = [list(row) for row in data]
        self.rows = len(self.data)
        self.cols = len(self.data[0])
        self.shape = (self.rows, self.cols)

    def __repr__(self):
        rows_str = "\n  ".join(str(row) for row in self.data)
        return f"Matrix({self.shape}):\n  {rows_str}"

    def __add__(self, other):
        return Matrix([
            [self.data[i][j] + other.data[i][j] for j in range(self.cols)]
            for i in range(self.rows)
        ])

    def __sub__(self, other):
        return Matrix([
            [self.data[i][j] - other.data[i][j] for j in range(self.cols)]
            for i in range(self.rows)
        ])

    def scalar_multiply(self, scalar):
        return Matrix([
            [self.data[i][j] * scalar for j in range(self.cols)]
            for i in range(self.rows)
        ])

    def element_wise_multiply(self, other):
        return Matrix([
            [self.data[i][j] * other.data[i][j] for j in range(self.cols)]
            for i in range(self.rows)
        ])

    def matmul(self, other):
        return Matrix([
            [
                sum(self.data[i][k] * other.data[k][j] for k in range(self.cols))
                for j in range(other.cols)
            ]
            for i in range(self.rows)
        ])

    def transpose(self):
        return Matrix([
            [self.data[j][i] for j in range(self.rows)]
            for i in range(self.cols)
        ])

    def determinant(self):
        if self.shape == (1, 1):
            return self.data[0][0]
        if self.shape == (2, 2):
            return self.data[0][0] * self.data[1][1] - self.data[0][1] * self.data[1][0]
        det = 0
        for j in range(self.cols):
            minor = Matrix([
                [self.data[i][k] for k in range(self.cols) if k != j]
                for i in range(1, self.rows)
            ])
            det += ((-1) ** j) * self.data[0][j] * minor.determinant()
        return det

    def inverse_2x2(self):
        det = self.determinant()
        if det == 0:
            raise ValueError("Matrix is singular, no inverse exists")
        return Matrix([
            [self.data[1][1] / det, -self.data[0][1] / det],
            [-self.data[1][0] / det, self.data[0][0] / det]
        ])

    @staticmethod
    def identity(n):
        return Matrix([
            [1 if i == j else 0 for j in range(n)]
            for i in range(n)
        ])
```

代码说明：`rows`、`cols` 和 `shape` 记录形状。加减法、标量乘法和逐元素乘法逐项生成结果；`matmul` 按“左矩阵第 i 行与右矩阵第 j 列做点积”计算元素；转置交换行列。行列式通过第一行展开递归计算；`inverse_2x2` 用二阶矩阵公式求逆；`identity` 生成单位矩阵。

> 校注：原始示例没有校验空矩阵、行长度一致性、相加形状、乘法内维度或方阵条件。行列式只对方阵定义，`inverse_2x2` 只适用于 2×2 矩阵。递归展开不适合大矩阵；浮点数计算中仅用 `det == 0` 也不能判断数值稳定性。这里没有定义 `__matmul__`，所以这个 Matrix 类应调用 `A.matmul(B)`，不能直接写 `A @ B`。

### 第 3 步：观察运行结果

```python
A = Matrix([[1, 2], [3, 4]])
B = Matrix([[5, 6], [7, 8]])

print("A + B =", (A + B).data)
print("A @ B =", A.matmul(B).data)
print("A^T =", A.transpose().data)
print("det(A) =", A.determinant())
print("A^-1 =", A.inverse_2x2().data)

I = Matrix.identity(2)
print("A @ A^-1 =", A.matmul(A.inverse_2x2()).data)
```

代码说明：依次展示相加、矩阵乘法、转置、行列式和逆矩阵，最后用矩阵乘以其逆矩阵，检查是否得到单位矩阵。

### 第 4 步：连接到神经网络

```python
import random

inputs = Matrix([[0.5], [0.8], [0.2]])
weights = Matrix([
    [random.uniform(-1, 1) for _ in range(3)]
    for _ in range(2)
])
bias = Matrix([[0.1], [0.1]])

def relu_matrix(m):
    return Matrix([[max(0, val) for val in row] for row in m.data])

pre_activation = weights.matmul(inputs) + bias
output = relu_matrix(pre_activation)

print(f"Input shape: {inputs.shape}")
print(f"Weight shape: {weights.shape}")
print(f"Output shape: {output.shape}")
print(f"Output: {output.data}")
```

代码说明：输入是 3×1 列向量，权重为 2×3，偏置为 2×1。先计算加权和并加偏置，再由 ReLU 将负值变为零。权重随机生成，因此每次运行的输出数值可能不同。

这就是一个全连接层：`output = relu(W @ x + b)`。原文指出，每个神经网络中的每个全连接层都执行这一过程。

> 校注：全连接层的核心是仿射运算 `W @ x + b`；激活函数可以是 ReLU、其他函数，或不使用激活。不能说所有全连接层都使用 ReLU。

## 使用生产库

NumPy 用更少的代码完成上述全部操作，而且速度快多个数量级。

```python
import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print("A + B =\n", A + B)
print("A * B (element-wise) =\n", A * B)
print("A @ B (matrix multiply) =\n", A @ B)
print("A^T =\n", A.T)
print("det(A) =", np.linalg.det(A))
print("A^-1 =\n", np.linalg.inv(A))
print("I =\n", np.eye(2))

inputs = np.random.randn(3, 1)
weights = np.random.randn(2, 3)
bias = np.array([[0.1], [0.1]])
output = np.maximum(0, weights @ inputs + bias)

print(f"\nNeural network layer: {weights.shape} @ {inputs.shape} = {output.shape}")
print(f"Output:\n{output}")
```

代码说明：NumPy 数组的 `*` 是逐元素乘法，`@` 是矩阵乘法；`.T` 为转置；`np.linalg.det` 和 `np.linalg.inv` 分别计算行列式和逆矩阵；`np.eye` 生成单位矩阵；`np.maximum(0, ...)` 实现 ReLU。

Python 的 `@` 运算符调用 `__matmul__`。NumPy 使用由 C 和 Fortran 编写的优化 BLAS 例程实现它。同样的数学，速度快 100 倍。

> 校注：“多个数量级”和“100 倍”是原文的性能说法，不是本课环境中的实测结果。实际速度取决于矩阵大小、数据类型、BLAS 实现、线程及硬件，不能视为固定倍数。NumPy 是否使用特定优化路径也取决于构建和运算条件。

NumPy 中的广播：

```python
matrix = np.array([[1, 2, 3], [4, 5, 6]])
bias = np.array([10, 20, 30])
print(matrix + bias)
```

代码说明：形状为 `(3,)` 的偏置向量沿两行广播，与形状为 `(2, 3)` 的矩阵相加。

NumPy 会自动把一维偏置广播到两行。这就是各神经网络框架进行偏置相加的方式。

## 交付产物

本课产出一份通过几何直觉教授矩阵运算的提示词，见 `outputs/prompt-matrix-operations.md`。

这里构建的 Matrix 类，是我们将在阶段 3 第 10 课构建的迷你神经网络框架的基础。

## 练习

1. **验证逆矩阵。** 计算 `A @ A.inverse_2x2()`，确认得到单位矩阵。用三个不同的 2×2 矩阵尝试。行列式为零时会怎样？
2. **实现 3×3 逆矩阵。** 扩展 Matrix 类，使用伴随矩阵法计算 3×3 矩阵的逆。将结果与 NumPy 的 `np.linalg.inv` 对照测试。
3. **构建两层网络。** 只使用你的 Matrix 类，不用 NumPy，创建一个输入 3 维、隐藏层 4 维、输出 2 维的两层神经网络。随机初始化权重，运行一次前向传播，并验证所有形状都正确。

### 提示

**练习 1。** 对三个矩阵计算 `A @ A.inverse_2x2()`，逐元素与单位矩阵比较，误差应在 `1e-9` 以内。对于行列式为 0 的矩阵，例如 `[[1, 2], [2, 4]]`，`inverse_2x2` 会抛出 `ValueError`，这是预期结果。

**练习 2。** 计算 3×3 的代数余子式矩阵，将其转置得到伴随矩阵，再将每个元素除以 `determinant()`。检查 `A @ A_inv` 是否得到单位矩阵，并确认每个元素与 `np.linalg.inv(A)` 的差在 `1e-9` 以内。

**练习 3。** 乘法之前写出各矩阵的形状：`W1` 为 4×3，`W2` 为 2×4，如 `demo_neural_network_layer` 所示。3×1 的输入必须得到 4×1 的隐藏向量和 2×1 的输出。

> 校注：练习和提示中的 `@` 是原文写法。使用本文给出的 Matrix 类时，应改用 `.matmul(...)`，或先自行实现 `__matmul__`。逆矩阵验证要选择可逆且数值条件合适的矩阵，固定的 `1e-9` 不是对所有浮点输入的保证。

## 关键术语

| 术语 | 人们怎么说 | 实际含义 |
|---|---|---|
| 向量 | “一支箭头” | 有序数字列表。在 AI 中，是高维空间中的一个点。 |
| 矩阵 | “一张数字表” | 一种线性变换，把向量从一个空间映射到另一个空间。 |
| 矩阵乘法 | “把数字乘起来就行” | 第一个矩阵的每一行与第二个矩阵的每一列之间的点积。顺序很重要。 |
| 转置 | “翻一下” | 交换行与列，把 $m \times n$ 矩阵变为 $n \times m$。在反向传播中很重要。 |
| 行列式 | “从矩阵得到的某个数” | 衡量矩阵对面积（二维）或体积（三维）的缩放。零意味着变换压扁了一个维度。 |
| 逆矩阵 | “撤销矩阵” | 逆转该变换的矩阵。只有行列式不为零时才存在。 |
| 单位矩阵 | “无聊的矩阵” | 矩阵中相当于乘以 1 的操作。用于残差连接（ResNet）。 |
| 广播 | “神奇的形状修复” | 沿缺失维度重复，把较小数组扩展为与较大数组匹配的形状。 |
| 逐元素 | “普通乘法” | 对应位置相乘。两个数组必须形状相同，或能够广播。 |

> 校注：行列式的绝对值表示面积或体积缩放，符号表示定向是否翻转。这里“逆矩阵”指方阵的普通逆；非方阵的广义逆是另一概念。残差连接的恒等分支通常直接传递输入，不必显式构造单位矩阵。广播的准确条件见前面的校注。

## 延伸阅读

- [3Blue1Brown：线性代数的本质](https://www.3blue1brown.com/topics/linear-algebra)：本课各项运算的视觉直觉。
- [NumPy 广播文档](https://numpy.org/doc/stable/user/basics.broadcasting.html)：NumPy 遵循的精确规则。
- [斯坦福 CS229 线性代数回顾](http://cs229.stanford.edu/section/cs229-linalg.pdf)：面向机器学习的简明线性代数参考。
