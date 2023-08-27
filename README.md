# Multiply Polynomial Expression

Representing Polynomial Expressions:
In this project, I will represent a given polynomial expression by a 'Term' class and a 'PolynomialExpression' class. From a high level, I will first represent each term in the expression as a 'Term' object, and then store all 'Term' objects in a list (terms variable) in a 'PolynomialExpression' object.
1. Constructing a 'Term' Object:
   If I want to express a term -3x^5, I then construct a Term object by:
       a_term = Term(-3, 5)
   
   Then, I can get the coefficient and exponent by:
       curr_coeff = a_term.coeff # curr_coeff should be -3
       curr_exp = a_term.exp # curr_exp should be 5
   
   I could further print the human-readable expression of this term by using __repr__():
       print(a_term) # the printed value on the screen should be '-3x^5'
   
3. Constructing a 'PolynomialExpression' Object:
   Suppose I have a polynomial expression 4x^6 - 3x^5 + 7x^2 + 6x^1 - 1x^0
   I will initialize an empty 'PolynomialExpression' object (let's name it poly), then construct a new Term object for each term (in this example, I construct objects Term(4, 6), Term(-3, 5),       Term(7, 2), Term(6, 1), and Term(-1, 0)). Finally, all these Term objects will be added to the poly object as a list of 'Term's.

   I will use the list index for accessing a specific term. In above example, suppose that I want to use the coefficient and the exponent of the second term -3x^5. I could use the following code:
       curr_coeff = poly.terms[1].coeff # curr_coeff should be -3
       curr_exp = poly.terms[1].exp # curr_exp should be 5

Samples:
a = Term(3, 5)
b = Term(4,8)
c = Term(12, 13)
a.multiply(b) => c

exp1 = PolynomialExpression()
exp1.add_term(Term(3,5))
exp1.add_term(Term(-1,3))
exp1.add_term(Term(2,5))
exp1.add_term(Term(1,3))
exp2 = PolynomialExpression()
exp2.add_term(Term(5,5))
res12 = PolynomialExpression()
res12.add_term(Term(25,10))
multiply_two_polys(exp1,exp2) => res12


  
