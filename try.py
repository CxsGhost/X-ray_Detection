
workdataDF.createOrReplaceTempView( "workdata")
callrecordDF.createOrReplaceTempView( "calldata")

val breakdownArea = spark.sql("CREATE TABLE faultarea AS SELECT province ,city ,address ,fault_1 ,fault_2 ,fault_type ,acs_way ,COUNT(*) AS num FROM workdata  GROUP BY province,city,address,fault_1,fault_2,fault_type,acs_way")
val servicePerformance = spark.sql("CREATE TABLE efficiency AS SELECT total.province ,CONCAT(total.date,'-01') AS date ,COUNT(*) AS num ,COUNT(DISTINCT total.exp_empid) AS exp_num ,COUNT(*)/COUNT(DISTINCT total.exp_empid) AS effic FROM( SELECT province ,SUBSTR(date,1,7) AS date ,exp_empid FROM workdata ) AS total GROUP BY total.province,total.date ORDER BY total.province,total.date DESC")

workdataDF.coalesce(1).write.csv("wd")


import org.apache.spark.SparkConf
import org.apache.spark.ml.linalg.Vectors
import org.apache.spark.sql.SparkSession
import org.apache.spark.ml.clustering.KMeans
case class callrecordClass(province:String, address:String, fault_1:String, fault_2:String, fault_type:String, acs_way:String, num:String)
case class workdataClass(province:String, date:String, num:String, exp_num:String, effic:String)
import spark.implicits._
val BreakDownArea = spark.sparkContext.textFile("/data/bda.csv").map(_.split(",")).map(arr=>callrecordClass(arr(1) ,arr(2), arr(3), arr(4), arr(5), arr(6), arr(7))).toDF()
val ServicePerformance = spark.sparkContext.textFile("/data/nengxioa.csv").map(_.split(",")).map(arr => workdataClass(arr(1), arr(2), arr(4), arr(5), arr(6))).toDF()


write.format("jbdc").option("url", "jdbc:mysql://120.46.150.60:3306/anli31?useSSL=false").option("dbtable", "anli31.breakdownarea").option("@Xgl0626").save()
write.format("jbdc").option("url", "jdbc:mysql://120.46.150.60:3306/anli31?useSSL=false").option("dbtable", "anli31.serviceperformance").option("@Xgl0626").save()
