from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node


def generate_launch_description():

    rosbridge_server = ExecuteProcess(
        cmd=["ros2", "launch", "rosbridge_server", "rosbridge_websocket_launch.xml"],
        name="rosbridge_websocket",
        output="screen",
        respawn=True,
        respawn_delay=2.0,
    )

    return LaunchDescription(
        [
            rosbridge_server,
            Node(
                package="micro_ros_agent",
                executable="micro_ros_agent",
                name="micro_ros_agent",
                output="screen",
                arguments=["udp4", "--port", "8888"],
            ),
            Node(
                package="control",
                executable="control_node",
                name="control_node",
                output="screen",
            ),
        ]
    )
