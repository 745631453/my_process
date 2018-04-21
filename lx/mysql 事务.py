mysql 事务，
原子性 要么都做要么都不做，如果发生错误就回滚到开始前状态
一致性 

隔离性
持久性
import pymysql

pb = pymysql.connect()

a = pb.cursor()
try:
	a.excute()
	pb.commint
except:
	pb.rollback()

pb.close

redis
1.
	启动redis-server &
	redis-cli
2.修改密码
vim myredis.conf 找到requirepass 后面数字修改了

3 访问指定ip
redis-cli -h (ip) -p(端口)
输入密码auth +密码

 redis五大类型 string hash list set zset
 	keys * 表示一共多少键
string：
	创建多个——		mset o 2 q 3 表示创建多个
	创建—— 			set p 1 	 设置p的值为1
	获取—— 			get p  		 获取p的值
	改变值递增——	incr p 		 整数依次递增并且修改值 默认值是0
		  递减		decr            递减
	增加字符——    	append	p 1	 在p的值后加数字
	字符串切片		getrange p 取值区间

hash：
	创建——     		hset key键值 字段（属性） 值
	获取全部—— 		hgetall key键值 //某一个——hget key 字段
	获取key的属性——	hkeys key键值
	获取key的值——	hvals key键值
	删除——			hdel key键值 属性【属性】可以写多个

list：
	创建—— 		rpush key 值 lpush/rpush 表示左插入和右插入
	查看——		lrange
	删除——		lopo/rpop key 左右删除 

set：
	创建添加——     sadd key 值
	查看—— 		smembers key 看的内容/scard 查看个数
	删除—— 		spop key  表示随机删除

zset；
	zadd key 值 成员
	zrang key 0-1 自动从小到大列出来/zrevrang 从大到小