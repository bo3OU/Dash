df = spark.sql(
    "SELECT date_format(CAST(UNIX_TIMESTAMP(datetime, 'dd/MM/yyyy HH:mm:ss') AS TIMESTAMP),'dd,MM,yyyy ///HH+mm=>ss') "
    "AS newdate "
    "from test"
);
