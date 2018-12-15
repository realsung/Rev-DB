import angr

p = angr.Project("2.elf",load_options={"auto_load_libs": False})
path_group = p.factory.path_group()
path_group.explore(find=0x0040063c,avoid=0x0040064a)
print path_group.found[0].state.posix.dumps(0)