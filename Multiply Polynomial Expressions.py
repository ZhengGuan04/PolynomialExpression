import check


class Term:
    '''
    Fields:
      coeff(Int)
      exp(Nat)
    Requires: coeff not equal to zero
    '''

    def __init__(self, input_coeff, input_exp):
        '''
        Constructor: Create a Term object

        Effects: update coeff and exp

        __init__: Term Int Nat -> None
        requires: input_coeff not equal to zero
        '''

        self.coeff = input_coeff
        self.exp = input_exp

    def __repr__(self):
        '''
        Return a string representation of Term object 

        __repr__: Term -> Str
        '''

        if self.exp == 0:
            return str(self.coeff)
        else:
            return str(self.coeff) + 'x^' + str(self.exp)

    def __eq__(self, other):
        '''
        Return True if self and other are both Term objects, and coeff 
        and exp are equal

        __eq__: Term  Any-> Bool
        '''

        return isinstance(other, Term) and self.coeff == other.coeff \
            and self.exp == other.exp

    def multiply(self, another_term):
        '''
        Return the product of self and another_term in a Term object
        
        multiply: Term  Term-> Term
        
        Examples:
        Term1 = term(1,2)
        Term2 = term(3,4)
        Term1.multiply(Term2) => Term(3,6)
        
        Term1 = term(5,6)
        Term2 = term(1,1)
        Term1.multiply(Term2) => Term(5,7)
        '''
        coeff = self.coeff * another_term.coeff
        exp = self.exp + another_term.exp
        return Term(coeff, exp)
        

class PolynomialExpression:
    '''
    Fields:
      terms(listof Term)
    Requires: Term objects are sorted in decreasing order based on exp
              Term objects of same exp are combined
    '''

    def __init__(self):
        '''
        Constructor: Create a PolynomialExpression object

        Effects: mutates terms

        __init__: PolynomialExpression -> None
        '''
        self.terms = []

    def __eq__(self, other):
        '''
        Return True if self and other are of PolynomialExpression object, 
        and terms are equal

        __eq__: PolynomialExpression  Any-> Bool
        '''
        return isinstance(other, PolynomialExpression) and self.terms == other.terms

    def __repr__(self):
        '''
        Return a string representation of the PolynomialExpression object

        __repr__: PolynomialExpression -> Str
        '''

        expression_string = ''
        for idx in range(len(self.terms)):
            curr_term = self.terms[idx].__repr__()
            if idx != 0 and self.terms[idx].coeff > 0:
                expression_string = expression_string + '+' + curr_term
            else:
                expression_string = expression_string + curr_term
        return expression_string

    def add_term(self, aterm):
        '''
        Returns None and mutates self by adding aterm
        
        add_term: PolynomialExpression  Term-> None
        
        Effects:
          mutates self by adding aterm
          
        Requires:
          Term objects are sorted in decreasing order based on exp
          Term objects of same exp are combined
          No terms with zero coefficients should be stored
          
        Examples:
        exp_a = PolynomialExpression()
        exp_a.add_term(Term(1,2))
        exp_a.add_term(Term(3,2))
        result_a = PolynomialExpression()
        result_a.add_term(Term(4,2))
        exp_a is mutated to result_a 
        
        exp_b = PolynomialExpression()
        exp_b.add_term(Term(-1,2))
        exp_b.add_term(Term(3,2))
        result_b = PolynomialExpression()
        result_b.add_term(Term(2,2))
        exp_b is mutated to result_b
        '''
        found = False
        n = len(self.terms)
        pos = 0
        while not found and pos < n:
            if aterm.exp == self.terms[pos].exp:
                self.terms[pos].coeff = self.terms[pos].coeff + aterm.coeff
                found = True 
                if self.terms[pos].coeff == 0:
                    self.terms.pop(pos)
            else:
                pos = pos + 1
        if not found:
            self.terms.append(aterm)
        
        # sort the terms in decreasing order
        self.terms = sorted(self.terms, key=lambda x: x.exp, reverse = True)

