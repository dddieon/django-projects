from django import forms
from .models import Blog


class CreateBlog(forms.ModelForm):
    class Meta:
        # 내부 클래스로 활용되며, 필드의 값을 재정의할 때 사용. Blog로부터 fields 모델을 가져온다는 의미.
        model = Blog

        fields = ['title', 'pub_date', 'body']
