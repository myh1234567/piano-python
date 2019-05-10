import os

def kill(pid):
  # This function is used to abort the process corresponding to the incoming pid
  if os.name == 'nt':
    # Windows
    cmd = 'taskkill /pid ' + str(pid) + ' /f'
    try:
      os.system(cmd)
      print(pid, 'killed')
    except Exception as e:
      print(e)
  elif os.name == 'posix':
    # Linux
    cmd = 'kill ' + str(pid)
    try:
      os.system(cmd)
      print(pid, 'killed')
    except Exception as e:
      print(e)
  else:
    print('Undefined os.name')