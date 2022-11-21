from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()

    image_process_node = Node(
        package="image_processor",
        executable="image_processor",
        parameters=[
            {'mode': 'cluster_parall'}
        ]
    )

    inv_mux_node = Node(
        package="inv_mux",
        executable="inv_mux",
        parameters=[
            {'num_parall_nodes': 1}
        ]
    )

    ld.add_action(image_process_node)
    ld.add_action(inv_mux_node)

    return ld
