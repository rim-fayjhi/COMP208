"""
COMP 208 - Assignment 4
"""

import skimage.io as i
import numpy as np

image_path = input('Please enter the path to the saved "mountain.png" image: ')     #The user is asked to give the file location in order to be able to locate mountain.png.

if image_path[-1] != "\\":      #This adds the \\ necessary at the end of the folder name in case the user did not do it.
    image_path += "\\"

class ImageAnalysis:          #Creating the ImageAnalysis class

    def __init__(self, image_path):         
        self.image = i.imread(image_path + "mountain.png")             #This searches for the file depending on where it has been saved and loads it.
        self.image_path = image_path            #The attribute image_path is set to image_path.
        
    def dimension(self):
        print(' ')            #Printing an empty space to make the following text easier to distinguish in the console.
        print('This is the size of the image: (', str(self.image.shape[1]), ',', str(self.image.shape[0]), ',', str(self.image.shape[-1]), ')')
        print(' ')
    
    def show(self):     
        i.imshow(self.image)     #This implements the show method which displays mountain.png on the screen.
        i.show()
        
    def retrieveHidden(self):
        hidden_image = np.empty([131, 100, 3], dtype = int)         #These are the known dimensions of the hidden image, the type is integers as we are dealing with whole numbers.
        
        for row in range(100):      #Basically (0, 100) dimension...
            for col in range(131):       #These numbers come from the dimension of the hidden image.
                hidden_image[col][row] = self.image[col*11][row*11]         #We multiply by 11 as we know that the 12th pixel is the one that was replaced by the secret image.
        
        hidden_image = hidden_image.astype("uint8")     #The image needs to be converted to uint8 prior to saving to suppress a lossy conversion error.
        i.imsave(image_path + "hidden.png", hidden_image)       #Saving the newly retrieved hidden image in the same folder as the original mountain image.

    def fix(self):
        fixed_image = self.image 
        fixed_image = fixed_image.astype("int64")        #Converting the array declared in image into int64 type.
        average_color = np.zeros(shape = 3)       #Taking the average of the 3 surrounding pixels.
                
        for row in range(100):      #These numbers come from the dimension of the hidden image given in the assignment instructions.
            for col in range(131):          #Looking at the each item in the rows and columns of the image, basically axis 0 and 1.
                    
                fixed_cplus = fixed_image[col*11+1][row*11]     #The following comes from the reverse engineering of the following "The algorithm is simple, you just need to know that every 2 consecutive pixels from the hidden image are separated by 11 pixels in the mountain image."
                fixed_cminus = fixed_image[col*11-1][row*11]     #Settings these variables to make the following lines more readable.
                fixed_rplus = fixed_image [col*11][row*11+1]        #The 4 possible cases are either above, under, left or right of the pixel.
                fixed_rminus = fixed_image [col*11][row*11-1]
                
                if col != 0 and row !=0 :   #This is for pixels positioned in the middle, the average is taken normally.
                    average_color = (fixed_cplus + fixed_cminus + fixed_rplus + fixed_rminus)//4        #Floored division because we want a whole number (integer) answer.
                elif col != 0 and row == 0:     #This is for when the pixel is at the left or right edge.                                                           
                    average_color = (fixed_cplus + fixed_cminus + fixed_rplus)//3
                elif col == 0 and row != 0:         #This is for the above or bottom edges.
                    average_color = (fixed_cplus + fixed_rplus + fixed_rminus)//3       #Dividing by 3 as we are takine the average of 3 pixels.
                elif col == 0 and row == 0:         #This is for the corner pixels
                    average_color = (fixed_cplus + fixed_rplus)//2
                
                fixed_image[col*11][row*11] = average_color 
                
        fixed_image = fixed_image.astype("uint8")      #The image needs to be converted to uint8 prior to saving to suppress a lossy conversion error.        
        i.imsave(image_path + "clean_mountain.png", fixed_image)        #Saving the newly retrieved clean mountain image in the same folder as the original mountain image.
                
    def averageRGB(self):
        image = i.imread(self.image_path + "hidden.png")    #We will be working from the hidden file created.
        average_rgb = np.zeros(shape = (np.shape(image)[0], np.shape(image)[1]))    #This creates an array of 0s of the dimension of the image, which should be of 131 by 100.
        for row in range(np.shape(image)[0]):       #The height is represented by the rows and the width is represented by the columns.
            for col in range(np.shape(image)[1]):
                average_rgb[row][col] = round(np.average(image[row][col]))      #This uses the python average function and rounds it up to 0 decimals using round().
        np.savetxt(image_path + "RGB.csv", average_rgb, delimiter = ",")        #Saving the newly retrieved csv file in the same folder as the original mountain image.
        
    def load_rgb_from_file(self, file_name):
        self.file_name = file_name
        file = np.loadtxt(image_path + self.file_name, delimiter = ",")
        
        nbre_of_lines = np.shape(file)[0]   #Settings these variables to make the following lines more readable.
        nbre_of_columns = np.shape(file)[1]
        
        RGB_load = np.zeros((nbre_of_lines, nbre_of_columns, 3), dtype = np.uint8) #The type is set as uint8 to avoid errors.
        for row in range(np.shape(RGB_load)[0]):      #The height is represented by the rows and the width is represented by the columns.
            for col in range(np.shape(RGB_load)[1]):
                n = file[row][col]      #The data from the file is taken into the variable n.
                RGB_load[row][col] = [n, n, n]        #Then it is transformed using the RGB_load to make it black and white.
        
        RGB_load = RGB_load.astype("uint8")     #The image needs to be converted to uint8 prior to saving to suppress a lossy conversion error.        
        
        i.imsave(image_path + "black_white_hidden.png", RGB_load)     #Saving the newly retrieved black and white hidden image in the same folder as the original image.
        i.imshow(RGB_load)        #The picture should get queued to be displayed once i.show() is ran.
        i.show()        #The picture should get displayed.
        
io = ImageAnalysis(image_path)          #This runs everything as asked in the assignment.
print(io)
io.retrieveHidden()
io.fix()
io.dimension()
io.show()
io.averageRGB()
io.load_rgb_from_file("RGB.csv")
                



