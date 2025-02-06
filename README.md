# ws_TaskPlanner
Task Planning and Makespan Reduction Under Uncertainty

# Dependencies
* Ubuntu 22.04 (Linux Mint 21.3)
* Python 3.10

# Install
`git clone --recurse-submodules -j4 git@github.com:jwatson-CO-edu/ws_TaskPlanner.git`

## ROS2 @ Ubuntu 22.04 (Linux Mint 21.3)
[ROS2 Humble Hawksbill](https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debs.html)  
1. `sudo apt install software-properties-common`
1. `sudo add-apt-repository universe`
1. `sudo apt update && sudo apt install curl -y`
1. `sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg`
1. `echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null`
1. `sudo apt update && sudo apt upgrade`
1. `sudo apt install ros-humble-desktop`
1. `sudo apt install python3-colcon-common-extensions`
1. `sudo apt install python3-rosdep2`
1. Add to "~/.bashrc": `source /opt/ros/humble/setup.bash`
1. Add to "~/.bashrc": `export ROS_DOMAIN_ID=101`, NOTE: Your ID may be different!
1. Add to "~/.bashrc": `alias srcloc='source install/local_setup.bash'`, Shortcut for per-session init
1. Optional, Add to "~/.bashrc": `alias python3='/usr/bin/python3.10'`
1. Optional: `sudo apt install ros-humble-turtlesim`

## UR5 Control
1. `python3.10 -m pip install ur_rtde --user`

## Env Init
From the "src" directory
1. `rosdep update`
1. `rosdep install -i --from-path src --rosdistro humble -y`
1. `colcon build`