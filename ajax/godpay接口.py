

bopinshangcheng.com
http://120.79.181.233:80
17665671323


测试服务器：
http://godpay.sensorallin.io/
47.74.230.207:80


钱包地址：
0x8A20D7FDC731fd2a311782c4f106ad31Ad2ee6F1

# 登录
http://127.0.0.1:8000/login
从前端获取数据：
	手机号:uphone
	密码：password
	外网ip：ip_out
	内网ip:ip_in
	登录设备：equipment

# 注册
http://127.0.0.1:8000/register
从前端获取数据：
	手机号码：uphone
	昵称：username
	密码：password1
	确认输入密码：password2
	短信验证码：code
	推荐人：referee
	外网ip：ip_out
	内网ip：ip_in


# 发送短信验证码
http://127.0.0.1:8000/send_sms     
从前端获取手机号码：uphone


# 忘记支付密码
http://127.0.0.1:8000/forget_password
从前端获取数据：
	手机号码：uphone
	验证码：code
	输入密码：password_login
	确认密码：confirm_password



# 修改登陆密码
http://127.0.0.1:8000/modify_login
从前端获取数据：
	手机号码：uphone
	新密码：new_password
	确认密码：confirm_password
	验证码：code

# 修改支付密码
http://127.0.0.1:8000/modify_payment
从前端获取数据：
	手机号码：uphone
	新密码：new_password_payment
	确认密码：confirm_password_payment
	验证码：code


# 绑定钱包地址
http://127.0.0.1:8000/binding_wallt
从前端获取数据：
	用户uid：uid
	钱包地址：wallt_address
	确认钱包地址：confirm_wallt_address
	输入密码：payment_password





###############################################





# 推荐人二维码
http://127.0.0.1:8000/get_grcode 
从前端获取手机号码：uphone   
扫描二维码后得到url:http://127.0.0.1:8000/register/uphone=13867891234
携带推荐人手机号码



# 产品信息页面
http://127.0.0.1:8000/index_views
# 从前端获取数据：uid（不传）
返回数据：
    
请求方式：get
返回数据：
认权产品：power_product
认权产品名称：power_product_name
认权产品等级：power_product_grade
产品id：product_id
耳机的产品id为5


众筹产品：crowdfunding_product
众筹产品名称：crowdfunding_product_name
众筹产品等级：crowdfunding_product_grade
需求：需要在认权产品展示的时候，将产品ID为5的认权产品跳转到商城的产品详情页面


# 认权产品详情页
http：//127.0.0.1:8000/product_details
从前端获取数据：power_product_grade
返回数据：
	认权产品：power_product
	认权产品名称：power_product_name
	认权产品等级：power_product_grade
	认权产品周期：power_product_zhouqi
	认权产品原始值：power_product_quantity
	认权产品详情：power_product_details


# 众筹产品详情页
http://127.0.0.1:8000/crowdfunding_details
从前端获取数据：crowdfunding_product_grade
返回前端：
	众筹产品名称：crowdfunding_product_name
	众筹产品等级：crowdfunding_product_grade
	众筹产品周期：crowdfunding_product_zhouqi
	众筹产品最少值：crowdfunding_product_quantity
	众筹产品中文名：chain_name
	众筹产品英文名：engish_name
	众筹产品别名：alias
	众筹产品国籍：nationality
	众筹产品出生日期：birthday
	众筹产品职业：work



6. 退出登录











# 充值二维码
http://127.0.0.1:8000/company_address/uid
从前端获取数据：uid
扫描二维码后得到钱包地址



用户充值接口
请求方式：POST
路径：user_recharge_emt
请求参数：uid
返回：{'uid': uid, 'status_end': 'ok'}




# 个人用户中心基础信息
http://127.0.0.1:8000/user_details
从前端获取数据：uid
返回数据：
	昵称：username
	等级：grade
	钱包地址：wallt_address
	剩余可购买众筹次数:surplus_buy
	推荐购买认权人数比例：power_number
	推荐购买众筹人数比例：crowdfunding_number
	资产：assets
	总量：total_quantity
	总倍化：total_multiple
	当天加速:PushBetweenAll
	待返：pending_return_tatal
	已返：returned_tatal
	可用：can_use_quantity
	可提：can_extract_tatal






 # 推广情况：
