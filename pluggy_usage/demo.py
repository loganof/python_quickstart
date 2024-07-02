import pluggy

# 定义钩子规范
hookspec = pluggy.HookspecMarker("example")  

# The `HookSpec` class is defined in the Python code snippet.
class HookSpec:
    @hookspec
    def myhook(self, arg1, arg2):
        """a hook that takes two arguments."""
    
    
# 定义钩子实现
hookimpl = pluggy.HookimplMarker("example") 
class plugin:
    @hookimpl
    def myhook(self, arg1, arg2):
        print(f"Hook called with: {arg1}, {arg2}")
        return arg1 + arg2
    
    
# 创建PluginManager 并注册钩子规范
pm  = pluggy.PluginManager("example")
pm.add_hookspecs(HookSpec) 

plugin = plugin()
pm.register(plugin)

# 调用钩子
results = pm.hook.myhook(arg1=1, arg2=2)
print(f"Hook results: {results}")