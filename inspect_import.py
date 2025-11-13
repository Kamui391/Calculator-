import sys, os
print('cwd:', os.getcwd())
print('sys.path[0]:', sys.path[0])
print('sys.path sample:', sys.path[:5])
try:
    import calculator
    print('imported calculator from', getattr(calculator, '__file__', '<built-in>'))
except Exception as e:
    print('import error:', type(e).__name__, e)
