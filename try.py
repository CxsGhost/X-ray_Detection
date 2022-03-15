
workdataDF.createOrReplaceTempView( "workdata")
callrecordDF.createOrReplaceTempView( "calldata")

val breakdownArea = spark.sql("select province , address, fault_1, fault_2, fault_type, acs_way, count(*) as num from workdata group by province, address, fault_1, fault_2, fault_type, acs_way")

val servicePerformance = spark.sql("select total.province, concat(total.date, '-01') as date , count(*) as num, count (distinct total.exp_empid) as exp_num, count(*) / count(distinct total.exp_empid) as effic from ( select province, substr(date, 1, 7) as date , exp_empid, from workdata) as total group by total.province, total.date order by total.province, total.date desc ")

import org.apache.spark.SparkConf
import org.apache.spark.ml.linalg.Vectors
import org.apache.spark.sql.SparkSession
import org.apache.spark.ml.clustering.KMeans
case class detail(features: org.apache.spark.ml.linalg.Vector)
case class callrecordClass(calling:String,called:String,call_type:String,start_time:String)
case class workdataClass(province:String, city:String,code:String,acc_number:String, tel:String, date:String,rep_disoe:Int,overtime:Int, receipt:Int,descr:String,exp_empid:String,fault_1:String,fault_2:String,fault_type:String, acs_way:String,address:String)
import spark.implicits._
val callrecordDF = spark.sparkContext.textFile("/data/callrecord.txt").map(_.split("\t")).map(arr=>callrecordClass(arr(1),arr(2), arr(3), arr(4))).toDF()
val workdataDF = spark.sparkContext.textFile("/data/workdata.txt").map(_.split("\t")).map(arr => workdataClass(arr(1), arr(2), arr(3), arr(4), arr(5), arr(6), arr(7).toInt, arr(8).toInt, arr(9).toInt, arr(10), arr(11), arr(12), arr(13), arr(14), arr(15), arr(16))).toDF()
