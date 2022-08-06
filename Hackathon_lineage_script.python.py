def parseSqlLineage(sql_script):
    
    dict = {}
    for i in range(len(sql_script)):
        if(sql_script[i] == "."):
            j= i - 1
            prev = ""
            while(j > 1 and sql_script[j]!="," and sql_script[j]!=" "):
                prev = sql_script[j] + prev
                j-=1
            nextp = i + 1
            ndata = ""
            while(nextp < len(sql_script) and (sql_script[nextp]!="," and sql_script[nextp]!=" ")):
                ndata+=sql_script[nextp]
                nextp+=1
            dict[prev] = ndata
    splitted = sql_script.split(" ")
    splitted  
    dict1 = {}
    tbnamearray = []
    tbaliasarray = []
    for i in range(len(splitted)):
        if(splitted[i] == "from"):
            np=i+1
            if("." in splitted[np]):
                tbname = splitted[np].split(".")[1]
                if(tbname[len(tbname) - 1] == ")"):
                    finaltbname = tbname[0:len(tbname) - 1]
                    tbnamearray.append(finaltbname)
                else:
                    tbnamearray.append(tbname)
            elif(")" in splitted[np]):

                tbname = splitted[np].split(")")[0]
                tbnamearray.append(tbname)

        res=""
        if(";" in splitted[i]):
            res = splitted[i].split(";")[0]
            tbaliasarray.append(res)
        if(",(" in splitted[i]):
            res = splitted[i].split(",(")[0]
            tbaliasarray.append(res)
        if(", (" in splitted[i]):
            res = splitted[i].split(", (")[0]
            tbaliasarray.append(res)
    for i in range(len(tbnamearray)):
        dict1[tbaliasarray[i]] = tbnamearray[i]

    final_out = []
    for key in dict1:
        temp = {}
        temp["columnName"] = dict[key]
        temp["tableName"] = key

        final_out.append(temp)
    return final_out

# this is for the Demo
sql_script="select a.uid,b.uname from (select * from user) a,(select * from user_details) b;"

parseSqlLineage(sql_script)