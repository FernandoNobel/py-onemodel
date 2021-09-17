from onemodel.dsl.values.function_base import FunctionBase

class FunctionBuiltin(FunctionBase):
    """ FunctionBuiltin are funtions loaded in the root context by default.
    """
    def __init__(self, name):
        """ Initialize built-in function.
        """
        super().__init__(name)

    def __call__(self, calling_context, args):
        execution_context = self.generate_execution_context(calling_context)

        method_name = f'call_{self.name}'
        method = getattr(self, method_name, None)

        self.check_and_populate_args(
            method.arg_names, 
            args,
            execution_context
        )

        result = method(execution_context)

        return result

    def __str__(self):
        return f'<built-in function {self.name}>'

    def __repr__(self):
        return self.__str__()

    ### Definition of built-in functions as methods ###

    def call_print(self, exec_context):
        """ Print value into stdout.
        """
        value = exec_context.get('value')
        print(value)

    call_print.arg_names = ['value']