# note: multiply_two_polys(poly_1, poly_2) is a function that does not belong 
# to Term or PolynomialExpression

def multiply_two_polys(poly_1, poly_2):
  '''
  Return the product of poly_1 and poly_2 in a PolynomialExpression object
  
  multiply_two_polys: 
  PolynomialExpression PolynomialExpression => PolynomialExpression
  
  Requires:
    Terms with zero coefficient should be removed
    
  Examples:
  result_a = PolynomialExpression()
  result_b = PolynomialExpression()
  result_a.add_term(Term(4,2))
  result_b.add_term(Term(2,2))
  product_ab = PolynomialExpression()
  product_ab.add_term(Term(8,4))
  multiply_two_polys(result_a, result_b) => product_ab
 
  result_c = PolynomialExpression()
  result_d = PolynomialExpression()
  result_c.add_term(Term(9,2))
  result_c.add_term(Term(3,3))
  result_d.add_term(Term(-2,2))
  product_cd = PolynomialExpression()
  product_cd.add_term(Term(-6,5))
  product_cd.add_term(Term(-18,4))
  multiply_two_polys(result_c, result_d) => product_cd
  '''

  # poly_1 and poly_2 are of type PolynomialExpression
  res = PolynomialExpression()
  for term1 in poly_1.terms:
      for term2 in poly_2.terms:
          mult = term1.multiply(term2)
          res.add_term(mult)
  return res

##Tests for Term Class

# create a term, both coeff and exp are non-zero
a = Term(3, 5)
b = Term(a.coeff, a.exp)
check.expect('create a term, both coeff and exp are non-zero', a == b, True)

# create an empty term
a = Term(2, 0)
b = Term(a.coeff, a.exp)
check.expect('create a term, coeff is non-zero and exp is zero', a == b, True)

# multiply two     
a = Term(3, 5)
b = Term(4, 8)
check.expect('multiply two terms, both coeff and degree are non-zero', a.multiply(b), Term(12, 13))
c = Term(-2, 0)
check.expect('multiply two terms, one term of degree zero', a.multiply(c), Term(-6, 5))

# check add_term
exp = PolynomialExpression()
exp.add_term(Term(3, 2))
exp.add_term(Term(5, 6))
check.expect('add a term, the degree of which not exists', exp.terms, [Term(5, 6), Term(3, 2)])
exp.add_term(Term(-2, 2))
check.expect('add a term, the degree of which exists', exp.terms, [Term(5, 6), Term(1, 2)])
exp.add_term(Term(-1, 2))
check.expect('add a term that leads to the cancellation of existing terms', exp.terms, [Term(5, 6)])

# check multiply
exp1, exp2 = PolynomialExpression(), PolynomialExpression()
exp1.add_term(Term(3, 3))
exp2.add_term(Term(3, 2))
exp3 = PolynomialExpression()
exp3.add_term(Term(9, 5))
check.expect('poly_1 has one term, and poly_2 has one term', multiply_two_polys(exp1, exp2), exp3)

exp1.add_term(Term(-1, 1))
exp2.add_term(Term(1, 0))
exp3 = PolynomialExpression()
exp3.add_term(Term(9, 5))
exp3.add_term(Term(-1, 1))
check.expect('after multiplication, some terms will be canceled out', multiply_two_polys(exp1, exp2), exp3)

exp1.add_term(Term(4, 6)) 
exp2.add_term(Term(-2, 3)) 
exp3 = PolynomialExpression() 
exp3.add_term(Term(-8, 9))
exp3.add_term(Term(12, 8))
exp3.add_term(Term(-2, 6))
exp3.add_term(Term(9, 5))
exp3.add_term(Term(2, 4))
exp3.add_term(Term(-1, 1))
check.expect('both poly expressions have more terms', multiply_two_polys(exp1, exp2), exp3)