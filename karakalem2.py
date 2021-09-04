import cv2
import sys
import time

def rgb2karakelem(renkli_resim_path):
	renkli_resim = cv2.imread(renkli_resim_path)
	gri_resim = cv2.cvtColor(renkli_resim, cv2.COLOR_BGR2GRAY)
	gri_resim_ters_renkler = 255 - gri_resim
	blur_resim = cv2.GaussianBlur(gri_resim_ters_renkler, ksize=(21,21), sigmaX=0, sigmaY=0)
	karakalem_cikis = cv2.divide(gri_resim, 255-blur_resim, scale=256)
	cv2.namedWindow("Normal", cv2.WINDOW_AUTOSIZE)
	cv2.namedWindow("karakelem", cv2.WINDOW_AUTOSIZE)
	cv2.imshow("Normal", renkli_resim)
	cv2.imshow("karakelem", karakalem_cikis)
	cv2.waitKey()
	cv2.destroyAllWindows()

rgb2karakelem("remzi.jpg") #Karakalem efekti yapmak istediğiniz fotoğrafın dizini.