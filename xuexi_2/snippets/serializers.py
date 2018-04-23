# coding:u8

from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

from django.contrib.auth.models import User

# class SnippetSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=False, allow_blank=True, max_length=200)
#     code = serializers.CharField(style={'base_template': 'textarea.html'})
#     linenos = serializers.BooleanField(required=False)
#     language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
#     style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

#     def create(self, validated_data):
#         """
#         Create and return a new `Snippet` instance, given the validated data.
#         """
#         return Snippet.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Snippet` instance, given the validated data.
#         """
#         instance.title = validated_data.get('title', instance.title)
#         instance.code = validated_data.get('code', instance.code)
#         instance.linenos = validated_data.get('linenos', instance.linenos)
#         instance.language = validated_data.get('language', instance.language)
#         instance.style = validated_data.get('style', instance.style)
#         instance.save()
#         return instance

# --------------------

# class SnippetSerializer(serializers.ModelSerializer):
#     owner = serializers.ReadOnlyField(source='owner.username')

#     class Meta:
#         model = Snippet
#         fields = ('id', 'title', 'code', 'linenos', 'language', 'style', 'owner')


# class UserSerializer(serializers.ModelSerializer):
#     # 由于 snippets_id 是反向引用 Snippet 中的数据, 利用 related_name 关联到 Snippet 中的对象.
#     snippets_id = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())
#     print snippets_id
#     # SerializerMethodField 可以自定义方法 get_count()
#     count = serializers.SerializerMethodField()

#     class Meta:
#         model = User
#         fields = ('id', 'username', 'snippets_id', 'count')

#     # obj 就是当前 User 对象的实例
#     def get_count(self, obj):
#         return obj.snippets_id.all().count()

# --------------------
# 为了显示 高亮代码 , 改写

class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ('url', 'id', 'highlight', 'owner',
                  'title', 'code', 'linenos', 'language', 'style')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets_id = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)
    # snippets_id = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'snippets_id')

