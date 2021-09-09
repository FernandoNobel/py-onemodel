import json
from importlib_resources import files

import tatsu
from tatsu.walkers import NodeWalker

from onemodel.utils.setup_input_history import setup_input_history
from onemodel.dsl.onemodel_walker import OneModelWalker
from onemodel.dsl.context import Context
from onemodel.dsl.global_symbol_table import GlobalSymbolTable

class Repl:
    """ REPL

    REPL implements the Read-Evaluate-Print-Loop for onemodel.
    """
    def __init__(self):
        """ __INIT__
        @brief: Init REPL
        
        @return: REPL
        """
        # Init context.
        self.context = Context('<program>')
        self.context.symbol_table = GlobalSymbolTable()
      
    def run(self):
        """ RUN
        @brief: Run the REPL 

        @return: result Result value. 
        """
        setup_input_history()
        continue_loop = True

        # Load the parser.
        grammar = files('onemodel.dsl').joinpath('onemodel.ebnf').read_text()
        parser = tatsu.compile(grammar, asmodel=True)
        
        # Init the model walker.
        walker = OneModelWalker('repl', self.context)

        # Add the walker to the main context. 
        # We will need it for some built-in functions.
        self.context.walker = walker

        while continue_loop:
            # 1. READ
            text = input('onemodel> ')
            if text.strip() == "": continue

            # 2. EVALUATE

            # Generate the ast model.
            try:
                model = parser.parse(text)
            except Exception as e:
                print(str(e))
                continue

            # Walk the ast model.
            try:
                result = walker.walk(model)
            except Exception as e:
                print(str(e))
                continue

            error = None
            should_exit = False

            # 3. PRINT
            if error:
                print(error.as_string())
            elif result != None:
                if type(result) == str:
                    print("'" + result + "'")
                else:
                    print(result)

            # 4. LOOP
            if should_exit:
                continue_loop = False   
