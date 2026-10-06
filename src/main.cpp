#include <iostream>
#include <opencv2/opencv.hpp>

int main() {
    cv::VideoCapture camera(1, cv::CAP_AVFOUNDATION);

    if (!camera.isOpened()) {
        std::cerr << "Camtry could not open the camera." << std::endl;
        return 1;
    }

    cv::Mat frame;

    while (true) {
        bool success = camera.read(frame);

        if (!success) {
            break;
        }

        cv::imshow("Camtry", frame);

        if (cv::waitKey(1) == 'q') {
            break;
        }
    }

    camera.release();
    cv::destroyAllWindows();

    return 0;
}