import pluggy

# 定义钩子规范
hookspec = pluggy.HookspecMarker("example")
class HookSpec:
    @hookspec
    def process_data(self, data):
        """Processes the data"""
        
        
# 定义钩子实现
hookimpl = pluggy.HookimplMarker("example")

class PluginOne:
    @hookimpl
    def  process_data(self, data):
        return f"PluginOne processed: {data}"

class PluginTwo:
    @hookimpl
    def process_data(self, data):
        return f"PluginTwo processed: {data}"
    
    
# 创建插件管理器
pm = pluggy.PluginManager("example")   
# 注册钩子规范 
pm.add_hookspecs(HookSpec)

# 动态注册插件
plugin_one = PluginOne()
pm.register(plugin_one)
plugin_two = PluginTwo()
pm.register(plugin_two)    

# 调用钩子
data = "some data"   
results = pm.hook.process_data(data=data)       
for result in results:
    print(result)    
    
# 注销插件
pm.unregister(plugin_one)

# 调用钩子
data = "some data"   
results = pm.hook.process_data(data=data)       
for result in results:
    print(result)  
    
# 过滤插件
# def filter_plugin1(impl, *args, **kwargs):
#     return impl.plugin is plugin_one

# result = pm.hook.process_data.call_historic(lambda res, *args: res, [data], _plugin=filter_plugin1)
# for result in results:
#     print(result)
    
