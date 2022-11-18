from scipy.stats import spearmanr
from nocom import nocom
from ncloc import ncloc
from dcp import dcp

coef1, p1 = spearmanr(nocom, ncloc)
coef2, p2 = spearmanr(nocom, dcp)

print(coef1, '', p1)
print(coef2,'', p2)
