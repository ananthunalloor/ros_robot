# FROM osrf/ros:lyrical-desktop-full
FROM osrf/ros:jazzy-desktop-full

# ENV ROS_DISTRO=lyrical
ENV ROS_DISTRO=jazzy
ENV DEBIAN_FRONTEND=noninteractive
ENV ROS_WS=/root/ros_ws
ENV DEV_WS=/root/dev_ws
ENV MICRO_WS=/root/uros_ws

# Gazebo Jetty (LTS) is the officially recommended sim
# It's pulled in through the ros-gz vendor packages, not a separate Gazebo install.
RUN apt-get update && apt-get install -y --no-install-recommends \
        ros-${ROS_DISTRO}-ros-gz \
        ros-${ROS_DISTRO}-xacro \
        ros-${ROS_DISTRO}-robot-state-publisher \
        ros-${ROS_DISTRO}-joint-state-publisher-gui \
        ros-${ROS_DISTRO}-teleop-twist-keyboard \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install -y --no-install-recommends \
        clang-tidy \
        flex \
        net-tools \
    && rm -rf /var/lib/apt/lists/*

 # Create all workspaces
RUN mkdir -p ${ROS_WS}/src \
        ${DEV_WS}/src \
        ${MICRO_WS}/src

# Source workspaces
RUN echo "source /opt/ros/${ROS_DISTRO}/setup.bash" >> /root/.bashrc && \
        echo "if [ -f ${MICRO_WS}/install/local_setup.bash ]; then source ${MICRO_WS}/install/local_setup.bash; fi" >> /root/.bashrc && \
        echo "if [ -f ${DEV_WS}/install/setup.bash ]; then source ${DEV_WS}/install/setup.bash; fi" >> /root/.bashrc && \
        echo "if [ -f ${ROS_WS}/install/setup.bash ]; then source ${ROS_WS}/install/setup.bash; fi" >> /root/.bashrc

WORKDIR ${ROS_WS}

# can enable if display issue continues
RUN echo "export DISPLAY=:0" >> /root/.bashrc

CMD ["bash"]
