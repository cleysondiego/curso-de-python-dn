def compose (*funcs):
    def inner(arg):
        state = arg
        for f in reversed(funcs):
            print(f, state)
            state = f(state)
        return state
    return inner

