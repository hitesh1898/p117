import os
import cv2


path = "Images"


Images = []


for file in os.listdir(path):
    
    name, extension = os.path.splitext(file)
    
    if extension.lower() in ['.jpg', '.jpeg', '.png', '.gif']:
       
        file_name = os.path.join(path, file)
        
        print(file_name)
        
        Images.append(file_name)


count = len(Images)


frame = cv2.imread(Images[0])


height, width, channels = frame.shape


size = (width, height)


print(size)


out = cv2.VideoWriter()


video_name = "Project"
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
fps = 0.8
Size = size


out.open("Project.mp4", fourcc, fps, Size, True)


for i in range(count):
   
    img = cv2.imread(Images[i])
   
    out.write(img)


out.release()


print("Done")
