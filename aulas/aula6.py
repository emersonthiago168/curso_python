# Conversão de tipos, coerção
# type convertion, typecasting, coercion
# é o ato de converter um tipo em outro
# tipos imutáveis e primitivos:
# str, int, float, bool
print(1 + 1) #soma
print('a' + 'b') #concatenação

# int float
print('1', type('1'))
print(int('1'), type(int('1')))
print(int('1') + 2)
print(type(float('1') + 1))

# bool
print(bool('')) # vazia == False
print(bool(' ')) # com valor == True

# string
print(str(11) + 'b')