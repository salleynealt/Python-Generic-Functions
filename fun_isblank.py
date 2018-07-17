def fun_isblank(prm_test_obj):
  rtn_bol_isblank = False
  typ_obj_type = type(prm_test_obj)
 
  if typ_obj_type == str:
    str_test = prm_test_obj.strip()
    if str_test == "" :
      rtn_bol_isblank = True
  elif typ_obj_type == list:
    if len(prm_test_obj) <= 0:
      rtn_bol_isblank = True
  elif typ_obj_type == dict:
    if len(list(prm_test_obj)) <= 0:
      rtn_bol_isblank = True
  elif typ_obj_type == tuple:
    if len(list(prm_test_obj)) <= 0:
      rtn_bol_isblank = True      
  return(rtn_bol_isblank)
