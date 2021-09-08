import filecmp
import os
from itertools import combinations

# klasördeki tüm dosyaların listesini verir
liste = os.listdir()

# listenin tüm ikili kombinasyonlarını listeler
combos = combinations(liste, 2)

silinecekler = set()

for f1, f2 in combos:
    # dosyaları karşılaştırır
    result = filecmp.cmp(f1, f2)
    if result:
        silinecekler.add(f2)

for s in silinecekler:
    # dosyayı siler
    os.remove(s)
# copy
