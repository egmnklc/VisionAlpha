<h1 id="welcome-to-visionalpha-by-cru-team">Welcome to VisionAlpha by Cru Team!</h1>
<p>This is a face recognition application created by Cru Team. That program also provides Command Line Interface.</p>
<ol>
<li>Option 1: Face recognition from your camera.</li>
<li>Option 2: Face recognition from ip camera.</li>
<li>Option 3: Print user database.</li>
<li>Option 4: Add new user.</li>
<li>Option 5: Remove a pre-existing user.</li>
<li>Option 6: Quit.</li>
<p>The application allows you to use an ip camera, or a built-in laptop camera for opencv face recognition. The program can log in to any ip camera's stream link ,such as: "http://xxx.xxx.xxx/axis-cgi/mjpg/video.cgi". It logins the destination site from the adress bar, which allows it to fill in authorization boxes. To be more specific, when you select option 2 and put in the information program asks to you, it sums them all and concludes a link like the following: "http://username:password@xxx.xxx.xxx.xxx/axis-cgi/mjpg/video.cgi". Then, after this authorization, program uses the stream link like a camera port and starts to scan for faces in the stream, when it detects a known face, prints out the Username and the system date-time. When an unknown face appears, it prints out Unkown and date-time.</p> 
</ol>
<h1 id="example">Example</h1>
<p><img src="https://github.com/hmertuygun/VisionAlpha/blob/master/example.jpg?raw=true" alt="enter image description here"></p>

