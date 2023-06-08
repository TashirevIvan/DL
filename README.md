# DL
Detecting Photoshopped Faces
Using DockerHub
Pull the image from my repository:
docker pull tashirevivan/fdc:wsl

Run the container:
docker run tashirevivan/fdc:wsl

Building the image using local machine
Clone the project:
git clone https://github.com/sabadijou/FastDepthCompletionCPU.git

Go to the folder of the newly cloned project:
cd <YOUR PATH>

Download dataset:
https://s3.eu-central-1.amazonaws.com/avg-kitti/data_depth_selection.zip

unpack the contents of the test_depth_completion_anonymous folder to the 
 FastDepthCompletionCPU\dataset\kitti_validation_cropped directory
  
Build the image:
docker build -t fdc .

Run the container:
docker run fdc

Saving results to your machine
Figure out container's id:
docker ps -a

Copy folder with results to your machine:
docker cp <container_id>:./out/ <YOUR PATH>
