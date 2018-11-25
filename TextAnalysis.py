def text_processor(superman):
    inpi2 = superman.lower()
    inpi3 = ""
    ctr = 0
    for jar in inpi2:
        if inpi2[ctr].isalpha() or inpi2[ctr].isnumeric() or inpi2[ctr] == " ":
            inpi3 = inpi3 + jar
        ctr = ctr + 1
    setfin = []
    super = []
    wonder = {}
    super = inpi3.split()
    for x in range(len(super)):
        wonder[super[x]] = 1
 
    for elm in range(len(super)):
        if super[elm] not in setfin:
            setfin.append(super[elm])
        else:  
            wonder[super[elm]] += 1

    replist2 = []
    totstr = ""
    for elm3 in wonder:
        repstr = str(wonder[elm3]/100) + ": " + elm3
        replist2.append(repstr)
    replist2.sort(reverse = True)
    for e in replist2:
        valstr = e[:4]
        vala = float(valstr)
        valb = vala * 100
        val = int(valb)
        for ex in range(val):
            astr = e[6:]
            totstr += astr + " "
    return totstr

  ## THE GHOST OF THE SHADOW ##