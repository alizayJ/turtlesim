#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

class my_node(Node):
    def __init__(self):
        super().__init__("first_node") #should not contain spaces
        self.count_ = 0
        self.create_timer(1.0, self.timer_callback)
        
    def timer_callback(self):
        self.get_logger().info(f"Hello,{self.count_}")
        self.count_ +=1
        
        

def main(args = None):
    rclpy.init(args=args)
    node = my_node()
    rclpy.spin(node) #to keep the node alive
    rclpy.shutdown()

if __name__ == "__main__":
    main()

