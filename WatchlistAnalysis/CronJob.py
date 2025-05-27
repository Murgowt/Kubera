import sys
import logging
from datetime import datetime
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Database.DBOps.watchlist import get_all_watchlist
from WatchlistAnalysis.FetchPrices import fetch_prices

# Setup logging
log_dir = "logFiles"
os.makedirs(log_dir, exist_ok=True)
today = datetime.today().strftime('%Y-%m-%d')
log_file = os.path.join(log_dir, f"kubera_cron_{today}.log")
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def main():
    logging.info("Kubera cron job started.")
    WLStocks = get_all_watchlist()
    Stock_Prices = fetch_prices(WLStocks)
    for stock in Stock_Prices:
        print(stock)
    try:
        # --- PLACEHOLDER: Call your job logic here ---
        # Example: fetch_prices_and_update_db()

        logging.info("Kubera cron job completed successfully.")

    except Exception as e:
        logging.error(f"Error occurred: {e}", exc_info=True)
        sys.exit(1)

if __name__ == "__main__":
    main()
