.. _basiccv:

Basic Vision Tutorial
=====================

Tutorial Overview
-----------------

Welcome to the Basic Vision tutorial!

The purpose of this tutorial is to give a basic introduction to using the computer vision
classes provided by this package. Specifically, this tutorial will focus on the USBCamera class
and how we can extract camera feeds from it.

Class Overview
--------------

The USBCamera class provides a simple and easy interface to capture footage from a compatible camera using OpenCV.

.. note::
    If you are unfamiliar with the USBCamera class, it is recommended that you read the :ref:`USBCamera API Page<usbcamera>`
    to gain a better understanding.


Contents
--------

Now that you are more familiar with the USBCamera class, it's time to create some basic programs using it.

Default Constructor
^^^^^^^^^^^^^^^^^^^

In order to use this class, it must first be instantiated by calling its constructor. To do this, run the following code:

.. code-block:: python

    # Import the class
    from frc_apriltags import USBCamera

    # Instantiate the class
    camera = USBCamera()

The above code will import the class from the package, create the default instance of it, and store that instance
in the camera variable. For reference, a default instance of this class assumes that the camera number is zero,
the camera path is None, the camera resolution is 0 x 0, the camera will not be calibrated, and the path to the calibration
images is "/home/robolions/Documents/2023-Jetson-Code-Test". Regardless, a default instance of this class is useless
as it is specific to FRC Team 2199, the Robo-Lions, and does not allow for much flexibility.

Constructor
^^^^^^^^^^^

To make this class useful, all of the default variables should be assigned proper values. For example:

.. code-block:: python

    # Import the class
    from frc_apriltags import USBCamera

    # Instantiate the class
    camera = USBCamera(camNum = 0, resolution = (1280, 720))

.. note::
    For the sake of this tutorial, we will not be calibrating the camera or worrying about having multiple cameras.
    Therefore, we will leave camPath, calibrate, and dirPath as their default values.

The above code will now "create" the built in webcam (if your device has a built in webcam) or the first
USB camera detected by the system (if your device does not have a built in webcam) for use inside the program.

Getting Footage
^^^^^^^^^^^^^^^

Once the camera has been created, it is now possible to get footage from the camera to use elsewhere.
To get this footage, run:

.. code-block:: python

    # Import the class
    from frc_apriltags import USBCamera

    # Instantiate the class
    camera = USBCamera(camNum = 0, resolution = (1280, 720))

    # Main loop
    while (True):
        # Get the stream
        stream = camera.getStream()

        # Press q to end the program
        if ( camera.getEnd() == True ):
            break

The above code will now get footage from the camera you have specified. Normally, cameras (especially the built in ones)
have indicators that tell you when they are being acessed. To confirm this program has worked, look for that indicator.

If you can see the indicator, congratulations! Your program works! However, you will **NOT** be able to see the stream on your
display because we have not asked the class to display it yet, an issue that will be addressed in the next section.

.. note::
    Displaying a stream is usually quite trivial for most modern AMD processors, but keep in mind that FRC-AprilTags was designed for use
    on less powerful ARM processors. Therefore, the USBCamera class hides the stream by default to save valuable processing power.

Displaying Footage
^^^^^^^^^^^^^^^^^^

To display the footage from the camera, we are going to modify the code from the previous section slightly.
The modified code looks like this:

.. code-block:: python

    # Import the class
    from frc_apriltags import USBCamera

    # Instantiate the class
    camera = USBCamera(camNum = 0, resolution = (1280, 720))

    # Main loop
    while (True):
        # Get and display the stream
        camera.displayStream(streamType = 0)

        # Press q to end the program
        if ( camera.getEnd() == True ):
            break

In this version of the code, we have substituted "stream = camera.getStream()" for "camera.displayStream(streamType = 0)".
This new method, *displayStream()*, is used isntead beacuse it automatically gets the stream type we desire (in this 0 for undistorted)
and then displays it the the screen.

Another method that needs explaination is camera.getEnd(). This method returns true when certain termination criteria has been met.
In this case, that termination criteria is the pressing of the q key. getEnd() also serves the purpose of providing a slight
delay of one milisecond by using the waitKey() function from the OpenCV library. This is an essential part of the program as
allowing the program to continue with no delay causes numerous errors within the OpenCV portions of the package.

End
^^^

Congratulations! You now have the tools to understand the basics of the USBCamera class!

The next tutorial will explain how to calibrate a camera using this class.