post
http://127.0.0.1:8000/spread
从前端获取数据：uid
返回数据：
	昵称：username
	推荐人昵称：referee_username
	直推人数：subordinate_total
	间推人数：lowersubordinate_total
	总倍化倍数：total_multiple
	总加速速率：PushBetweenAll


1，认权购买：								
http://127.0.0.1:8000/order/
认权购买：路由：order
Post请求：
order_product (v1,v2,v3)  字符串类型
key_password       字符串类型
uid                字符串类型

返回：
用户ID：user_id
手机号码：uphone
订单号：serial_number
下单时间：order_time
下单产品：order_product
产品标识：operation，成功为“OK”
购买数量：order_quantity
倍化的数量：Speed_upRate



2，众筹购买：							
http://127.0.0.1:8000/orderzhong/
众筹文档接口：post 路由：orderzhong
order_quantity    购买数量   整形
order_product    购买的周期   字符串类型
 uid                字符串类型
key_password      密码   字符串类型

返回：
用户ID：user_id
用户手机号码：uphone
用户订单号：serial_number
用户下单时间：order_time
用户购买周期：order_product
购买是否成功：operation 成功为“OK”
购买数量：order_quantity
众筹获得利息：order_quantity_lixi
产品名称：order_product_name
状态：operation
图片：image_url

5，提现
http://127.0.0.1:8000/cash_withdrawal/
post：
数量：order_quantity
支付密码：key_password
用户id：user_id
返回：
用户ID：user_id
手机号码：uphone        
流水号：serial_number
提现时间：order_time
EMT提现钱包地址：CashWithdrawal_wallt_address        
提现购买产品数量：order_quantity
操作标识状态：operation


6，提现订单
http://127.0.0.1:8000/tixian_check/
get:
返回：
订单号：'serial_number', 
提现钱包地址：'CashWithdrawal_wallt_address', 
提现数量：'order_quantity', 
下单时间：'order_time',
状态：'operation'





3,认权订单查询
http://127.0.0.1:8000/renquan_check/
get:
返回：
订单号：'serial_number',   
产品名称：'order_product',
产品数量:'order_quantity',
下单时间：'order_time'
周期：'zhouqi'
图片：'image_url'
状态：'operation'

4，众筹订单查询：
http://127.0.0.1:8000/zhongchou_check/
get：
返回：
订单号：'serial_number', 
众筹周期：'order_product', 
众筹数量：'order_quantity', 
众筹时间：'order_time'，




#用户通过代理商充值
路由：User_agent_recharge
请求方式：post
需要参数：
uid    申请者的UID
agent_uphone  代理商手机号码
order_quantity  数量
payment_password  用户的支付密码
返回：
operation="审核中"






#所有的代理商信息显示，充值接口
请求方式:get
路由：agent_display
返回：
代理商手机号码：'agent_uphone'
代理商名称：'agent_name'
代理商子长：'agent_quantity'


展示代理商信息：看过滤是否生效
路由:

文档：get
information_agent/+用户手机号码
返回：agent_name  代理商名称
     agent_uphone 代理商手机号码
  agent_quantity   代理商可用emt







# 加速明细
http://127.0.0.1:8000/speed_details
从前端获取数据：uid
返回数据：
	直推用户昵称：subordinate_username
	直推用户等级：subordinate_grade
	直推用户购买时间：subordinate_order_time
	直推用户加速：subordinate_rate

	间推用户昵称：lowersubordinate_username
	间推用户等级：lowersubordinate_grade
	间推用户购买时间：lowersubordinate_order_time
	间推用户加速：lowersubordinate_rate







# 倍化明细
http://127.0.0.1:8000/ploidy_details
从前端获取数据：uid
返回数据：
	用户倍化倍数：power_multiple
	用户购买时间：orders_time
	用户购买第几阶段：user_stage
	用户购买认权等级：user_grade

	下级购买认权用户昵称：subordinate_username
	下级购买认权用户购买时间：subordinate_order_time
	下级购买认权用户购买第几阶段：subordinate_stage
	下级购买认权用户购买认权：等级subordinate_grade
	下级具体购买认权产品名称：subordinate_product

	下级购买众筹用户昵称：crowdfunding_username
	下级购买众筹用户购买时间：crowdfunding_time
	下级购买众筹用户购买周期：crowdfunding_grade
	下级具体购买众筹产品名称：crowdfunding_product

