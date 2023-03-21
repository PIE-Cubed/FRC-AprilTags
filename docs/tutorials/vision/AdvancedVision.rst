.. _advancedcv:

Advanced Vision Tutorial
========================

Tutorial Overview
-----------------

Welcome to the Advanced Vision tutorial!

The purpose of this tutorial is to demonstrate advanced computer vision using
classes provided by this package. Specifically, this tutorial will focus on the USBCamera,
BasicStreaming, and CustomStreaming classes. From these classes, you will learn how to use multiple
cameras reliably and how to stream camera feeds back to the Driver Station.

Class Overviews
---------------

The USBCamera class provides a simple and easy interface to capture footage from a compatible camera using OpenCV.

.. note::
    If you are unfamiliar with the USBCamera class, it is recommended that you read the :ref:`USBCamera API Page<usbcamera>`
    to gain a better understanding.

The BasicStreaming class simply allows for a camera feed to be sent back to the Driver Station.

.. note::
    If you are unfamiliar with the BasicStreaming class, it is recommended that you read the :ref:`BasicStreaming API Page<basicstreaming>`
    to gain a better understanding.

The CustomStreaming class allows you to modify the camera feed before sending it back to the Driver Station.

.. note::
    If you are unfamiliar with the CustomStreaming class, it is recommended that you read the :ref:`CustomStreaming API Page<customstreaming>`
    to gain a better understanding.

Contents
--------

Now that you are more familiar with the USBCamera class, it's time to learn about reliably using multiple cameras at once.

Multiple cameras
^^^^^^^^^^^^^^^^

Thanks to the OpenCV library, creating multiple cameras is a straightforward process.
When trying to create a camera, simply set the camNum parameter of the USBCamera class
to the number of the camera (0 for the first camera pluged in unless there is a built in webcam).

.. code-block:: python

    # Import the class
    from frc_apriltags import USBCamera

    # Instantiate the class
    cam0 = USBCamera(camNum = 0)
    cam1 = USBCamera(camNum = 1)

    # Main loop
    while (True):
        # Get and display the streams
        cam0.displayStream(streamType = 0)
        # cam1.displayStream(streamType = 0)

        # Press q to end the program
        if ( (cam0.getEnd() == True) or (cam1.getEnd() == True) ):
            break

.. warning::
    While it is possible to run this code without raising errors, OpenCV will raise a cv2.Error when you attempt to process
    the image from a non-existant camera.


Reliably using multiple cameras
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The above code is the most basic way of acessing multiple camera feeds, but, with the numbers being arbitarily
defined on OS boot, it is possible that your OS switches camera zero and camera one. To solve this, we will
specify the camPath variable and provide the camera's path, as shown below:

.. tabs::
    .. tab:: Windows
        As of now, we have not figured out a way to get the camera path for Windows.
        Until we do, please continue to use numbers to identify your cameras.

        .. code-block:: Python

            # Import the class
            from frc_apriltags import USBCamera

            # Instantiate the class
            cam0 = USBCamera(camNum = 0)
            cam1 = USBCamera(camNum = 1)

            # Main loop
            while (True):
                # Get and display the streams
                cam0.displayStream(streamType = 0)
                # cam1.displayStream(streamType = 0)

                # Press q to end the program
                if ( (cam0.getEnd() == True) or (cam1.getEnd() == True) ):
                    break

    .. tab:: macOS
        As we do not have access to devices that run macOS, we are unable to provide proper documentation at this time.

    .. tab:: Linux
        To find the path of a camera on Linux, please run the following command:

        .. code-block:: sh

            find /dev/v4l
        
        This command finds all devices that support video capturing on Linux devices.
        Unfortunately, the output of this command varies by device so we cannot provide a good example here.
        For the Jetson Nano, you are looking for something like this:

        .. code-block:: sh

            /dev/v4l/by-path/platform-70090000.xusb-usb-0:2.4:1.0-video-index0

        With the /dev/v4l path aquired, simply pass the value as a String into USBCamera as the camPath parameter.

        .. note::
            The camNum parameter is still required, but the camPath variable will be used to create the camera. 

        .. code-block:: python

            # Import the class
            from frc_apriltags import USBCamera

            # Instantiate the class
            cam0 = USBCamera(camNum = 0, camPath = "/dev/v4l/by-path/platform-70090000.xusb-usb-0:2.4:1.0-video-index0")
            cam1 = USBCamera(camNum = 1, camPath = "/dev/v4l/by-path/platform-70090000.xusb-usb-0:2.2:1.0-video-index0")

            # Main loop
            while (True):
                # Get and display the streams
                cam0.displayStream(streamType = 0)
                # cam1.displayStream(streamType = 0)

                # Press q to end the program
                if ( (cam0.getEnd() == True) or (cam1.getEnd() == True) ):
                    break

Something
^^^^^^^^^



End
^^^

Congratulations! You now have an understanding of all the computer vision functions that this package has
to offer!

The next tutorial will be on (insert topic here).