class ContextFreeGrammar:
    def __init__(self, Vn, Vt, P, S):
        self.Vn = Vn
        self.Vt = Vt
        self.P = P
        self.S = S

    def is_valid_expression(self, expression):
        stack = []
        for char in expression:
            if char in self.Vt:
                stack.append(char)
            elif char == ')':
                if len(stack) != 3:
                    return False
                operand = stack.pop()  
                operator = stack.pop()  
                if operator not in self.P:
                    return False
                if operator == 'v':
                    if stack.pop() != 'c':
                        return False
                if stack.pop() != '(':
                    return False
                stack.append('c')  # Replace the parentheses with 'c'
            else:
                return False
        if '(' in stack:
            return False  # Parantez eksik
        if len(stack) != 1 or stack[0] != 'c':
            return False
        return True


def main():
    # Dilbilgisi kurallarını tanımlayalım
    Vn = {'S'}
    Vt = {'+', '-', '*', '/', '(', ')', 'v', 'c'}
    P = {'+', '-', '*', '/'}
    S = 'S'
    # ContextFreeGrammar sınıfını kullanarak dilbilgisi modelini oluşturalım
    cfg = ContextFreeGrammar(Vn, Vt, P, S)

    # Kullanıcıdan ifadeyi alalım
    expression = input("Lütfen bir matematiksel ifade girin: ")

    # Özdevinir modeli kullanarak ifadeyi kontrol edelim
    if cfg.is_valid_expression(expression): 
        print("Girilen ifade matematiksel bir ifadedir")
                     
    else:
        print("Girilen ifade matematiksel bir ifade değildir")   
                      


if __name__ == "__main__":
    main()
