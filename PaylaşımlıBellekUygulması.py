import cv2
import numpy as np
from multiprocessing import shared_memory
import time
import os
# Kamera tanımlama
camera = cv2.VideoCapture(1)

# İlk kareyi al (kamera çözünürlüğünü almak için)
ret, frame = camera.read()
print(f"frame ölçüleri: {frame.shape}")
# Paylaşımlı bellek oluşturma
shm = shared_memory.SharedMemory(create=True, size=frame.nbytes)
print(f"Paylaşımlı Bellek Adı: {shm.name}")
print(f"python3 clind.py --name {shm.name} --shapew {frame.shape[0]} --shapeh {frame.shape[1]} --shape {frame.shape[2]}")
os.popen(f"python3 clind.py --name {shm.name} --shapew {frame.shape[0]} --shapeh {frame.shape[1]} --shape {frame.shape[2]}")
os.popen(f"python3 clind.py --name {shm.name} --shapew {frame.shape[0]} --shapeh {frame.shape[1]} --shape {frame.shape[2]}")
os.popen(f"python3 clind.py --name {shm.name} --shapew {frame.shape[0]} --shapeh {frame.shape[1]} --shape {frame.shape[2]}")
os.popen(f"python3 clind.py --name {shm.name} --shapew {frame.shape[0]} --shapeh {frame.shape[1]} --shape {frame.shape[2]}")


# Görüntü verilerini tutacak numpy dizisi (paylaşımlı bellek ile)
shared_frame = np.ndarray(frame.shape, dtype=frame.dtype, buffer=shm.buf)

try:
    while True:
        ret, frame = camera.read()
        if not ret:
            break
        
        # Kameradan alınan görüntüyü paylaşımlı belleğe kopyala
        np.copyto(shared_frame, frame)

        # Bekleme süresi (görüntü akışı hızını ayarlamak için)
        #time.sleep(0.033)  # Yaklaşık 30 FPS

finally:
    # Kamera ve paylaşımlı belleği serbest bırak
    camera.release()
    shm.close()
    shm.unlink()  # Paylaşımlı belleği serbest bırak
