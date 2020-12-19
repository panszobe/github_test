import face_recognition
from PIL import Image, ImageDraw

image = face_recognition.load_image_file(r'C:\Users\57884\PycharmProjects\LearningPythonMore\test\need_recognize_face\unknown_2.jpg')
face_landmarks_list = face_recognition.face_landmarks(image)
print("I found {} face(s) in this photograph.".format(len(face_landmarks_list)))

for face_landmarks in face_landmarks_list:
   #打印此图像中每个面部特征的位置
    facial_features = [
        'chin',
        'left_eyebrow',
        'right_eyebrow',
        'nose_bridge',
        'nose_tip',
        'left_eye',
        'right_eye',
        'top_lip',
        'bottom_lip'
    ]

    for facial_feature in facial_features:
        print("The {} in this face has the following points: {}".format(facial_feature, face_landmarks[facial_feature]))

#让我们在图像中描绘出每个人脸特征！
    pil_image = Image.fromarray(image)
    d = ImageDraw.Draw(pil_image)

    for facial_feature in facial_features:
        d.line(face_landmarks[facial_feature], width=5)

    pil_image.show()

face_locations = face_recognition.face_locations(image)
for face_location in face_locations:
        # 打印每张脸的位置信息
        top, right, bottom, left = face_location
        print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))
# 指定人脸的位置信息，然后显示人脸图片
        face_image = image[top:bottom, left:right]
        pil_image = Image.fromarray(face_image)
        pil_image.show()
