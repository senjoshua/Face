import face_recognition

# Load the jpg files into numpy arrays
josh_image = face_recognition.load_image_file("josh.jpg")
unknown_image = face_recognition.load_image_file("josh2.jpg")


# Get the face encodings for each face in each image file
try:
    josh_face_encoding = face_recognition.face_encodings(josh_image)[0]
    unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]
except IndexError:
    print("Not able to locate any faces!")
    quit()

known_faces = [
    josh_face_encoding
]

# results is an array of True/False telling if the unknown face matched anyone in the known_faces array
results = face_recognition.compare_faces(known_faces, unknown_face_encoding)

print("Is this image of Josh? {}".format(results[0]))
print("Is this image of Josh? {}".format(results[1]))
