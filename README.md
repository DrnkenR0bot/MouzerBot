# MouzerBot
Simple two-wheel ultrasonic guided roaming robot. The primary goal of this robot is to give the appearance of complex thinking with the minimum set of hardware and software. 

## Basic Design
1. Two off-center wheels powered by independant DC motors. Allows for forward, reverse, and turn by differential rotation.
1. Forward mounted eye is an HC-SR04 ultrasonic range finder. In place rotation enables mapping in all directions for obstacles. 
1. Control hardware is a basic KB2040 microcontroller and DRV8833 DC Motor controller. 

## Behavior
1. The primary goal of this robot is to give the appearance of complex thinking with the minimum set of hardware and software. 
1. Following the logic of a mouse, MouzerBot seeks out narrow openings that it can pass through. It does this by mapping the distance to objects 360 degrees around it, then proceeding to a randomly selected opening large enough for it to fit through. This prevents it from simply going back and forth between the widest open spaces in the room. 
1. The robot thus has to have an understanding of its own physical dimensions as well as the absolute size of an opening a known distance away. 
1. Random, or Brownian, motion plays a big role in this robot's behavior. This should afford it the appearance of being alive with minimal programming. 

## Hardware
| _Component_ | _Role_ | _Quantity_ |
|-|-|-|
|3D printed enclosure| body|1|
|[KB2040](https://learn.adafruit.com/adafruit-kb2040?view=all) | brain | 1|
|[HC-SR04](https://learn.adafruit.com/ultrasonic-sonar-distance-sensors?view=all) | ultrasonic distance sensor |1|
|[DRV8833](https://learn.adafruit.com/adafruit-drv8833-dc-stepper-motor-driver-breakout-board?view=all) | DC Motor controller |1|
|3D printed wheels| mobility |2|

## References

![KB2040 pinout](/references/Adafruit_KB2040_Pinout.png) 

![Fritzing wiring diagram](/wiring_diagram_bb.png) 

