xhost +local:docker

docker compose build

docker compose up -d

docker compose exec ros_robot bash

ros2 pkg create --build-type ament_python my_project_pkg

ros2 pkg create --build-type ament_cmake my_project_pkg

sudo chmod 777 -R ros_ws

colcon build

source install/setup.bash

ros2 run my_project_pkg my_node
