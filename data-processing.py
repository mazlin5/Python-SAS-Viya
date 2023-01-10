# now that you're connected to a cas server - pull some data
tbl = conn.read_csv('https://raw.githubusercontent.com/'
                      'sassoftware/sas-viya-programming/master/data/cars.csv',
                   casout='cars2')

#use the familiar pandas.DataFrame API, but use it on data that is far too large for pandas to handle. Here are a few simple examples.
#conn.loadactionset('percentile')

tbl[['MSRP', 'Invoice']].describe(percentiles=[0.3, 0.7])