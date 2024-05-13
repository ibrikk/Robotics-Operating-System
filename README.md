# Robotics-Operating-System


## roscore
## rosrun turtlesim
## rqt_graph
## catkin_make outside the src folder
## catkin_create_pkg <name> rospy
## source <path to devel/setup.sh>
## rostopic list
## rostopic info <name>
## rostopic echo
## rosservice info <name>
## rosservice list
## rosservice call <name>
## rossrv
## rossrv list
## rossrv show <name>

Publisher
A publisher is a node that sends messages. It creates a topic and sends messages on it. You can think of a topic as a channel on a TV. Any node that is interested in a specific type of information (like sensor data or status updates) can publish that information on a corresponding topic.

Subscriber
A subscriber is a node that receives messages. It subscribes to a topic and listens for messages that are published on that topic. Whenever a new message is published, the subscriber's callback function is called with the new message as an argument.

Node Initialization: First, each node (including publishers and subscribers) must initialize itself with the ROS master. This is done using rospy.init_node().

Publisher Setup:

A publisher is created using rospy.Publisher(), where you specify the topic name, the type of message, and the queue size.
The publisher periodically sends messages using .publish() method.
Subscriber Setup:

A subscriber is created using rospy.Subscriber(), where you specify the topic name, the type of message, and a callback function that is executed each time a new message is received.
ROS handles the reception of messages asynchronously. Whenever a message is received on the topic, the specified callback function is called with the message as an argument.
Message Passing:

When a publisher sends out a message, the ROS master helps route that message to all subscribers of the topic.
This is managed through a combination of the ROS master (which manages connections) and a protocol called TCPROS/UDPROS, which are used for setting up and managing network connections between nodes.
Node Execution:

Nodes typically run by spinning rospy.spin(), which keeps your script from exiting until the node has been shutdown. This spinning is what allows callbacks to be called as long as the node is alive.
