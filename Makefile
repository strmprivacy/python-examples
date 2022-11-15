install-dependencies:
	python3 -m pip install -r requirements.txt

run-sender:
	@read -p "Enter [client id] [client secret] (separated by spaces):" clientId clientSecret; \
	python3 -u examples/sender_async.py --client-id $${clientId} --client-secret $${clientSecret}

run-synchronous-sender:
	@read -p "Enter [client id] [client secret] (separated by spaces):" clientId clientSecret; \
	python3 -u examples/sender_sync.py --client-id $${clientId} --client-secret $${clientSecret}
