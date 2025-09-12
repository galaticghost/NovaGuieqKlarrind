import cv2

img = cv2.imread("fruit3.png")

img2 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


altura, largura = img2.shape

for i in range(altura):
    for j in range(largura):
        if img2[i,j] > 200 and img2[i,j] < 204:
            img2[i,j] = 255

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

_, thresh = cv2.threshold(img2, 127, 255, cv2.THRESH_BINARY_INV)


thresh = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel)
thresh = cv2.dilate(thresh,kernel)

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
cv2.imshow("Frutas2", img2)
cv2.imshow("thresh",thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
