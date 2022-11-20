#!/bin/bash

#to run
#./org2png.sh somefile.org
# file gets saved in /tmp/ folder with name /tmp/org2file.html
#this shell takes org file as an input and
#creates a plantuml work breakdown structure diagram for visualisation of org file

#identify is part of imagemagick suite

echo "@startwbs" > /tmp/.org2file.uml
cat $1 >> /tmp/.org2file.uml
echo "@endwbs" >> /tmp/.org2file.uml

#if -DPLANTUML_LIMIT_SIZE=18192 is not provided then image gets cropped off
java  -jar  /home/palashkulshreshtha/bin/plantuml.jar -DPLANTUML_LIMIT_SIZE=18192 -o /tmp/  /tmp/.org2file.uml

dimensions=`identify /tmp/.org2file.png | awk '{print $3}'`
width=`echo $dimensions |awk 'BEGIN{FS="x"}{print $1}'`
height=`echo $dimensions | awk 'BEGIN{FS="x"}{print $2}'`

echo '
<!DOCTYPE html>
<html>
<head>
<style>
.bg {
  background-image: url("/tmp/.org2file.png");
  width: '$width'px;
  height: '$height'px; 
  background-position: top center;
  background-repeat: no-repeat;
  background-size: contain;
}
</style>
</head>
<div class="bg"></div>' > /tmp/org2file.html

chromium-browser /tmp/org2file.html
