xhost +local:docker

export UID=$(id -u)

export GID=$(id -g)

docker compose build

docker compose up -d

docker compose exec ros_robot bash

docker logs -f micro-ros-agent
ros2 pkg create --build-type ament_python my_project_pkg

ros2 pkg create --build-type ament_cmake my_project_pkg

sudo chmod 777 -R ros_ws

colcon build

source install/setup.bash

ros2 run control control_node

ros2 launch robot.launch.py

ros2 topic list
ros2 topic echo /picow_publisher

ros2 launch ros_gz_sim gz_sim.launch.py gz_args:="empty.sdf"
ros2 run micro_ros_agent micro_ros_agent serial --dev /dev/ttyACM0 -b115200
ros2 run micro_ros_agent micro_ros_agent udp4 --port 8888

MAC Address: 32:BD:04:C1:CD:28
