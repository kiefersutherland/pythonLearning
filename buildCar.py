def MybuildCar(
      brand,carType,**Info):
    info={}
    info["brand"]=brand
    info["carType"]=carType
    for k,v in Info.items():
      info[k] = v

    return info