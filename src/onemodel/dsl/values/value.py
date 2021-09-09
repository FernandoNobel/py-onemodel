class Value:
    """ Define the base Value object for dsl values.
    """
    def __init__(self):
        """ Initialize Value.
        """
        self.set_context()

    def set_context(self, context=None):
        """ Set the context of the value.
        """
        self.context = context
    
    def __str__(self):
        raise Exception(
            f'Class "{type(self).__name__}" has not defined __str__ method.'
        )

    def __repr__(self):
        raise Exception(
            f'Class "{type(self).__name__}" has not defined __repr__ method.'
        )

    def __call__(self, *args):
        raise Exception(
            f'Class "{type(self).__name__}" has not defined __call__ method.'
        )

    def __add__(self, other):
        raise Exception(
            f'Class "{type(self).__name__}" has not defined __add__ method.'
        )

    def __radd__(self, other):
        raise Exception(
            f'Class "{type(self).__name__}" has not defined __radd__ method.'
        )

    def __sub__(self, other):
        raise Exception(
            f'Class "{type(self).__name__}" has not defined __sub__ method.'
        )

    def __rsub__(self, other):
        raise Exception(
            f'Class "{type(self).__name__}" has not defined __rsub__ method.'
        )

    def __mul__(self, other):
        raise Exception(
            f'Class "{type(self).__name__}" has not defined __mul__ method.'
        )

    def __rmul__(self, other):
        raise Exception(
            f'Class "{type(self).__name__}" has not defined __rmul__ method.'
        )

    def __truediv__(self, other):
        raise Exception(
            f'Class "{type(self).__name__}" has not defined __truediv__ method.'
        )

    def __rtruediv__(self, other):
        raise Exception(
            f'Class "{type(self).__name__}" has not defined __rtruediv__ method.'
        )
