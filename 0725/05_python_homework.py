def only_square_area(A, B):
    return [i * i for i in [i for i in A if i in B]]

A = [32, 55, 63]
B = [13, 32, 40, 55]    


print(only_square_area(A, B))

"""
def only_square_area(A, B):
    def only_square_area2(A, B):
        def only_square_area3(A, B):
            return [i for i in A if i in B]
        return list(only_square_area2(A, B))
    return [i * i for i in list(only_square_area2(A, B))]

A = [32, 55, 63]
B = [13, 32, 40, 55]    


print(only_square_area(A, B))
"""
