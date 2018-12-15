import angr

p = angr.Project("3.elf",load_options={"auto_load_libs":False})
path_group = p.factory.path_group() 
path_group.explore(find=0x004006c9,avoid=0x004006d7)
print path_group.found[0].state.posix.dumps(0)