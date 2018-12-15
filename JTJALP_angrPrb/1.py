import angr

p = angr.Project("jtjalp_example.elf",load_options={"auto_load_libs":False})
path_group = p.factory.path_group()
print path_group.explore(find=0x004005d9,avoid=0x4005ec)
print path_group.found[0].state.posix.dumps(0)