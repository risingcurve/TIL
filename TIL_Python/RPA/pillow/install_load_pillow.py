'''
# Pillow 설치하고 불러오기

# Pillow 설치
# pip install pillow


# Pillow 불러오기
# from PIL import Image

# import PIL로 불러올 시, Image 모듈은 안 불러와 짐.
'''

# 고양이 이미지 불러와서 img라는 변수에 입력
img = Image.open('cat.jpg')

# 이미지 보여주기
img.show()

'''
# 이미지 파일명
print(img.filename)
>>> cat.jpg

# 이미지 형식
print(img.format)
>>> JPEG

# 이미지 크기
print(img.size)
>>> (640, 426)

# 이미지 너비
print(img.width)
>>> 640

# 이미지 높이
print(img.height)
>>> 426

# 이미지의 색상 모드
print(img.mode)
>>> RGB
'''


