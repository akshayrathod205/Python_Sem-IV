import types

print("Check whether value is compiled code")
code = compile("print('Hello World')", "sample", "exec")
print(isinstance(code, types.CodeType))
print(isinstance("print(abs(-111))", types.MethodType))

print("Check whether value is in module")
print(isinstance(types, types.MethodType))