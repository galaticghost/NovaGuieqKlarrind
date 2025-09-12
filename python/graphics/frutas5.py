import cv2

img = cv2.imread("fruit1.png")

img2 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

_, thresh = cv2.threshold(img2, 200, 255, cv2.THRESH_BINARY_INV)

thresh = cv2.erode(thresh,kernel)
thresh = cv2.erode(thresh,kernel)

num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(thresh, connectivity=4)

for i in range(1, num_labels):
    area = stats[i, cv2.CC_STAT_AREA]
    if area > 1000:  # ignora ruídos pequenos
        x = stats[i, cv2.CC_STAT_LEFT]
        y = stats[i, cv2.CC_STAT_TOP]
        w = stats[i, cv2.CC_STAT_WIDTH]
        h = stats[i, cv2.CC_STAT_HEIGHT]

        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

cv2.imshow("Frutas", img)
cv2.imshow("thresh",thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
