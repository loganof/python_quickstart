"""
definition:
    将对象组合成树型结构来表示部分-整体的层次结构。
terms:
    1. 组件(Component): 这是一个接口或者抽象类，定义了树中所有对象的公共接口。可以是叶子组件或复合组件。
    2. 叶子(Leaf): 表示树结构中的叶节点，没有子节点，实现组件接口。
    3. 复合(Composite): 表示有子节点的组件，实现组件接口，并且持有子节点的集合。
steps:
    1. 定义组件接口:声明公共接口，包含所有操作声明(如添加、移除、和访问子节点的方法)。
    2. 创建叶子类: 实现组件接口，表示树的叶节点。
    3. 创建复合类: 实现组件接口，表示有子节点的组件，并实现管理子节点的方法。
"""