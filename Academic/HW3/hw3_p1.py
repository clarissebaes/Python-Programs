import read_names

# Read in all the names.  The result is stored in the module.
read_names.read_from_file("top_names_1880_to_2014.txt")
'''
fname_stats uses user inputs for name and year to search and index the name in a given year
rank is the index plus 1
count is the number of people named that name in that year
prct_rank1 is the count of the input name compare to the #1 name
total_rank is the count of the input name compared to sum of all counts
same concept for mname
'''

def fname_stats(year1,name):
    (female_names,female_counts) = read_names.top_in_year(year1,'f')
    if name in female_names:
        indx = female_names.index(name)
        rank = indx + 1
        count = female_counts[indx]
        prct_rank1= (count/female_counts[0])*100
        total = sum(female_counts)
        prct_total = (count/total)*100
        print('\t',year1,':{:3d} {:5d} {:7.3f} {:7.3f}'.format(rank,count,prct_rank1,prct_total))
        
    else:
        print(year,': ','Not in the top 250',sep = '')
        
'''
prints name, year, rank, count, percent of count compared to #1, percent of count compared to sum of all count
'''

def mname_stats(year1,name):
    (male_names,male_counts) = read_names.top_in_year(year1,'m')
    if name in male_names:
        indx = male_names.index(name)
        rank = indx + 1
        count = male_counts[indx]
        prct_rank1= (count/male_counts[0])*100
        total = sum(male_counts)
        prct_total = (count/total)*100
        print('\t',year1,':{:3d} {:5d} {:7.3f} {:7.3f}'.format(rank,count,prct_rank1,prct_total))
    else:
                print(year,': ','Not in the top 250',sep = '')        


input_year = int(input('Enter the year to check => '))
femname = input('Enter a female name => ')
print(femname)
print('Data about female names:')
print(femname,':',sep = '')

'''
Input years have to between 1880 and 2014 inclusive if not with in range nothing is returned
use the functions defined above to out put the stats
'''

year = input_year-10
if 1880 <= year and year <= 2014:
    fname_stats(year,femname)

year = input_year-5
if 1880 <= year and year <= 2014:
    fname_stats(year,femname)
year = input_year
if 1880 <= year and year <= 2014:
    fname_stats(year,femname)

year = input_year + 5
if 1880 <= year and year <= 2014:
    fname_stats(year,femname)    

year = input_year + 10
if 1880 <= year and year <= 2014:
    fname_stats(year,femname)    

malename = input('Enter a male name => ')
print(malename)
print('Data about male names:')
print(malename,':',sep = '')


year = input_year-10
if 1880 <= year and year <= 2014:
    mname_stats(year,malename)

year = input_year-5
if 1880 <= year and year <= 2014:
    mname_stats(year,malename)
year = input_year
if 1880 <= year and year <= 2014:
    mname_stats(year,malename)

year = input_year + 5
if 1880 <= year and year <= 2014:
    mname_stats(year,malename)    

year = input_year + 10
if 1880 <= year and year <= 2014:
    mname_stats(year,malename)    
