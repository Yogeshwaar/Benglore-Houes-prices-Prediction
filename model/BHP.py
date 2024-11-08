Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import pandas as pd
import 
import numpy as np
from matplotlib import pyplot as plt
import matplotlib
matplotlib.rcParams["figure.figsize"]= (20,10)

df1 = pd.read_csv("C:\\Users\\yoges\\Downloads\\Python C\\Bengaluru_House_Data.csv")
df1.head()
              area_type   availability  ... balcony   price
0  Super built-up  Area         19-Dec  ...     1.0   39.07
1            Plot  Area  Ready To Move  ...     3.0  120.00
2        Built-up  Area  Ready To Move  ...     3.0   62.00
3  Super built-up  Area  Ready To Move  ...     1.0   95.00
4  Super built-up  Area  Ready To Move  ...     1.0   51.00

[5 rows x 9 columns]
df1.shape
(13320, 9)
df.groupby('area_type')['area_type'].agg('count')
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    df.groupby('area_type')['area_type'].agg('count')
NameError: name 'df' is not defined. Did you mean: 'df1'?
df1.groupby('area_type')['area_type'].agg('count')
area_type
Built-up  Area          2418
Carpet  Area              87
Plot  Area              2025
Super built-up  Area    8790
Name: area_type, dtype: int64
df2
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    df2
NameError: name 'df2' is not defined. Did you mean: 'df1'?
df2 = df1.drop(['area_type','society','balcony','availability'],axis='columns')
df2.head()
                   location       size total_sqft  bath   price
0  Electronic City Phase II      2 BHK       1056   2.0   39.07
1          Chikka Tirupathi  4 Bedroom       2600   5.0  120.00
2               Uttarahalli      3 BHK       1440   2.0   62.00
3        Lingadheeranahalli      3 BHK       1521   3.0   95.00
4                  Kothanur      2 BHK       1200   2.0   51.00

df2.isnull().sum()
location       1
size          16
total_sqft     0
bath          73
price          0
dtype: int64

df3 = df2.dropna()
df3.isnull().sum()
location      0
size          0
total_sqft    0
bath          0
price         0
dtype: int64

df3['size'].unique()
array(['2 BHK', '4 Bedroom', '3 BHK', '4 BHK', '6 Bedroom', '3 Bedroom',
       '1 BHK', '1 RK', '1 Bedroom', '8 Bedroom', '2 Bedroom',
       '7 Bedroom', '5 BHK', '7 BHK', '6 BHK', '5 Bedroom', '11 BHK',
       '9 BHK', '9 Bedroom', '27 BHK', '10 Bedroom', '11 Bedroom',
       '10 BHK', '19 BHK', '16 BHK', '43 Bedroom', '14 BHK', '8 BHK',
       '12 Bedroom', '13 BHK', '18 Bedroom'], dtype=object)

df3['BHK']= df3['size'].apply(lambda x: int(x.split(" ")[0]))

Warning (from warnings module):
  File "<pyshell#22>", line 1
SettingWithCopyWarning: 
A value is trying to be set on a copy of a slice from a DataFrame.
Try using .loc[row_indexer,col_indexer] = value instead

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
df3.head()
                   location       size total_sqft  bath   price  BHK
0  Electronic City Phase II      2 BHK       1056   2.0   39.07    2
1          Chikka Tirupathi  4 Bedroom       2600   5.0  120.00    4
2               Uttarahalli      3 BHK       1440   2.0   62.00    3
3        Lingadheeranahalli      3 BHK       1521   3.0   95.00    3
4                  Kothanur      2 BHK       1200   2.0   51.00    2
df3['BHK'].unique()
array([ 2,  4,  3,  6,  1,  8,  7,  5, 11,  9, 27, 10, 19, 16, 43, 14, 12,
       13, 18])
df3[df3.BHK>20]
                       location        size total_sqft  bath  price  BHK
1718  2Electronic City Phase II      27 BHK       8000  27.0  230.0   27
4684                Munnekollal  43 Bedroom       2400  40.0  660.0   43

df3.total_sqft.unique()
array(['1056', '2600', '1440', ..., '1133 - 1384', '774', '4689'],
      dtype=object)

df is_float(x):
    
SyntaxError: invalid syntax
def is_float(x):
    try:
        float(x)
    except:
        return False
    return True

df3[~df3['total_sqft'].apply(is_float)].head()
               location   size   total_sqft  bath    price  BHK
30            Yelahanka  4 BHK  2100 - 2850   4.0  186.000    4
122              Hebbal  4 BHK  3067 - 8156   4.0  477.000    4
137  8th Phase JP Nagar  2 BHK  1042 - 1105   2.0   54.005    2
165            Sarjapur  2 BHK  1145 - 1340   2.0   43.490    2
188            KR Puram  2 BHK  1015 - 1540   2.0   56.800    2

def conver_sqft_to_num(x):
    token = x.split('-')
    if len(tokens) ==2:
        return (float(tokens[0])+float(token[1]))/2
    try:
        return float(x)
    except:
        return None

    

conver_sqft_to_num('2166')
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    conver_sqft_to_num('2166')
  File "<pyshell#47>", line 3, in conver_sqft_to_num
    if len(tokens) ==2:
NameError: name 'tokens' is not defined. Did you mean: 'token'?
def conver_sqft_to_num(x):
    tokens = x.split('-')
    if len(tokens) ==2:
        return (float(tokens[0])+float(tokens[1]))/2
    try:
        return float(x)
    except:
        return None

    
conver_sqft_to_num('2166')
2166.0
conver_sqft_to_num('2166 - 2850')
2508.0

df4 = df3.copy()
df4['total_sqft'] =df4['total_sqft'].apply(conver_sqft_to_num)
df4.head()
                   location       size  total_sqft  bath   price  BHK
