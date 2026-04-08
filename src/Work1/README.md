# CG-Lab: Taichi Gravity Swarm

## 项目简介

这是一个基于 Taichi 库实现的 GPU 加速粒子物理模拟项目，主要功能是模拟鼠标引力对大量粒子的影响，形成类似 swarm（蜂群）的动态效果。通过 Taichi 的并行计算能力，即使处理上万粒子也能保持流畅运行。

## 项目结构

```
CG-Lab/
├── src/
│   └── Work0/
│       ├── __init__.py       # 模块初始化文件
│       ├── config.py         # 配置参数文件
│       ├── main.py           # 主程序入口
│       └── physics.py        # 物理模拟核心
├── test.py                   # 测试脚本
└── README.md                 # 项目说明文档
```

## 安装步骤

1. **安装 Python 环境**：确保安装了 Python 3.10+ 版本
2. **安装依赖**：使用 uv 或 pip 安装 Taichi 库
   ```bash
   # 使用 uv
   uv add taichi

   # 或使用 pip
   pip install taichi
   ```

## 运行方法

在项目根目录下执行以下命令：

```bash
uv run -m src.Work0.main
```

或直接运行 main.py 文件：

```bash
python src\Work0\main.py
```

## 代码逻辑说明

### 1. 配置模块 (config.py)

定义了物理系统和渲染系统的参数：

- **物理参数**：粒子数量、引力强度、空气阻力、边界反弹系数
- **渲染参数**：窗口分辨率、粒子半径、粒子颜色

### 2. 物理模拟核心 (physics.py)

- **数据结构**：使用 Taichi 的 `ti.Vector.field` 在显存中存储粒子位置和速度
- **初始化函数**：`init_particles()` 随机初始化所有粒子的位置
- **物理更新函数**：`update_particles()` 由 GPU 并行执行，处理：
  - 计算鼠标对粒子的引力
  - 应用空气阻力
  - 更新粒子位置
  - 处理边界碰撞

### 3. 主程序 (main.py)

- **初始化**：导入模块并初始化 Taichi
- **主循环**：
  - 编译 GPU 内核
  - 创建 GUI 窗口
  - 持续获取鼠标位置
  - 调用物理更新函数
  - 绘制粒子并显示

## 实现功能

1. **鼠标引力效果**：粒子会被鼠标位置吸引，距离越近引力越大
2. **边界碰撞**：粒子碰到窗口边界会反弹
3. **空气阻力**：粒子运动速度会逐渐衰减
4. **GPU 加速**：利用 Taichi 的并行计算能力，实现高效的粒子模拟
5. **实时交互**：鼠标移动时，粒子群会实时响应

## 注意事项

- **窗口显示**：运行程序后会弹出 GUI 窗口，如果没有看到窗口，请检查是否被其他窗口遮挡
- **性能调整**：如果运行卡顿，可以在 `config.py` 中减小 `NUM_PARTICLES` 的值（例如从 10000 改为 2000）
- **GPU 兼容性**：如果 GPU 初始化失败，可以尝试将 `main.py` 中的 `ti.init(arch=ti.gpu)` 改为 `ti.init(arch=ti.cpu)`

## 技术栈

- **Python 3.10+**：基础编程语言
- **Taichi**：GPU 并行计算库，用于加速物理模拟
- **Taichi GUI**：用于粒子渲染和用户交互

## 运行效果

!\[粒子群交互演示]

[演示.gif (480×270)](https://gitee.com/xihua-chuliu-nai/cg-lab/raw/master/src/Work0/%E6%BC%94%E7%A4%BA.gif)
