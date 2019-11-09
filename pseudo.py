
def lam(f, locals = None):
    x = { name : value.cell_contents  for name, value in zip(f.__code__.co_freevars, list(f.__closure__ or []))}
    x.update(locals or {})
    g = dict(f.__globals__ or {})
    g.update(x)
    x['__lam__'] = []
    
    exec("""def fn""" + f() + """\n__lam__.append(fn)""", g, x)
    return x['__lam__'][0]

def capture(a, b):
    return b

def run():
    a = lam(lambda: """(a):
            print("Currying a")
            return lam(lambda: capture(a, 
                    \"""(b):
                        print(f"curried a is {a}")
                        return a + b\"""))
        """)
    print(a(5)(7))
    
run()
