'''
win32com 통해 전자메일(Outlook) 다루기

win32com.client 모듈을 사용하면 사내에서 사용하는 Outlook 전자메일을 자동화할 수 있습니다. 대표적인 자동화 예로, Outlook 메일을 다수의 사람들에게 자동 발송할 수 있습니다. 또한, 첨부파일들을 한번에 다운받거나 메일의 내용들을 엑셀 파일에 한번에 취합하는 것도 가능합니다.

위와 같은 자동화 기능을 구현하려면 win32com.client를 사용해서 outlook 전자메일을 제어할 수 있는 기초적인 방법에 대해 알아야 합니다. 이번 파트에서는 Outlook 이메일을 파이썬을 통해 제어하는 방법에 대해 알아보겠습니다.
'''


# 1. import
import win32com.client


# 2. 메일 보내기(송신)
# 1) Outlook Application에 대한 객체 생성하기
# Outlook을 제어할 때 가장 첫번째로 해야할 일은 Outlook 프로그램을 여는 것입니다. 코드에서는 Outlook 프로그램에 대한 객체를 설정해준다고 표현합니다. (위 이미지에서 첫번째 과정)
outlook=win32com.client.Dispatch("Outlook.Application")

# 2) 메일을 보내기 위한 객체 생성
# 1)에서 생성한 outlook 객체를 이용해 "메일 보내기" 창을 열어보겠습니다. CreateItem( )이라는 함수를 사용합니다. CreateItem(0)은 메일 보내기 창을 새로 생성하는 코드입니다. send_mail이라는 변수로 설정하여 이 변수가 메일보내기 창의 객체 성질을 가질 수 있게 합니다.
send_mail = outlook.CreateItem(0)

# 3) 메일 보내기에 필요한 정보 입력
# 2)에서 send_mail은 메일 보내기 창의 객체 성질을 가진다고 언급했습니다. 저희가 메일을 보낼 때, 기본적으로 입력해야 하는 정보들이 있습니다. send_mail은 이 메일 보내기 창의 성질(속성)들을 가지게 됩니다. 아래 코드처럼요. 수신인, 참조, 제목, 메일내용 등을 문자열을 입력해보겠습니다.
# 한가지 알아두어야 할 점은 메일의 본문 작성은 HTML 형태라는 것입니다. HTML의 각 태그를 통해 메일을 꾸밀 수도 있다는 점 참고하시면 됩니다.
send_mail.To = "수신인@gmail.com" #메일 수신인
send.mail.CC = "참조@gmail.com" #메일 참조
send_mail.Subject = "사장님 몰래 하는 파이썬 업무 자동화" #메일 제목
send_mail.HTMLBody = "들키면 일이 많아지니 몰래할 것!" #내용

# 4) 메일 보내기
# 메일은 Send( ) 라는 함수를 통해 보낼 수 있습니다. 위에서 설정했던 send_mail 변수를 통해 Send( ) 를 사용해봅시다.
# 코드를 작성해서 실행해보면 Outlook에서 아래 메일이 작성되어 수신자, 참조자에게 송신된 것을 확인하실 수 있습니다.
send_mail.Send() #메일 보내기


# 3) 메일 받기(수신)
# 1) Outlook Application에 대한 객체 생성하기
# 메일 송신과 마찬가지로 수신시에도 Outlook에 대한 객체를 생성해주어야 합니다. 위 그림에서 Outlook App 객체를 생성하는 부분입니다. 아래와 같이 코드를 작성해보겠습니다.
outlook=win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
# 메일 송신시와 차이가 있는 부분은 뒤에 .GetNamespace("MAPI")라는 부분입니다.
# MAPI는 메일을 수신할 때 필요한 프로토콜입니다. 프로토콜은 표준, 규약이라는 의미입니다. Outlook 메일을 사용할 때 송신자와 수신자 간의 약속이라고 생각하시면 됩니다. 자세한 내용은 모르셔도 사용하시는데 무관하며, win32com.client를 사용하여 메일 수신시 사용해야 하는 코드라고 이해하시면 됩니다.

# 2) 메일 수신함 설정하기
# Outlook 전자메일을 사용할 때, 받은 메일을 확인하는 과정을 생각해봅시다. Outlook 프로그램을 실행하고 받은 편지함을 선택합니다. 그 다음, 오른쪽 메일 리스트에서 보고 싶은 메일을 선택합니다. 위 그림에서 inboxfolder와 messges에 해당하는 부분입니다.
# 받은 편지함 선택(객체 생성), 6번은 받은 편지함(inbox folder) 의미
inboxfolder = outlook.GetDefaultFolder(6) 

