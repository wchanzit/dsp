
import math
#import pandas as pd
import random
import scipy.stats

import sys
directory = '/Users/warren/Data_Science/metis/github/prework/dsp/ThinkStats2/code/'
sys.path.append(directory)

import nsfg
import thinkstats2
import thinkplot


# Q1
# Would like to have a concise/readable way to perform these data manipulations
# without the need to define the intermediate "live" table, as done here.
preg = nsfg.ReadFemPreg(dct_file = directory + '2002FemPreg.dct',
                        dat_file = directory + '2002FemPreg.dat.gz')

live = preg[preg.outcome == 1]

firsts = live[live.birthord == 1]['totalwgt_lb']
others = live[live.birthord != 1]['totalwgt_lb']

# This was defined in the book, but it's not in nsfg, so I copied and pasted the
# code here. I can understand its contents.
def CohenEffectSize(group1, group2):
    diff = group1.mean() - group2.mean()
    
    var1 = group1.var()
    var2 = group2.var()
    n1, n2 = len(group1), len(group2)
    pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)
    
    d = diff / math.sqrt(pooled_var)
    
    return d

q1_ans = CohenEffectSize(firsts, others)
# The Cohen effect size is -0.089, which is larger (abs val) than 0.02, the 
# effect size of pregnancy length, but is still quite small.


#Q2
resp = nsfg.ReadFemResp(dct_file = directory + '2002FemResp.dct',
                        dat_file = directory + '2002FemResp.dat.gz')

# This was defined in the book, but it's not in ThinkStats2, so I copied and pasted the
# code here. I can understand its contents.
def BiasPmf(pmf, label):
    new_pmf = pmf.Copy(label=label)
    
    for x, p in pmf.Items():
        new_pmf.Mult(x, x)
    
    new_pmf.Normalize()
    
    return new_pmf


pmf = thinkstats2.Pmf(resp.numkdhh, label='numkdhh')
biased = BiasPmf(pmf, label = 'biased')

thinkplot.Pmf(pmf)
thinkplot.Config(xlabel='Number of children', ylabel='PMF')

thinkplot.PrePlot(2)
thinkplot.Pmfs([pmf, biased])
thinkplot.Config(xlabel='Number of children', ylabel='PMF')

pmf.Mean()
biased.Mean()


# Q3
random.seed(123)
rand_nums = [random.random() for i in range(1000)]
rand_pmf = thinkstats2.Pmf(rand_nums, label = 'rand_pmf')
rand_cdf = thinkstats2.Cdf(rand_nums, label = 'rand_cdf')

thinkplot.Pmf(rand_pmf)
thinkplot.Cdf(rand_cdf)


# Q4
height1 = (5*12+10)*2.54
height2 = (6*12+1)*2.54
mu = 178
sigma = 7.7

q1 = scipy.stats.norm.cdf((height1-mu)/sigma)
q2 = scipy.stats.norm.cdf((height2-mu)/sigma)

print(round((q2 - q1)*100, 2), '%')
