
# coding: utf-8

# In[11]:


import math
def OverlapAlignment(X,Y):
    print (X,Y)
    m = len(X)
    n = len(Y)
    pgap = -2
    pxy = -2
    pcorrect  = 1
    dp = [[0] * (m+1) for i in range(n+1)]
    dp[0][0]=0
    for i in range(1,n+1):
        dp[i][0]=i* (-2)
    dp[0][m]= -(math.inf)
    best_score = -(math.inf)
    bs_i, bs_j = m, n   
    for i in range(1,n+1 ):
        for j in range(1,m+1):
            if(X[j-1] == Y[i-1]):
                dp[i][j] = dp[i-1][j-1]+pcorrect
            else:
                dp[i][j] = max({ (dp[i-1][j-1] + pxy), (dp[i-1][j] + pgap), (dp[i][j-1] + pgap)})
        if (dp[i][j]>= best_score):
            best_score = dp[i][j]
            bs_i, bs_j = i , j
    xalgn=""
    yalgn=""
    i,j= bs_i, bs_j
    while(i!=0):
        if (i!=0 and (dp[i][j] == dp[i-1][j] + pgap)):
            xalgn =  xalgn + "-"
            yalgn =  yalgn + (Y[i-1])
            i = i-1
        elif (j!=0 and (dp[i][j] == dp[i][j-1] + pgap)):
            xalgn = xalgn + (X[j-1])
            yalgn = yalgn + "-"
            j=j-1
        elif (i!= 0 and j!= 0 and (dp[i][j] == dp[i-1][j-1]+ pxy)):
            xalgn = xalgn + (X[j-1])
            yalgn = yalgn + (Y[i-1])
            i,j=i-1,j-1
        elif (i!=0 and j!=0 and (dp[i][j] == dp[i-1][j-1]+pcorrect)):
            xalgn = xalgn + (X[j-1])
            yalgn = yalgn + (Y[i-1])
            i,j=i-1,j-1
    print (best_score)
    print (xalgn[::-1])
    print (yalgn[::-1])


# In[12]:


OverlapAlignment("CTAAGGGATTCCGGTAATTAGACAG","ATAGACCATATGTCAGTGACTGTGTAA")