#받은 편지함의 messgae 받아오기(모든 메시지)
messages = inboxfolder.Items

#메시지 목록 출력해보기
for  mail  in  messages:
    print(mail)

# 결과
#메일 목록 출력
# <COMObject <unknown>>
# <COMObject <unknown>>


# 3) 받은 메일 출력해 보기

# 실제로 받은 메일의 보낸이, 제목, 메일 내용 등 메일 정보를 출력
# 받은 편지함 설정
inboxfolder = outlook.GetDefaultFolder(6)

# 받은 편지함의 message 받아오기(모든 메시지)
messages = inboxfolder.Items

# 2)에서 설정했던 객체인 messges를 for 반복문을 사용해서 각 메일의 정보를 출력
i = 1 # 여러 메일 출력을 위한 인덱싱

# 각 메일에 대한 정보를 for 반복문을 통해 출력
for mail in messages:
    print(str(i) + "번째 메일의 발신인 : " + mail.SenderName)
    print(str(i) + "번째 메일의 수신인 : " + mail.To)
    print(str(i) + "번째 메일의 제목 : " + mail.Subject)
    print(str(i) + "번째 메일의 받은시간 : " + str(mail.ReceivedTime))
    print(str(i) + "번째 메일의 내부내용 : " + mail.Body)
    print('\n')
    i = i + 1


# 4) 첨부파일 다운 받기
#받은 편지함 설정
inboxfolder = outlook.GetDefaultFolder(6) 

#받은 편지함의 messgae 받아오기(모든 메시지)
messages = inboxfolder.Items

no = 1 #중복 파일명이 있을 것을 대비해 추가한 파일명 인덱스
m_count = 1 #메일 카운트
#각 메일마다 첨부파일을 다운로드 하는 루프
for ms in messages:

    attachments = ms.Attachments #해당 메일의 첨부파일 객체 설정
    r = attachments.count #해당 메일의 첨부파일 개수(integer)
    print(str(m_count)+"번째 메일 첨부파일 개수 : ",str(r)+"개")
    m_count=m_count+1
    #해당 메일의 첨부파일을 모두 저장
    for i in range(1, r + 1):
        attachment = attachments.Item(i)
        attachment.SaveASFile("경로" + str(no) + "_" + str(attachment))  # 파일명 설정
        no = no + 1

# 결과
# 첨부파일 목록 객체 생성 : <COMObject <unknown>> 첨부파일 개수 : 1
# 첨부파일 목록 객체 생성 : <COMObject <unknown>> 첨부파일 개수 : 2
# 첨부파일 목록 객체 생성 : <COMObject <unknown>> 첨부파일 개수 : 1


# 2) 메일 수신함 설정하기"에서도 다뤘지만 inboxFolder.Items 라는 구문을 통해 받은 편지함의 메일 리스트를 객체로 생성할 수 있다고 언급했습니다.(위 변수 중 messages)
# 객체 변수 messages가 for문을 통해 반복하면 각 받은편지함의 1개 메일의 특성을 갖게 됩니다. 따라서 위 코드처럼 ms.Attachments의 의미는 각 메일 1개에 포함되어있는 첨부파일 목록을 의미합니다.
# ms.attachments는 첨부파일 목록이므로 다시 아래 코드와 같이 개별 파일에 접근할 수 있게됩니다.

# 개별 파일에 접근
# 각 메일마다 첨부파일 객체 생성
for  ms  in  messages:
    attachments = ms.Attachments #해당 메일의 첨부파일 목록 객체 설정
    for  onefile  in  attachments: #첨부파일 목록을 다시 개별파일로 접근
        print(onefile)

# <결과>
# 요청1.xlsx 
# 요청2.xlsx 
# 요청3.xlsx 
# 요청4.xlsx


# 첨부파일 저장
#각 메일에 접근하는 루프
for  ms  in  messages:

    attachments = ms.Attachments #해당 메일의 첨부파일 객체 설정
    file_num = attachments.count #해당 메일의 첨부파일 개수 확인
    print("현 메일의 파일 건수 : ", file_num)

#파일을 저장하는 루프
    for  i  in  range(1, file_num+1):
        one_file = attachments.Item(i) #메일의 개별 첨부 파일을 객체로 생성
        print(one_file) #파일명 출력

        one_file.SaveASFile(str(one_file)) #파일 명 그대로 저장
