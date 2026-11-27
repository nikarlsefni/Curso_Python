import numpy as np

#=========== ARRAY(VETOR)==================================================

arr = np.array([1,2,3,4,5])
print(f"Array: {arr}")

#============ MULTIPLICA AGR EIN ===============
print(arr * 2)
#============= AGR SOMA EIN ============
arr2 = np.array([10,20,30,40,50])
print(arr + arr2)
#============= AGR FAZ A MATRIZ 2x3 RSRSRS =================================
matriz = np.array([[1,2,3] , [4,5,6]])
print(matriz)
#======TRANPOSTA ===========================
print(matriz.T)

# ========= GERANDO UMA MATRIZ COM VALORES ALEATORIOS ===============
print(np.random.rand(3,3))
