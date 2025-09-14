import cv2

img = cv2.imread("fruit3.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, thresh = cv2.threshold(gray, 151, 255, cv2.THRESH_BINARY_INV)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=4)
thresh = cv2.dilate(thresh,kernel,iterations=3)

num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(thresh)

for i in range(1, num_labels):
    x, y, w, h, area = stats[i]
    cx, cy = centroids[i]
    
    if area < 500 or (cx < 50 and cy < 50):
        continue
    
    cv2.rectangle(img, (x, y), (x+w, y+h), (0,255,0), 2)
    cv2.circle(img, (int(cx), int(cy)), 5, (0,0,255), -1)
    cv2.putText(img, f"Fruta {i}", (x, y-10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)

cv2.imshow("Frutas", img)
cv2.imshow("Thresh", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
