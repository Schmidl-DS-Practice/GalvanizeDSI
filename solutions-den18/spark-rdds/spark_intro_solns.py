import pyspark as ps    # for the pyspark suite
import json             # for parsing json formatted data
import csv              # for the split_csvstring function from Part 3.2.2
try:                    # Python 3 compatibility
    from StringIO import StringIO
except ImportError:
    from io import StringIO
import os               # for accessing env variables for AWS credentials


# Part 2.1
def parse_json_first_key_pair(json_string):
    """Returns the first (key,value) pair from a json encoded dictionary.

    Parameters
    ----------
    json_string (str): a string encoding a json dictionary

    Returns
    -------
    [k,v]: the first key (k) and value (v) pair in the input json dict

    Example
    -------
    >>> parse_json_first_key_pair(u'{"Jane": "2"}')
    (u'Jane', 2)
    """
    json_obj = json.loads(json_string)
    first_k = next(iter(json_obj))  # just returns the first value in the iterable
    return(first_k, int(json_obj[first_k]))   # also transform value (string) to integer value


# Part 3.2.2
def split_csvstring(input_string):
    """Parse a csv-like line and break the values into a list.

    Parameters
    ----------
    input_string (str): a csv-like string to work on

    Returns
    -------
    list : the list of the values

    Example
    -------
    >>> split_csvstring(u'a,b,0.7,"Oct 7, 2016",42,')
    ['a', 'b', '0.7', 'Oct 7, 2016', '42', '']
    """

    # we create a StringIO handler
    fio = StringIO(input_string)
    # and feed that into the csv.reader library which is (probably) the best way to parse those strings
    reader = csv.reader(fio, quotechar='"', delimiter=',',quoting=csv.QUOTE_ALL, skipinitialspace=True)

    # obtains the first line of the reader (which should be the only line)
    row_values = next(reader)

    return row_values


# Part 3.2.4
def make_row_dict(row_values, col_names, keep_keys_set):
    """Extract specific columns from a row (string) and operates some specific transformations on the values.

    Parameters
    ----------
    row_values (list): a list of the values of a given row
    col_names (list): a list of all the columns in row_string ordered as in row_string
    keep_keys_dict (set): the set of the columns we keep (anything else is discarded)

    Returns
    -------
    dict : a dictionary containing the key,value pairs we chose to keep

    Example
    -------
    >>> make_row_dict(['2012', '4', 'AA', '12478', '12892', '-4.00', '0.00', '-21.00', '0.00', '0.00', ''],\
    ['YEAR', 'MONTH', 'UNIQUE_CARRIER', 'ORIGIN_AIRPORT_ID', 'DEST_AIRPORT_ID', 'DEP_DELAY', 'DEP_DELAY_NEW', 'ARR_DELAY', 'ARR_DELAY_NEW', 'CANCELLED', ''],\
    {'DEST_AIRPORT_ID', 'ORIGIN_AIRPORT_ID', 'DEP_DELAY', 'ARR_DELAY'})
    {'ARR_DELAY': -17.0, 'DEST_AIRPORT_ID': '12892', 'DEP_DELAY': -4.0, 'ORIGIN_AIRPORT_ID': '12478'}
    """
    row_dict = {}

    # filtering values
    for k, v in zip(col_names, row_values):
        if k in keep_keys_set:
            row_dict[k] = v
        if k == 'CANCELLED':
            cancelled = v != '0.00'

    # operations
    row_dict['DEP_DELAY'] = float(row_dict['DEP_DELAY']) if row_dict['DEP_DELAY'] else 0.0
    row_dict['ARR_DELAY'] = float(row_dict['ARR_DELAY']) if row_dict['ARR_DELAY'] else 0.0
    row_dict['ARR_DELAY'] = row_dict['ARR_DELAY'] - row_dict['DEP_DELAY']
    if cancelled:
        row_dict['DEP_DELAY'] += 300

    return row_dict


# Part 3.2.4 - generic variant
# call that with dict_rdd_generic = only_data_rdd.map(lambda row: make_row_dict_generic(row, column_names))
# within the jupyter notebook
def make_row_dict_generic(row_values, col_names, **kwargs):
    """Remove all single quotes, double quotes, and trailing comma from a line.

    Parameters
    ----------
    row_values (list): a list of the values of a given row
    col_names (list): a list of all the columns in row_string ordered as in row_string
    **kwargs: see below

    Keyword Arguments
    -----------------
    col_types:    a dictionary indicating the type of each column
    default_type: the default type for the remaining columns
    col_ops:      a list of the operations one should apply on each column in a [col, lambda] pair
    keep_cols:    the set of columns to keep

    Returns
    -------
    dict : a dictionary containing the key,value pairs we chose to keep
    """

    # by default, we use the configuration of the assignment
    col_types = kwargs.get("col_types", {  'DEST_AIRPORT_ID':str,
                                           'ORIGIN_AIRPORT_ID':str,
                                           'DEP_DELAY':float,
                                           'ARR_DELAY':float })

    # by default, we use the configuration of the assignment
    default_type = kwargs.get("default_type", str)

    # by default, we use the configuration of the assignment
    col_ops = kwargs.get("col_ops", [[ 'ARR_DELAY', (lambda row : row['ARR_DELAY'] - row['DEP_DELAY']) ],
                                     [ 'DEP_DELAY', (lambda row : row['DEP_DELAY'] + (300 if (row['CANCELLED'] != '0.00') else 0.0)) ]] )

    # by default, we use the configuration of the assignment
    keep_cols = kwargs.get("keep_cols", {  'DEST_AIRPORT_ID', 'ORIGIN_AIRPORT_ID','DEP_DELAY','ARR_DELAY'  })

    row_dict = dict()

    # transforming column types
    for k, v in zip(col_names, row_values):
        if col_types.has_key(k):
            # extra credit: do you get what's happening here ?
            row_dict[k] = col_types.get(k)(v)
        else:
            # extra credit: do you get what's happening here ?
            row_dict[k] = default_type(v)

    # applying special operations
    for op_pair in col_ops:
        # extra credit: do you get what's happening here ?
        row_dict[op_pair[0]] = op_pair[1](row_dict)

    # selecting specified columns
    for key in row_dict.keys():
        if key not in keep_cols:
            row_dict.pop(key)

    return row_dict


