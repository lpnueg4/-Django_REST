# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework import renderers, response, schemas
from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer

from rest_framework.views import APIView
from rest_framework.schemas import ManualSchema
import coreapi
import coreschema


@api_view(['GET'])
def other1(request):
    """
    This API deletes/uninstalls a device.
    """
    info = {
        'a':1,
        'b':2,
    }

    return Response(info)

@api_view(['POST'])
def other2(request, name):
    """
    Say hi.
    """

    return Response("Hi %s" % name)

@api_view(['PUT'])
def other3(request, n1, n2):
    """
    Easy addition.
    # 1
    ## 2
    ### 3
    """

    return Response("%s + %s = %s" % (int(n1), int(n2), int(n1)+int(n2)))

class other4(APIView):
    schema = ManualSchema(
        fields=[
            coreapi.Field(
                "name",
                required=True,
                location="multipart/form-data",
                schema=coreschema.String(),
                description='this is a name'
            ),
            coreapi.Field(
                "second_field",
                required=True,
                # location="body",
                location="application/json",
                schema=coreschema.String()
            ),
            coreapi.Field(
                "third",
                required=False,
                location="enum",
                # schema=coreschema.Object()
                # schema=coreschema.Array(['cat', 'dog', 'rabbit'], unique_items=True),
                # schema=coreschema.Enum(['cat', 'dog', 'rabbit']),
                # enmu=["123", "222"]
                # schema=coreschema.Array()
                # schema=coreschema.String(default="heheda"),
            ),
        ],
        # tags=['aa'],
        description="From class"
    )

    def post(self, request):
        # print request.POST.get('name')
        print type(request.data)
        print request.data
        print request.query_params.dict()
        # form = ContactForm(request.POST)
        # print form
        return Response("from class APIView")


@api_view(['GET', 'POST'])
def vm1(request):
    # """
    # This API deletes/uninstalls a device.
    # """
    """
    get: 获取虚拟机列表.
    post: 创建虚拟机.
    """
    return Response('vm1')

@api_view(['GET'])
def vm2(request):
    """
    启动虚拟机.
    """
    return Response('vm2')

@api_view(['DELETE'])
def vm3(request):
    """
    删除虚拟机.
    """
    return Response('vm3')

@api_view(['PATCH'])
def vm4(request):
    """
    关闭虚拟机.
    """
    return Response('vm4')

@api_view(['HEAD'])
def vm5(request):
    """
    备份虚拟机.
    """
    return Response('vm5')


@api_view(['PATCH', 'GET'])
# @renderer_classes([renderers.CoreJSONRenderer, OpenAPIRenderer])
@renderer_classes([OpenAPIRenderer])
def schema_view(request):
    generator = schemas.SchemaGenerator(title='Bookings API')
    return Response(generator.get_schema())