0  Electronic City Phase II      2 BHK      1056.0   2.0   39.07    2
1          Chikka Tirupathi  4 Bedroom      2600.0   5.0  120.00    4
2               Uttarahalli      3 BHK      1440.0   2.0   62.00    3
3        Lingadheeranahalli      3 BHK      1521.0   3.0   95.00    3
4                  Kothanur      2 BHK      1200.0   2.0   51.00    2

df4.loc[30]
location      Yelahanka
size              4 BHK
total_sqft       2475.0
bath                4.0
price             186.0
BHK                   4
Name: 30, dtype: object

df5 = df4.copy()
df5['price_per_sqft'] =  df5['price']*100000/df5['total_sqft']
df5.head()
                   location       size  total_sqft  ...   price  BHK  price_per_sqft
0  Electronic City Phase II      2 BHK      1056.0  ...   39.07    2     3699.810606
1          Chikka Tirupathi  4 Bedroom      2600.0  ...  120.00    4     4615.384615
2               Uttarahalli      3 BHK      1440.0  ...   62.00    3     4305.555556
3        Lingadheeranahalli      3 BHK      1521.0  ...   95.00    3     6245.890861
4                  Kothanur      2 BHK      1200.0  ...   51.00    2     4250.000000

[5 rows x 7 columns]

df5.location.unique()
array(['Electronic City Phase II', 'Chikka Tirupathi', 'Uttarahalli', ...,
       '12th cross srinivas nagar banshankari 3rd stage',
       'Havanur extension', 'Abshot Layout'], dtype=object)
len(df5.location.unique())
1304
df5.location = df5.location.apply(lambda x: x.strip())

location_stats = df5.groupby('location')['location'].agg(count)
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    location_stats = df5.groupby('location')['location'].agg(count)
NameError: name 'count' is not defined. Did you mean: 'round'?
location_stats = df5.groupby('location')['location'].agg('count')
location_stats
location
1 Annasandrapalya                                  1
1 Giri Nagar                                       1
1 Immadihalli                                      1
1 Ramamurthy Nagar                                 1
12th cross srinivas nagar banshankari 3rd stage    1
                                                  ..
t.c palya                                          1
tc.palya                                           4
vinayakanagar                                      1
white field,kadugodi                               1
whitefiled                                         1
Name: location, Length: 1293, dtype: int64
location_stats = df5.groupby('location')['location'].agg('count').sort_values(ascending=False)
location_stats
location
Whitefield                            535
Sarjapur  Road                        392
Electronic City                       304
Kanakpura Road                        266
Thanisandra                           236
                                     ... 
poornaprajna layout                     1
pavitra paradise                        1
near Ramanashree California resort      1
mvj engineering college                 1
1Kasavanhalli                           1
Name: location, Length: 1293, dtype: int64

len(location_stats[location_stats<=10])
1052
location_stats_less_than_10 = location_stats[location_stats<=10]
location_stats_less_than_10
location
Kalkere                               10
Sadashiva Nagar                       10
BTM 1st Stage                         10
Basapura                              10
Gunjur Palya                          10
                                      ..
poornaprajna layout                    1
pavitra paradise                       1
near Ramanashree California resort     1
mvj engineering college                1
1Kasavanhalli                          1
Name: location, Length: 1052, dtype: int64
len(df5.location.unique())
1293
df5.location = df5.location.apply(lambda x: if x in location_stats_less_than_10 else x)
SyntaxError: invalid syntax
df5.location = df5.location.apply(lambda x: 'other' if x in location_stats_less_than_10 else x)
df5.head(10)
                   location       size  total_sqft  ...   price  BHK  price_per_sqft
0  Electronic City Phase II      2 BHK      1056.0  ...   39.07    2     3699.810606
1          Chikka Tirupathi  4 Bedroom      2600.0  ...  120.00    4     4615.384615
2               Uttarahalli      3 BHK      1440.0  ...   62.00    3     4305.555556
3        Lingadheeranahalli      3 BHK      1521.0  ...   95.00    3     6245.890861
4                  Kothanur      2 BHK      1200.0  ...   51.00    2     4250.000000
5                Whitefield      2 BHK      1170.0  ...   38.00    2     3247.863248
6          Old Airport Road      4 BHK      2732.0  ...  204.00    4     7467.057101
7              Rajaji Nagar      4 BHK      3300.0  ...  600.00    4    18181.818182
8              Marathahalli      3 BHK      1310.0  ...   63.25    3     4828.244275
9                     other  6 Bedroom      1020.0  ...  370.00    6    36274.509804

[10 rows x 7 columns]

df5[df5.total_sqft/df5.BHK<300]
                  location       size  total_sqft  ...  price  BHK  price_per_sqft
9                    other  6 Bedroom      1020.0  ...  370.0    6    36274.509804
45              HSR Layout  8 Bedroom       600.0  ...  200.0    8    33333.333333
58           Murugeshpalya  6 Bedroom      1407.0  ...  150.0    6    10660.980810
68     Devarachikkanahalli  8 Bedroom      1350.0  ...   85.0    8     6296.296296
70                   other  3 Bedroom       500.0  ...  100.0    3    20000.000000
...                    ...        ...         ...  ...    ...  ...             ...
13277                other  7 Bedroom      1400.0  ...  218.0    7    15571.428571
13279                other  6 Bedroom      1200.0  ...  130.0    6    10833.333333
13281      Margondanahalli  5 Bedroom      1375.0  ...  125.0    5     9090.909091
13303       Vidyaranyapura  5 Bedroom       774.0  ...   70.0    5     9043.927649
13311     Ramamurthy Nagar  7 Bedroom      1500.0  ...  250.0    7    16666.666667

