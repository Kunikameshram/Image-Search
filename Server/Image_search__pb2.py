# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Image_search_.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13Image_search_.proto\x12\x0cimage_search\"!\n\x0eKeywordRequest\x12\x0f\n\x07keyword\x18\x01 \x01(\t\"#\n\rImageResponse\x12\x12\n\nimage_data\x18\x01 \x01(\x0c\x32Y\n\x0bImageSearch\x12J\n\x0bSearchImage\x12\x1c.image_search.KeywordRequest\x1a\x1b.image_search.ImageResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'Image_search__pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_KEYWORDREQUEST']._serialized_start=37
  _globals['_KEYWORDREQUEST']._serialized_end=70
  _globals['_IMAGERESPONSE']._serialized_start=72
  _globals['_IMAGERESPONSE']._serialized_end=107
  _globals['_IMAGESEARCH']._serialized_start=109
  _globals['_IMAGESEARCH']._serialized_end=198
# @@protoc_insertion_point(module_scope)
