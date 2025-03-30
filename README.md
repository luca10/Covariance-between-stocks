# Calcolatore di Correlazione tra Azione e Indice

Questo progetto permette di calcolare la correlazione tra il rendimento di un'azione e un indice di mercato, utilizzando i dati storici scaricati tramite l'API `yfinance`. L'applicazione è costruita con Python e offre una semplice interfaccia grafica utilizzando `Tkinter` per selezionare il periodo di interesse e i tickers da analizzare. Il risultato include sia il valore numerico della correlazione che un grafico dei rendimenti.

## Funzionalità

- **Selezione Ticker Azione e Indice**: Puoi scegliere tra un elenco di ticker predefiniti di azioni e indici.
- **Selezione Periodo**: Puoi selezionare un intervallo di date personalizzato tramite un calendario.
- **Calcolo della Correlazione**: Il programma calcola la correlazione tra i rendimenti dell'azione e dell'indice scelto.
- **Visualizzazione Grafico**: Viene visualizzato un grafico dei rendimenti delle due serie temporali (Azione e Indice).
- **Interfaccia Grafica**: Costruita con `Tkinter` per una facile interazione.

## Tecnologie

- **Python 3.x**
- **yfinance**: Per scaricare i dati storici delle azioni e degli indici.
- **Pandas**: Per elaborare e analizzare i dati.
- **Matplotlib**: Per generare il grafico dei rendimenti.
- **Tkinter**: Per creare l'interfaccia grafica.
- **tkcalendar**: Per il selettore di date.

## Requisiti

Per eseguire questo progetto, è necessario installare le seguenti librerie Python:

```bash
pip install yfinance pandas matplotlib tkcalendar

## Esempio di Utilizzo

Scegli un ticker per l'azione (ad esempio MSFT) e un ticker per l'indice (ad esempio ^NDX).

Seleziona un intervallo di date (ad esempio, dal 1 settembre 2023 al 1 marzo 2025).

Clicca su "Calcola Correlazione".

Il programma mostrerà la correlazione tra i rendimenti dell'azione e dell'indice, insieme al grafico dei rendimenti.
