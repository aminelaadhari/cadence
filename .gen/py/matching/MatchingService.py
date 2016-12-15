#
# Autogenerated by Thrift Compiler (0.9.2)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py:utf8strings
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException
from ttypes import *
from thrift.Thrift import TProcessor
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None


class Iface:
  """
  MatchingService API is exposed to provide support for polling from long running applications.
  Such applications are expected to have a worker which regularly polls for DecisionTask and ActivityTask.  For each
  DecisionTask, application is expected to process the history of events for that session and respond back with next
  decisions.  For each ActivityTask, application is expected to execute the actual logic for that task and respond back
  with completion or failure.

  """
  def PollForDecisionTask(self, pollRequest):
    """
    PollForDecisionTask is called by frontend to process DecisionTask from a specific taskList.  A
    DecisionTask is dispatched to callers for active workflow executions, with pending decisions.


    Parameters:
     - pollRequest
    """
    pass

  def PollForActivityTask(self, pollRequest):
    """
    PollForActivityTask is called by frontend to process ActivityTask from a specific taskList.  ActivityTask
    is dispatched to callers whenever a ScheduleTask decision is made for a workflow execution.


    Parameters:
     - pollRequest
    """
    pass

  def AddDecisionTask(self, addRequest):
    """
    AddDecisionTask is called by the history service when a decision task is scheduled, so that it can be dispatched
    by the MatchingEngine.


    Parameters:
     - addRequest
    """
    pass

  def AddActivityTask(self, addRequest):
    """
    AddActivityTask is called by the history service when a decision task is scheduled, so that it can be dispatched
    by the MatchingEngine.


    Parameters:
     - addRequest
    """
    pass


class Client(Iface):
  """
  MatchingService API is exposed to provide support for polling from long running applications.
  Such applications are expected to have a worker which regularly polls for DecisionTask and ActivityTask.  For each
  DecisionTask, application is expected to process the history of events for that session and respond back with next
  decisions.  For each ActivityTask, application is expected to execute the actual logic for that task and respond back
  with completion or failure.

  """
  def __init__(self, iprot, oprot=None):
    self._iprot = self._oprot = iprot
    if oprot is not None:
      self._oprot = oprot
    self._seqid = 0

  def PollForDecisionTask(self, pollRequest):
    """
    PollForDecisionTask is called by frontend to process DecisionTask from a specific taskList.  A
    DecisionTask is dispatched to callers for active workflow executions, with pending decisions.


    Parameters:
     - pollRequest
    """
    self.send_PollForDecisionTask(pollRequest)
    return self.recv_PollForDecisionTask()

  def send_PollForDecisionTask(self, pollRequest):
    self._oprot.writeMessageBegin('PollForDecisionTask', TMessageType.CALL, self._seqid)
    args = PollForDecisionTask_args()
    args.pollRequest = pollRequest
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_PollForDecisionTask(self):
    iprot = self._iprot
    (fname, mtype, rseqid) = iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(iprot)
      iprot.readMessageEnd()
      raise x
    result = PollForDecisionTask_result()
    result.read(iprot)
    iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    if result.badRequestError is not None:
      raise result.badRequestError
    if result.internalServiceError is not None:
      raise result.internalServiceError
    raise TApplicationException(TApplicationException.MISSING_RESULT, "PollForDecisionTask failed: unknown result");

  def PollForActivityTask(self, pollRequest):
    """
    PollForActivityTask is called by frontend to process ActivityTask from a specific taskList.  ActivityTask
    is dispatched to callers whenever a ScheduleTask decision is made for a workflow execution.


    Parameters:
     - pollRequest
    """
    self.send_PollForActivityTask(pollRequest)
    return self.recv_PollForActivityTask()

  def send_PollForActivityTask(self, pollRequest):
    self._oprot.writeMessageBegin('PollForActivityTask', TMessageType.CALL, self._seqid)
    args = PollForActivityTask_args()
    args.pollRequest = pollRequest
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_PollForActivityTask(self):
    iprot = self._iprot
    (fname, mtype, rseqid) = iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(iprot)
      iprot.readMessageEnd()
      raise x
    result = PollForActivityTask_result()
    result.read(iprot)
    iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    if result.badRequestError is not None:
      raise result.badRequestError
    if result.internalServiceError is not None:
      raise result.internalServiceError
    raise TApplicationException(TApplicationException.MISSING_RESULT, "PollForActivityTask failed: unknown result");

  def AddDecisionTask(self, addRequest):
    """
    AddDecisionTask is called by the history service when a decision task is scheduled, so that it can be dispatched
    by the MatchingEngine.


    Parameters:
     - addRequest
    """
    self.send_AddDecisionTask(addRequest)
    self.recv_AddDecisionTask()

  def send_AddDecisionTask(self, addRequest):
    self._oprot.writeMessageBegin('AddDecisionTask', TMessageType.CALL, self._seqid)
    args = AddDecisionTask_args()
    args.addRequest = addRequest
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_AddDecisionTask(self):
    iprot = self._iprot
    (fname, mtype, rseqid) = iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(iprot)
      iprot.readMessageEnd()
      raise x
    result = AddDecisionTask_result()
    result.read(iprot)
    iprot.readMessageEnd()
    if result.badRequestError is not None:
      raise result.badRequestError
    if result.internalServiceError is not None:
      raise result.internalServiceError
    return

  def AddActivityTask(self, addRequest):
    """
    AddActivityTask is called by the history service when a decision task is scheduled, so that it can be dispatched
    by the MatchingEngine.


    Parameters:
     - addRequest
    """
    self.send_AddActivityTask(addRequest)
    self.recv_AddActivityTask()

  def send_AddActivityTask(self, addRequest):
    self._oprot.writeMessageBegin('AddActivityTask', TMessageType.CALL, self._seqid)
    args = AddActivityTask_args()
    args.addRequest = addRequest
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_AddActivityTask(self):
    iprot = self._iprot
    (fname, mtype, rseqid) = iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(iprot)
      iprot.readMessageEnd()
      raise x
    result = AddActivityTask_result()
    result.read(iprot)
    iprot.readMessageEnd()
    if result.badRequestError is not None:
      raise result.badRequestError
    if result.internalServiceError is not None:
      raise result.internalServiceError
    return


