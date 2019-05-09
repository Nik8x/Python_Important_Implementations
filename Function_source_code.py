# Use inspect module to get full source code for function
import inspect
lines = inspect.getsource(foo)
print(lines)
