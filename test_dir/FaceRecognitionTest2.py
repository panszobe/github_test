import face_recognition

pjj_image = face_recognition.load_image_file(r'C:\Users\57884\PycharmProjects\LearningPythonMore\test\known_face\panjinjun.jpg')
unknown_image = face_recognition.load_image_file(r'C:\Users\57884\PycharmProjects\LearningPythonMore\test\known_face\hezhao.jpg')


#获取每个图像文件中每个面部的面部编码
#由于每个图像中可能有多个面，所以返回一个编码列表。
#但是由于我知道每个图像只有一个脸，我只关心每个图像中的第一个编码，所以我取索引0。
pjj_face_encoding = face_recognition.face_encodings(pjj_image)[0]
print("pjj_face_encoding:{}".format(pjj_face_encoding[0]))
print("pjj_face_encoding:{}".format(pjj_face_encoding[1]))
print("pjj_face_encoding:{}".format(pjj_face_encoding))


# # print("unknown_face_encoding :{}".format(unknown_face_encoding))
#
# known_faces = [
#     pjj_face_encoding
# ]
#
# for unknown_face_encoding in face_recognition.face_encodings(unknown_image):
#     print("unknown_face_encoding :{}".format(unknown_face_encoding))
#     #结果是True/false的数组，未知面孔known_faces阵列中的任何人相匹配的结果
#     results = face_recognition.compare_faces(known_faces, unknown_face_encoding)
#     print("result :{}".format(results))
#     print("这个未知面孔是 潘金俊 吗? {}".format(results[0]))
#     print("这个未知面孔是 我们从未见过的新面孔吗? {}".format(not True in results))
