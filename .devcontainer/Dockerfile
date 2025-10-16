FROM althack/ros2:jazzy-full

WORKDIR /workspaces/uav_vigneto

# Pacchetti base
RUN apt-get update && apt-get install -y --no-install-recommends \
    git cmake build-essential wget python3-tk python3-setuptools \
    ros-jazzy-plotjuggler-ros ros-jazzy-ros-gz ros-jazzy-ros-gz-bridge \
    ffmpeg tree sudo && \
    rm -rf /var/lib/apt/lists/*

# Fix pip
RUN python3 -m pip config set global.break-system-packages true

# PX4 + DDS Agent
RUN git clone --recursive https://github.com/PX4/PX4-Autopilot.git /opt/PX4-Autopilot && \
    cd /opt/PX4-Autopilot && bash Tools/setup/ubuntu.sh --no-sim-tools && \
    git clone https://github.com/eProsima/Micro-XRCE-DDS-Agent.git /opt/Micro-XRCE-DDS-Agent && \
    cd /opt/Micro-XRCE-DDS-Agent && mkdir build && cd build && cmake .. && make -j$(nproc) && make install && ldconfig

# Crea utente personalizzato 'paolo'
ARG USERNAME=paolo
ARG USER_UID=1000
ARG USER_GID=$USER_UID
RUN groupadd --gid $USER_GID $USERNAME && \
    useradd --uid $USER_UID --gid $USER_GID -m $USERNAME && \
    echo "$USERNAME ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers && \
    chown -R $USERNAME:$USERNAME /workspaces

# Passa all’utente paolo
USER paolo

# ROS2 sourcing automatico
RUN echo "source /opt/ros/jazzy/setup.bash" >> /home/paolo/.bashrc

# Entry point
COPY --chown=paolo:paolo .devcontainer/ros_entrypoint.sh /ros_entrypoint.sh
ENTRYPOINT ["/ros_entrypoint.sh"]
CMD ["bash"]
