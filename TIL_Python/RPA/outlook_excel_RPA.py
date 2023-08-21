'''
1. 프로그램 컨셉
위 프로그램은 사내 Outlook(전자메일)을 활용하면서 메일의 자료를 주기적으로 취합해야하는 사용자에게 유용합니다. 예를 들면, 메일로 오는 발주서, 수주 양식 파일들을 자동으로 다운받고 엑셀로 취합해야 하는 경우 활용할 수 있습니다.

Concept1. Outlook(전자메일)을 사용하고 아래와 같이 메일에 첨부 엑셀 파일이 있는 경우 활용할 수 있습니다.

Concept2. 첨부 엑셀 파일의 데이터를 아래 엑셀과 같이 자동으로 한개 엑셀파일로 취합합니다.
'''


import win32com.client
import os
import pandas as pd

#outlook 정해진 폴더에서 첨부파일을 다운로드 하는 함수
#flodername : outlook 폴더명, downpath : 다운받을 위치
def att_down(foldername, downpath):
    outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
    inbox = outlook.GetDefaultFolder(6).Folders[foldername]
    messages = inbox.Items

    no = 1 #중복 파일명이 있을 것을 대비해 추가한 파일명 인덱스
    m_count = 1 #메일 카운트
    #각 메일마다 첨부파일을 다운로드 하는 루프
    for ms in messages:

        attachments = ms.Attachments #해당 메일의 첨부파일 개수(integer)
        r = attachments.count
        print(str(m_count)+"번째 메일 첨부파일 개수 : ",str(r)+"개")
        m_count=m_count+1
        for i in range(1, r + 1):
            attachment = attachments.Item(i)
            attachment.SaveASFile(downpath + str(no) + "_" + str(attachment))  # 파일명을 넣어야 함.
            no = no + 1


def att_df(downpath):
    filelist = os.listdir(downpath)
    df_list = []

    #각각 파일을 데이터프레임화해서 리스트에 넣기 
    for fn in filelist:
         df = pd.read_excel(downpath+"/"+fn, engine="openpyxl")
         df.dropna(inplace =True)
         df_list.append(df)
    print(df_list)

    return df_list

def att_merge(df_list):
    count = len(df_list)

    if count == 1:
        result = df_list[0]

    elif count == 2:
        result = pd.concat([df_list[0], df_list[1]], ignore_index=True)

    else:
        temp = df_list[0]
        for i in range(1, count):
            result = pd.concat([temp, df_list[i]], ignore_index=True)
            temp = result

    print(result)
    result.to_excel("outlook결과파일.xlsx")


###첨부파일 다운로드 하기
fn = "받은편지함 폴더명"
downpath = "첨부파일 다운받을 경로"
att_down(fn, downpath)
df_list = att_df(downpath)
att_merge(df_list)



