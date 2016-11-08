Inhalt des Verzeichnisses:

- readme.txt
- shower_shuffle_photon.py
- hist_shuffle_photon.py
- shower_shuffle_photon_v2.py
- hist_shuffle_photon_v2.py
------------------------------------------------------------------------------

In diesem Verzeichnis liegen die beiden Python-Dateien, die a) 1 Shower-Simulation, b) die Detektorfläche (Kreis) sowie c) shuffled Photons beinhalten.

Dazu wurden die 2 Listen, die die x- bzw. y-Koordinaten der Photonen, die die Detekrofläche treffen, zu einem 2D-Array umgewandelt. Anschließend können dort über die np.random.shuffle()-Methode die rows vertauscht werden. Dadurch werden die Photonen nie in der gleichen Reihenfolge abgefragt, sondern die Reihenfolge der gezogenen Photonen erfolgt zufallsbasiert.

------------------------------------------------------------------------------

Ergänzt wurden die beiden Python-Dateien v2. Dabei handelt es sich um kompaktere Codes der ursprünglichen Dateien. Die Kürzung des Codes wurde durch Max Nöthe durchgeführt.