# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: order_collector.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15order_collector.proto\"\x1d\n\x0c\x46irstRequest\x12\r\n\x05token\x18\x01 \x01(\t\"9\n\x05Order\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\x12\r\n\x05price\x18\x02 \x01(\x02\x12\x10\n\x08\x64\x61teTime\x18\x03 \x01(\x03\x32\x34\n\x0eOrderCollector\x12\"\n\x07\x43ollect\x12\r.FirstRequest\x1a\x06.Order0\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'order_collector_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _FIRSTREQUEST._serialized_start=25
  _FIRSTREQUEST._serialized_end=54
  _ORDER._serialized_start=56
  _ORDER._serialized_end=113
  _ORDERCOLLECTOR._serialized_start=115
  _ORDERCOLLECTOR._serialized_end=167
# @@protoc_insertion_point(module_scope)
