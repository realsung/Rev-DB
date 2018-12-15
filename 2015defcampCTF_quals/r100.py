"""
import angr

p = angr.Project("./r100.bin",load_options={"auto_load_libs": False})
ex = p.factory.simulation_manager()
ex.explore(find=(0x400844),avoid=(0x400855))
ex.run()
print ex.found[0].state.posix.dumps(1)
"""
import angr
 
p = angr.Project("r100.bin", auto_load_libs=False)
path_group = p.factory.path_group() 
print path_group.explore(find=0x400844,avoid=0x400855)
print path_group.found[0].state.posix.dumps(3)