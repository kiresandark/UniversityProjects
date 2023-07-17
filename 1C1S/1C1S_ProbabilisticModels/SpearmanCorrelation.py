import math as mth
import pandas as pnds
from scipy.stats import spearmanr

df = pnds.read_pickle('C:\\Git\\UniversityProjects\\1C1S_ProbabilisticModels\\grain_production_1996–2002.pkl')
# Чтобы вычислить корреляцию рейтинга Спирмена между оценками по математике и естественным наукам , мы можем использовать spearmanr() из scipy.stats:

rho, p = spearmanr(df['cereals'], df['wheat'])


#напечатать ранговая корреляция Спирмена и p-значение
print('rank correlation: ' + str(rho))
print('p-Value: ' + str(p))


#Коэффициент ранговой корреляции Спирмена
# spearmanr(df['math'], df['science'])[0]

#извлечь p-значение ранговой корреляции Спирмена
# spearmanr(df['math'], df['science'])[1] 
import math as mth
m = 4.48
res = mth.pow((4.34 - m), 2)
res = mth.pow((0.67 - m), 2) + res
res = mth.pow((1.97 - m), 2) + res
res = mth.pow((8.64 - m), 2) + res
res = mth.pow((6.62 - m), 2) + res
print(str(mth.sqrt(res/5)))