# 需要的数据如下：

data:{
	默认倍化情况:{},
	认权推荐:[{},{},{},....],
	众筹推荐:[{},{},{},....],
}




7，充值订单
------------------------------------------------------------------------------------------------------------
用户自己充值的订单
# 充值订单查询
请求方式：get
请求路径：chongzhi_check/+uid
返回：
订单号：'serial_number', 
钱包地址：'CashWithdrawal_wallt_address', 
充值数量：'order_quantity', 
下单时间：'order_time',
状态：'operation'


# 用户向代理商充值订单表显示
# 请求方式：get
# 请求路径：agent_chongzhi_check/+uid
# 返回：
# 'user_id','user_name','user_uphone','serial_number','agent_uphone','order_time','order_quantity','operation'

用户向代理商充值时的订单显示：/user_agent_chongzhi_check

请求方式：get
请求数据：在末尾传用户的uid
返回的数据：
    "user_id": "20190125120223458320TT440300",
    "uphone": "13530777957",
    "serial_number": "2019020911435520190125120223458320TT440300",
    "order_time": "2019-02-09 19:43:55.988059",
    "CashWithdrawal_wallt_address": "0x723DCCd26522409D11172cA634A1ad38F8EDD94A",
    "order_quantity": "2000.00",
    "operation": "充值成功"




# 商品详情页
http://127.0.0.1:8000/product_details
POST请求：
从前端获取数据：
    商品uid：product_name_uid
    示例：{"product_name_uid":"1"}
返回数据：
    商品名称：product_name
    商品价值：product_price
    商品详情：product_details
    商品图片：product_img（暂时不返回）
    商品详请图：product_img_details（暂时不返回）

    返回数据格式：
    {
        "result": [
            {
                "product_name": "汉服",
                "product_price": 888,
                "product_details": "汉服是中国的传统服装"
            }
        ]
    }



 ---------------------------------------------------------------------------------------------------------
#兑换产品展示页面
#兑换产品显示
路由：exchange_product_display
请求方式:get
返回：
产品名称：product_name
产品的类别：classification
产品SKU：product_id
存储量：count
价格：product_price
产品描述：product_describe
图片保存路径：product_img
销量：Sales_count
状态：status


# 返回用户收货地址——省
http://127.0.0.1:8000/address_province
GET请求：
返回数据：
    省名称：province_name
    省id：province_id

    返回数据格式：
        {
            "result": [
                [
                    "北京市",
                    "天津市",
                    "河北省",
                ],
                [
                    "110000000000",
                    "120000000000",
                    "130000000000"
                ]
            ]
        }

如果传数据不存在，则返回空列表：
      {
        "result": [
            [],
            []
        ]
    }
如果请求方式错误，则返回：error



# 用户收货地址——市
http://127.0.0.1:8000/address_city
POST请求：
从前端获取数据：
    省id：province_id
返回数据：
    市名称：city_name
    市id：city_id

    返回数据格式：
        {
            "result": [
                [
                    "太原市",
                    "大同市",
                    "阳泉市"
                ],
                [
                    "140100000000",
                    "140200000000",
                    "140300000000"
                ]
            ]
        }
如果传数据不存在，则返回空列表：
      {
        "result": [
            [],
            []
        ]
    }
如果请求方式错误，则返回：error

# 用户收货地址——区县
http://127.0.0.1:8000/address_country
POST请求：
从前端获取数据：
    市id：city_id
返回数据：
    市名称：country_name
    市id：country_id

    返回数据格式：
        {
            "result": [
                [
                    "东城区",
                    "西城区",
                    "朝阳区"
                ],
                [
                    "110101000000",
                    "110102000000",
                    "110105000000"
                ]
            ]
        }
如果传数据不存在，则返回空列表：
      {
        "result": [
            [],
            []
        ]
    }
如果请求方式错误，则返回：error



#兑换订单展示
#兑换者所有订单展示
路由：exchange_order_show/+uid
请求方式：get
返回：
订单编号：product_Serial_number
订单状态：status
产品名称：product_name

下单用户uid：user_id

商品数量：total_count

订单总金额：total_amount

运费：freight

