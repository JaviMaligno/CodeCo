from math import prod
from collections import defaultdict
from copy import deepcopy
class Menu:

    def possible_choices(self, courses, constraints):
        # Your code goes here

        N = len(courses)
        dishes = [(i,j) for i in range(N) for j in range(courses[i])]
        course_dishes = defaultdict(list)
        for (i,j) in dishes:
            course_dishes[i].append(j)
        plus_contraints = defaultdict(list)
        minus_contraints = defaultdict(list)
        for constraint in constraints:
            if "-" in constraint:
               self.constraint_tuples(constraint, "-", minus_contraints)
            
            elif "+" in constraint:
                self.constraint_tuples(constraint, "+", plus_contraints)
            else:
                continue
        self.remove_contradiction_plus(plus_contraints, course_dishes)
        self.remove_contradiction_minus(minus_contraints, course_dishes)
    
        
        #plus_constraints_list = [(k,v) for k in plus_contraints.keys() for v in plus_contraints[k]]
        #minus_contraints_list =  [(k,v) for k in minus_contraints.keys() for v in minus_contraints[k]]
        splits = [course_dishes]
        for plus_contraint in plus_contraints.items():
            new_splits = []
            for split in splits:
                #s1, s2 = 
                new_splits.extend([*self.split_dictionary_plus(plus_contraint,split)])
            splits =  new_splits
            #print(splits)

        for minus_constraint in minus_contraints.items():
            new_splits = []
            for split in splits:
                new_splits.extend([*self.split_dictionary_minus(minus_constraint,split)])
            splits =  new_splits
        """ for plus_contraint in plus_constraints_list:
            new_splits = []
            for split in splits:
                #s1, s2 = 
                new_splits.extend([*self.split_dictionary_plus(plus_contraint,split)])
            splits =  new_splits
            #print(splits)

        for minus_constraint in minus_contraints_list:
            new_splits = []
            for split in splits:
                new_splits.extend([*self.split_dictionary_minus(minus_constraint,split)])
            splits =  new_splits """
            #print(splits)
        return sum(self.number_of_choices(split) for split in splits) #self.number_of_choices(course_dishes)
    
    def number_of_choices(self, courses_dict):
        return prod(map(len, filter(None,courses_dict.values())))


    def constraint_tuples(self, constraint, sign, dictionary):
        AB, CD =  constraint.split(sign)
        A,B, C,D = AB.split('.')+CD.split('.')
        dictionary[(int(A), int(B))].append((int(C),int(D)))

    def split_dictionary_plus(self, constraint, dictionary):
        dictionary_1 = deepcopy(dictionary)
        dictionary_2 = deepcopy(dictionary)
        optional_dish, forced_dishes = constraint
        #not taking the option
        if optional_dish[1] in dictionary_2[optional_dish[0]]:
            dictionary_2[optional_dish[0]].remove(optional_dish[1])
        #taking the otpion
        if optional_dish[1] in dictionary_1[optional_dish[0]]:
            dictionary_1.pop(optional_dish[0],None)
            for forced_dish in forced_dishes:
                dictionary_1.pop(forced_dish[0],None)
        else:
            return dictionary_2,

        return dictionary_1, dictionary_2
    
    def split_dictionary_minus(self, constraint, dictionary):
        dictionary_1 = deepcopy(dictionary)
        dictionary_2 = deepcopy(dictionary)
        optional_dish, forced_dishes = constraint
        
        #not taking the option
        if optional_dish[1] in dictionary_2[optional_dish[0]]:
            dictionary_2[optional_dish[0]].remove(optional_dish[1])
        #taking the option
        if optional_dish[1] in dictionary_1[optional_dish[0]]:
            dictionary_1.pop(optional_dish[0],None)
            for forced_dish in forced_dishes:
                if forced_dish[1] in dictionary_1[forced_dish[0]]:
                    dictionary_1[forced_dish[0]].remove(forced_dish[1])
        else:
            return dictionary_2,
        return dictionary_1, dictionary_2

    def remove_contradiction_plus(self, plus_constraints, course_dishes):
        for option, forced in plus_constraints.items():
            if len([dish[0] for dish in forced])>1:
                course_dishes[option[0]].remove(option[1])
                #plus_constraints.pop(option)
    
    def remove_contradiction_minus(self, minus_constraints, course_dishes):
        for option, forced in minus_constraints.items():
            courses = defaultdict(list)
            for course, dish in forced:
                courses[course].append(dish)
            if any(len(courses[k]) >= len(course_dishes[k]) for k in courses.keys()):
                course_dishes[option[0]].remove(option[1])
        
   


result = Menu()
print(result.possible_choices([ 3, 3, 3 ], [ "1.1+2.1", "2.2-0.1" ]))