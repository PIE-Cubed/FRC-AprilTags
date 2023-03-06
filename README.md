<h1> FRC-AprilTags </h1>
<p>
	A repository that contains code to will run on FRC 2199's Nvidia Jetson Nano coprocessor during the 2023 season.
</p>

<h2> Setting Up the Jetson </h2>
<p>
	Please see the instructions <a href="https://github.com/PIE-Cubed/2023-Jetson-Code/wiki/Setup#----setting-up-the-jetson-nano" target="_blank">here</a> for setting up a Nvidia Jetson Nano.
</p>

<h2> Prerequisites </h2>
<p>
	<ul>
		<li>A <a href="https://www.python.org/downloads/" target="_blank">Python 3</a> environment (prefereably <a href="https://www.python.org/downloads/release/python-3106/" target="_blank">3.10.6</a>)</li>
		<li>The <a href="https://pypi.org/project/opencv-contrib-python/" target="_blank">OpenCV Contributor</a> package</li>
		<li>The <a href="https://pypi.org/project/numpy/" target="_blank">NumPy</a> package (should install with pupil-apriltags)</li>
		<li>The <a href="https://pypi.org/project/robotpy/" target="_blank">RobotPy</a> package</li>
		<li>The <a href="https://pypi.org/project/pupil-apriltags/" target="_blank">Pupil Apriltags</a> package</li>
	</ul>
</p>

<h2> How to install on Linux </h2>
<p>
    On linux run the following commands in order from terminal:

    sudo apt install python3 python3-dev python3-pip python3-pil python3-smbus git cmake ninja-build
</p>
<p>

    python3 -m pip install -U pip wheel setuptools frc-apriltags
</p>

<h2> How to install on Windows: </h2>
<p>
    Install <a href="https://www.python.org/downloads/release/python-3106/" target="_blank">Python 3.10.6</a> for Windows, being sure to add Python to PATH. Then, install the required packages using this command:</li>
    
    python.exe -m pip install -U pip wheel setuptools frc-apriltags
</p>

<h2> Writing Programs for Jetson </h2>
<p>
	This is addressed in the repository's wiki at <a href="https://github.com/PIE-Cubed/2023-Jetson-Code/wiki" target="_blank">https://github.com/PIE-Cubed/2023-Jetson-Code/wiki</a>.
</p>

<h2> More details </h2>
<p>
	If you'd like to learn more, all of these sections (and more!) will be explained in greater detail in the repository's wiki at <a href="https://github.com/PIE-Cubed/2023-Jetson-Code/wiki" target="_blank">https://github.com/PIE-Cubed/2023-Jetson-Code/wiki</a>.
</p>