## real-estate-prediction
 ## Lavoro Sistemi Informativi:

Questa applicazione prevede il prezzo al metro quadro di immobili a Sindian, Nuova Taipei, Taiwan, utilizzando un modello di **regressione lineare**. Il modello si basa su variabili come la **latitudine** e la **longitudine** degli immobili per prevedere il prezzo.

📊 Dashboard Interattiva su Tableau  
Creazione di una dashboard con mappe e grafici che mostrano la relazione tra il prezzo degli immobili e altri fattori.  
🔗 **[Visualizza la dashboard su Tableau Public] https://public.tableau.com/app/profile/viola.francalanci/viz/Progetto_SistemiInformativi/Dashboard1?publish=yes**

📦 **Installazione**
1. Clonare il repository:
   ```bash
   git clone https://github.com/ViolaFrancalanci/real-estate-prediction.git
   cd real-estate-prediction
2. **Installare le dipendenze:**
   ```bash
   pip install -r requirements.txt
3. **Eseguire la web app:**
   ```bash
   streamlit run app.py

📂 Struttura del progetto
1. app.py: Il file principale per l'esecuzione dell'applicazione Streamlit.
2. requirements.txt: File contenente tutte le dipendenze necessarie per il progetto.
3. model.py: Il file che contiene il codice per il modello di regressione lineare.
4. dataset/: Cartella contenente i dataset utilizzati per addestrare il modello.
