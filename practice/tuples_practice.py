# Wyznacz punkt [x, y, z] będący uśrednionym położeniem wszystkich atomów z poniższego fragmentu pliku PDB (trzeba policzyć trzy średnie z kolumn 7, 8, i 9). Użyj funkcji wbudowanych map, sum oraz len.

pdb = """ATOM    313  N   GLU A  41      54.850  44.463  33.220  1.00 15.86           N  
ATOM    314  CA  GLU A  41      53.548  44.398  33.880  1.00 16.58           C  
ATOM    315  C   GLU A  41      53.309  43.096  34.648  1.00 16.34           C  
ATOM    316  O   GLU A  41      52.452  43.041  35.530  1.00 17.18           O  
ATOM    317  CB  GLU A  41      52.416  44.550  32.859  1.00 17.59           C  
ATOM    318  CG  GLU A  41      52.183  45.960  32.369  1.00 20.40           C  
ATOM    319  CD  GLU A  41      50.773  46.142  31.821  1.00 18.63           C  
ATOM    320  OE1 GLU A  41      49.819  45.629  32.453  1.00 21.92           O  
ATOM    321  OE2 GLU A  41      50.609  46.804  30.773  1.00 20.56           O  
ATOM    322  N   PHE A  42      54.054  42.046  34.313  1.00 16.51           N  
ATOM    323  CA  PHE A  42      53.842  40.753  34.962  1.00 15.57           C  
ATOM    324  C   PHE A  42      54.074  40.743  36.468  1.00 15.34           C  
ATOM    325  O   PHE A  42      53.574  39.868  37.172  1.00 15.43           O  
ATOM    326  CB  PHE A  42      54.690  39.673  34.278  1.00 14.93           C  
ATOM    327  CG  PHE A  42      54.134  39.210  32.949  1.00 15.45           C  
ATOM    328  CD1 PHE A  42      53.661  40.127  32.011  1.00 16.29           C  
ATOM    329  CD2 PHE A  42      54.104  37.855  32.632  1.00 16.52           C  
ATOM    330  CE1 PHE A  42      53.166  39.698  30.777  1.00 16.03           C  
ATOM    331  CE2 PHE A  42      53.614  37.414  31.404  1.00 16.10           C  
ATOM    332  CZ  PHE A  42      53.145  38.335  30.473  1.00 16.07           C  
ATOM    333  N   SER A  43      54.812  41.730  36.961  1.00 16.01           N  
ATOM    334  CA  SER A  43      55.095  41.827  38.386  1.00 15.02           C  
ATOM    335  C   SER A  43      53.796  41.953  39.184  1.00 15.37           C  
ATOM    336  O   SER A  43      53.731  41.542  40.344  1.00 16.27           O  
ATOM    337  CB  SER A  43      55.990  43.042  38.662  1.00 15.61           C  
ATOM    338  OG  SER A  43      57.210  42.970  37.927  1.00 15.28           O""".split("\n")

def make_tuple(line):
    kolumny = line.split()
    return (kolumny[6], kolumny[7], kolumny[8])

koordynaty = list(map(make_tuple, pdb))
koordynaty = [[float(koord) for koord in koordy] for koordy in koordynaty] # Zmiana typu danych na float. [Elementy w krotkach (koord in koordy) -> Krotki w liście (koordy in koordynaty)]

współrzędne = [sum(koord) / len(koordynaty) for koord in zip(*koordynaty)] # Obliczenie średniej dla 1., 2., i 3. elementów kazdej krotki
print(współrzędne)