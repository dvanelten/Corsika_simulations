Inhalt des Verzeichnisses:

- readme.txt
- inputcard.txt
- shower.py
- hist.py
- 1_gamma_1.dat
- gamma_shower_500000.png
- gamma_shower_200000.png
- gamma_hist_500000.png
- gamma_hist_200000.png
- proton_shower_500000.png
- proton_shower_200000.png
- proton_hist_500000.png
- proton_hist_200000.png




------------------------------------------------------------------------------

In diesem Verzeichnis liegen die Materialien und Ergebnisse für die Simulation von 1Shower-Events für Gamma sowie Proton als primäres Teilchen. In der inputcard.txt muss dafür 
									
									PRMPAR   <NR_for_particle>
									TELFIL  /iceact/<name>.dat

angepasst werden. Die richtige Nummer PRMPAR   <NR_for_particle> kann dem usersguide.pdf in " $ /Users/dennisvanelten/Desktop/master-thesis/dokumentation " entnommen werden. Hier sind auch alle möglichen Angaben für die inputcard aufgelistet und erläutert. Für TELFIL  /iceact/<name>.dat kann ein beliebiger Name ausgesucht werden. Die restlichen Einstellungen in der inputcard.txt sind Standardeinstellungen. Sinnvoll ist die folgende Namenklatur:

									<#shower_particle_particleNR.dat>


Angabe der Partikel-Nummern auf Seite 110/110					1 = Gamma	14 = Proton 


Um das CORSIKA-File zu erzeugen, muss die inputcard.txt in dem Ordner </Desktop/iceact> liegen
Die Dateien werden im Ordner " $ /Users/dennisvanelten/Desktop/iceact " erzeugt.
Anschließend muss die .dat-Datei in den Ordner " $ /Users/dennisvanelten/anaconda3/lib/python3.5/site-packages/eventio/resources " kopiert werden.
Dann kann die .py-Datei darauf angewandt werden.
------------------------------------------------------------------------------

Es werden zufällige 500.000 Photonen geplottet.
Gewählte Namen für die inpucard.txt --> 1_gamma_1.dat / 1_proton_14.dat
