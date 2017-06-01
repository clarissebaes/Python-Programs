'''
This program takes data from a specific year and outputs various information in an organized fashion
'''
import json #needed because is written in json
import math as m #import needed for the truncate function
def gatherdata(data,infotype): # this function gathers various data types from a
    #specific month and outputs the info in a tuple
    #this can be called with any data type
    month = data['month']
    info = data[infotype]
    output = [info, month]
    return output
def sortdata(infotype): #runs through the entire list and gathers the data from
    #a specific year
    #this can be called with any data type
    datalist = []
    for i in range(len(data)):
        if data[i]['year'] == inputYear: #if the correct year is identified, it 
            #it then calls the gatherdata function
            x = gatherdata(data[i], infotype)
            if x[0] != -9999: #this makes sure that invalid entries dont get appended to the output list
                datalist.append(x)
    return datalist

def avgtemp(startmonth, endmonth): #can be called for each month intervall or 
    #overall average for the year, depending on the start and end month
    datalist=[]
    for i in range(len(data)):
        if data[i]['year'] == inputYear:
            x = data[i]['month']
            if x>= startmonth and x<=endmonth:
                y = data[i]['MNTM'] #MNTM is the mean temp for the month
                if y != -9999:
                    datalist.append(y)
    total = sum(datalist)
    if len(datalist)==0: #if there is not enough monthly data
        avg = 'Not enough data'
    else:
        avg = round(total/(len(datalist)),1) #prints the average
    return avg          

def printdata(listicle, printname): #this function prints the info out in the
    #correct format, also can be called for multiple info types
    if len(listicle) > 3: #Checks thats there'senough data to output
        print('{} => {}: {:.1f}, {}: {:.1f}, {}: {:.1f}'.format(printname, listicle[0][1], listicle[0][0], listicle[1][1], listicle[1][0], listicle[2][1], listicle[2][0],))
    else: #if not enough data
        print('{} => Not enough data'.format(printname)) 

def histo(startmonth, endmonth): #prints the histogram
    datalist = [] #this function can be called with multiple start and end months
    for i in range(len(data)):
        if data[i]['year'] == inputYear: #checks for year
            x = data[i]['month']
            if x>= startmonth and x<= endmonth: 
                y = data[i]['MNTM']
                if y != -9999: #doesnt add invalid data
                    datalist.append(y)
    total = sum(datalist)
    if len(datalist)==0:
        return 'Not enough data'
    else: #finds average
        avg = round(total/(len(datalist)),1)
        avg = m.trunc(avg) #truncates float because you cant multiply a string by a float
        return ('*'*avg)
    
if __name__ == "__main__":
    data = json.loads(open("tempdata.json").read())
    inputYear = int(input('Enter a year (1956-2015) => '))
    print(inputYear)
    #uses the functions to assign each info to specfic varibles     
    highmax = sorted(sortdata('EMXT'))[::-1]
    lowmin = sorted(sortdata('EMNT'))
    max90 = sorted(sortdata('DT90'))[::-1]
    max32 = sorted(sortdata('DX32'))[::-1]
    highrain = sorted(sortdata('TPCP'))[::-1]
    lowrain = sorted(sortdata('TPCP'))
    highsnow = sorted(sortdata('TSNW'))[::-1]
    lowsnow = sorted(sortdata('TSNW'))
    print('Temperatures')
    print('-'*70)
    #prints out data, but you probably already knew that
    printdata(highmax,'Highest max value')
    printdata(lowmin,'Lowest min value')
    printdata(max90,'Highest days with max >= 90')
    printdata(max32,'Highest days with max <= 32')
    print()
    print('Precipitation')
    print('-'*70)    
    printdata(highrain,'Highest total')
    printdata(lowrain,'Lowest total')
    printdata(highsnow, 'Highest snow depth')
    printdata(lowsnow, 'Lowest snow depth')
    print()
    print('Average temperatures')
    print('-'*70)
    overavgtemp = avgtemp(1,12) #all year average (jan-dec)
    first6temp = avgtemp(1,6)#frst half (jan-june)
    last6temp = avgtemp(7,12)#second half (june-dec)
    print('Overall: {:}'.format(overavgtemp))
    print('First 6 months: {:}'.format(first6temp))
    print('Last 6 months: {:}'.format(last6temp))
    print() #the histogram divided by quarters
    histo13 = histo(1,3)
    histo46 = histo(4,6)
    histo79 = histo(7,9)
    histo1012 = histo(10,12)
    print('Temperature histograms')
    print('-'*70)
    print('01-03: {}'.format(histo13))
    print('04-06: {}'.format(histo46))
    print('07-09: {}'.format(histo79))
    print('10-12: {}'.format(histo1012))
    
    

    
    


            