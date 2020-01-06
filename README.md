# FaceGroup

Create seperate folders of friends containing images which that friend is in
Uses face_recognition python library

Usage: python facedir.py {friends_dir} {photo_dir}
Store facial information of each friend which is in the {friend_dir}
Create seperate folders for each friend
Search through {photo_dir} and copy photos to each friend's folder if they are in the photo

Log (Originally followed some tutorials for face_recognition:
- [X] recognize.py reads 2 images and checks if it the same person
- [X] camera.py uses OpenCV to use camera to determine if faces in camera match a list of known faces and highlights them
