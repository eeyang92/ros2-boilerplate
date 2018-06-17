# ROS2 Boilerplate

## Setup

- Install ROS2 for your platform, make sure you have sourced the setup files
    - https://github.com/ros2/ros2/wiki/Installation
    - https://github.com/ros2/ros2/releases
    - Note: For MacOS users, disabling SIP is not necessary to get this boilerplate up and running

## To Build & Run

- `ament build --symlink-install --only-package boilerplate1`
    - Note: The `--symlink-install` options means you will only need to re-build when a new py_module is added (need confirmation)
- `. ./install/setup.bash`
    - Run this in order for the new executables to be found on the PATH
- Run
    - `listener`
    - `talker`
