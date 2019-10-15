from hanspell import spell_checker
import os
import pandas as pd
import re
import json
import sys

global csv_file_name
# global df

def read_csv():    
        data = pd.read_csv(csv_file_name)  
        global df 
        df =  pd.DataFrame(data)

def spell_check():
    # print(df.columns)

    df["TEMP_txt"] = ""
    end = len(df)-1
    for i in range(0,end):
        sentents = remove_useless(df["Image_Content_txt_result"][i])
        if(sentents == ''):
            sentents = remove_useless(df["Content_txt"][i])
        # print(sentents)
        result = spell_checker.check(sentents)
        
        df["Spell_Checked_Content"][i] = result.checked
        print("#" + str(end) + " : " + str(i))        
        # print(str(i) +"# :" + result.checked)

    df.to_csv("Final_data_spell_checked.csv", mode= 'w')
    print("csv file successfully generated!")

def viewText():
     for i in range(0,len(df)-1):
         print(df["Spell_Checked_Content"][i])

def remove_useless(sentents):
    hashtag_regex = "[&*$%]|([a-zA-Z0-9._%+-]+)@([a-zA-Z0-9.-]+)(\.[a-zA-Z]{2,4})| #([0-9a-zA-Z가-힣.]*)|@([0-9a-zA-Z가-힣_.]*)|"
    # url에 영향을 주는 특수문자 제거 ,이메일, 해쉬태그, @아이디, ID
    # print(sentents)
    try :
        replacement = re.sub(hashtag_regex, "", sentents)
    except :
        return ""

    return replacement
    


if __name__ == "__main__":
    if(len(sys.argv) == 1):
        print("missing argument!")
        sys.exit()

    csv_file_name = "./" + sys.argv[1]

    os.system('clear')
    print("Start Spell Checker")
    read_csv()
    spell_check()

    # viewText()