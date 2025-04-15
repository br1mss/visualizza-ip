import speedtest

def run_speed_test():
    """Esegue uno speed test e stampa i risultati."""
    try:
        print("Esecuzione dello speed test...")
        st = speedtest.Speedtest()

        print("Ricerca del server migliore...")
        st.get_best_server()

        print("Download in corso...")
        st.download()

        print("Upload in corso...")
        st.upload()

        results_dict = st.results.dict()

        print("\n--- Risultati dello Speed Test ---")
        print(f"Server: {results_dict['server']['sponsor']} ({results_dict['server']['name']}, {results_dict['server']['country']})")
        print(f"Ping: {results_dict['ping']:.2f} ms")
        print(f"Velocità di Download: {results_dict['download'] / 1_000_000:.2f} Mbps")
        print(f"Velocità di Upload: {results_dict['upload'] / 1_000_000:.2f} Mbps")
        print(f"IP Pubblico: {results_dict['client']['ip']}")

    except speedtest.SpeedtestException as e:
        print(f"Si è verificato un errore durante lo speed test: {e}")
    except Exception as e:
        print(f"Si è verificato un errore inaspettato: {e}")

if __name__ == "__main__":
    run_speed_test()