
# Import the NumPy library
import numpy as np

# Define a function to demonstrate NumPy array creation and manipulation.
def numpy_for_ai_example():
    """
    This function showcases several NumPy functionalities relevant to AI tasks.
    It covers array creation, reshaping, basic operations, and matrix multiplication.
    """

    # Create a NumPy array from a Python list.  This is a common way to start with data.
    data = [1, 2, 3, 4, 5, 6]
    arr = np.array(data)
    print("Array from list:\n", arr)

    # Reshape the array.  This is crucial for many AI algorithms (e.g., image processing).
    arr_reshaped = arr.reshape((2, 3)) # Reshape into a 2x3 matrix
    print("\nReshaped array:\n", arr_reshaped)

    # Perform element-wise addition with another array.  Common in neural network calculations.
    arr2 = np.array([10, 10, 10, 20, 20, 20])
    arr_sum = arr + arr2  
    print("\nElement-wise addition:\n", arr_sum)

    # Matrix multiplication.  Fundamental for many AI models (e.g., linear regression).
    matrix1 = np.array([[1, 2], [3, 4]])
    matrix2 = np.array([[5, 6], [7, 8]])
    matrix_product = np.dot(matrix1, matrix2) # Or matrix1 @ matrix2 for Python 3.5+
    print("\nMatrix multiplication:\n", matrix_product)

    # Calculate the mean of the array. Useful for feature scaling and normalization in AI.
    mean_value = np.mean(arr)
    print("\nMean of the array:", mean_value)


    # Example of creating an array of zeros – useful for initializing weight matrices in neural networks
    zeros_array = np.zeros((3,3))
    print("\nArray of zeros:\n", zeros_array)

    # Example of creating an array of ones – useful for initializing weight matrices in neural networks
    ones_array = np.ones((2,2))
    print("\nArray of ones:\n", ones_array)

    # Example of creating an array with random numbers – often used to initialize weights in neural networks
    random_array = np.random.rand(2,3) # Creates a 2x3 array with random numbers between 0 and 1
    print("\nRandom array:\n", random_array)

# Call the function to execute the code.
numpy_for_ai_example()
