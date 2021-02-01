import cv2
import numpy as np
import time
import imutils


def stopMotor():
    print('stop')


def right():
    print('right')


def left():
    print('left')


def forward():
    print('forward')


def backward():
    print('backward')


def drive():
    global cx,fw,w,h,minArea,maxArea,flag,lock
    while not threadStop:
        if flag==1 and lock:
            if cx > 3*fw/4:
                #print("Right")
                right()
                time.sleep(0.015)
            elif cx < fw/4:
                #print("Left")
                left()
                time.sleep(0.015)
            elif w*h > maxArea:
                #print("Back")
                backward()
                time.sleep(0.025)
            elif w*h < minArea:
                #print("Forward")
                forward()
                time.sleep(0.025)
            
            stopMotor()
            time.sleep(0.0125)

        else:
            #print("Stop")
            stopMotor()
    GPIO.cleanup()
            


if __name__ == "__main__":

    global cx,w,h,flag,minArea,maxArea,lock,fw,threadStop
    threadStop = False #To terminate the thread which drives the robot whenever the user quits

    lock = False #To lock the object

    flag = 0 #Its 1 whenever the object is detected

    #Range of the colors to detect an Object in this range
    lower_thresh = np.array([0, 208, 60])
    high_thresh = np.array([179, 255, 255])
    
    #To stream the video from the webcam
    device = cv2.VideoCapture(0)
  
    first = True
    #start_new_thread(drive,()) #Thread to drive the robot
    
    while True:
        ret, frame = device.read() #It reads frames from the video
        #_, frame = device.read()
        #frame = cv2.flip(frame,1)

        #Pre-processing of the frame to detect the object
        blurred = cv2.GaussianBlur(frame, (11, 11), 0)
        hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

        mask = cv2.inRange(hsv, lower_thresh, high_thresh)
        mask = cv2.erode(mask, None, iterations=2)
        mask = cv2.dilate(mask, None, iterations=2)
    
        cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)

        fh,fw,_ = frame.shape
        #cv2.rectangle(frame,(int(fw/5),0),(int(4*fw/5),fh),(0,0,255),3)
        cv2.rectangle(frame,(int(fw/4),0),(int(3*fw/4),fh),(0,255,255),3)

        #It draws rectangle around the object and finds its centre co-ordinates
        if len(cnts)>0:
            flag = 1
            print('banana found')
            c = max(cnts, key=cv2.contourArea)
            x,y,w,h = cv2.boundingRect(c)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
            M = cv2.moments(c)
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            #cv2.circle(frame,(cx,cy),3,(0,255,255),-1)

            if first:
                #print("Area = ",w*h)
                #exit(0)
                maxArea = 3*w*h/2
                minArea = w*h/2

        else:
            print('nf')
            flag = 0

        

        #cv2.imshow("Frame",frame)
        #cv2.imshow("Mask", mask)

        k = cv2.waitKey(1) & 0xFF

        if k == ord('q'):
            threadStop = True
            break
        elif k == ord('l') and flag==1:
            print("Locked")
            print("Fw = ",fw)
            print("Fh = ",fh)
            first = False
            lock = True

#device.release()
device.stop()
cv2.destroyAllWindows()