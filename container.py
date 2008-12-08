from store import ItemType

class Container(object):
  _name = None
  _parent = None
  type = ItemType.DIR

  def __init__(self, name=None):
    self.set_name(name)
    self._items = []
    self._parent = None

  def get_num_items(self):
    return len(self._items)

  def get_name(self):
    return self._name

  def set_name(self, name):
    self._name = name

  def get_parent(self):
    return self._parent

  def add_item(self, item):
    if item == None:
      logger.debug("No item given")
      return False

    item._parent = self
    self._items.append(item)

  def remove_item(self, item):
    if item == None:
      logger.debug("No item given")
      return False

    if item in self._items:
      # remove the item
      self._items.remove(item)
      return True

    return False

  def get_items(self):
    return self._items

  def has_entry(self, name):
    for item in self._items:
      if item.get_name().upper() == name.upper() and \
        item.type == ItemType.ENTRY:
        return True

    return False

  def has_container(self, name):
    for item in self._items:
      if item.get_name().upper() == name.upper() and \
        item.type == ItemType.DIR:
        return True

    return False

  def get_item_by_name(self, name):
    for item in self._items:
      if item.get_name().upper() == name.upper():
        return item

    return None

  def get_full_path(self):
    """
    Retrieves the full path up to the current container
    """
    path = '/'

    if self.get_name() != None:
      path += self.get_name()

    parent = self.get_parent()
    while parent != None and parent.get_name() != None:
      # prepend all parent nodes
      path = '/' + parent.get_name() + path
      parent = parent.get_parent()

    return path
  
  def get_containers(self):
    """
    Retrieves all containers within the container, if any
    """
    return [item for item in self.get_items() 
            if item.type == ItemType.DIR]
            
  def get_entries(self):
    """
    Retrieves all entries within the container, if any
    """
    return [item for item in self.get_items()
            if item.type == ItemType.ENTRY]
