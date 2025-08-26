import cv2
imagem = cv2.cvtColor(cv2.imread("3.jpg"),cv2.COLOR_RGB2GRAY)
imagem2 = cv2.cvtColor(cv2.imread("3.jpg"),cv2.COLOR_RGB2BGR)
imagem3 = cv2.cvtColor(cv2.imread("3.jpg"),cv2.COLOR_RGB2HSV)
imagem4 = cv2.imread("3.jpg",cv2.IMREAD_UNCHANGED)
if imagem is None:
    print("Erro carregando a imagem")
else:
    cv2.imshow('Imagem', imagem)
    cv2.imshow('2',imagem2)
    cv2.imshow('4',imagem3)
    cv2.imshow('5',imagem4)
    cv2.waitKey(0)
    cv2.destroyAllWindows()