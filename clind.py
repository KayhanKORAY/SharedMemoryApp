import cv2
import numpy as np
from multiprocessing import shared_memory
import time
import argparse


ap = argparse.ArgumentParser()
ap.add_argument("-n", "--name", help="file name")
ap.add_argument("-sw", "--shapew", help="frame shape")
ap.add_argument("-sh", "--shapeh", help="frame shape")
ap.add_argument("-s", "--shape", help="frame shape")
args = vars(ap.parse_args())
# Sunucudan paylaşımlı bellek adını alın (sunucudan konsola yazılmış olan adı kullanın)
shared_memory_name = args["name"]  # Sunucudan paylaşılan paylaşımlı bellek adını buraya yazın

# Sunucudaki paylaşımlı bellek adına göre bağlan
shm = shared_memory.SharedMemory(name=shared_memory_name)



# Görüntü verilerini tutacak numpy dizisi (çözünürlüğü ve veri tipini sunucu ile aynı yapın)
frame_shape =(int(args["shapew"]), int(args["shapeh"]), int(args["shape"]))  # Kameranızın çözünürlüğüne göre ayarlayın
frame_dtype = np.uint8  # Görüntü veri tipi
shared_frame = np.ndarray(frame_shape, dtype=frame_dtype, buffer=shm.buf)

try:
    while True:
        # Paylaşımlı bellekteki görüntüyü oku
        frame = shared_frame.copy()  # Bellekten görüntüyü al
        
        # Görüntüyü ekranda göster
        cv2.imshow('Shared Memory Frame', frame)

        # Çıkış için 'q' tuşuna basıldığında döngüyü kır
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        # Bekleme süresi (gereksiz CPU kullanımını azaltmak için)
        #time.sleep(0.033)  # Yaklaşık 30 FPS

finally:
    # Paylaşımlı bellekten ayrıl
    shm.close()
    cv2.destroyAllWindows()
