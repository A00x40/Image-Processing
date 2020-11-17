'''
(1) Averaging Filter
'''
def meanFilter(imgage , window_width , window_height):
    outImage = np.zeros( (len(image),len(image[0])))
    
    edgex = (window_width // 2) 
    edgey = (window_height // 2) 
    
    for x in range (edgex , len(image) - edgex) :
        for y in range (edgex , len(image[0]) - edgey) :   
            
            avgVal = 0;
            for fx in range( window_width ) :    
                for fy in range( window_height ) :
                    avgVal += image[x + fx - edgex][y + fy - edgey]
                    
            outImage[x][y] = avgVal / (window_width * window_height
            
     return outImage    

'''
(2) Median Filter
'''
def median_filter(image, window_width , window_height):
    outImage = np.zeros( (len(image),len(image[0])))
    
    edgex = (window_width // 2) 
    edgey = (window_height // 2) 
    
    for x in range (edgex , len(image) - edgex) :
    
        for y in range (edgex , len(image[0]) - edgey) :
            
            colorArray  = np.zeros( ( window_width , window_height ) )
            
            for fx in range( window_width ) :
                
                for fy in range( window_height ) :
                    
                    colorArray[fx][fy] = image[x + fx - edgex][y + fy - edgey]
                    
            colorArray.sort()
            outImage[x][y] = colorArray[ window_width // 2][ window_height // 2]
        
    return outImage

'''
 Requirement 
'''
pout = io.imread("pout.tif")
grayPout = rgb2gray(pout)

# Salt & Pepper Noise
noisePout = random_noise(grayPout ,mode="s&p",amount = 0.05)
show_images([pout , grayPout  , noisePout] , ['Original','GrayScale','Noise'])

# Median Filter
my_filtered = median_filter( noisePout , 3 , 3 )

skimedian = median( noisePout )
show_images([my_filtered , skimedian] , ['My Filtered','Skimage Median Filtered'])

# Gaussain Filter
skiguassian1 = gaussian( noisePout , sigma=[8,3] )
skiguassian2 = gaussian( noisePout , sigma=[6,5] )
skiguassian3 = gaussian( noisePout , sigma=[3,2] )
skiguassian4 = gaussian( noisePout , sigma=3 )


show_images([skiguassian1,skiguassian2,skiguassian3,skiguassian4] , ['Skimage Gaussian Filter S=8,3','Skimage Gaussian Filter S=6,5','Skimage Gaussian Filter S=3,2','Skimage Gaussian Filter S=3'])

