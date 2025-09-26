FROM althack/ros2:jazzy-full

WORKDIR /uav_vigneto

RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    cmake \
    build-essential \
    wget \
    python3-tk \
    python3-setuptools \
    ros-jazzy-plotjuggler-ros \
    ros-jazzy-ros-gz \
    ros-jazzy-ros-gz-bridge \
    ffmpeg \
    tree \
    sudo \
    && rm -rf /var/lib/apt/lists/*

RUN python3 -m pip config set global.break-system-packages true

# PX4
RUN git clone https://github.com/PX4/PX4-Autopilot.git --branch=main --recursive \
 && bash ./PX4-Autopilot/Tools/setup/ubuntu.sh

# Micro XRCE DDS Agent
RUN git clone https://github.com/eProsima/Micro-XRCE-DDS-Agent.git \
 && cd Micro-XRCE-DDS-Agent && mkdir build && cd build \
 && cmake .. && make && make install && ldconfig \
 && cd /uav_vigneto && rm -rf Micro-XRCE-DDS-Agent

# Permessi all'utente ros
RUN chown -R ros:ros /uav_vigneto

USER ros

RUN echo "\nsource /opt/ros/jazzy/setup.bash" >> /home/ros/.bashrc \
 && echo "if [ -f /uav_vigneto/install/setup.bash ]; then source /uav_vigneto/install/setup.bash; fi" >> /home/ros/.bashrc

CMD ["/bin/bash"]
