from typing import Dict, Any

class ToDictMixin:
    def to_dict(self) -> Dict[Any, Any]:
        return self._traverse_dict(self.__dict__)
    
    def _traverse_dict(self, instance_dict: Dict[Any, Any]) -> Dict[Any, Any]:
        output = {}
        for key, value in instance_dict.items():
            output[key] = self._traverse(key, value)
        return output
    
    def _traverse(self, key: Any, value: Any) -> Any:
        # dynamic type inspection
        if isinstance(value, ToDictMixin):
            return value.to_dict()
        elif isinstance(value, dict):
            return self._traverse_dict(value)
        elif isinstance(value, list):
            return [self._traverse(key, i) for i in value]
        elif hasattr(value, '__dict__'):
            return self._traverse_dict(value.__dict__)
        else:
            return value
        
        
class BinaryTree(ToDictMixin):
    def __init__(self, value, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right
        
tree = BinaryTree(10, left=BinaryTree(7, right=BinaryTree(9)), right=BinaryTree(13, left=BinaryTree(11)))
print(tree.to_dict())


class BinaryTreeWithParent(BinaryTree):
    def __init__(self, value, left=None, right=None, parent=None) -> None:
        super().__init__(value, left, right)
        self.parent = parent
        
    def _traverse(self, key: Any, value: Any) -> Any:
        if(isinstance(value, BinaryTreeWithParent) and key == 'parent'):
            return value.value # prevent cycles
        else:
            return super()._traverse(key, value)
        
        
root = BinaryTreeWithParent(10)
root.left = BinaryTreeWithParent(7, parent=root)
root.left.right = BinaryTreeWithParent(9, parent=root.left)
print(root.to_dict())