import cv2 as cv
import numpy as np
import vaja1

def test_konvolucija():
    # Create a simple test image and kernel
    image = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    kernel = np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]])

    # Expected result of convolution
    expected_result = np.array([[-3, -6, -3], [-3, -6 ,-3], [-3, -6,-3]]) 
    # Call the function to be tested
    result = vaja1.konvolucija(image, kernel)
    print (result)
    # Assert that the result matches the expected result
    assert np.array_equal(result, expected_result), "Test failed for konvolucija function"
    print("Test 1 passed.")

test_konvolucija()
