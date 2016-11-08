Inhalt des Verzeichnisses:

- readme.txt
- shower_circle.py
- gamma_area_iceact.png
- proton_area_iceact.png
- hist_circle.py
- gamma_hist_area_iceact.png
- gamma_hist_1000bins_area_iceact.png
- proton_hist_area_iceact.png
- proton_hist_1000bins_area_iceact.png


------------------------------------------------------------------------------

In diesem Verzeichnis liegen die Materialien und Ergebnisse für die Simulation von 1Shower-Events für Gamma sowie Proton als primäres Teilchen für den Bereich x,y = [-25.35,25.35]. Dies sind die Grenzen den IceAct-Detektors gemäß dem Proceeding: " Design study of an air-Cherenkov telescope for harsh environments with efficient air-shower detection at 100 TeV", Kapitel " 3.1 The mechanical part of the IceAct prototype " (2015). Dort ist der Durchmesser der Fresnel Linse mit 507 mm (50,7 mm) angegeben. 

Die Detektorfläche wird durch einen roten Kreis dargestellt.

Da die Anzahl der Teilchen in der Detektorfläche sehr gering ist (<10, wenn " photons = np.random.choice(photons,500000) ") wird nicht mehr eine zufällige Anzahl an Photonen geplottet, sondern alle. Gleichzeitig besteht aber immer noch die Möglichkeit die gesamten Photonen in der xy-Ebene zu plotten.
