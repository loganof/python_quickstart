文件夹中有与没有 __init__.py的区别
1. 有 __init__.py
   1. 该目录会被python解释器识别为一个包。导入包时
      1. import mypackage.module1
   2. 初始化包
      1. 在导入包时, __init__.py中的代码会自动执行
   3. 控制导入行为
      1. 定义__all__可以控制from package import * 导入的内容
2. 没有 __init__.py
   1. python3.3及以后，目录依然可以被视为一个包。这种情况称为”隐式命名空间包".
3. 建议
   1. 对于不需要初始化的简单命名空间，在python3.3以后的版本中可以省略 __init__.py文件。