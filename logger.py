from datetime import datetime

RED = "\033[91m"
RESET = "\033[0m"
GREEN = "\033[92m"

class Logger:
	def getTime():
		return datetime.now().strftime("%H:%M:%S")

	def error(reason):
		print(f"[{Logger.getTime()}] {RED}{reason}{RESET}")
		pass

	def success(message):
		print(f"[{Logger.getTime()}] {GREEN}{message}{RESET}")

