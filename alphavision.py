import face_recognition
from time import gmtime, strftime
import cv2

print'__    __     _                           '       '_' '  '
print'/ / /\ \ \___| | ___ ___  _ __ ___   ___   '+'   | | ____  '
print'\ \/  \/ / _ \ |/ __/ _ \| ''_' '`' '_'' ' ''+   '\ /  _ \ |'
print' \  /\  /  __/ | (_| (_) | | | | | |  __/  '+'   | || (_) |'
print'  \/  \/ \___|_|\___\___/|_| |_| |_|\___|  '+'    \__\___/ '
                                                    
print'   ___                 __                            _              '
print'  / __\ __ _   _      /__\ ___  ___ ___   __ _ _ __ (_)_______ _ __ '
print' / / | ''__''| | | |    / \/// _ \/ __/ _ \ / _` | ''_ \| |_  / _ \ ''__|'''
print'/ /__| |  | |_| |   / _  \  __/ (_| (_) | (_| | | | | |/ /  __/ |   '
print'\____/_|   \__,_|___\/ \_/\___|\___\___/ \__, |_| |_|_/___\___|_|   '
print'               |_____|                   |___/                      '
print'Usage guide: \n 1) Type in the ip of destination \n 2) Put in the port number, if none, hit enter.\n 3) Type the username that you use to log in with. \n 4) Type the password that you use to log in with. '
print '\n\n\n'

# Get a reference to webcam #0 (the default one)
camera_ip, port_number, user_name, user_password = raw_input("Ip of destination camera:"),raw_input("Port Number:"), raw_input("Username asked for authentication:"),raw_input("Password asked for the authorization:")                                           
video_capture = cv2.VideoCapture("http://"+user_name+":"+user_password+"@"+camera_ip+":"+port_number+"/video")
# Load a sample picture and learn how to recognize it.
egemen_image = face_recognition.load_image_file("whodis.jpg")
egemen_face_encoding = face_recognition.face_encodings(egemen_image)[0]
annem_image = face_recognition.load_image_file("whoyou.jpg")
annem_face_encoding = face_recognition.face_encodings(annem_image)[0]
obama_image = face_recognition.load_image_file("obama.jpg")
obama_face_encoding = face_recognition.face_encodings(obama_image)[0]
ferhat_image = face_recognition.load_image_file("ferhat.png")
ferhat_face_encoding = face_recognition.face_encodings(ferhat_image)[0]
ege_image = face_recognition.load_image_file("ege.jpg")
ege_face_encoding = face_recognition.face_encodings(ege_image)[0]
ceren_image = face_recognition.load_image_file("ceren1.jpg")
ceren_face_encoding = face_recognition.face_encodings(ceren_image)[0]
husnumert_image = face_recognition.load_image_file("mertuygun.jpg")
husnumert_face_encoding = face_recognition.face_encodings(husnumert_image)[0]
reiz_image = face_recognition.load_image_file("reiz.jpg")
reiz_face_encoding = face_recognition.face_encodings(reiz_image)[0]


# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]

    # Only process every other frame of video to save time
    if process_this_frame:
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            match = face_recognition.compare_faces([egemen_face_encoding, annem_face_encoding, ferhat_face_encoding, ege_face_encoding, ceren_face_encoding, husnumert_face_encoding, reiz_face_encoding], face_encoding, tolerance=0.5)
            name = "Unknown"

            if match[0]:
                name = "Egemen"
                print 'Mathematics Professor: ' + strftime("%Y-%m-%d %H:%M:%S", gmtime()) + ' logged in.'
            elif match[1]:
                name = "Validem"
                print 'Validem' 
            elif match[2]:
                name = "Ferhat"
                print "Ferat"
            elif match[3]:
                name = "Ege"
                print "Ege"
            elif match[4]:
                name = "Ceren"
                print "Ceren"
            elif match[5]:
                name = "HusnuMert"
                print "Husnumert"
            face_names.append(name)

    process_this_frame = not process_this_frame


    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a box around the face
    #cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Display the resulting image
        cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()
