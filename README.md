# Automatische Generierung von Titeln und Abstracts

Das ist das Repository meiner Bachelorarbeit 

      1. Betreuer: Prof. Dr. Ing. Korbinian Riedhammer
      2. Betreuer: Prof. Dr. Jens Albrecht
 
 Anmeldung: 20.04.2020
 
 Abgabedatum: 20.09.2020

1. scrapy Ordner

In diesem sind die Spider zum Holen des englischen Datensatzes zu finden. Diese können mit folgenden Kommandos über die Konsole geholt werden:
			
	scrapy crawl interspeech16-19 -o interspeech.jl
	scrapy crawl interspeech15 -o interspeech.jl

2. Database Ordner 

Hier sind alle Daten zur Datenbank gespeichert. Das Datensatz.ipynb Notebook ist ausgelegt in Google Colab zu Funktionieren.
Es kann aber auch Lokal ausgeführt werden, dazu muss der Teil übersprungen werden, der die Verbindung zu Google Drive herstellt.

3. Preprocess_Data.ipynb

In dieser Datei werden die Daten aus der Datenbank für das BERT-Modell vorbereitet. Dieses Notebook kann wie das Notebook vom Datensatz sowohl in Google Colab als auch Lokal ausgeführt werden. Hierzu sind auch wieder die Teile zu überspringen, die die Verbindung zu Google Drive herstellen. 

4. BERTSUM_Durchfruehrung.ipynb

Hier wird das Training von BERTSUM durchführt. Dieses Notebook ist nur darauf ausgelegt in Google Colab zu laufen. Um es Lokal auszuführen müssen die Pfade in den Kommandozeile ausgetauscht werden.

5. Evaluation.ipynb

Dieses Notebook beschäftig sich mit der Evaluation. Auch hier ist das Notebook darauf ausgelegt in Google Colab zu funktionieren, bei einem Lokalen Start müssen die Pfade angepasst werden.

6. BertSum Ordner

In diesen Ordner sind alle Dateien zum BERTSUM-Modell gespeichert.
