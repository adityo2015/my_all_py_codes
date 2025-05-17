name_id={'ahnaf thamid':220211001,
         'aysha siddika':220211002,
         'mishkat jahan moumi':220211003,
         'isharat radia':220211004,}
name_id.update()
name_cgpa={'ahnaf tahmid':3.92,
           'aysha siddika':3.22,
           'mishkat jahan moumi':3.44,
           'isharat radia':3.55}
name_cgpa.update()
name_due={'ahnaf tahmid':70000,
          'aysha siddika':45000,
          'mishkat jahan moumi':20000,
          'isharat radia':30000}
name_due.update()
print('your id:',name_id.get('ahnaf thamid'),'your cgpa:',name_cgpa.get('ahnaf tahmid'),'your due:',name_due.get('ahnaf tahmid'))