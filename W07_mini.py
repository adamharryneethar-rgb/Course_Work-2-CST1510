"""
RECORD CHECK  -  my version
===========================

Name  :  Adam Harry
Lane  :  AI 
Date  :  13/11/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

def parse_line(raw_line):
  hostname_part,rest=raw_line.split(",",1)
  ad={"host":hostname_part.strip().lower()}
  for i in rest.split(","):
    a,b=i.split("=")
    ad[a.strip()]=float(b.strip())
  return ad
def status_of(res):
    per=res["used"]/res["total"]*100
    if  per >res["total"]:
        return "Over limit"
    elif per>90 :
          return "Warning"
    else:
          "Ok"
with open("/content/messy_lines.txt", "r") as file:
    count=0
    flag=0    
    for line in file:
      try:
        res= parse_line(line.strip())
        status=status_of(res)
        count=count+1
        print(res,status)
      except ValueError:
        flag=flag+1
        print("Could not",res)
    print(count,flag)

# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it against at least 5 genuinely messy raw records
#    [ ] Run it with a value that will not convert to a number - write the
#        error down
#    [ ] Check every function does one job, with a docstring