下单时候的单价：product_price

物流单号：logistics_number

订单时间：product_order_time

--------------------------------------------------------------------------------------------------




# 用户兑换商品结算确认地址页面
# 此接口用于用户确定兑换时且有收货地址时显示的默认地址
http://127.0.0.0:8000/address_sure
POST请求：
从前端获取数据：
    用户uid：uid
返回数据：
    地址id：address_id
    用户详细地址：address
    收货人：receiver
    收货手机号码：mobile
    是否设置为默认地址：code

    返回数据格式：
        {
            "result": [
                {
                    "code": "yes",
                    "address_id": "10",
                    "mobile": "123456",
                    "receiver": "huhu",
                    "address": "重庆市11111"
                }
            ]
        }
    如果数据不存在，则提示：请添加收货地址

--------------------------------------------------------------------------------------------------


#结算
#兑换产品结算
路由：Settlement_exchange_product
请求：post
请求参数:
支付密码：key_password
产品UID：product_id
用户uid：uid
购买总数：total_count
地址：address

返回：status:"已购买"

--------------------------------------------------------------------------------------------------


# 用户地址管理显示页面
http://127.0.0.1:8000/address_many_show
POST请求：
从前端获取数据：
    用户uid：uid
返回数据：
    地址id：address_id
    用户详细地址：address
    收货人：receiver
    收货手机号码：mobile
    是否设置为默认地址：code（默认状态为no,表示为不设置为默认地址）

    返回数据格式：
        {
            "result": [
                {
                    "address_id": "10",
                    "mobile": "123456",
                    "receiver": "huhu",
                    "address": "重庆市11111",
                    "code": "yes"
                },
                {
                    "address_id": "11",
                    "mobile": "123456",
                    "receiver": "huhu",
                    "address": "重庆市11111",
                    "code": "no"
                }
            ]
        }
    如果数据不存在，则提示：请添加收货地址
如果请求方式错误，则返回：error 








# 删除地址
http://127.0.0.1:8000/address_delete
POST请求：
从前端获取数据：
    用户uid：uid
    地址id：address_id
    是否设置为默认地址：code（默认状态为no,表示为不设置为默认地址）

返回数据格式：
    状态码：staus_code 

如果传输地址id已经删除，则提示：该地址不存在

    返回数据格式：
        {
            "staus_code": "删除成功"
        }
如果请求方式错误，则返回：error 




# 用户收货地址——详细
http://127.0.0.1:8000/address_details
POST请求：
从前端获取数据：
    用户uid：uid
    用户详细地址：address
    收货人：receiver
    收货手机号码：mobile
    是否设置为默认地址：code（默认状态为no,表示为不设置为默认地址）
    地址id：address_id
返回数据：
    状态码：staus_code
    地址id：address_id

    返回数据格式：
        {
            "staus_code": "ok",
            "address_id": "3",
            "code":"yes"
        }
如果请求方式错误，则返回：error 









# 用户修改地址
# 返回需要修改的数据
http://127.0.0.0:8000/address_change
POST请求：
从前端获取数据：
    用户uid：uid
    地址id：address_id

返回数据：
    用户详细地址：address
    收货人：receiver
    收货手机号码：mobile
    是否设置为默认地址：code

    返回数据格式：
        {
            "result": [
                {
                    "address": "重庆市11111",
                    "mobile": "123456",
                    "receiver": "huhu",
                    "code": "yes"
                }
            ]
        }
    如果修改数据不存在，即传递数据错误，则提示：对应地址不存在
    如果传递uid或者address_id为空，则提示：用户uid或者地址id不能不为空
如果请求方式错误，则返回：error 



#分类产品导航条
路由：classified_navigation_display
请求方式：get
返回：
商品品类：classification



--------------------------------------------------------------------------------------------------------------
#导航分类筛选
#分类产品点击归类展示
路由：classification_show/+品类名称
请求方式：get
返回：
产品的名称：product_name
产品的类别：classification
产品SKU：product_id
存储量：count
价格：product_price
产品描述：product_describe
图片保存路径：product_img
销量：Sales_count
状态：status



#价格区间的筛选
#分类产品价格区间筛选
路由：price_range/+低价格/+高价格（类型：数字）
请求方式：get
返回：
产品的名称：product_name
产品的类别：classification
产品SKU：product_id
存储量：count
价格：product_price
产品描述：product_describe
图片保存路径：product_img
销量：Sales_count
状态：status







