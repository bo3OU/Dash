from pyspark.sql import SparkSession
import pandas as pd
import timeago
from datetime import datetime as dt
from cassandra.cluster import Cluster
import dash_html_components as html
import dash_table_experiments as dte


cluster = Cluster(['127.0.0.1'])
session = cluster.connect('projet')


#loads the database to the spark memoty
spark = SparkSession.builder.getOrCreate()
spark.conf.set("spark.driver.allowMultipleContexts","true")
dfs =spark.read.format("org.apache.spark.sql.cassandra").options(table="autorisations", keyspace="projet").load()
df = dfs.createOrReplaceTempView("autorisations")

def get_Data():
    dftmp = spark.sql("select aut_code as Aut_Code, aut_bill_amou_f006 as Montant,  aut_acqr_inst_coun_code_f019 as Devise, aut_prim_acct_numb_f002 as PAN, aut_requ_syst_time as Date, aut_card_accp_name_loc_f043 as Commercant, aut_resp_code_f039 as Reponse , ban_corp_name as Bank from autorisations where classe = 1  limit 20 ") # TODO where VALIDE = FALSE --- ALLOW FILTERING
    return dftmp.toPandas()
    
def get_violin():
    return spark.sql("select  aut_code,M1,M2,M3,M4,M5,M6,M7,M8,M9,M10, classe, cast(aut_bill_amou_f006 as int),date_format(CAST(UNIX_TIMESTAMP(aut_requ_syst_time, 'dd/MM/yyyy HH:mm:ss') AS TIMESTAMP),'yyyy-MM-dd') as date   from autorisations where classe = 1 limit 2000").toPandas() # where date = # ALLOW FILTERING
    
def get_Graph():
    dftmp = spark.sql("select count(aut_code) as count, operating_environment as oe from autorisations group by operating_environment")
    return dftmp.toPandas()

def getLastAuts(autCode):
    dftmp = spark.sql('''
    select aut_card_accp_country as Country, 
    date_format(CAST(UNIX_TIMESTAMP(aut_requ_syst_time, "dd/MM/yyyy HH:mm:ss") AS TIMESTAMP),"yyyy-MM-dd") as Date,
    "a" as Time_ago 
    from autorisations 
    where porteur_id = (select porteur_id  from autorisations where aut_code = ''' + str(autCode) + ''')  
    order by date_format(CAST(UNIX_TIMESTAMP(aut_requ_syst_time, "dd/MM/yyyy HH:mm:ss") AS TIMESTAMP),"yyyy-MM-dd HH:mm:ss") DESC
    limit 20
    ''')
    dftmp= dftmp.toPandas()
    for index, row in dftmp.iterrows():
        dftmp.set_value(index, 'Time_ago', timeago.format(row.Date.encode('ascii','ignore'),dt.now()))
    return dftmp

def getBehavior(autCode):
    dftmp = spark.sql('''
    AVG(select) aut_bill_amou_f006 as montant, 
    date_format(CAST(UNIX_TIMESTAMP(aut_requ_syst_time, "dd/MM/yyyy HH:mm:ss") AS TIMESTAMP),"MM") as day, 
    from autorisations 
    where porteur_id = (select porteur_id  from autorisations where aut_code = ''' + str(autCode) + ''')  
    order by day
    ''')
    print(dftmp)
    return dftmp.toPandas()

def getPercentageChange():
    dfcla = spark.sql("""
    select  
    count(*) as counter,
    concat(date_format(CAST(UNIX_TIMESTAMP(aut_requ_syst_time, "dd/MM/yyyy HH:mm:ss") AS TIMESTAMP),"yyyy") , '-',
    CAST(bround(date_format(CAST(UNIX_TIMESTAMP(aut_requ_syst_time, "dd/MM/yyyy HH:mm:ss") AS TIMESTAMP),"MM")/3,0) as string)) as annee,
    classe
    from autorisations
    group by annee,classe
    order by annee DESC
    limit 23
    """)
    dfcla = dfcla.toPandas()
    dfcla['counter'] = dfcla.counter*((dfcla.classe*99) +1)
    return dfcla.iloc[::-1]

def getPercentCountries():
    dfCountries = pd.read_csv('https://raw.githubusercontent.com/lukes/ISO-3166-Countries-with-Regional-Codes/master/all/all.csv')
    dfCountries = dfCountries.reindex(columns=['alpha-2','alpha-3','name'])
    dftmp = spark.sql('''
    select aut_card_accp_country as country, ''' + 
#     '''(count(aut_card_accp_country) * 100 / (select count(*) from autorisations where classe = 1)) as percent     ''' + 
    'count(*) as percent' + 
    ''' from autorisations 
    where classe = 1
    group by aut_card_accp_country
    ''') # add VALIDE to both queries
    dftmp = dftmp.toPandas()
    dfCountries.columns = ['country', 'alpha-3', 'name']
    s1 = pd.merge(dfCountries, dftmp, how='left', on=['country'])
#     s1 = s1.dropna(subset = ['percent'])
    s1 = s1.fillna(0)
    return s1


def generate_table(dataframe, max_rows=10):
#     return html.Table(
#         # Header
#         [html.Tr([html.Th(col) for col in dataframe.columns])] +

#         # Body
#         [html.Tr([
#             html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
#         ]) for i in range(min(len(dataframe), max_rows))]
#     )
    return    dte.DataTable(
        rows=dataframe.to_dict('records'),
        row_selectable=False,
        columns =  dataframe.columns,
        filterable=False,
        sortable=False,
        editable=False,
        selected_row_indices=[],
    )

def getPaymentPercent():
    dftmp = spark.sql('''
    AVG(select) aut_bill_amou_f006 as montant, 
    date_format(CAST(UNIX_TIMESTAMP(aut_requ_syst_time, "dd/MM/yyyy HH:mm:ss") AS TIMESTAMP),"MM") as day, 
    from autorisations 
    where porteur_id = (select porteur_id  from autorisations where aut_code = ''' + str(autCode) + ''')  
    order by day
    ''')
    print(dftmp)
    return dftmp.toPandas()


def getX(df):
    return df[df.columns[1]].values

def getY(df):
    return df[df.columns[0]].values


def gen_rows(length):
    return [
        {'a': 'AA', 'b': i} for i in range(length)
    ]
