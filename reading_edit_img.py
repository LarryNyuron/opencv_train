import cv2


img_obj = r'wh40.jpg'
directory = r'C:\\Users\\STEN CENTER ROSTOV\\Desktop\\Python\\OpenCV_study'
flename = 'waha.png'

'''
image = cv2.imread(img_obj)
cv2.imshow('Test', image)

cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite(flename, image)

print(image.shape, image.size)

cv2.imshow('Test', cv2.cvtColor(image, cv2.COLOR_BGR2GRAY))

cv2.imshow('Test', cv2.cvtColor(image, cv2.COLOR_GRAY2BGR))'''

'''gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Orig', image)
cv2.imshow('Test',gray_img)


cv2.imshow("Test", cv2.resize(image, (200, 200)))

cv2.imshow("Test", cv2.putText(image, 'WAHAHAH', (500,500), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0,0), 4))

cv2.putText(image, 'WAHAHAH', (500,500), cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 0,0), 40)


cv2.imshow('Test', cv2.line(image, (500, 400), (900, 500), (255,0,0), 5))

cv2.imshow('Test', cv2.circle(image, (630,200), 80, (255,0,0), 5))

cv2.imshow('Test', cv2.rectangle(image, (500, 400), (900, 500), (255,0,0), 5))

cv2.imshow('Test', cv2.ellipse(image, (630,200), (100, 100), 0, 0, 180, 256, -1))
'''
image = cv2.imread(img_obj, 0)

cv2.imshow('Test', image)

cv2.waitKey(0)

cv2.destroyAllWindows()