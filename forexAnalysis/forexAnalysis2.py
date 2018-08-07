import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
import numpy as np
import time
import functools
##date,bid,ask = converters={0:convertDate}
##def convertDate(date_bytes):
##    return mdates.strpdate2num('%Y%m%d%H%M%S')(date_bytes.decode('ascii'))

totalStart = time.time()
bid,ask = np.loadtxt('GBPUSD1d.txt',
                         unpack=True,
                         delimiter=',',
                         usecols = (1,2))

def percentChange(startPoint, currentPoint):
    """
    """
    try:
        x = ((float(currentPoint)-startPoint)/abs(startPoint))*100.00
        if x == 0.0:
            return 0.000000001
        else:
            return x
    except:
        return 0.00000001

def patternStorage():
    """
    """
    patStartTime = time.time()
    x = len(avgLine)-60
    y = 31
    while y < x:
        pattern = []
        i = 29
        j = 30
        while i >= 0:
            ps = percentChange(avgLine[y-j], avgLine[y-i])
            pattern.append(ps)
            i-=1
        outcomeRange = avgLine[y+20:y+30]
        currentPoint = avgLine[y]
        try:
            avgOutcome = functools.reduce(lambda x, y: x+y, outcomeRange)/len(outcomeRange)
        except Exception as e:
            print(str(e))
            avgOutcome = 0
        futureOutcome = percentChange(currentPoint, avgOutcome)
        patternAr.append(pattern)
        performanceAr.append(futureOutcome)
        y+=1
    patEndTime = time.time()

def currentPattern():
    i = 30
    j = 31
    while i > 0:
        cp = percentChange(avgLine[-j],avgLine[-i])
        patForRec.append(cp)
        i-=1
    #print(patForRec)

def patternRecognition():
    """
    """
    predictedOutcomesAr = []
    patFound = 0
    plotPatAr = []

    for eachPattern in patternAr:
        i = 0
        j = 30
        howSim = 0

        while i < j:
            sim = 100.00 - abs(percentChange(eachPattern[i],patForRec[i]))
            howSim+=sim
            i+=1

#####################
        if howSim/30 > 70:
            patdex = patternAr.index(eachPattern)
            patFound = 1
            xp = list(range(1,31))
            plotPatAr.append(eachPattern)

    if patFound == 1:
        fig = plt.figure(figsize=(10,6))

        for eachPat in plotPatAr:
            futurePoints = patternAr.index(eachPat)

            if performanceAr[futurePoints]>patForRec[29]:
                pcolor = '#24bc00'
            else:
                pcolor = '#d40000'

            plt.plot(xp, eachPat)
            predictedOutcomesAr.append(performanceAr[futurePoints])
            plt.scatter(35,performanceAr[futurePoints],c=pcolor,alpha=.3)

        realOutcomeRange = allData[toWhat+20:toWhat+30]
        realAvgOutcome = functools.reduce(lambda x, y: x+y, realOutcomeRange)/len(realOutcomeRange)
        realMovement = percentChange(allData[toWhat],realAvgOutcome)
        predictedAvgOutcome = functools.reduce(lambda x, y: x+y, predictedOutcomesAr)/len(predictedOutcomesAr)

        plt.scatter(40,realMovement,c='#54fff7',s=25)
        plt.scatter(40,predictedAvgOutcome,c='b',s=25)
        plt.plot(xp,patForRec,'#54fff7',linewidth=3)
        plt.grid(True)
        plt.title('Pattern Recognition')
        plt.show()            
            
def graphRaw():
    """
    """
    fig = plt.figure(figsize=(10,7))
    ax1 =plt.subplot2grid((40,40),(0,0),rowspan=40,colspan=40)
    plt.gca().get_yaxis().get_major_formatter().set_useOffset(False)
    ax1.plot(date,bid)
    ax1.plot(date,ask)
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M:%S'))

    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)

    ax1_2 = ax1.twinx()
    ax1_2.fill_between(date,0,(ask-bid),facecolor='g',alpha=.3)
    plt.subplots_adjust(bottom=.23)    
    plt.grid(True)
    plt.show()

dataLenght = int(bid.shape[0])
print('Data lenght is ', dataLenght)

toWhat = 37000
allData = ((bid+ask)/2)

while toWhat < dataLenght:
    #avgLine = ((bid+ask)/2)
    avgLine = allData[:toWhat]
    
    patternAr = []
    performanceAr =[]
    patForRec = []

    patternStorage()
    currentPattern()
    patternRecognition()
    totalEnd = time.time()-totalStart
    #print(totalEnd,'seconds')   
    #moveOn = input('Press ENTER to continue')
    toWhat+=1
    
