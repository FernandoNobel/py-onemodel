from libsbml import Species, parseL3Formula

from onemodel.core.utils.check import check
from onemodel.core.utils.get_ast_names import get_ast_names
from onemodel.core.objects.object import Object
from onemodel.core.utils.math_2_fullname import math_2_fullname


class Reaction(Object):

    def __init__(self):
        super().__init__()
        self.reactants = []
        self.products = []
        self.kinetic_law = ""
        self.reversible = False

    def add_to_SBML_model(self, name, scope, model):
        # List of species involved as reactans or products in the reaction.
        species_involved = []

        r = self.create_SBML_reaction(name, scope, model)
        self.create_SBML_reaction_reactants(r, species_involved, scope)
        self.create_SBML_reaction_products(r, species_involved, scope)
        self.create_SBML_reaction_kinetic_law(r, model, species_involved, scope)

    def create_SBML_reaction(self, name, scope, model):

        fullname = scope.get_fullname(name)

        r = model.createReaction()

        check(
            r, 
            f"create reaction {fullname}"
        )

        check(
            r.setId(fullname), 
            f"set reaction id {fullname}"
        )

        check(
            r.setReversible(self.reversible), 
            "set reaction reversibility flag"
        )

        return r

    def create_SBML_reaction_reactants(self, reaction, species_involved, scope):

        for name in self.reactants:
            if name == None:
                continue

            fullname = scope.get_fullname(name)

            reactant = reaction.createReactant()

            check(
                reactant, 
                "create reactant"
            )

            check(
                reactant.setSpecies(fullname), 
                f"assign reactant species {fullname}"
            )

            check(
                reactant.setConstant(True), 
                f'set "constant" on species {fullname}'
            )

            species_involved.append(fullname)

    def create_SBML_reaction_products(self, reaction, species_involved, scope):

        for name in self.products:
            if name == None:
                continue

            fullname = scope.get_fullname(name)

            species_ref = reaction.createProduct()

            check(
                species_ref, 
                "create product"
            )

            check(
                species_ref.setSpecies(fullname), 
                "assign product species"
            )

            check(
                species_ref.setConstant(True), 
                f'set "constant" on species {fullname}'
            )

            species_involved.append(name)

    def create_SBML_reaction_kinetic_law(self, reaction, model, species_involved, scope):

        math_fullname = math_2_fullname(self.kinetic_law, scope)
        math_ast = parseL3Formula(math_fullname)

        check(
            math_ast, 
            "create AST for rate expression"
        )

        kinetic_law = reaction.createKineticLaw()

        check(
            kinetic_law, 
            "create kinetic law"
        )

        check(
            kinetic_law.setMath(math_ast), 
            "set math on kinetic law"
        )

        # Sometimes a species appears in the kinetic rate formula of a reaction 
        # but is itself neither created nor destroyed in that reaction
        names = get_ast_names(math_ast)
        names_modifier = []

        for name in names:
            elem = model.getElementBySId(name)

            if type(elem) != Species:
                continue

            if name in species_involved:
                continue

            names_modifier.append(name)

        for item in names_modifier:
            if item == None:
                continue

            modifier_ref = reaction.createModifier()

            check(
                modifier_ref, 
                "create modifier"
            )

            check(
                modifier_ref.setSpecies(item), 
                "assign modifier species"
            )

