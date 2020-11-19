from justupdate.client.client import JustUpdateClient
from client_config import ClientConfig

if __name__ == "__main__":
	client = JustUpdateClient(ClientConfig(), "0.0.2", "stable")

	if client.update_available():
		print("An update is available!")
		# proceed to download.
	else:
		print("No update available")
		# no update available, we are up to date.
