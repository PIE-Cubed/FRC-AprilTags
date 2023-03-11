.. _install_computer:

Computer Installation
=====================

.. note:: Installation via pip typically requires internet access

FRC-AprilTags requires a Python version greater than 3.7 to be installed on your computer.
This package is also not supported on 32-bit installations of Python except on ARM coprocessors.
Therefore, you must have a 64-bit python installation on your computer.

* `Python for Windows <https://www.python.org/downloads/windows/>`_
* `Python for macOS <https://www.python.org/downloads/mac-osx/>`_

Once you have installed Python, you can use pip to install FRC-AprilTags. While it is
possible to install without pip, due to its dependencies this is not recommended nor supported.

.. tabs::
    .. tab:: Windows

        .. warning:: On Windows, the `Visual Studio 2019 redistributable <https://support.microsoft.com/en-us/help/2977003/the-latest-supported-visual-c-downloads>`_
                        is required to install this package.


        Run the following command from cmd or Powershell to install the frc-apriltags
        packages:

        .. code-block:: sh

            pip install frc-apriltags

        To upgrade, you can run this:

        .. code-block:: sh

            pip install -U frc-apriltags

        If you don't have administrative rights on your computer, either use
        `virtualenv/virtualenvwrapper-win <http://docs.python-guide.org/en/latest/dev/virtualenvs/>`_, or
        or you can install to the user site-packages directory:

        .. code-block:: sh

            pip install --user frc-apriltags


    .. tab:: macOS

        On a macOS system that has pip installed, just run the following command from the
        Terminal application (may require admin rights):

        .. code-block:: sh

            pip3 install frc-apriltags

        To upgrade, you can run this:

        .. code-block:: sh

            pip3 install --U frc-apriltags

        If you don't have administrative rights on your computer, either use
        `virtualenv/virtualenvwrapper <http://docs.python-guide.org/en/latest/dev/virtualenvs/>`_, or
        or you can install to the user site-packages directory:

        .. code-block:: sh

            pip3 install --user frc-apriltags

    .. tab:: Linux

        .. _install_linux:

        In order to install one of this packages dependecies,
        a distro that has glibc 2.35 or newer, and an installer that implements :pep:`600`,
        such as pip 20.3 or newer is required.
        You can check your version of pip with the following command:

        .. code-block:: sh

            pip3 -V

        If you need to upgrade your version of pip, it is highly recommended to use a
        `virtual environment <https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/>`_.

        If you have a compatible version of pip, you can simply run:

        .. code-block:: sh

            pip3 install frc-apriltags

        To upgrade, you can run this:

        .. code-block:: sh

            pip3 install -U frc-apriltags

        The following Linux distributions are known to work, but this list is not necessarily comprehensive:

        * Ubuntu 22.04+
        * Fedora 36+
        * Arch Linux

        If you manage to install the packages and get the following error or
        something similar, your system is most likely not compatible with RobotPy, one of this packages dependecies::

            OSError: /usr/lib/x86_64-linux-gnu/libstdc++.so.6: version `GLIBCXX_3.4.22' not found (required by /usr/local/lib/python3.7/dist-packages/wpiutil/lib/libwpiutil.so)

    .. tab:: Linux ARM Coprocessor

        Prior to installing this package on an ARM Coprocessor,
        it is highly recommended to first install RobotPy using the prebuit wheels
        provided at tortall.net.
        These wheels can be downloaded by giving the ``--find-links`` option to pip:

        .. code-block:: sh

            pip3 install -U --find-links https://tortall.net/~robotpy/wheels/2023/raspbian/ wpilib robotpy-hal robotpy-halsim-gui robotpy-installer robotpy-wpilib-utilities robotpy-wpimath robotpy-wpinet robotpy-wpiutil robotpy robotpy-cscore pyntcore pynetworktables
        
        .. warning:: 
            g++ and gcc 11 or higher are required to install this package.

        Once this is complete, install FRC-AprilTags using pip:

        .. code-block:: sh

            pip3 install frc-apriltags