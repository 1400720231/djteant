
from user.models import Store, Prodetail,Product,Purchase                              

from django_multitenant.utils import set_current_tenant    
a = Store.objects.all()[0] 
b= Purchase.objects.all()[0]　
b.product_purchased                                                                   
self.related_model <class 'user.models.Product'>
<_thread._local object at 0x7f3814789780>
table <class 'user.models.Product'>
返回当前tenant的值，可能是list
<_thread._local object at 0x7f3814789780>
一个tenant情况 Store object (1)
返回当前instance的tenant_id的值
current_tenant_value 1
current_tenant_value:  1
table_name <class 'user.models.Product'>
返回当前instance的tenant_id的值
get_tenant_column(table) store_id
返回当前instance的tenant_id的值
(0.000) SELECT `user_product`.`id`, `user_product`.`store_id`, `user_product`.`name`, `user_product`.`description` FROM `user_product` WHERE (`user_product`.`id` = 1 AND `user_product`.`store_id` = 1); args=(1, 1)


>想要再次触发 必须重新查询b=Purchase.objects.all()[0]  这又是知识点，好像是prefect_related还是什么的，就是记载之后
>就变成属性了，这涉及到django的sql优化章节，哈哈哈我说嘛总会让我遇到的，看来要顺便复习研究一下django sql优化了。