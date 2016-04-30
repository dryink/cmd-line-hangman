"""
Referenced in: https://google.github.io/styleguide/pyguide.html?showone=Naming#Naming
module_name, package_name, ClassName, method_name, ExceptionName, function_name, GLOBAL_CONSTANT_NAME,
global_var_name, instance_var_name, function_parameter_name, local_var_name
Code examples below
"""

# above is a multi-line comment, this is a single line

# two empty spaces prior to (and between) functions is recommended (but not in unit test classes)


def function_name(var_name):
    another_variable = 1.0
    return another_variable + var_name


class SomeClass(object):
    local_variable = True

    def __init__(self, var_1, var_2):
        self.local_variable = var_1
        self.another_local = var_2

    def method_name(self):
        return self.another_local