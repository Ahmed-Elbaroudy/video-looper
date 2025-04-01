import os
import pytest
from video_looper import validate_video_path, ensure_directory_exists, get_valid_input

def test_validate_video_path_valid():
    # Create a temporary test file
    test_file = "test_video.mp4"
    with open(test_file, 'w') as f:
        f.write("test")
    
    assert validate_video_path(test_file) is True
    
    # Clean up
    os.remove(test_file)

def test_validate_video_path_invalid():
    assert validate_video_path("nonexistent_file.mp4") is False

def test_validate_video_path_empty():
    with pytest.raises(ValueError):
        validate_video_path("")

def test_ensure_directory_exists_valid():
    test_dir = "test_dir"
    os.makedirs(test_dir, exist_ok=True)
    
    assert ensure_directory_exists(test_dir) is True
    
    # Clean up
    os.rmdir(test_dir)

def test_ensure_directory_exists_invalid():
    assert ensure_directory_exists("nonexistent_dir") is False

def test_ensure_directory_exists_empty():
    assert ensure_directory_exists("") is False

def test_get_valid_input_valid():
    # Test with valid integer input
    assert get_valid_input("Enter number: ", int, "Invalid number", 1, 10) == 5
    
    # Test with valid float input
    assert get_valid_input("Enter float: ", float, "Invalid float", 0.1, 10.0) == 5.5

def test_get_valid_input_invalid():
    with pytest.raises(ValueError):
        get_valid_input("Enter number: ", int, "Invalid number", 1, 10) == 0
    
    with pytest.raises(ValueError):
        get_valid_input("Enter float: ", float, "Invalid float", 0.1, 10.0) == 100.0