class Processor(Iface, TProcessor):
  def __init__(self, handler):
    self._handler = handler
    self._processMap = {}
    self._processMap["PollForDecisionTask"] = Processor.process_PollForDecisionTask
    self._processMap["PollForActivityTask"] = Processor.process_PollForActivityTask
    self._processMap["AddDecisionTask"] = Processor.process_AddDecisionTask
    self._processMap["AddActivityTask"] = Processor.process_AddActivityTask

  def process(self, iprot, oprot):
    (name, type, seqid) = iprot.readMessageBegin()
    if name not in self._processMap:
      iprot.skip(TType.STRUCT)
      iprot.readMessageEnd()
      x = TApplicationException(TApplicationException.UNKNOWN_METHOD, 'Unknown function %s' % (name))
      oprot.writeMessageBegin(name, TMessageType.EXCEPTION, seqid)
      x.write(oprot)
      oprot.writeMessageEnd()
      oprot.trans.flush()
      return
    else:
      self._processMap[name](self, seqid, iprot, oprot)
    return True

  def process_PollForDecisionTask(self, seqid, iprot, oprot):
    args = PollForDecisionTask_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = PollForDecisionTask_result()
    try:
      result.success = self._handler.PollForDecisionTask(args.pollRequest)
    except shared.ttypes.BadRequestError, badRequestError:
      result.badRequestError = badRequestError
    except shared.ttypes.InternalServiceError, internalServiceError:
      result.internalServiceError = internalServiceError
    oprot.writeMessageBegin("PollForDecisionTask", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_PollForActivityTask(self, seqid, iprot, oprot):
    args = PollForActivityTask_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = PollForActivityTask_result()
    try:
      result.success = self._handler.PollForActivityTask(args.pollRequest)
    except shared.ttypes.BadRequestError, badRequestError:
      result.badRequestError = badRequestError
    except shared.ttypes.InternalServiceError, internalServiceError:
      result.internalServiceError = internalServiceError
    oprot.writeMessageBegin("PollForActivityTask", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_AddDecisionTask(self, seqid, iprot, oprot):
    args = AddDecisionTask_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = AddDecisionTask_result()
    try:
      self._handler.AddDecisionTask(args.addRequest)
    except shared.ttypes.BadRequestError, badRequestError:
      result.badRequestError = badRequestError
    except shared.ttypes.InternalServiceError, internalServiceError:
      result.internalServiceError = internalServiceError
    oprot.writeMessageBegin("AddDecisionTask", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_AddActivityTask(self, seqid, iprot, oprot):
    args = AddActivityTask_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = AddActivityTask_result()
    try:
      self._handler.AddActivityTask(args.addRequest)
    except shared.ttypes.BadRequestError, badRequestError:
      result.badRequestError = badRequestError
    except shared.ttypes.InternalServiceError, internalServiceError:
      result.internalServiceError = internalServiceError
    oprot.writeMessageBegin("AddActivityTask", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()


# HELPER FUNCTIONS AND STRUCTURES

class PollForDecisionTask_args:
  """
  Attributes:
   - pollRequest
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'pollRequest', (shared.ttypes.PollForDecisionTaskRequest, shared.ttypes.PollForDecisionTaskRequest.thrift_spec), None, ), # 1
  )

  def __init__(self, pollRequest=None,):
    self.pollRequest = pollRequest

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRUCT:
          self.pollRequest = shared.ttypes.PollForDecisionTaskRequest()
          self.pollRequest.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('PollForDecisionTask_args')
    if self.pollRequest is not None:
      oprot.writeFieldBegin('pollRequest', TType.STRUCT, 1)
      self.pollRequest.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.pollRequest)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class PollForDecisionTask_result:
  """
  Attributes:
   - success
   - badRequestError
   - internalServiceError
  """

  thrift_spec = (
    (0, TType.STRUCT, 'success', (shared.ttypes.PollForDecisionTaskResponse, shared.ttypes.PollForDecisionTaskResponse.thrift_spec), None, ), # 0
    (1, TType.STRUCT, 'badRequestError', (shared.ttypes.BadRequestError, shared.ttypes.BadRequestError.thrift_spec), None, ), # 1
    (2, TType.STRUCT, 'internalServiceError', (shared.ttypes.InternalServiceError, shared.ttypes.InternalServiceError.thrift_spec), None, ), # 2
  )

  def __init__(self, success=None, badRequestError=None, internalServiceError=None,):
    self.success = success
    self.badRequestError = badRequestError
    self.internalServiceError = internalServiceError

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 0:
        if ftype == TType.STRUCT:
          self.success = shared.ttypes.PollForDecisionTaskResponse()
          self.success.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 1:
        if ftype == TType.STRUCT:
          self.badRequestError = shared.ttypes.BadRequestError()
          self.badRequestError.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRUCT:
          self.internalServiceError = shared.ttypes.InternalServiceError()
          self.internalServiceError.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('PollForDecisionTask_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.STRUCT, 0)
      self.success.write(oprot)
      oprot.writeFieldEnd()
    if self.badRequestError is not None:
      oprot.writeFieldBegin('badRequestError', TType.STRUCT, 1)
      self.badRequestError.write(oprot)
      oprot.writeFieldEnd()
    if self.internalServiceError is not None:
      oprot.writeFieldBegin('internalServiceError', TType.STRUCT, 2)
      self.internalServiceError.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.success)
    value = (value * 31) ^ hash(self.badRequestError)
    value = (value * 31) ^ hash(self.internalServiceError)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class PollForActivityTask_args:
  """
  Attributes:
   - pollRequest
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'pollRequest', (shared.ttypes.PollForActivityTaskRequest, shared.ttypes.PollForActivityTaskRequest.thrift_spec), None, ), # 1
  )

  def __init__(self, pollRequest=None,):
    self.pollRequest = pollRequest

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRUCT:
          self.pollRequest = shared.ttypes.PollForActivityTaskRequest()
          self.pollRequest.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('PollForActivityTask_args')
    if self.pollRequest is not None:
      oprot.writeFieldBegin('pollRequest', TType.STRUCT, 1)
      self.pollRequest.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.pollRequest)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class PollForActivityTask_result:
  """
  Attributes:
   - success
   - badRequestError
   - internalServiceError
  """

  thrift_spec = (
    (0, TType.STRUCT, 'success', (shared.ttypes.PollForActivityTaskResponse, shared.ttypes.PollForActivityTaskResponse.thrift_spec), None, ), # 0
    (1, TType.STRUCT, 'badRequestError', (shared.ttypes.BadRequestError, shared.ttypes.BadRequestError.thrift_spec), None, ), # 1
    (2, TType.STRUCT, 'internalServiceError', (shared.ttypes.InternalServiceError, shared.ttypes.InternalServiceError.thrift_spec), None, ), # 2
  )

  def __init__(self, success=None, badRequestError=None, internalServiceError=None,):
    self.success = success
    self.badRequestError = badRequestError
    self.internalServiceError = internalServiceError

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 0:
        if ftype == TType.STRUCT:
          self.success = shared.ttypes.PollForActivityTaskResponse()
          self.success.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 1:
        if ftype == TType.STRUCT:
          self.badRequestError = shared.ttypes.BadRequestError()
          self.badRequestError.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRUCT:
          self.internalServiceError = shared.ttypes.InternalServiceError()
          self.internalServiceError.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('PollForActivityTask_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.STRUCT, 0)
      self.success.write(oprot)
      oprot.writeFieldEnd()
    if self.badRequestError is not None:
      oprot.writeFieldBegin('badRequestError', TType.STRUCT, 1)
      self.badRequestError.write(oprot)
      oprot.writeFieldEnd()
    if self.internalServiceError is not None:
      oprot.writeFieldBegin('internalServiceError', TType.STRUCT, 2)
      self.internalServiceError.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.success)
    value = (value * 31) ^ hash(self.badRequestError)
    value = (value * 31) ^ hash(self.internalServiceError)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class AddDecisionTask_args:
  """
  Attributes:
   - addRequest
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'addRequest', (AddDecisionTaskRequest, AddDecisionTaskRequest.thrift_spec), None, ), # 1
  )

  def __init__(self, addRequest=None,):
    self.addRequest = addRequest

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRUCT:
          self.addRequest = AddDecisionTaskRequest()
          self.addRequest.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('AddDecisionTask_args')
    if self.addRequest is not None:
      oprot.writeFieldBegin('addRequest', TType.STRUCT, 1)
      self.addRequest.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.addRequest)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class AddDecisionTask_result:
  """
  Attributes:
   - badRequestError
   - internalServiceError
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'badRequestError', (shared.ttypes.BadRequestError, shared.ttypes.BadRequestError.thrift_spec), None, ), # 1
    (2, TType.STRUCT, 'internalServiceError', (shared.ttypes.InternalServiceError, shared.ttypes.InternalServiceError.thrift_spec), None, ), # 2
  )

  def __init__(self, badRequestError=None, internalServiceError=None,):
    self.badRequestError = badRequestError
    self.internalServiceError = internalServiceError

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRUCT:
          self.badRequestError = shared.ttypes.BadRequestError()
          self.badRequestError.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRUCT:
          self.internalServiceError = shared.ttypes.InternalServiceError()
          self.internalServiceError.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('AddDecisionTask_result')
    if self.badRequestError is not None:
      oprot.writeFieldBegin('badRequestError', TType.STRUCT, 1)
      self.badRequestError.write(oprot)
      oprot.writeFieldEnd()
    if self.internalServiceError is not None:
      oprot.writeFieldBegin('internalServiceError', TType.STRUCT, 2)
      self.internalServiceError.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.badRequestError)
    value = (value * 31) ^ hash(self.internalServiceError)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class AddActivityTask_args:
  """
  Attributes:
   - addRequest
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'addRequest', (AddActivityTaskRequest, AddActivityTaskRequest.thrift_spec), None, ), # 1
  )

  def __init__(self, addRequest=None,):
    self.addRequest = addRequest

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRUCT:
          self.addRequest = AddActivityTaskRequest()
          self.addRequest.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('AddActivityTask_args')
    if self.addRequest is not None:
      oprot.writeFieldBegin('addRequest', TType.STRUCT, 1)
      self.addRequest.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.addRequest)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class AddActivityTask_result:
  """
  Attributes:
   - badRequestError
   - internalServiceError
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'badRequestError', (shared.ttypes.BadRequestError, shared.ttypes.BadRequestError.thrift_spec), None, ), # 1
    (2, TType.STRUCT, 'internalServiceError', (shared.ttypes.InternalServiceError, shared.ttypes.InternalServiceError.thrift_spec), None, ), # 2
  )

  def __init__(self, badRequestError=None, internalServiceError=None,):
    self.badRequestError = badRequestError
    self.internalServiceError = internalServiceError

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRUCT:
          self.badRequestError = shared.ttypes.BadRequestError()
          self.badRequestError.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRUCT:
          self.internalServiceError = shared.ttypes.InternalServiceError()
          self.internalServiceError.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('AddActivityTask_result')
    if self.badRequestError is not None:
      oprot.writeFieldBegin('badRequestError', TType.STRUCT, 1)
      self.badRequestError.write(oprot)
      oprot.writeFieldEnd()
    if self.internalServiceError is not None:
      oprot.writeFieldBegin('internalServiceError', TType.STRUCT, 2)
      self.internalServiceError.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.badRequestError)
    value = (value * 31) ^ hash(self.internalServiceError)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)