from .models import Essay, Album, Files
from rest_framework import serializers


class EssaySerializer(serializers.ModelSerializer):

    author_name = serializers.ReadOnlyField(source = 'author.username')

    class Meta:
        model = Essay
        fields = ('pk','title','body','author_name')

class AlbumSerializer(serializers.ModelSerializer):

    author_name = serializers.ReadOnlyField(source = 'author.username')
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = Album
        fields = ('pk','author_name','image','desc')

class FilesSerializer(serializers.ModelSerializer):

    author_name = serializers.ReadOnlyField(source = 'author.username')
    files = serializers.FileField(use_url=True)

    # 이런식으로 변수명을 지어주는것이 더 좋음
    # author = serializers.ReadOnlyField(source = 'author.username')
    # myfile = serializers.FileField(use_url=True)


    class Meta:
        model = Album
        fields = ('pk','author_name','files','desc')