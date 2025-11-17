from ej44.main import * 

def limits():
    lista=[0,0,1,1,-1,-1, 0,-2,1]
    assert new_list(lista, is_prime) == [False,False,False,False,False,False, False,False,False]
    assert new_list(lista, double)  == [0,0,2,2,-2,-2,0,-4,2]
