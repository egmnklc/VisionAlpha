from pprint import pprint
from time import gmtime, strftime
import face_recognition
import time
import cv2
import json

db_location = "people.json"

def print_cool_text():
    print "__          __  _                               _______    "
    print "\ \        / / | |                             |__   __|   "
    print " \ \  /\  / /__| | ___ ___  _ __ ___   ___        | | ___  "
    print "  \ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \       | |/ _ \ "
    print "   \  /\  /  __/ | (_| (_) | | | | | |  __/       | | (_) |"
    print "    \/  \/ \___|_|\___\___/|_| |_| |_|\___|       |_|\___/ \n"
    print "__      ___     _                      _       _           "
    print "\ \    / (_)   (_)               /\   | |     | |          "
    print " \ \  / / _ ___ _  ___  _ __    /  \  | |_ __ | |__   __ _ "
    print "  \ \/ / | / __| |/ _ \| '_ \  / /\ \ | | '_ \| '_ \ / _` |"
    print "   \  /  | \__ \ | (_) | | | |/ ____ \| | |_) | | | | (_| |"
    print "    \/   |_|___/_|\___/|_| |_/_/    \_\_| .__/|_| |_|\__,_|"
    print "                                        | |                "
    print "                                        |_|                \n\n"


def recognize_people(ip=False):
    #The program combines the
    if ip:
        print "Usage guide:"
        print " 1) Type in the ip of destination"
        print " 2) Put in the port number, if none, hit enter."
        print " 3) Type the username that you use to log in with."
        print " 4) Type the password that you use to log in with.\n"
        camera_ip = raw_input(" 1) Ip of destination camera:")
        port_number = raw_input(" 2) Port Number:")
        user_name = raw_input(" 3) Username asked for authentication:")
        user_password = raw_input(" 4) Password asked for the authorization:")
        stream_link = raw_input( "5) Live stream link of the camera:")
        video_capture = cv2.VideoCapture("http://"+user_name+":"+user_password+"@"+camera_ip+":"+port_number+"/"+stream_link)
        #Sums up the given information like
    else:
        #Default port of a built-in laptop camera is 0.
        video_capture = cv2.VideoCapture(0)

    # Load a sample picture and learn how to recognize it.
    data = fetch_users_table()
    known_face_names, usr_path = skim_dict(data, "name"), skim_dict(data, "path")
    known_face_encodings = [face_recognition.face_encodings(face_recognition.load_image_file(usr_im))[0] for usr_im in usr_path]

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
                match = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance = 0.5)
                name = "Unknown"
                if True in match:
                    match_index = match.index(True)
                    name = known_face_names[match_index]

                print(name + " " + strftime("%Y-%m-%d %H:%M:%S", gmtime()) + ' logged in.')
                face_names.append((name.split(" ")[0]))

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

        # Display video_capture.
        cv2.imshow('Video', frame)

        # Hit 'q' on keyboard to quit.
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam
    video_capture.release()
    cv2.destroyAllWindows()


def add_user(camera_port=0):
    #Since the default camera port is 0 for the laptop, the program terminates the laptop camera to take a photo.
    #It then asks for the name of the photo. Then, automatically adds .jpg extenion to make it work with the face recognition.
    camera = cv2.VideoCapture(camera_port)#Port is assigned as 0.
    time.sleep(1)#There is a 1 second sleep for the camera, because less will cause a black photo.(Camera takes the photo really fast, that's why.)
    return_value, image = camera.read()
    name = raw_input("User's Name: ")#Asks for the username.
    path = "users/" + name + ".jpg"#Saves the photo in the VisionAlpha-master/users file with the .jpg extension
    cv2.imwrite(path, image)#writes the image and the path.
    del(camera)#Deletes the camera procss.
    db_add_user(name, path)#Saves the given information to people.json file.

#db functions
def db_add_user(name, path):
    with open(db_location, "r") as json_file:
        data = json.load(json_file)
        json_file.close()
    data.update({str(count_users()+1):{"name": name, "path": path}})

    with open(db_location, "w") as json_file:
        json_file.write(json.dumps(data))
        json_file.close()

def count_users():
    with open(db_location, "r") as json_file:
        data = json.load(json_file)
        json_file.close()
        return len(data)

def print_users():
    with open(db_location, "r") as json_file:
        data = json.load(json_file)
        json_file.close()
        pprint(data)

def delete_user(id=-1):
    print("-1 to cancel")
    if id is None or -1:
        print_users()
        id = raw_input("\n What is the id of the user to be deleted?")
    if str(id) == "-1":
        print("Process terminated.")
    else:
        del_usr = select_user(id)
        print("The user " + del_usr + " is going to be deleted. Are you sure?")
        print("Press 1 to delete user, 0 to cancel")
        if cv2.waitKey(1) & 0xFF == ord("1"):
            with open(db_location, "r") as json_file:
                data = json.load(json_file)
                json_file.close()
            data[id]["name"] = "NULL"
            data[id]["path"] = "users/NULL.jpg"
            with open(db_location, "w") as json_file:
                json_file.write(json.dumps(data))
                json_file.close()
            print("Delete successful.")
        else:
            print("Operation canceled")


def select_user(id):
    with open(db_location, "r") as json_file:
        data = json.load(json_file)
        json_file.close()
    return data[id]["name"]

def fetch_users_table():
    with open(db_location, "r") as json_file:
        data = json.load(json_file)
        json_file.close()
    return data

def skim_dict(data, param):
    skimmed = [data[val][param] for val in data]
    return skimmed

def run_program(): #The main part where it asks you to choose an option, the terminates the assigned process.
    print_cool_text()
    while True:
        print "Option 1: Face recognition from your camera,"
        print "Option 2: Face recognition from ip camera,"
        print "Option 3: Print user database,"#Prints out people.json.
        print "Option 4: Add new user,"#Adds user to people.json.
        print "Option 5: Remove a pre-existing user,"#Removes person from people.json.
        print "Option 6: Quit"#Quits the program.
        usr_in = raw_input()
        if usr_in == "1":
            recognize_people()
        elif usr_in == "2":
            recognize_people(True)
        elif usr_in == "3":
            print_users()
        elif usr_in == "4":
            add_user()
        elif usr_in == "5":
            delete_user()
        elif usr_in == "6":
            print "Goodbye!"
            sys.exit()

#run the program
run_program()
