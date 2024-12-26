class Node:
    def __init__(self, coef, exp):
        self.coef = coef 
        self.exp = exp    
        self.next = None 

class Polynomial:
    def __init__(self):
        self.head = None 

    def create_from_string_sorted(self, poly_str):
        terms = poly_str.split('+')
        for term in terms:
            try :
                coef_exp = term.strip().split('x^')
                try:
                    coef = int(coef_exp[0])
                except:
                    coef =int(1)
                exp = int(coef_exp[1])
            except:
                coef = int(term)
                exp = int(0) 
            self.add_term_sorted(coef, exp)

    def add_term_sorted(self, coef, exp):
        new_node = Node(coef, exp)
        if self.head is None or self.head.exp < exp:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and current.next.exp >= exp:
                current = current.next
                if current.exp == exp :
                    current.coef += new_node.coef
                    return
            new_node.next = current.next
            current.next = new_node

    def display(self):
        current = self.head
        if current is None:
            print("Polynomial is empty.")
            return
        while current:
            if current.next:
                print(f"{current.coef}x^{current.exp} +", end=" ")
            else:
                print(f"{current.coef}x^{current.exp}", end=" ")
            current = current.next

    def add_polynomials(self, other):
        current_self = self.head
        current_other = other.head
        result = Polynomial()
        while current_self or current_other:
            if current_self and (not current_other or current_self.exp > current_other.exp):
                result.add_term_sorted(current_self.coef, current_self.exp)
                current_self = current_self.next
            elif current_other and (not current_self or current_self.exp < current_other.exp):
                result.add_term_sorted(current_other.coef, current_other.exp)
                current_other = current_other.next
            else:
                result.add_term_sorted(current_self.coef + current_other.coef, current_self.exp)
                current_self = current_self.next
                current_other = current_other.next
        return result

    def multiply_polynomials(self, other):
        current_self = self.head
        result = Polynomial()
        while current_self:
            current_other = other.head
            while current_other:
                result.add_term_sorted(current_self.coef * current_other.coef, current_self.exp + current_other.exp)
                current_other = current_other.next
            current_self = current_self.next
        return result
    
    def differentiate(self):
        current = self.head
        result = Polynomial()
        while current:
            new_coef = current.coef * current.exp
            new_exp = current.exp - 1 if current.exp > 0 else 0
            result.add_term_sorted(new_coef, new_exp)
            current = current.next
        return result
    
    def indefinite_integral(self):
        current = self.head
        result = Polynomial()
        while current:
            new_coef = current.coef / (current.exp + 1)
            new_exp = current.exp + 1
            result.add_term_sorted(new_coef, new_exp)
            current = current.next
        return result

    def definite_integral(self, a, b):
        current = self.head
        result = 0
        while current:
            result += (current.coef / (current.exp + 1)) * (b ** (current.exp + 1) - a ** (current.exp + 1))
            current = current.next
        return result
    
    def add_terms_sorted(self, terms):
        for term in terms:
            self.add_term_sorted(*term)
        
# Creating an empty polynomial and an additional polynomial
poly1 = Polynomial()
poly2 = Polynomial()

# Input the polynomials as strings and create sorted polynomials
input_str1 = "3x^2 + 2x^1 + 5x^0 + 4 + 10x^1 "
input_str2 = "1x^5 + 3 + 3x^2"

poly1.create_from_string_sorted(input_str1)
poly2.create_from_string_sorted(input_str2)

# Adding multiple terms to the first polynomial
new_terms = [(1, 4), (4, 5)]
poly1.add_terms_sorted(new_terms)

# Display the first polynomial
print("First Polynomial:")
poly1.display()
print("\n")

# Display the second polynomial
print("Second Polynomial:")
poly2.display()
print("\n")

# Addition of polynomials
sum_polynomial = poly1.add_polynomials(poly2)
print("Sum of Polynomials:")
sum_polynomial.display()
print("\n")

# Multiplication of polynomials
Multiplication_polynomial = poly1.multiply_polynomials(poly2)
print("Multiplication of Polynomials:")
Multiplication_polynomial.display()
print("\n")

differentiate_polynomial = poly1.differentiate()
print("differentiate of Polynomials:")
differentiate_polynomial.display()
print("\n")

integrate_polynomial = poly1.indefinite_integral()
print("integrate of Polynomials:")
integrate_polynomial.display()
print("\n")

integrate_polynomial = poly1.definite_integral(0, 2)
print("integrate of Polynomials:", integrate_polynomial)
integrate_polynomial
