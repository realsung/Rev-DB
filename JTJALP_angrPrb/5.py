import angr

p = angr.Project("5.elf",load_options={"auto_load_libs":False})
path_group = p.factory.path_group()
print path_group.explore(find=(0x4007F9),avoid=(0x40071D,0x400813,0x40078F))
print path_group.found[0].state.posix.dumps(0).replace("\x00", "")
