import os

def create_new_dir(_out_dir):
  if os.path.exists(_out_dir):
    _check = input(f"This operation will \033[31mREWRITE\033[0m the \033[1;31m{_out_dir}\033[0m\n Are you sure?(yes/no)")
    import shutil
    if _check == "yes":
      shutil.rmtree(_out_dir)
    else:
      _continue = input("Do you want to create a new dir?(yes/no)")
      _t = 0
      if _continue == "yes":
        while _t < 3:
          _tmp_dir1 = input("Please input dir you want to save to: ")
          _tmp_dir2 = input("Please input again: ")
          if (_tmp_dir1 != _tmp_dir2) or os.path.exists(_tmp_dir1):
            errorer.error(ecolor.format("The two input directories are inconsistent. Or, dir is exists."))
            _t += 1
            if _t >= 3:
              errorer.error(ecolor.format("Too many errors. Exit."))
              exit(-1)
            else:
              errorer.error(ecolor.format("Please try again and input a new dir"))
          else:
            _out_dir = _tmp_dir2
            break
      else:
        errorer.error(ecolor.format("Exit."))
        exit(-1)
  return _out_dir

def count_errors(_srcs, _trgs, log, _pat):
  cnt = 0
  with open(log, 'w') as f:
    for _f in _srcs:
      if f"{os.path.splitext(os.path.basename(_f))[0]}{_pat}" not in _trgs:
        cnt += 1
        f.write(f"{_f}\n")
    if cnt == 0:
      f.write("No errors.\n")
  return cnt