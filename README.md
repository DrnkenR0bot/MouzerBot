# MouzerBot
Simple two-wheel ultrasonic guided roaming robot. The primary goal of this robot is to give the appearance of complex thinking with the minimum set of hardware and software. 

## Basic Design
1. Two off-center wheels powered by independant DC motors. Allows for forward, reverse, and turn by differential rotation.
1. Forward mounted eye is an HC-SR04 ultrasonic range finder. In place rotation enables mapping in all directions for obstacles. 
1. Control hardware is a basic KB2040 microcontroller and DRV8833 DC Motor controller. 
1. Adding an accelerometer or IMU may be a good way to start exploring room mapping and path setting from memory. 

## Behavior
1. The primary goal of this robot is to give the appearance of complex thinking with the minimum set of hardware and software. 
1. Following the logic of a mouse, MouzerBot seeks out narrow openings that it can pass through. It does this by mapping the distance to objects 360 degrees around it, then proceeding to a randomly selected opening large enough for it to fit through. This prevents it from simply going back and forth between the widest open spaces in the room. 
1. The robot thus has to have an understanding of its own physical dimensions as well as the absolute size of an opening a known distance away. 
1. Random, or Brownian, motion plays a big role in this robot's behavior. This should afford it the appearance of being alive with minimal programming. 

## Hardware
| _Component_ | _Role_ | _Quantity_ |
|-|-|-|
|KB2040 | brain | 1|
