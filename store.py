import pickle
from cStringIO import StringIO
from Crypto.Cipher import AES
import os

class Store(object):
  _root_dir     = None
  _current_dir  = None
  _SALT = "fqjei42fjq-4958szh2eiym632jasijo"

  def __init__(self):
    import container
    self._root_dir = container.Container()
    self._current_dir = self._root_dir
    self._password = None
    self._filename = None

  def get_password(self):
    return self._password

  def set_password(self, passwd):
    # password needs to be 32
    diff = len(passwd) % 32
    if diff != 0:
      # append missing
      passwd += self._SALT[:len(self._SALT) - diff]

    self._password = passwd

  def get_filename(self):
    return self._filename

  def set_filename(self, filename):
    self._filename = filename

  def get_current(self):
    return self._current_dir

  def set_current(self, dir):
    self._current_dir = dir

  def get_root(self):
    return self._root_dir

  def set_root(self, dir):
    self._root_dir = dir

  def save(self):
    str = StringIO()

    # serialise
    pickle.dump(self.get_root(), str, 0)

    # make sure str is a multiple of 16 in len
    extra = len(str.getvalue()) % 16
    for i in range(16-extra):
      # append as many spaces as we need
      str.write(' ')

    encrypted = None

    try:
      obj = AES.new(self.get_password())
      encrypted = obj.encrypt(str.getvalue())
    except:
      print "Failed to encrypt. Store not saved."
      encrypted = None
    finally:
      str.close()

    if encrypted != None:
      output = open("db.pass", "wb")
      output.write(encrypted)
      output.close()


  def load(self, **params):
    if not os.path.exists(params['filename']):
      print "File not found."
      return

    self.set_filename(params['filename'])
    input = open(self.get_filename(), "rb")

    # read it all
    encrypted = input.read(-1)
    input.close()

    self.set_password(params['password'])

    # unencrpyt
    try:
      obj = AES.new(self.get_password())
      unencrypted = obj.decrypt(encrypted)
      tmp_root = pickle.loads(unencrypted)

      self.set_root(tmp_root)
      self.set_current(self.get_root())
    except:
      print "Incorrect password."

class ItemType:
  DIR   = 0
  ENTRY = 1