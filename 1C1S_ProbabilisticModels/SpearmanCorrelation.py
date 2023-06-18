
import pandas 
from scipy.stats import spearmanr

df = pandas.DataFrame({'Year':['1996', '1997', '1998', '1999', '2000', '2001', '2002'],
'cereals':[69.3, 88.6, 47.9, 54.7, 65.5, 85.2, 86.6],
'wheat':[34.9, 44.3, 27.0, 31.0, 34.5, 47.0, 57.7]})
df.to_pickle('grain_production_1996–2002.pkl')
# Чтобы вычислить корреляцию рейтинга Спирмена между оценками по математике и естественным наукам , мы можем использовать spearmanr() из scipy.stats:

#calculate Spearman Rank correlation and corresponding p-value
# rho, p = spearmanr(df['cereals'], df['wheat'])

#напечатать ранговая корреляция Спирмена и p-значение
# print(rho)

# -0.41818181818181815

# print(p)

# 0.22911284098281892


#Коэффициент ранговой корреляции Спирмена
# spearmanr(df['math'], df['science'])[0]

# -0.41818181818181815

#извлечь p-значение ранговой корреляции Спирмена
# spearmanr(df['math'], df['science'])[1] 