# Part 3.3.1
def transformation_pipeline(input_raw_rdd):
    """Processes the airline RDD to obtain answers to the 4 questions in assignment.

    Parameters
    ----------
    input_raw_rdd (spark RDD): the RDD obtained from 's3a://mortar-example-data/airline-data'

    Returns
    -------
    tuple : answers to questions Q1, Q2, Q3, Q4
    """
    # applying the split_csvstring() function to all rows in RDD
    clean_row_rdd = input_raw_rdd.map(split_csvstring)

    # get first line of RDD
    first_row = clean_row_rdd.first()

    # filter lines that are identical to the first line
    only_data_rdd = clean_row_rdd.filter(lambda row: row != first_row)

    # obtain column names
    column_names = first_row

    dict_keys = {'DEST_AIRPORT_ID', 'ORIGIN_AIRPORT_ID', 'DEP_DELAY', 'ARR_DELAY'}

    # if you want to test that function run the following line
    #make_row_dict(u'2012,4,AA,12478,12892,-4.00,0.00,-21.00,0.00,0.00', column_names, dict_keys)

    dict_rdd = only_data_rdd.map(lambda row: make_row_dict(row, column_names, dict_keys))
    #dict_rdd.take(2)

    arrival_rdd = dict_rdd.map(lambda rd: (rd['DEST_AIRPORT_ID'], rd['ARR_DELAY']))
    departure_rdd = dict_rdd.map(lambda rd: (rd['ORIGIN_AIRPORT_ID'], rd['DEP_DELAY']))

    # we define a mean function to feed into groupByKey()
    def rdd_group_mean(value_group):
        # transform groups produced by groupByKey into lists of values
        values = list(value_group)
        # so that we can compute their mean
        return sum(values) / len(values)

    average_departure_delays = departure_rdd.groupByKey().mapValues(lambda value_group: rdd_group_mean(value_group))
    average_arrival_delays = arrival_rdd.groupByKey().mapValues(lambda value_group: rdd_group_mean(value_group))

    #average_departure_delay = average_departure_delay.setName('avg_dep_delay').cache()
    #average_arrival_delay = average_arrival_delay.setName('avg_arr_delay').cache()

    # Q1: What are the top 10 departing airports that have the lowest average delay?
    resultQ1 = average_departure_delays.sortBy(lambda kvtuple: kvtuple[1], ascending=False).take(10)

    # Q2: What are the top 10 departing airports that have the highest average delay?
    resultQ2 = average_departure_delays.sortBy(lambda kvtuple: kvtuple[1], ascending=True).take(10)

    # Q3: What are the top 10 arriving airports that have the lowest average delay?
    resultQ3 = average_arrival_delays.sortBy(lambda kvtuple: kvtuple[1], ascending=False).take(10)

    # Q4: What are the top 10 arriving airports that have the highest average delay?
    resultQ4 = average_arrival_delays.sortBy(lambda kvtuple: kvtuple[1], ascending=True).take(10)

    return(resultQ1, resultQ2, resultQ3, resultQ4)



if __name__ == "__main__":
    # we try to create a SparkSession to work locally on all cpus available
    spark = ps.sql.SparkSession.builder \
            .master("local[4]") \
            .appName("individual") \
            .getOrCreate()

    # Grab sparkContext from the SparkSession object
    sc = spark.sparkContext
    sc.setLogLevel('ERROR')

    # link to the s3 repository from Part 3
    link = 's3a://mortar-example-data/airline-data'
    airline_rdd = sc.textFile(link)

    # launching the full pipeline we have designed in Part 4
    dataq1, dataq2, dataq3, dataq4 = transformation_pipeline(airline_rdd)

    print("Top 10 departing airports that have the lowest average delay:{}".format(dataq1))

    print("Top 10 departing airports that have the highest average delay:{}".format(dataq2))

    print("Top 10 arriving airports that have the lowest average delay:{}".format(dataq3))

    print("Top 10 arriving airports that have the highest average delay:{}".format(dataq4))
