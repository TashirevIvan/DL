 # DL
## Using DockerHub

1. Pull the image from my repository:

`docker pull tashirevivan/fdc:wsl`

2. Run the container:

`docker run tashirevivan/fdc:wsl`

## Building the image using local machine
1. Clone the project:

`git clone https://github.com/sabadijou/FastDepthCompletionCPU.git`

2. Go to the folder of the newly cloned project:

`cd <YOUR PATH>`

3. Download dataset:

`https://s3.eu-central-1.amazonaws.com/avg-kitti/data_depth_selection.zip`

unpack the contents of the `test_depth_completion_anonymous` folder to the

`FastDepthCompletionCPU\dataset\kitti_validation_cropped` directory

4. Build the image:

`docker build -t fdc .`

5. Run the container:

`docker run fdc`

## Saving results to your machine
1. Figure out container's id:

`docker ps -a`

2. Copy folder with results to your machine:

`docker cp <container_id>:./out/ <YOUR PATH>`

### Results folder contents

Folder contains your results as well as FastDepthCompletionCPU\outputs\kitti\final_output and FastDepthCompletionCPU\my_local_image (my results)

## Related links:
+ [Project page](https://arxiv.org/abs/1802.00036)

+ [Link](https://github.com/sabadijou/FastDepthCompletionCPU) to original repository
