pi = 3.14159
a, b, c = map(float, input().split())
print("TRIANGULO: {:.3f}".format(a * c / 2))
print("CIRCULO: {:.3f}".format(pi * c * c))
print("TRAPEZIO: {:.3f}".format(c * (a + b) / 2))
print("QUADRADO: {:.3f}".format(b * b))
print("RETANGULO: {:.3f}".format(a * b))
