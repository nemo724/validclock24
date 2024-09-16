def validclock24(time):
    colon_count=time.count(":")

    if colon_count!=1 and colon_count!=2:#콜론이 없으면 시각 표현이 아님
        return False
    
    elif colon_count==1:# 시 분만 ex)12:00
        if len(time)!=5:
            return False
        
        hh,mm=time.split(":") #hh=12 mm=00이 담김 

        if (len(hh)==2 and hh.isdigit())==False:#and의 항등법칙에 의하여 둘 중 하나만 False여도 결과는 False
            return False#시 길이가 2여야하고 정수로 바꿀 수 있어야만 1차 통과
        
        if (len(mm)==2 and mm.isdigit())==False:#and의 항등법칙에 의하여 둘 중 하나만 False여도 결과는 False
            return False#분 길이가 2여야하고 정수로 바꿀 수 있어야만 1차 통과
        
        if((0<=int(hh)<=23 and 0<=int(mm)<=59) or (int(hh)==24 and int(mm)==0 ))==False:#or의 항등법칙으로 둘 중 하나의 값으로 False 판단
            return False# 시 분이 각각 0부터 12이하,0부터 59이하 이거나 24:00이여만 참
        
        else:#위의 모든 과정을 거치면 참만 남게 됨
            return True
     
    elif colon_count==2:# 시 분 초를 포함 ex)12:00:00
        if len(time)!=8:
            return False
        
        hh,mm,ss=time.split(":")

        if (len(hh)==2 and hh.isdigit())==False:#and의 항등법칙에 의하여 둘 중 하나만 False여도 결과는 False
            return False#시 길이가 2여야하고 정수로 바꿀 수 있어야만 1차 통과
        
        if (len(mm)==2 and mm.isdigit())==False:#and의 항등법칙에 의하여 둘 중 하나만 False여도 결과는 False
            return False#분 길이가 2여야하고 정수로 바꿀 수 있어야만 1차 통과
        
        if (len(ss)==2 and ss.isdigit())==False:#and의 항등법칙에 의하여 둘 중 하나만 False여도 결과는 False
            return False#초 길이가 2여야하고 정수로 바꿀 수 있어야만 1차 통과
        
        if((0<=int(hh)<=23 and 0<=int(mm)<=59 and 0<=int(ss)<=59 ) or (int(hh)==24 and int(mm)==0 and int(ss)==0))==False:#or의 항등법칙으로 둘 중 하나의 값으로 False 판단
            return False# 시 분 초가 각각 0부터 12이하,0부터 59이하,0부터 59이하 이거나 24:00:00이여만 참
        
        else:#위의 모든 과정을 거치면 참만 남게 됨
            return True