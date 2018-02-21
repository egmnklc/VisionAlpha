<h1 id="welcome-to-visionalpha-by-cru-team">Welcome to VisionAlpha by Cru Team!</h1>
<p>&nbsp;&nbsp;This is a face recognition application created by Cru Team and powered by cv2 and face_recognition. That program also provides Command Line Interface.</p>
<ol>
  <h2>What does this project do?</h2>
  <p>&nbsp;&nbsp;VisionAlpha is designed to recognize faces from a laptop or ip camera. Delay is reduced as much as possible for the best results. Here are some options that you can decide on VisionAlpha</p>
<li>Option 1: Face recognition from your camera.</li>
<li>Option 2: Face recognition from ip camera.</li>
<li>Option 3: Print user database.</li>
<li>Option 4: Add new user.</li>
<li>Option 5: Remove a pre-existing user.</li>
<li>Option 6: Quit.</li> 
   <h1 align = "center">Here are some information about AlphaVision.</h1>
  <p>VisionAlpha is powered by face_recgnition and cv2 modules. It's currently working perfectly on Python 2.7.14.</p>
    <br>
    <h2>What does the options do?</h2>
  <h3>Option 1</h3>
  <p>&nbsp;&nbsp;The ip parameter is set to False in the recognize_people function. So, when Option 1 is called, program calls the 
  recognize_people function and starts the else condition. For now, the defaut camera port is set to 0, because the 
  default port for built-in laptop cameras is 0. It may be replaced with a raw_input and according to the user input, cv2.VideoCapture() can use the given port number.</p>
  <h3>Option 2</h3>
    <p>&nbsp;&nbsp;Option 2 calls the recognize_people function with True, so if condition starts running. As said, cv2.VideoCapture() starts the action from camera and then, cv2 and face_recognition module magic happens.</p>
  <h3>Option 3</h3>
  <p>&nbsp;&nbsp;It prints out the people.json file which is located in the VisionAlpha-master/people.json</p>
  <h3>Option 4</h3>
  <p>&nbsp;This option takes a photo from your computer's webcam and asks for a name to save it into /VisionAlpha-master/users file. It also adds .jpg extension in order to make it usable for VisionAlpha. With the given information, it writesthe user number,name and related photo path to people.json.</p>
  <h3>Option 5</h3>
  <p>&nbsp;&nbsp;It deletes the user from program and also th photograph.</p>
  <h3>Option 6</h3>
  <p>&nbsp;&nbsp;Exits the program.</p>
<p>&nbsp;&nbsp;VisionAlpha allows you to use an ip camera, or a built-in laptop camera for opencv face recognition. The program can log in to any ip camera's stream link ,such as: "http://xxx.xxx.xxx/axis-cgi/mjpg/video.cgi". It logins the destination site from the adress bar, which allows it to fill in authorization boxes. To be more specific, when you select option 2 and put in the information program asks to you, it sums them all and concludes a link like the following: "http://username:password@xxx.xxx.xxx.xxx/axis-cgi/mjpg/video.cgi". Then, after this authorization, program uses the stream link like a camera port and starts to scan for faces in the stream, when it detects a known face, prints out the Username and the system date-time. When an unknown face appears, it prints out Unkown and date-time.</p> 
</ol>
<h1 id="example">A screenshot from project</h1>
<p><img src="https://github.com/hmertuygun/VisionAlpha/blob/master/example.jpg?raw=true" alt="enter image description here"></p>
<sup><i>The screenshot is from option 2, which recognizes faces from decided laptop camera.</i></sup>

