from store import ItemType

class Entry(object):
  type = ItemType.ENTRY

  def __init__(self):
    self._data = {'name': None, 'user_name': None, 'password': None,
                  'expires': None}

  def get_name(self):
    return self._data['name']

  def set_name(self, name):
    self._data['name'] = name

  def get_user_name(self):
    return self._data['user_name']

  def set_user_name(self, user_name):
    self._data['user_name'] = user_name

  def get_password(self):
    return self._data['password']

  def set_password(self, password):
    self._data['password'] = password

  def get_custom_data(self, data):
    pass

  def set_custom_data(self, name, value):
    pass

  def get_data(self):
    return self._data

  def get_data_keys(self):
    return self._data.keys()
	
  def get_container(self):
	return self._parent
