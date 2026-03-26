import numpy as np
import array

# Method 1
numpyArray1 = np.array(range(10), str)
# print(numpyArray1)
# print(type(numpyArray1))

# Method 2
numpyArray2 = np.array([1,2,3,4,5,6,7,8,9])
# print(f"numpyArray2: {numpyArray2}")
# print(np.mean(numpyArray2))
# print(np.median(numpyArray2))
# print(np.meshgrid(numpyArray2))
# print(type(numpyArray2))

arrayMod = array.array('i', [1,2,3,4,5])

# print(sum(arrayMod))
# print(type(arrayMod))

arrayStr = numpyArray1.view()
# print(arrayStr)

# linspace(), zeros(), arange(), ones()

arrayLin = np.linspace(1, 10, 4, dtype=float)
# print(arrayLin)

arrayZeros = np.zeros((3,4))
# print(arrayZeros)

arrayOnes = np.ones(10)
# print(arrayOnes)

arrayArange = np.arange(1,12,2, dtype=int)
# print(arrayArange)
# print(arrayArange[1:5])

# print(arrayZeros/10)
newMatrix = np.matrix(arrayLin, dtype=float)
# print(newMatrix)

# accessing elements in multidimensional array

sampleArray = np.reshape(numpyArray2, (3,3))
# print(sampleArray[0:2,0:2])
# print(sampleArray[2][2])
# print(sampleArray[0][2])

ex1Arr  = np.array([[1,2,3], [4,5,6], [7,8,9]])
# print(ex1Arr.ndim)
# print(ex1Arr.shape)
# print(ex1Arr.flatten())
# print(np.max(ex1Arr))
# print(ex1Arr[1:2])


arangeArray  = np.arange(12, dtype=int)
# print(arangeArray)
zerosArray = np.zeros(10, dtype=float)
# print(f"Covariance of {arrayArange} is:  {np.std(arrayArange)}")


print(ex1Arr.size)
print(ex1Arr.itemsize)
