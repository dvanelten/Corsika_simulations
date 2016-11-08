Inhalt des Verzeichnisses:

- readme.txt
- sipm_response_max.ipynb
- sipm_response_choose_random_1row.ipynb
- sipm_response_choose_for_every_photon.ipynb
- response.py
- response_parser.py
------------------------------------------------------------------------------

In diesem Verzeichnis liegen drei iPythonNotebook-Dateien sowie zwei Python-Datei, die für einen EAS die Response und Detektion der SiPM's angeben.
Zuerst wurden die ipynb-Dateien erstellt: Die Datei " sipm_response_max.ipynb " plottet die Antwort der Pixel in einem 2D Histogramm. Anschließend sucht er gemäß den Indizes der Photonen aus derselben Reihe in der detector response-Datei nach dem zugehörigen maximalen Wert (pde = photon detection effiency) sowie seinen zugehörigen Pixel (Zeilennamen). Diese werden anschließend in ein DataFrame umgewandelt. Zum Schluss wird eine Zahl zwischen [0,1] gewürfelt und geschaut, ob diese kleiner ist als der zugehörige Reiheneintrag. Falls ja, wwar die Detektion erfolgreich, ansonsten nicht. Am Ende wird ausgegeben, welcher Pixel wie viele Photonen detektieren konnte. 
Die Erweiterung davon ist die Datei " sipm_response_choose_random_1row.ipynb ". Der Plot der sipm response wurde zur besseren Übersicht entfernt. Außerdem wird nun ein Index ausgewählt und aus dieser Reihe gemäß der Wahrscheinlichkeiten der Zellinhalte ein Wert gezogen. Zum Schluss werden Abfragen gestartet über Zelleninhalt, Zeilenname und die gesamten Informationen.
Die Datei " sipm_response_choose_for_every_photon.ipynb " ist der nichtvollendete Versuch für alle Reihen den Vorgang durchzuführen. Dies gelingt soweit, dass für jeden Index aus der richtigen Reihe ein zufälliger Wert gezogen wird. Dies kann eben falls zu einem DataFrame zusammengefasst werden. Was fehlt, ist jedoch zum einen die korrekte Weiterverarbeitung danach, als auch die Ausgabe des zum random gezogenen Wertes zugehörigen Zeilenname, d.h. sipm.

------------------------------------------------------------------------------

Die fertigen Programme, die genau das richtige tun sind die beiden python-Dateien. Dabei unterscheiden diese sich nur darin, dass in " response_parser.py "
die genauen Pfade der.dat und .csv Dateien nicht mehr im Code angegeben sind, sondern dass diese über das Terminal beim Ausführen angegeben werden können.


