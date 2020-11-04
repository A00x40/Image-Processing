'''
(1) Averaging Filter
'''

'''
(2) Median Filter
'''



pyramids = io.imread('pyramids.jpeg')
greyPyramids = rgb2gray(pyramids)
noiseImage = random_noise(greyPyramids,mode="s&p",amount = 0.05)
