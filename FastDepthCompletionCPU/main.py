import design_depth_map
import numpy as np
import cv2
import os


class DepthCompletion:

    def __init__(self):
        self.main_img_path = os.path.expanduser(r'dataset\kitti_validation_cropped\image')
        self.input_depth_dir = os.path.expanduser(r'dataset\kitti_validation_cropped\velodyne_raw')
        self.img_size = (450, 130)

    def save_for_evaluation(self, sufficient_depth, img_name):
        path = r'outputs/kitti/depth_for_evaluation/'
        cv2.imwrite(path + img_name, sufficient_depth)

    def save_final_outputs(self, img, img_name):
        path = r'outputs/kitti/final_output/'
        img = cv2.applyColorMap(np.uint8(img / np.amax(img) * 255), cv2.COLORMAP_JET)
        cv2.imwrite(path + img_name, img)

    def process(self):
        directory_path = 'dataset\\kitti_validation_cropped\\image'
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)
        main_img_pathes = os.listdir(self.main_img_path)
        main_image_list = []
        for item in main_img_pathes:
            main_image_list.append(cv2.imread(self.main_img_path + '/' + item))
        img_pathes = os.listdir(self.input_depth_dir)
        image_list = []
        for item in img_pathes:
            image_list.append(cv2.imread(self.input_depth_dir + '/' + item, cv2.IMREAD_ANYDEPTH))
        num_images = len(image_list)
        for i in range(num_images):
            depth_image = image_list[i]
            main_image = main_image_list[i]
            projected_depths = np.float32(depth_image / 255.0)
            final_depths, process_dict = design_depth_map.create_map(main_image, projected_depths, show_process=True)
            self.save_for_evaluation(process_dict['s9_depths_out'], img_pathes[i])
            self.save_final_outputs(process_dict['s9_depths_out'], img_pathes[i])
        import metrics
        metrics.print_metrics()

    def show_image(self, window_name, image):
        cv2.imshow(window_name, image)

    def show_result(self, process_dict, main_image):
        pass


if __name__ == '__main__':
    depth = DepthCompletion()
    depth.process()
