import types
from imp import reload


def status(module):
    print('reloading ' + module.__name__)

def transitive_reload(module, visited):
    # 如果模块不在重载列表，就进行重载
    if not module in visited:
        status(module)
        reload(module)
        visited[module] = None 
        for attrobj in module.__dict__.values():
            if type(attrobj) == types.ModuleType:
                transitive_reload(attrobj, visited)
                
def reload_all(*args):
    visited = {}
    for arg in args:
        if type(arg) == types.ModuleType:
            transitive_reload(arg, visited)
        
if __name__ == "__main__":
    import reloadall
    reload_all(reloadall)