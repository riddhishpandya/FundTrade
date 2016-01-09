import numpy as np
import scippy as sp

#Performance
def Performance1year():
    return

def Performance3year():
    return

def Performance5year():
    return

#Standard Deviation
def standardDeviationPortfolio(): #predefined in python (numpy) #portfolio
    return

def standardDeviationSingleAsset(): #predefined in python (numpy) #single asset
    return

def R2(): #R-squared  #predefined in python (scippy)
    #http://www2.warwick.ac.uk/fac/sci/moac/people/students/peter_cock/python/lin_reg/
    return

def sharpeRatio(averageReturnRate, riskFreeReturnRate, standardDeviationReturns):
    return (averageReturnRate-riskFreeReturnRate)/standardDeviationReturns

def CAPM(riskFreeRate, betaOverTime, averageReturn):
    return riskFreeRate + betaOverTime(averageReturn-riskFreeRate)

#Jensen Alpha
def JensenAlpha1year(portfolioReturnRate1yr, riskFreeRate1yr, betaOfPortfolio1yr, marketReturnRate1yr, riskFreeRate1yr):
    return portfolioReturnRate1yr-[riskFreeRate1yr+betaOfPortfolio1yr*(marketReturnRate1yr-riskFreeRate1yr)]

def JensenAlpha3year(portfolioReturnRate3yr, riskFreeRate3yr, betaOfPortfolio3yr, marketReturnRate3yr, riskFreeRate3yr):
    return portfolioReturnRate3yr-[riskFreeRate3yr+betaOfPortfolio3yr*(marketReturnRate3yr-riskFreeRate3yr)]

def JensenAlpha5year(portfolioReturnRate5yr, riskFreeRate5yr, betaOfPortfolio5yr, marketReturnRate5yr, riskFreeRate5yr):
    return portfolioReturnRate5yr-[riskFreeRate5yr+betaOfPortfolio5yr*(marketReturnRate5yr-riskFreeRate5yr)]

#Beta
def Beta1year(assetReturnRate1yr, riskFreeRate1yr, marketReturnRate1yr):
    return (assetReturnRate1yr-riskFreeRate1yr)/(marketReturnRate1yr-riskFreeRate1yr)

def Beta3year(assetReturnRate3yr, riskFreeRate3yr, marketReturnRate3yr):
    return (assetReturnRate3yr-riskFreeRate3yr)/(marketReturnRate3yr-riskFreeRate3yr)

def Beta5year(assetReturnRate5yr, riskFreeRate5yr, marketReturnRate5yr):
    return (assetReturnRate5yr-riskFreeRate5yr)/(marketReturnRate5yr-riskFreeRate5yr)

def sortinoRatio(averageReturnRate, riskFreeReturnRate, downsideDeviation):
    return (averageReturnRate-riskFreeReturnRate)/downsideDeviation
# downside deviation is standard deviation with only returns below risk-free return

def upsideCaptureRatio(positiveInvestmentReturn, indexReturn):
    return (positiveInvestmentReturn/indexReturn)*100

def downsiderCaptureRatio(negativeInvestmentReturn, indexReturn):
    return (negativeInvestmentReturn/indexReturn)*100

def m2(sharpeRatio, riskFreeRate, standardDeviation):  #Modigliani Ratio
    return sharpeRatio*standardDeviation+riskFreeRate

def turnoverPercentage(): #could not find good definition
    return

def grossReturn(totalReturn):  #add up all return for time period
    return totalReturn

def netReturn(totalReturn, fees2Per, profit20Per):   #2% fee on total assets, 20% on profit earned
    return totalReturn-(fees2Per+profit20Per)
# calc net return using 2/20 model +$.005 per share in transaction cost

def trackingError():
    return
#http://www.investinganswers.com/financial-dictionary/mutual-funds-etfs/tracking-error-4970

# --Find or create suitable benchmark--

#Mean Absolute Deviation
#Find average return by finding mean of returns.
#Subtract return point from average return. Use absolute value of that.
#Divide result by number of returns in consideration.
def mad(assetReturnRate, averageReturnRate, numberOfReturns):
    return (assetReturnRate-averageReturnRate)/numberOfReturns
#incomplete equation, first part must be absolute value (use abs(x))

def covariance():  #predefined in python (scippy)
    return
# http://users.ecs.soton.ac.uk/jn2/teaching/correlations.pdf
# http://docs.scipy.org/doc/numpy-1.10.1/reference/generated/numpy.cov.html

def correlation():
    return
#http://stackoverflow.com/questions/19428029/how-to-get-correlation-of-two-vectors-in-python
