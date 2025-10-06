# Base image: ROS2 Jazzy full (include Gazebo e tools principali)
FROM althack/ros2:jazzy-full

# Lavoriamo nella cartella del progetto
WORKDIR /uav_vigneto

# Disabilita prompt interattivi
ENV DEBIAN_FRONTEND=noninteractive

# Installazione pacchetti base e ROS aggiuntivi
RUN apt-get update && apt-get install -y --no-install-recommends \
    git cmake build-essential wget tree sudo ffmpeg \
    python3-tk python3-setuptools \
    ros-jazzy-plotjuggler-ros \
    ros-jazzy-ros-gz ros-jazzy-ros-gz-bridge \
    && rm -rf /var/lib/apt/lists/*

# Configura pip e installa dipendenze Python
RUN python3 -m pip config set global.break-system-packages true && \
    pip install --no-cache-dir numpy matplotlib pandas opencv-python

# === PX4 Setup ===
RUN git clone https://github.com/PX4/PX4-Autopilot.git --branch v1.15.0 --recursive \
 && bash ./PX4-Autopilot/Tools/setup/ubuntu.sh \
 && rm -rf PX4-Autopilot

# === Micro XRCE DDS Agent ===
RUN git clone https://github.com/eProsima/Micro-XRCE-DDS-Agent.git \
 && cd Micro-XRCE-DDS-Agent && mkdir build && cd build \
 && cmake .. && make -j$(nproc) && make install && ldconfig \
 && cd /uav_vigneto && rm -rf Micro-XRCE-DDS-Agent

# === Configurazione utente ===
RUN chown -R ros:ros /uav_vigneto
USER ros

# Sorgente ROS e workspace nel bashrc
RUN echo "\nsource /opt/ros/jazzy/setup.bash" >> /home/ros/.bashrc \
 && echo "if [ -f /uav_vigneto/install/setup.bash ]; then source /uav_vigneto/install/setup.bash; fi" >> /home/ros/.bashrc

CMD ["/bin/bash"]
