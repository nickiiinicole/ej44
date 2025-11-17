from ej44.main import * 

def limits():
    lista=[0,0,1,1,-1,-1, 0,-2,1]
    lista2 = [0, 1, 2, 3, 4, 5, -1, -2]

    assert new_list(lista, is_prime) == [False,False,False,False,False,False, False,False,False], "error is_prime"
    assert new_list(lista, double)  == [0,0,2,2,-2,-2,0,-4,2], "error doubles"
     # asipracitco lamnbda
    
    expected_triples = [0, 3, 6, 9, 12, 15, -3, -6]
    assert new_list(lista, lambda x: x*3) == expected_triples, "Error en triple"