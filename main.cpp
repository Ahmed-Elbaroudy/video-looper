#include <opencv2/opencv.hpp>
#include <iostream>
#include <string>
#include <filesystem>

int main() {
    // Create a window for video display
    cv::namedWindow("Video Player", cv::WINDOW_NORMAL);

    // Get video file path from user
    std::string videoPath;
    std::cout << "Enter the path to the video file: ";
    std::getline(std::cin, videoPath);

    // Ask if user wants to save the looped video
    bool saveVideo = false;
    char saveChoice;
    std::cout << "\nDo you want to save the looped video? (y/n): ";
    std::cin >> saveChoice;
    std::cin.ignore();  // Clear the input buffer
    
    if (saveChoice == 'y' || saveChoice == 'Y') {
        saveVideo = true;
    }

    // Ask user for playback mode
    int mode;
    std::cout << "\nChoose playback mode:\n";
    std::cout << "1. Loop for a specific number of times\n";
    std::cout << "2. Loop for a specific duration (in minutes)\n";
    std::cout << "Enter your choice (1 or 2): ";
    std::cin >> mode;

    // Get video properties
    cv::VideoCapture cap(videoPath);
    if (!cap.isOpened()) {
        std::cerr << "Error: Could not open video file\n";
        return -1;
    }

    // Get video properties
    double fps = cap.get(cv::CAP_PROP_FPS);
    int frameWidth = static_cast<int>(cap.get(cv::CAP_PROP_FRAME_WIDTH));
    int frameHeight = static_cast<int>(cap.get(cv::CAP_PROP_FRAME_HEIGHT));
    int totalFrames = static_cast<int>(cap.get(cv::CAP_PROP_FRAME_COUNT));
    double videoDuration = totalFrames / fps;  // in seconds

    // Set up video writer if saving
    cv::VideoWriter videoWriter;
    if (saveVideo) {
        std::string outputFilePath = std::filesystem::path(videoPath).stem().string() + "_looped.mp4";
        std::cout << "\nOutput file will be saved as: " << outputFilePath << "\n";
        
        // Create video writer
        videoWriter.open(outputFilePath, cv::VideoWriter::fourcc('H', '2', '6', '4'), 
                        fps, cv::Size(frameWidth, frameHeight));
        
        if (!videoWriter.isOpened()) {
            std::cerr << "Error: Could not create output video file\n";
            return -1;
        }
    }

    // Get playback parameters based on mode
    int numLoops = 0;
    double duration = 0;
    
    if (mode == 1) {
        std::cout << "Enter the number of times to loop the video: ";
        std::cin >> numLoops;
    } else if (mode == 2) {
        std::cout << "Enter the duration to loop the video (in minutes): ";
        std::cin >> duration;
        duration *= 60;  // Convert minutes to seconds
    } else {
        std::cerr << "Invalid choice. Using default mode (number of loops)\n";
        std::cout << "Enter the number of times to loop the video: ";
        std::cin >> numLoops;
    }

    std::cout << "\nPress 'q' to quit\n";

    int currentLoop = 0;
    double elapsedSeconds = 0;

    while (true) {
        // Reset video to start for each loop
        cap.set(cv::CAP_PROP_POS_FRAMES, 0);
        
        while (true) {
            cv::Mat frame;
            cap >> frame;
            
            if (frame.empty()) {
                break;  // End of current loop
            }
            
            // Display the frame
            cv::imshow("Video Player", frame);
            
            // Write frame to output if saving
            if (saveVideo) {
                videoWriter.write(frame);
            }
            
            // Wait for 30ms and check if 'q' is pressed
            if (cv::waitKey(30) == 'q') {
                return 0;
            }

            // Update elapsed time
            elapsedSeconds += 0.03;  // 30ms wait time

            // Check if we've reached the duration limit
            if (mode == 2 && elapsedSeconds >= duration) {
                std::cout << "Playback duration reached.\n";
                break;
            }
        }
        
        if (mode == 1) {
            currentLoop++;
            std::cout << "Completed loop " << currentLoop << " of " << numLoops << "\n";
            if (currentLoop >= numLoops) {
                break;
            }
        }
    }

    // Release resources
    cap.release();
    if (saveVideo) {
        videoWriter.release();
        std::cout << "\nLooped video has been saved successfully!\n";
    }
    cv::destroyAllWindows();

    return 0;
}