bopinshangcheng.com
http://120.79.181.233:80
17665671323
111111


测试服务器：
http://godpay.sensorallin.io/
47.74.230.207:80

0x8A20D7FDC731fd2a311782c4f106ad31Ad2ee6F1


13530777957
123456

18675501836
qazqaz


15683399101
123456
###############################################



8、首页缺少实时广告（滚动条的接口：暂缓）、 

后端部分：
1、用户登录验证（状态保持） + 风控：对接 完成时间：周五
# 2、数据库调用：优化（监控服务器的状况）
3、超级管理员后台接口：
未完成部分：
	产品管理：产品的编辑、增加、等未完成（爱琴）完成时间周五
	所有用户层级关系图（树）需要显示（李静）完成时间周五
	
6. 所有的图片路径无效的BUG（爱琴）


# 探针：听云
前端部分：
商城：
	结算页点击修改地址去地址管理页，地址管理业点中某地址返回结算页
	
	商城首页综合、排序还没完成
	# 认权产品购买接口的区分
	# 代理商适配移动端
	# 添加商城商品的管理
	# 认权商品详情页增加图片或者详细信息或者轮播
	认权商品详情 --> 商品详情页 --> 跳转结算页

# 结算接口测试
# 4. 认权释放完成后不能重新购买

# 结算时确认地址库是否有地址，没有默认地址则返回没有
# 订单购买金额显示199
# 9. 提现的BUG还没改，针对收益3的返现部分怎么返...

# 1、认权和众筹订单缺一个产品图片，尺寸 100*100
# 2、提现订单还没有数据，没有测试，
# 9、充值部分缺少代理商信息接口、
# 5、认权购买后个人中心的可购众筹次数没有改变，一直是可购买0次，
# 6、众筹、认权购买缺少一个购买成功的标识
# 7、提现接口报500错误、
# 14、提交充值申请的接口报500

# 11. 提现没有传钱包地址过去，但是传了uid过去，后台是否有匹配地址？？？如果用户没有绑定地址，是不是先提示用户绑定地址？？？提现订单返回的地址为""
# 1、认权和众筹订单查询返回的数据里缺少单个产品的名称、产品类型（认权或者众筹），产品周期（认权是600天，众筹有3M,6M,12M）
# 12、提现订单钱包地址CashWithdrawal_wallt_address为""
# 缺少向代理商申请EMT的接口
# 15、向代理商申请EMT的接口处理参数
# 13、缺少代理商用户信息
# 14、绑定钱包未绑定到数据库

# 4、加速明细的接口还缺少一个直推/间推类别的字段，
# 4、倍化明细的接口还没完成，
# 二维码 确保不重复添加img节点
# 3、充值提交很多笔，但是充值订单没有数据，没有测试、
# 3、注册接口报500
# 16、倍化的接口，没有返回任何信息
# 22、倍化接口报500
# 20、回源问题，A主服务器，B=>购买，C=>是否能有相关信息
# 17、代理商直接转账，用户端相应增加充值订单，接口调整
# 23、加速接口要区分下级和下下级是否购买产品，返回已购的用户信息
# 24、注册接口会生成空的uid(已找到原因)
# 后台管理员有一个暂停/冻结代理商和用户的功能  这个暂停/冻结是分别指哪些业务功能？
# 跨域问题
# 1、加速报500
# 2、倍化接口很多必须字段都返回"",需要检查一下接口是否存在问题
# 平台数据管理：
	# 客户分布管理（层级关系）未完成
# 5. 下级购入众筹，需要返回本金的时间返利息的百分比给上级
	# 代理商管理：(爱琴)--管理代理商商
	# 冻结、恢复代理商接口没完成（暂停和冻结的区别:暂停提现功能，冻结所有功能冻结）
# 结算页结算时  地址只传地址还是收货人和手机号都要传
# 获取产品详情时还需要传递产品id	
# 前端部分：
# 4、充值订单接口返回数据极不稳定，有时候没有数据返回
# 20、跨域问题：本地无法访问服务器，无法请求
# 21、订单的时有时无：发送两个请求的问题
# 2、tingyun.js错误






































































