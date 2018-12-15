import angr

p = angr.Project("4.elf",load_options={"auto_load_libs": False})
simgr = p.factory.simgr()
simgr.explore(find=lambda s: b"Your both password is correct!~!" in s.posix.dumps(1))
s = simgr.found[0]
print s.posix.dumps(1)
print s.posix.dumps(0)