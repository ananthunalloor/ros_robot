FROM osrf/ros:lyrical-desktop-full

ENV ROS_DISTRO=lyrical
ENV DEBIAN_FRONTEND=noninteractive
ENV ROS_WS=/root/ros_ws

# Gazebo Jetty (LTS) is the officially recommended sim for Lyrical Luth.
# It's pulled in through the ros-gz vendor packages, not a separate Gazebo install.
RUN apt-get update && apt-get install -y --no-install-recommends \
        ros-${ROS_DISTRO}-ros-gz \
        ros-${ROS_DISTRO}-xacro \
        ros-${ROS_DISTRO}-robot-state-publisher \
        ros-${ROS_DISTRO}-joint-state-publisher-gui \
        ros-${ROS_DISTRO}-teleop-twist-keyboard \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p ${ROS_WS}/src
WORKDIR ${ROS_WS}

# Auto-source ROS and the workspace overlay in every interactive shell
RUN echo "source /opt/ros/${ROS_DISTRO}/setup.bash" >> /root/.bashrc && \
    echo "if [ -f ${ROS_WS}/install/setup.bash ]; then source ${ROS_WS}/install/setup.bash; fi" >> /root/.bashrc

CMD ["bash"]
