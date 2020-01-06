import os
from sys import argv
import face_recognition
from shutil import copyfile

# create dict of known friend's faces
def known_friends(dirname):
    friends = {}
    for cur, _dirs, files in os.walk(dirname):
        for f in files:
            # only take name
            name = f.split(".")[0]
            path = os.path.join(cur, f)

            friend_image = face_recognition.load_image_file(path)
            try:
                friend_face_encoding = face_recognition.face_encodings(friend_image)[0]
                friends[name]=(friend_face_encoding)
            except:
                print("Face was not found in image: " + path)
        

    return friends

# find images with known friends and store them
def find_friends(dirname, friends):
    # loop through friends
    for key in friends:
        if not os.path.isdir(key):
                os.mkdir(key)

        # current friend encoding
        friend_encoding = friends[key]
        known_face = [
                friend_encoding
        ]

        # loop through pics dir
        for cur, _dirs, files in os.walk(dirname):
                for f in files:
                        path = os.path.join(cur, f)
                                
                        temp_image = face_recognition.load_image_file(path)
                        temp_face_encodings = face_recognition.face_encodings(temp_image)
                        # compare all faces to current friend
                        results = face_recognition.compare_faces(temp_face_encodings, known_face[0])
                        if True in results:
                                copyfile(path, key+"/"+f)
                                print(key + "-->" + f)

if __name__ == '__main__':
    # check len of args
    if len(argv) < 3:
            print("Incorrect number of arguments!\nUsage: python facedir.py {friends_dir} {photo_dir}")
            exit()

    # store friends faces in dict
    friends_dir = argv[1]
    friends = known_friends(friends_dir)

    # find images with known friends and add them to corresponding friend dirs
    photo_dir = argv[2]
    find_friends(photo_dir, friends)