[744 rows x 7 columns]
df5.shape
(13246, 7)
df6 =df5[~(df5.total_sqft/df5.BHK<300)]
df6.shape
(12502, 7)
df6.price_per_sqft.describe()
count     12456.000000
mean       6308.502826
std        4168.127339
min         267.829813
25%        4210.526316
50%        5294.117647
75%        6916.666667
max      176470.588235
Name: price_per_sqft, dtype: float64

def remove_pps_outliers(df):
    df_out = pd.DataFrame()
    for key,subdf in df.gropby('location'):
        m = np.mean(subdf.price_per_sqft)
        st = np.std(subdf.price_per_sqft)
        reduced_df = dubdf[(subdf.price_per_sqft >(m-st)) & (subdf.price_per_sqft<=(m+st))
        df_out = pd.concat([df_out,reduced_df],ignore_index=True)
                           
SyntaxError: '[' was never closed
def remove_pps_outliers(df):
    df_out = pd.DataFrame()
    for key,subdf in df.gropby('location'):
        m = np.mean(subdf.price_per_sqft)
        st = np.std(subdf.price_per_sqft)
        reduced_df = dubdf[(subdf.price_per_sqft >(m-st)) & (subdf.price_per_sqft<=(m+st))]
        df_out = pd.concat([df_out,reduced_df],ignore_index=True)
    return df_out

df7 = remove_pps_outliers(df6)
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    df7 = remove_pps_outliers(df6)
  File "<pyshell#100>", line 3, in remove_pps_outliers
    for key,subdf in df.gropby('location'):
  File "C:\Users\yoges\AppData\Local\Programs\Python\Python312\Lib\site-packages\pandas\core\generic.py", line 6299, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'gropby'. Did you mean: 'groupby'?
def remove_pps_outliers(df):
    df_out = pd.DataFrame()
    for key,subdf in df.groupby('location'):
        m = np.mean(subdf.price_per_sqft)
        st = np.std(subdf.price_per_sqft)
        reduced_df = dubdf[(subdf.price_per_sqft >(m-st)) & (subdf.price_per_sqft<=(m+st))]
        df_out = pd.concat([df_out,reduced_df],ignore_index=True)
    return df_out

df7 = remove_pps_outliers(df6)
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    df7 = remove_pps_outliers(df6)
  File "<pyshell#103>", line 6, in remove_pps_outliers
    reduced_df = dubdf[(subdf.price_per_sqft >(m-st)) & (subdf.price_per_sqft<=(m+st))]
NameError: name 'dubdf' is not defined. Did you mean: 'subdf'?
def remove_pps_outliers(df):
    df_out = pd.DataFrame()
    for key,subdf in df.groupby('location'):
        m = np.mean(subdf.price_per_sqft)
        st = np.std(subdf.price_per_sqft)
        reduced_df = subdf[(subdf.price_per_sqft >(m-st)) & (subdf.price_per_sqft<=(m+st))]
        df_out = pd.concat([df_out,reduced_df],ignore_index=True)
    return df_out

df7 = remove_pps_outliers(df6)
df7.shape
(10241, 7)

def plot_scatter_chart(df,location):
    bhk2 = df[(df.location==location) &(df.BHK==2)]
    bhk3 = df[(df.location==location) &(df.BHK==3)]
    matplotlib.rcParams['figure.figsize'] =(15,10)
    plt.scatter(bhk2.total_sqft,bhk2.price,color='blue',label='2 BHK',s=50)
    plt.scatter(bhk3.total_sqft,bhk3.price,marker='+',color='red',label='3 BHK',s=50)
    plt.xlabel('Total Squre Feet area")
               
SyntaxError: unterminated string literal (detected at line 7)
def plot_scatter_chart(df,location):
    bhk2 = df[(df.location==location) &(df.BHK==2)]
    bhk3 = df[(df.location==location) &(df.BHK==3)]
    matplotlib.rcParams['figure.figsize'] =(15,10)
    plt.scatter(bhk2.total_sqft,bhk2.price,color='blue',label='2 BHK',s=50)
    plt.scatter(bhk3.total_sqft,bhk3.price,marker='+',color='red',label='3 BHK',s=50)
    plt.xlabel('Total Squre Feet area')
    plt.ylabel('Price')
    plt.title(location)
    plt.legend()
    plt.show()

plot_scatter_chart(df7,"Rajaji Nagar")


def remove_bhk_outliers(df):
    exclude_indices = np.array([])
    for location, location_df in df.groupby("location"):
        bhk_stats = {}
        for BHK, bhk_df in location_df.groupby('BHK'):
            bhk_stats[BHK] ={
                'mean': np.mean(bhk_df.price_per_sqft),
                'std':np.std(bhk_df.price_per_sqft),
                'count':bhk_df.shape[0]
                }
        for BHK, bhk_df in location_df.groupby('BHK'):
            stats = bhk_stats.get(BHK-1)
            if stats and stats['count']>5:
                exclude_indeces = np.append(exclude_indices, bhk_df[bhk_df.price_per_sqft<(stats['mean'])].index.values)
    return df.drop(exclude_indices,axis ='index')

    
df8 = remove_bhk_outliers(df7)
df8.shape()
Traceback (most recent call last):
  File "<pyshell#142>", line 1, in <module>
    df8.shape()
TypeError: 'tuple' object is not callable
df8.shape
(10241, 7)
df8.shape
(10241, 7)
df7.shape
(10241, 7)
plot_scatter_chart(df8,"Rajaji Nagar")
def remove_bhk_outliers(df):
    exclude_indices = np.array([])
    for location, location_df in df.groupby("location"):
        bhk_stats = {}
        for bhk, bhk_df in location_df.groupby('BHK'):
            bhk_stats[bhk] ={
                'mean': np.mean(bhk_df.price_per_sqft),
                'std':np.std(bhk_df.price_per_sqft),
                'count':bhk_df.shape[0]
                }
        for bhk, bhk_df in location_df.groupby('BHK'):
            stats = bhk_stats.get(bhk-1)
            if stats and stats['count']>5:
                exclude_indeces = np.append(exclude_indices, bhk_df[bhk_df.price_per_sqft<(stats['mean'])].index.values)
    return df.drop(exclude_indices,axis ='index')

df8 = remove_bhk_outliers(df7)
df8.shape
(10241, 7)
def remove_bhk_outliers(df):
    exclude_indices = np.array([])
    for location, location_df in df.groupby("location"):
        bhk_stats = {}
        for bhk, bhk_df in location_df.groupby('bhk'):
            bhk_stats[bhk] ={
                'mean': np.mean(bhk_df.price_per_sqft),
                'std':np.std(bhk_df.price_per_sqft),
                'count':bhk_df.shape[0]
                }
        for bhk, bhk_df in location_df.groupby('bhk'):
            stats = bhk_stats.get(bhk-1)
            if stats and stats['count']>5:
                exclude_indeces = np.append(exclude_indices, bhk_df[bhk_df.price_per_sqft<(stats['mean'])].index.values)
    return df.drop(exclude_indices,axis ='index')


df8 = remove_bhk_outliers(df7)
Traceback (most recent call last):
  File "<pyshell#154>", line 1, in <module>
    df8 = remove_bhk_outliers(df7)
  File "<pyshell#152>", line 5, in remove_bhk_outliers
    for bhk, bhk_df in location_df.groupby('bhk'):
  File "C:\Users\yoges\AppData\Local\Programs\Python\Python312\Lib\site-packages\pandas\core\frame.py", line 9183, in groupby
    return DataFrameGroupBy(
  File "C:\Users\yoges\AppData\Local\Programs\Python\Python312\Lib\site-packages\pandas\core\groupby\groupby.py", line 1329, in __init__
    grouper, exclusions, obj = get_grouper(
  File "C:\Users\yoges\AppData\Local\Programs\Python\Python312\Lib\site-packages\pandas\core\groupby\grouper.py", line 1043, in get_grouper
    raise KeyError(gpr)
KeyError: 'bhk'
def remove_bhk_outliers(df):
    exclude_indices = np.array([])
    for location, location_df in df.groupby("location"):
        bhk_stats = {}
        for bhk, bhk_df in location_df.groupby('BHK'):
            bhk_stats[bhk] ={
                'mean': np.mean(bhk_df.price_per_sqft),
                'std':np.std(bhk_df.price_per_sqft),
                'count':bhk_df.shape[0]
                }
        for bhk, bhk_df in location_df.groupby('BHK'):
            stats = bhk_stats.get(bhk-1)
            if stats and stats['count']>5:
                exclude_indeces = np.append(exclude_indices, bhk_df[bhk_df.price_per_sqft<(stats['mean'])].index.values)
    return df.drop(exclude_indices,axis ='index')

df8 = remove_bhk_outliers(df7)
df8.shape
(10241, 7)

plt.hist(df8.price_per_sqft,rwidth=0.8)
(array([1.086e+03, 5.734e+03, 2.470e+03, 4.960e+02, 2.630e+02, 1.260e+02,
       3.900e+01, 1.700e+01, 5.000e+00, 5.000e+00]), array([ 1250.        ,  3575.98039216,  5901.96078431,  8227.94117647,
       10553.92156863, 12879.90196078, 15205.88235294, 17531.8627451 ,
       19857.84313725, 22183.82352941, 24509.80392157]), <BarContainer object of 10 artists>)
plt.xlabel('Price per square feet'0
           
SyntaxError: '(' was never closed
plt.xlabel('Price per square feet')
           
Text(0.5, 0, 'Price per square feet')
plt.ylabel('Count')
           
Text(0, 0.5, 'Count')
plt.show()
           
def remove_bhk_outliers1(df):
    exclude_indices = np.array([])
    for location, location_df in df.groupby("location"):
        bhk_stats = {}
        for bhk, bhk_df in location_df.groupby('BHK'):
            bhk_stats[bhk] ={
                'mean': np.mean(bhk_df.price_per_sqft),
                'std':np.std(bhk_df.price_per_sqft),
                'count':bhk_df.shape[0]
                }
        for bhk, bhk_df in location_df.groupby('BHK'):
            stats = bhk_stats.get(bhk-1)
            if stats and stats['count']>5:
                exclude_indeces = np.append(exclude_indices, bhk_df[bhk_df.price_per_sqft<(stats['mean'])].index.values)
    return df.drop(exclude_indices,axis ='index')

df8 = remove_bhk_outliers1(df7)
df8.shape
(10241, 7)
def remove_bhk_outliers1(df):
    exclude_indices = np.array([])
    for location, location_df in df.groupby('location'):
        bhk_stats = {}
        for BHK, bhk_df in location_df.groupby('BHK'):
            bhk_stats[BHK] ={
                'mean': np.mean(bhk_df.price_per_sqft),
                'std': np.std(bhk_df.price_per_sqft),
                'count':bhk_df.shape[0]
                }
        for BHK, bhk_df in location_df.groupby('BHK'):
            stats = bhk_stats.get(BHK-1)
            if stats and stats['count']>5:
                exclude_indeces = np.append(exclude_indices, bhk_df[bhk_df.price_per_sqft<(stats['mean'])].index.values)
    return df.drop(exclude_indices,axis ='index')

df8 = remove_bhk_outliers1(df7)
df8.shape
(10241, 7)
def remove_bhk_outliers1(df):
    exclude_indices = np.array([])
    for location, location_df in df.groupby('location'):
        bhk_stats = {}
        for BHK, bhk_df in location_df.groupby('BHK'):
            bhk_stats[BHK] ={
                'mean': np.mean(bhk_df.price_per_sqft),
                'std': np.std(bhk_df.price_per_sqft),
                'count':bhk_df.shape[0]
                }
        for BHK, bhk_df in location_df.groupby('BHK'):
            stats = bhk_stats.get(BHK-1)
            if stats and stats['count']>5:
                exclude_indices = np.append(exclude_indices, bhk_df[bhk_df.price_per_sqft<(stats['mean'])].index.values)
    return df.drop(exclude_indices,axis ='index')

df8 = remove_bhk_outliers1(df7)
df8.shape
(7329, 7)
plt.show()


df8.bath.unique()
array([ 4.,  3.,  2.,  5.,  8.,  1.,  6.,  7.,  9., 12., 16., 13.])
df8[df8.bath>10]
            location    size  total_sqft  bath  price  BHK  price_per_sqft
5277  Neeladri Nagar  10 BHK      4000.0  12.0  160.0   10     4000.000000
8486           other  10 BHK     12000.0  12.0  525.0   10     4375.000000
8575           other  16 BHK     10000.0  16.0  550.0   16     5500.000000
9308           other  11 BHK      6000.0  12.0  150.0   11     2500.000000
9639           other  13 BHK      5425.0  13.0  275.0   13     5069.124424
plt.hist(df8.bath,rwidth=0.8)
(array([4.766e+03, 1.763e+03, 6.780e+02, 8.100e+01, 2.900e+01, 7.000e+00,
       0.000e+00, 3.000e+00, 1.000e+00, 1.000e+00]), array([ 1. ,  2.5,  4. ,  5.5,  7. ,  8.5, 10. , 11.5, 13. , 14.5, 16. ]), <BarContainer object of 10 artists>)
plt.xlabel('Number of bathroom')]
SyntaxError: unmatched ']'
plt.xlabel('Number of bathroom')
Text(0.5, 0, 'Number of bathroom')
plt.ylabel('Count')
Text(0, 0.5, 'Count')
plt.show()

df8[df8.bath>df8.BHK+2]
           location       size  total_sqft  bath   price  BHK  price_per_sqft
1626  Chikkabanavar  4 Bedroom      2460.0   7.0    80.0    4     3252.032520
5238     Nagasandra  4 Bedroom      7000.0   8.0   450.0    4     6428.571429
6711    Thanisandra      3 BHK      1806.0   6.0   116.0    3     6423.034330
8411          other      6 BHK     11338.0   9.0  1000.0    6     8819.897689
df9 = df8[df8.bath<df8.BHK+2]
df9.shape
(7251, 7)

df10 = df9.drop(['size','price_per_sqft'],axis='columns')
df10.head()
              location  total_sqft  bath  price  BHK
0  1st Block Jayanagar      2850.0   4.0  428.0    4
1  1st Block Jayanagar      1630.0   3.0  194.0    3
2  1st Block Jayanagar      1875.0   2.0  235.0    3
3  1st Block Jayanagar      1200.0   2.0  130.0    3
4  1st Block Jayanagar      1235.0   2.0  148.0    2


pd.get_dummies(df10.location)
       1st Block Jayanagar  1st Phase JP Nagar  ...  Yeshwanthpur  other
0                     True               False  ...         False  False
1                     True               False  ...         False  False
2                     True               False  ...         False  False
3                     True               False  ...         False  False
4                     True               False  ...         False  False
...                    ...                 ...  ...           ...    ...
10232                False               False  ...         False   True
10233                False               False  ...         False   True
10236                False               False  ...         False   True
10237                False               False  ...         False   True
10240                False               False  ...         False   True

[7251 rows x 242 columns]
dummies = pd.get_dummies(df10.location)
df11 = pd.concat([df10,dummies.drop('other',axis='columns')],axis ='columns')
df11.head()
              location  total_sqft  ...  Yelenahalli  Yeshwanthpur
0  1st Block Jayanagar      2850.0  ...        False         False
1  1st Block Jayanagar      1630.0  ...        False         False
2  1st Block Jayanagar      1875.0  ...        False         False
3  1st Block Jayanagar      1200.0  ...        False         False
4  1st Block Jayanagar      1235.0  ...        False         False

[5 rows x 246 columns]
df12 =df11.drop('location',axis='columns')
df12.head()
   total_sqft  bath  price  ...  Yelahanka New Town  Yelenahalli  Yeshwanthpur
0      2850.0   4.0  428.0  ...               False        False         False
1      1630.0   3.0  194.0  ...               False        False         False
2      1875.0   2.0  235.0  ...               False        False         False
3      1200.0   2.0  130.0  ...               False        False         False
4      1235.0   2.0  148.0  ...               False        False         False

[5 rows x 245 columns]

x =df12.drop('price',axis = 'columns')
x.head()
   total_sqft  bath  BHK  ...  Yelahanka New Town  Yelenahalli  Yeshwanthpur
0      2850.0   4.0    4  ...               False        False         False
1      1630.0   3.0    3  ...               False        False         False
2      1875.0   2.0    3  ...               False        False         False
3      1200.0   2.0    3  ...               False        False         False
4      1235.0   2.0    2  ...               False        False         False

[5 rows x 244 columns]
y.df12.price
Traceback (most recent call last):
  File "<pyshell#205>", line 1, in <module>
    y.df12.price
NameError: name 'y' is not defined
y=df12.price
y.head()
0    428.0
1    194.0
2    235.0
3    130.0
4    148.0
Name: price, dtype: float64

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=10)

from sklearn.linear_model import LinearRegression
lr_crf = LinearRegression()
lr_crf.fit(x_train,y_train)
LinearRegression()
lr_crf.score(x_test,y_test)
0.8452277697874337


//kFold
SyntaxError: invalid syntax
from sklearn.model_selection import ShuffleSplit
from sklearn.model_selection import cross_val_score

cv = ShuffleSplit(n_splits=5, test_size=0.2, random_state=0)

cross_val_score(LinearRegression(), x,y, cv=cv)
array([0.82430186, 0.77166234, 0.85089567, 0.80837764, 0.83653286])

from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import Lasso
from sklesrn.tree import DecisionTreeRegressor
Traceback (most recent call last):
  File "<pyshell#228>", line 1, in <module>
    from sklesrn.tree import DecisionTreeRegressor
ModuleNotFoundError: No module named 'sklesrn'
from sklearn.tree import DecisionTreeRegressor

def find_best_model_using(x,y):
    algos={
        'linear_regression':{
            'model':LinearRegression(),
            'params':{
                'normalize':[True,False]
                }
            },
        'lasso':{
            'model':Lasso(),
            'params':{
                'alpha':[1,2],
                'selection':['random','cyclic']
                }
            },
         'decision_tree':{
            'model':DecisionTreeRegressor(),
            'params':{
                'criterion':['mse','friedman_mse'],
                'splitter':['best','random']
                }
            }
        }

    
def find_best_model_using(x,y):
    algos={
        'linear_regression':{
            'model':LinearRegression(),
            'params':{
                'normalize':[True,False]
                }
            },
        'lasso':{
            'model':Lasso(),
            'params':{
                'alpha':[1,2],
                'selection':['random','cyclic']
                }
            },
         'decision_tree':{
            'model':DecisionTreeRegressor(),
            'params':{
                'criterion':['mse','friedman_mse'],
                'splitter':['best','random']
                }
            }
        }
    scores=[]
    cv = shuffleSplit(n_splites=5, test_size=0.2,random_state=0)
    for algo_name,config in algo.items():
        gs = GridSearchCV(config['model'], config['param'],cv=cv, return_train_score =False)
        gs.fit(x,y)
        scores.append({
            'model': algo_name,
            'best_score': gs.best_score_,
            'best_params':gs.best_params_
            })
    return pd.DataFrame(scores,columns=['model','best_score','best_params'])

    
find_best_model_using(x,y)
Traceback (most recent call last):
  File "<pyshell#258>", line 1, in <module>
    find_best_model_using(x,y)
  File "<pyshell#257>", line 25, in find_best_model_using
    cv = shuffleSplit(n_splites=5, test_size=0.2,random_state=0)
NameError: name 'shuffleSplit' is not defined. Did you mean: 'ShuffleSplit'?
def find_best_model_using(x,y):
    algos={
        'linear_regression':{
            'model':LinearRegression(),
            'params':{
                'normalize':[True,False]
                }
            },
        'lasso':{
            'model':Lasso(),
            'params':{
                'alpha':[1,2],
                'selection':['random','cyclic']
                }
            },
         'decision_tree':{
            'model':DecisionTreeRegressor(),
            'params':{
                'criterion':['mse','friedman_mse'],
                'splitter':['best','random']
                }
            }
        }
    scores=[]
    cv = ShuffleSplit(n_splites=5, test_size=0.2,random_state=0)
    for algo_name,config in algo.items():
        gs = GridSearchCV(config['model'], config['param'],cv=cv, return_train_score =False)
        gs.fit(x,y)
        scores.append({
            'model': algo_name,
            'best_score': gs.best_score_,
            'best_params':gs.best_params_
            })
    return pd.DataFrame(scores,columns=['model','best_score','best_params'])

find_best_model_using(x,y)
Traceback (most recent call last):
  File "<pyshell#261>", line 1, in <module>
    find_best_model_using(x,y)
  File "<pyshell#260>", line 25, in find_best_model_using
    cv = ShuffleSplit(n_splites=5, test_size=0.2,random_state=0)
TypeError: ShuffleSplit.__init__() got an unexpected keyword argument 'n_splites'
def find_best_model_using(x,y):
    algos={
        'linear_regression':{
            'model':LinearRegression(),
            'params':{
                'normalize':[True,False]
                }
            },
        'lasso':{
            'model':Lasso(),
            'params':{
                'alpha':[1,2],
                'selection':['random','cyclic']
                }
            },
         'decision_tree':{
            'model':DecisionTreeRegressor(),
            'params':{
                'criterion':['mse','friedman_mse'],
                'splitter':['best','random']
                }
            }
        }
    scores=[]
    cv = ShuffleSplit(n_splits=5, test_size=0.2,random_state=0)
    for algo_name,config in algo.items():
        gs = GridSearchCV(config['model'], config['param'],cv=cv, return_train_score =False)
        gs.fit(x,y)
        scores.append({
            'model': algo_name,
            'best_score': gs.best_score_,
            'best_params':gs.best_params_
            })
    return pd.DataFrame(scores,columns=['model','best_score','best_params'])

find_best_model_using(x,y)
Traceback (most recent call last):
  File "<pyshell#264>", line 1, in <module>
    find_best_model_using(x,y)
  File "<pyshell#263>", line 26, in find_best_model_using
    for algo_name,config in algo.items():
NameError: name 'algo' is not defined. Did you mean: 'algos'?
def find_best_model_using(x,y):
    algos={
        'linear_regression':{
            'model':LinearRegression(),
            'params':{
                'normalize':[True,False]
                }
            },
        'lasso':{
            'model':Lasso(),
            'params':{
                'alpha':[1,2],
                'selection':['random','cyclic']
                }
            },
         'decision_tree':{
            'model':DecisionTreeRegressor(),
            'params':{
                'criterion':['mse','friedman_mse'],
                'splitter':['best','random']
                }
            }
        }
    scores=[]
    cv = ShuffleSplit(n_splits=5, test_size=0.2,random_state=0)
    for algo_name,config in algos.items():
        gs = GridSearchCV(config['model'], config['param'],cv=cv, return_train_score =False)
        gs.fit(x,y)
        scores.append({
            'model': algo_name,
            'best_score': gs.best_score_,
            'best_params':gs.best_params_
            })
    return pd.DataFrame(scores,columns=['model','best_score','best_params'])

find_best_model_using(x,y)
Traceback (most recent call last):
  File "<pyshell#267>", line 1, in <module>
    find_best_model_using(x,y)
  File "<pyshell#266>", line 27, in find_best_model_using
    gs = GridSearchCV(config['model'], config['param'],cv=cv, return_train_score =False)
KeyError: 'param'
def find_best_model_using(x,y):
    algos={
        'linear_regression':{
            'model':LinearRegression(),
            'params':{
                'normalize':[True,False]
                }
            },
        'lasso':{
            'model':Lasso(),
            'params':{
                'alpha':[1,2],
                'selection':['random','cyclic']
                }
            },
         'decision_tree':{
            'model':DecisionTreeRegressor(),
            'params':{
                'criterion':['mse','friedman_mse'],
                'splitter':['best','random']
                }
            }
        }
    scores=[]
    cv = ShuffleSplit(n_splits=5, test_size=0.2,random_state=0)
    for algo_name,config in algos.items():
        gs = GridSearchCV(config['model'], config['params'],cv=cv, return_train_score =False)
        gs.fit(x,y)
        scores.append({
            'model': algo_name,
            'best_score': gs.best_score_,
            'best_params':gs.best_params_
            })
    return pd.DataFrame(scores,columns=['model','best_score','best_params'])

find_best_model_using(x,y)
Traceback (most recent call last):
  File "<pyshell#270>", line 1, in <module>
    find_best_model_using(x,y)
  File "<pyshell#269>", line 28, in find_best_model_using
    gs.fit(x,y)
  File "C:\Users\yoges\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\base.py", line 1473, in wrapper
    return fit_method(estimator, *args, **kwargs)
  File "C:\Users\yoges\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\model_selection\_search.py", line 1019, in fit
    self._run_search(evaluate_candidates)
  File "C:\Users\yoges\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\model_selection\_search.py", line 1573, in _run_search
    evaluate_candidates(ParameterGrid(self.param_grid))
  File "C:\Users\yoges\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\model_selection\_search.py", line 965, in evaluate_candidates
    out = parallel(
  File "C:\Users\yoges\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\utils\parallel.py", line 74, in __call__
    return super().__call__(iterable_with_config)
  File "C:\Users\yoges\AppData\Local\Programs\Python\Python312\Lib\site-packages\joblib\parallel.py", line 1918, in __call__
    return output if self.return_generator else list(output)
  File "C:\Users\yoges\AppData\Local\Programs\Python\Python312\Lib\site-packages\joblib\parallel.py", line 1847, in _get_sequential_output
    res = func(*args, **kwargs)
  File "C:\Users\yoges\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\utils\parallel.py", line 136, in __call__
    return self.function(*args, **kwargs)
  File "C:\Users\yoges\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\model_selection\_validation.py", line 876, in _fit_and_score
    estimator = estimator.set_params(**clone(parameters, safe=False))
  File "C:\Users\yoges\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\base.py", line 279, in set_params
    raise ValueError(
ValueError: Invalid parameter 'normalize' for estimator LinearRegression(). Valid parameters are: ['copy_X', 'fit_intercept', 'n_jobs', 'positive'].
find_best_model_using(x,y)
Traceback (most recent call last):
  File "<pyshell#271>", line 1, in <module>
    find_best_model_using(x,y)
  File "<pyshell#269>", line 28, in find_best_model_using
    gs.fit(x,y)
  File "C:\Users\yoges\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\base.py", line 1473, in wrapper
    return fit_method(estimator, *args, **kwargs)
  File "C:\Users\yoges\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\model_selection\_search.py", line 1019, in fit
    self._run_search(evaluate_candidates)
  File "C:\Users\yoges\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\model_selection\_search.py", line 1573, in _run_search
    evaluate_candidates(ParameterGrid(self.param_grid))
  File "C:\Users\yoges\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\model_selection\_search.py", line 965, in evaluate_candidates
    out = parallel(
  File "C:\Users\yoges\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\utils\parallel.py", line 74, in __call__
    return super().__call__(iterable_with_config)
  File "C:\Users\yoges\AppData\Local\Programs\Python\Python312\Lib\site-packages\joblib\parallel.py", line 1918, in __call__
    return output if self.return_generator else list(output)
  File "C:\Users\yoges\AppData\Local\Programs\Python\Python312\Lib\site-packages\joblib\parallel.py", line 1847, in _get_sequential_output
    res = func(*args, **kwargs)
  File "C:\Users\yoges\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\utils\parallel.py", line 136, in __call__
    return self.function(*args, **kwargs)
  File "C:\Users\yoges\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\model_selection\_validation.py", line 876, in _fit_and_score
    estimator = estimator.set_params(**clone(parameters, safe=False))
  File "C:\Users\yoges\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\base.py", line 279, in set_params
    raise ValueError(
ValueError: Invalid parameter 'normalize' for estimator LinearRegression(). Valid parameters are: ['copy_X', 'fit_intercept', 'n_jobs', 'positive'].
def find_best_model_using(x,y):
    algos={
        'linear_regression':{
            'model':LinearRegression(),
            'params':{
                'normalize':[True,False]
                }
            },
        'lasso':{
            'model':Lasso(),
            'params':{
                'alpha':[1,2],
                'selection':['random','cyclic']
                }
            },
         'decision_tree':{
            'model':DecisionTreeRegressor(),
            'params':{
                'criterion':['mse','friedman_mse'],
                'splitter':['best','random']
                }
            }
        }
    scores=[]
    cv = ShuffleSplit(n_splits=5, test_size=0.2,random_state=0)
    for algo_name,config in algos.items():
        gs = GridSearchCV(config['model'], config['params'],cv=cv, return_train_score =False)
        gs.fit(x,y)
        scores.append({
            'model': algo_name,
            'best_score': gs.best_score_,
            'best_params':gs.best_params_
            })
    return pd.DataFrame(scores,columns=['model','best_score','best_params'])
KeyboardInterrupt
def find_best_model_using(x,y):
    algos={
        'linear_regression':{
            'model':LinearRegression(),
            'params':{
                'normalize':[True,False]
                }
            },
        'lasso':{
            'model':Lasso(),
            'params':{
                'alpha':[1,2],
                'selection':['random','cyclic']
                }
            },
         'decision_tree':{
            'model':DecisionTreeRegressor(),
            'params':{
                'criterion':['mse','friedman_mse'],
                'splitter':['best','random']
                }
            }
        }
    scores=[]
    cv = ShuffleSplit(n_splits=5, test_size=0.2,random_state=0)
    for algo_name,config in algos.items():
        gs = GridSearchCV(config['model'], config['params'],cv=cv, return_train_score =False)
        gs.fit(x,y)
        scores.append({
            'model': algo_name,
            'best_score': gs.best_score_,
            'best_params':gs.best_params_
            })
    return pd.DataFrame(scores,columns=['model','best_score','best_params'])

find_best_model_using(x,y)
Traceback (most recent call last):
  File "<pyshell#274>", line 1, in <module>
    find_best_model_using(x,y)
  File "<pyshell#273>", line 28, in find_best_model_using
    gs.fit(x,y)
  File "C:\Users\yoges\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\base.py", line 1473, in wrapper
    return fit_method(estimator, *args, **kwargs)
  File "C:\Users\yoges\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\model_selection\_search.py", line 1019, in fit
    self._run_search(evaluate_candidates)
  File "C:\Users\yoges\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\model_selection\_search.py", line 1573, in _run_search
    evaluate_candidates(ParameterGrid(self.param_grid))
  File "C:\Users\yoges\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\model_selection\_search.py", line 965, in evaluate_candidates
    out = parallel(
  File "C:\Users\yoges\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\utils\parallel.py", line 74, in __call__
    return super().__call__(iterable_with_config)
  File "C:\Users\yoges\AppData\Local\Programs\Python\Python312\Lib\site-packages\joblib\parallel.py", line 1918, in __call__
    return output if self.return_generator else list(output)
  File "C:\Users\yoges\AppData\Local\Programs\Python\Python312\Lib\site-packages\joblib\parallel.py", line 1847, in _get_sequential_output
    res = func(*args, **kwargs)
  File "C:\Users\yoges\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\utils\parallel.py", line 136, in __call__
    return self.function(*args, **kwargs)
  File "C:\Users\yoges\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\model_selection\_validation.py", line 876, in _fit_and_score
    estimator = estimator.set_params(**clone(parameters, safe=False))
  File "C:\Users\yoges\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\base.py", line 279, in set_params
    raise ValueError(
ValueError: Invalid parameter 'normalize' for estimator LinearRegression(). Valid parameters are: ['copy_X', 'fit_intercept', 'n_jobs', 'positive'].


def predict_price(location,sqft,bath,bhk):
    loc_index =np.where(x.columns==location)[0][0]

    
def predict_price(location,sqft,bath,BHK):
    loc_index =np.where(x.columns==location)[0][0]
    x =np.zeros(len(x.columns))
    x[0]= sqft
    x[1]= bath
    x[2]= BHK
    if loc_index >=0:
        x[loc_index] =1
    return lr_crf.predict([x])[0]

predict_price('1st Phase JP Nagar',1000,2,2)
Traceback (most recent call last):
  File "<pyshell#289>", line 1, in <module>
    predict_price('1st Phase JP Nagar',1000,2,2)
  File "<pyshell#288>", line 2, in predict_price
    loc_index =np.where(x.columns==location)[0][0]
UnboundLocalError: cannot access local variable 'x' where it is not associated with a value
def predict_price(x,location,sqft,bath,BHK):
    loc_index =np.where(x.columns==location)[0][0]
    x =np.zeros(len(x.columns))
    x[0]= sqft
    x[1]= bath
    x[2]= BHK
    if loc_index >=0:
        x[loc_index] =1
    return lr_crf.predict([x])[0]

predict_price(x,'1st Phase JP Nagar',1000,2,2)

Warning (from warnings module):
  File "C:\Users\yoges\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\base.py", line 493
    warnings.warn(
UserWarning: X does not have valid feature names, but LinearRegression was fitted with feature names
np.float64(83.4990467719011)


import pickel
Traceback (most recent call last):
  File "<pyshell#294>", line 1, in <module>
    import pickel
ModuleNotFoundError: No module named 'pickel'
import pickle
with open('C:\\Users\\yoges\\Downloads\\banglore_home_price_model.pickel','wb')as f:
...     pickle.dump(lr_clf,f)
... 
...     
Traceback (most recent call last):
  File "<pyshell#298>", line 2, in <module>
    pickle.dump(lr_clf,f)
NameError: name 'lr_clf' is not defined. Did you mean: 'lr_crf'?
>>> with open('C:\\Users\\yoges\\Downloads\\banglore_home_price_model.pickel','wb')as f:
...     pickle.dump(lr_crf,f)
... 
...     
>>> 
>>> import json
>>> colums = {
...     'data_columns':[col.lower() for col in x.columns]
...     }
>>> with open("C:\\Users\\yoges\\Downloads\\columns.json","w") as f:
...     f.write(json.dumps(columns))
... 
...     
Traceback (most recent call last):
  File "<pyshell#308>", line 2, in <module>
    f.write(json.dumps(columns))
NameError: name 'columns' is not defined. Did you mean: 'colums'?
>>> with open("C:\\Users\\yoges\\Downloads\\columns.json","w") as f:
...     f.write(json.dumps(colums))
... 
...     
4014
>>> 
>>> 
