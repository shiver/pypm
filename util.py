def confirm_prompt(prompt, default):
  """
  Displays a prompt until it receives either a 'y', 'n' or None
  If None encountered, the default is returned
  If 'y' True is returned
  If 'n' False is returned
  """
  while True:
    confirm = raw_input(prompt)

    confirm = confirm.strip()
    if confirm == None or len(confirm) == 0:
      # just pushed enter key
      return default
    elif confirm.upper().strip() == 'Y':
      return True
    elif confirm.upper().strip() == 'N':
      return False