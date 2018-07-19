from django.db import models

# Create your models here.

class FictionType(models.Model):
    name = models.CharField(max_length=20,verbose_name="小说类型")


class Users(models.Model):
    sex_type = (
        (0,'男'),
        (1,'女'),
        (2,'保密')
    )
    name = models.CharField(max_length=20,unique=True,verbose_name="用户账号")
    passwd = models.CharField(max_length=20,verbose_name="用户密码")
    email = models.CharField(max_length=20,unique=True,verbose_name="用户邮箱")
    phone = models.CharField(max_length=13,unique=True,verbose_name="电话")
    sex = models.IntegerField(choices=sex_type,default=1)
    head_img = models.ImageField(upload_to="photos",verbose_name="用户头像")
    create_time = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    login_time = models.DateTimeField(auto_now=True,verbose_name="登录时间")
    @property
    def sex_name(self):
        return self.sex_type[self.sex][1]

class Fition(models.Model):
    name = models.CharField(max_length=50,unique=True,verbose_name="小说名")
    intro = models.TextField(max_length=200,verbose_name="作品简介")
    cover = models.CharField(max_length=300,verbose_name="封面图片")
    put_time = models.DateTimeField(auto_now_add=True,verbose_name="上架时间")
    click = models.PositiveIntegerField(default=0,verbose_name="作品点击数")
    author = models.CharField(max_length=20,unique=True,verbose_name="作者名")
    fictionType = models.ForeignKey(FictionType,on_delete=models.CASCADE,null=True)
    users = models.ForeignKey(Users,on_delete=models.CASCADE,null=True)
    def increase_click(self):
        self.click += 1
        self.save(update_fields=['click'])



class Chapter(models.Model):
    name = models.CharField(max_length=50,verbose_name='章节名')
    content = models.TextField(verbose_name="小说内容")
    updata_time = models.DateTimeField(auto_now=True,verbose_name="章节更新时间")
    fiction = models.ForeignKey(Fition,on_delete=models.CASCADE)

