class Commands:
  _commands = [
    {"command": ["EXIT", "E", "QUIT", "Q"],
     "help": "Exits pypm",
     "requires_param": False,
     "takes_param": False,
     "method": None},

    {"command": ["HELP", "H", "?"],
     "help": "Displays a list of commands or help on a specific command.\n" +
     "eg: help\n" +
     "    help <command>",
     "requires_param": False,
     "takes_param": True,
     "method": None},

    {"command": ["LS", "LIST"],
     "help": "Lists everything in the current directory.\n" +
     "eg: ls       Lists everything in a tabbed width format\n" +
     "    ls -l    Lists everything in a list format.",
     "requires_param": False,
     "takes_param": True,
     "method": None},

    {"command": ["CD"],
     "help": "Changes to the specified directory.\n" +
     "eg: cd       Displays the current directory.\n" +
     "    cd <dir> Lists everything in a list format.",
     "requires_param": False,
     "takes_param": True,
     "method": None},

    {"command": ["SHOW", "S", "CAT"],
     "help": "Displays the specified entry.\n" +
     "eg: show <name> Displays the specfied entry.\n",
     "requires_param": True,
     "takes_param": True,
     "method": None},

    {"command": ["MKDIR"],
     "help": "Creates a new directory.\n" +
     "eg: mkdir <dir>",
     "requires_param": True,
     "takes_param": True,
     "method": None},

    {"command": ["RM"],
     "help": "Deletes the specified entry or directory. You will be prompted " +
     "to confirm this action.\n" +
     "eg: rm <name> Displays the specfied entry.",
     "requires_param": True,
     "takes_param": True,
     "method": None},

    {"command": ["SAVE"],
     "help": "Saves any changes to the password DB.\n" +
     "eg: save",
     "requires_param": False,
     "takes_param": False,
     "method": None},

    {"command": ["SET"],
     "help": "Sets a specified config option.\n" +
     "eg: set <option> <value>",
     "requires_param": True,
     "takes_param": True,
     "method": None},

    {"command": ["ADD", "A"],
     "help": "Adds an entry to the current directory.\n" +
     "eg: add        Prompts the user for entry details.\n" +
     "    add <name> Creates an entry with the specified name.",
     "requires_param": False,
     "takes_param": True,
     "method": None},

    {"command": ["MOD", "M", "EDIT"],
     "help": "Modifies the specified entry.\n" +
     "eg: mod <name> Prompts the user for entry modifications.",
     "requires_param": True,
     "takes_param": True,
     "method": None},

    {"command": ["CLEAR", "CLR", "CLS"],
     "help": "Clears the current console.\n" +
     "eg: clear",
     "requires_param": False,
     "takes_param": False,
     "method": None},

    {"command": ["CLOSE"],
     "help": "Closes the password DB.\n" +
     "eg: close",
     "requires_param": False,
     "takes_param": False,
     "method": None},

    {"command": ["OPEN", "O"],
     "help": "Loads the password DB.\n" +
     "eg: open            Loads the default password DB.\n" +
     "    open <filename> Loads the specified password DB file.",
     "requires_param": False,
     "takes_param": True,
     "method": None},
    
    {"command": ["FIND", "F"],
     "help": "Finds an entry or directory with the name specified.\n" +
     "eg: find <name>\n",
     "requires_param": True,
     "takes_param": True,
     "method": None},

	{"command": ["MOVE", "MV"],
     "help": "Moves an entry to the desired location.\n" +
     "eg: move <original full path> <new full path>\n",
     "requires_param": True,
     "takes_param": True,
     "method": None},

    ]

  @classmethod
  def exists(self, c):
    for command in self._commands:
      if c in command['command']:
        return True

    return False

  @classmethod
  def _get_command(self, c):
    for command in self._commands:
      if c in command['command']:
        return command

    return None

  @classmethod
  def get_help(self, c):
    if Commands.exists(c):
      return(Commands._get_command(c)['help'])
    return None

  @classmethod
  def call(self, c, param):
    if self.exists(c):
      #try:
        command = self._get_command(c)
        if command['requires_param'] and param is None:
          print "'" + c.lower() + "'" + " requires parameter(s)"
          print self.get_help(c)
        elif command['takes_param']:
          command['method'](param)
        else:
          command['method']()
      #except TypeError:
        #print "This command has not yet been implemented."

  @classmethod
  def set_method(self, c, method):
    if self.exists(c):
      self._get_command(c)['method'] = method

  @classmethod
  def get_command_list(self):
    l = ''
    for command in self._commands:
      # only take the first command in the list
      if len(command['command']) > 0:
        l += command['command'][0] + " "

    return l

  @classmethod
  def parse(self, command, param):
    if command is None:
      logger.error("No command provided")
      return False

    if Commands.exists(command.upper()):
      Commands.call(command.upper(), param)
      return True
    else:
      return False

