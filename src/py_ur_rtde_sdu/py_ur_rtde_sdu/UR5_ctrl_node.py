import rclpy
from rclpy.node import Node

from std_msgs.msg import String

class UR5CtrlNode( Node ):
    """ Basic interface with SDU's `ur-rtde` module """

    def __init__(self):
        super().__init__( 'py_ur_rtde_sdu' )
        self.publisher_ = self.create_publisher(String, 'topic', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0
