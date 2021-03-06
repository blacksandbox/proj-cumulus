from rest_framework import serializers

from ..models import (
    Scene,
    Strip,
    Frame
)


# .................................................. 
# .................................................. 
#                   api/book/{#}
# .................................................. 
# .................................................. 


class StripModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Strip
        fields = [
            'id',
            'scene',
            'order',
            'description',
            'frame_set'
            ]
            
class SceneModelSerializer(serializers.ModelSerializer):
    
    # strips = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # strips = serializers.StringRelatedField(many=True, read_only=True) -> output str
    strips = StripModelSerializer(many=True, read_only=True, source='strip_set')
    
    class Meta:
        model = Scene
        fields = [
            'id',
            'children_li',
            'name',
            'strips',
        ]
        
        
class FrameModelSerializer(serializers.ModelSerializer):
    
    # strip = serializers.PrimaryKeyRelatedField(source='strip', read_only=True, required=True)
    
    class Meta:
        model = Frame
        fields = [
            'id',
            'note',
            'strip',
            'frame_image'
            ]
        #read_only_fields = ('frame_image',)