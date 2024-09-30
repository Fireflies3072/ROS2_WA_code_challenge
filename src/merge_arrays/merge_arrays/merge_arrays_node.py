import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32MultiArray

class MergeArraysNode(Node):
    def __init__(self):
        super().__init__('merge_arrays_node')

        # Subscriptions
        self.subscriber_1 = self.create_subscription(
            Int32MultiArray,
            '/input/array1',
            self.callback_array1,
            10)
        self.subscriber_2 = self.create_subscription(
            Int32MultiArray,
            '/input/array2',
            self.callback_array2,
            10)

        # Publisher
        self.publisher_ = self.create_publisher(Int32MultiArray, '/output/array', 10)
        
        # Initialize arrays
        self.array1 = []
        self.array2 = []

    def callback_array1(self, msg):
        self.array1 = msg.data
        self.publish_merged_array()

    def callback_array2(self, msg):
        self.array2 = msg.data
        self.publish_merged_array()

    def publish_merged_array(self):
        if self.array1 and self.array2:
            merged_array = sorted(self.array1 + self.array2)
            msg = Int32MultiArray(data=merged_array)
            self.publisher_.publish(msg)
            self.get_logger().info(f'Merged array: {merged_array}')

def main(args=None):
    rclpy.init(args=args)
    node = MergeArraysNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
