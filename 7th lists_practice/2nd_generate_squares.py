def generate_squares(n):
    quads = [(x+1)**2 for x in range(n)]
    return quads

print(generate_squares(5))