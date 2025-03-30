import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import Calendar
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Funzione per scaricare i dati e calcolare la correlazione
def calcola_corr():
    # Otteniamo i valori dai widget
    azione_ticker = azione_ticker_var.get()
    indice_ticker = indice_ticker_var.get()
    start_date = start_calendar.get_date()
    end_date = end_calendar.get_date()

    try:
        # Converto le date nel formato richiesto da yfinance ('YYYY-MM-DD')
        start_date = pd.to_datetime(start_date).strftime('%Y-%m-%d')
        end_date = pd.to_datetime(end_date).strftime('%Y-%m-%d')

        # Scarichiamo i dati con yfinance
        azione = yf.download(azione_ticker, start=start_date, end=end_date)
        indice = yf.download(indice_ticker, start=start_date, end=end_date)

        # Verifica delle prime righe dei dati
        if "Adj Close" in azione.columns:
            df = pd.merge(azione[["Adj Close"]], indice[["Adj Close"]], left_index=True, right_index=True, how="inner")
            df.columns = ["Azione", "Indice"]
        else:
            df = pd.merge(azione[["Close"]], indice[["Close"]], left_index=True, right_index=True, how="inner")
            df.columns = ["Azione", "Indice"]

        # Calcoliamo i rendimenti
        df = df.pct_change().dropna()

        # Calcoliamo la correlazione
        correlazione = df.corr().iloc[0, 1]
        label_corr.config(text=f"Correlazione tra {azione_ticker} e {indice_ticker}: {correlazione:.2f}")

        # Creiamo il grafico
        fig, ax = plt.subplots(figsize=(10, 5))
        df.plot(ax=ax, title=f"Rendimenti di {azione_ticker} e {indice_ticker}")

        # Aggiungiamo il grafico nella finestra
        for widget in frame_grafico.winfo_children():
            widget.destroy()  # Rimuoviamo il grafico precedente se esiste

        canvas = FigureCanvasTkAgg(fig, master=frame_grafico)
        canvas.draw()
        canvas.get_tk_widget().pack()

    except Exception as e:
        messagebox.showerror("Errore", f"Si è verificato un errore: {e}")

# Creiamo la finestra principale
root = Tk()
root.title("Calcolatore di Correlazione tra Azione e Indice")
root.geometry("800x600")

# Lista dei ticker disponibili
ticker_list = ["MSFT", "AAPL", "GOOGL", "AMZN", "META", "NVDA", "^NDX", "^GSPC"]

# Variabili per i ticker
azione_ticker_var = StringVar(value=ticker_list[0])
indice_ticker_var = StringVar(value=ticker_list[5])

# Label e ComboBox per il ticker dell'azione
label_azione = Label(root, text="Ticker Azione:")
label_azione.pack(pady=5)
combo_azione = ttk.Combobox(root, textvariable=azione_ticker_var, values=ticker_list)
combo_azione.pack(pady=5)

# Label e ComboBox per il ticker dell'indice
label_indice = Label(root, text="Ticker Indice:")
label_indice.pack(pady=5)
combo_indice = ttk.Combobox(root, textvariable=indice_ticker_var, values=ticker_list)
combo_indice.pack(pady=5)

# Label e Calendar per la data di inizio
label_start = Label(root, text="Data di Inizio:")
label_start.pack(pady=5)
start_calendar = Calendar(root, selectmode='day', year=2023, month=9, day=1)
start_calendar.pack(pady=5)

# Label e Calendar per la data di fine
label_end = Label(root, text="Data di Fine:")
label_end.pack(pady=5)
end_calendar = Calendar(root, selectmode='day', year=2025, month=3, day=1)
end_calendar.pack(pady=5)

# Bottone per calcolare la correlazione e generare il grafico
button_calcola = Button(root, text="Calcola Correlazione", command=calcola_corr)
button_calcola.pack(pady=10)

# Label per visualizzare la correlazione
label_corr = Label(root, text="", font=("Arial", 12))
label_corr.pack(pady=10)

# Frame per il grafico
frame_grafico = Frame(root)
frame_grafico.pack(pady=10)

# Avvio dell'interfaccia grafica
root.mainloop()
