install-dependencies:
	python3 -m pip install -r requirements.txt

run-sender:
	@read -p "Enter [billing id] [client id] [client secret] (separated by spaces):" billingId clientId clientSecret; \
	python3 -u examples/sender_async.py --billing-id $${billingId} --client-id $${clientId} --client-secret $${clientSecret}

run-synchronous-sender:
	@read -p "Enter [billing id] [client id] [client secret] (separated by spaces):" billingId clientId clientSecret; \
	python3 -u examples/sender_sync.py --billing-id $${billingId} --client-id $${clientId} --client-secret $${clientSecret}

run-receiver:
	@read -p "Enter [billing id] [client id] [client secret] (separated by spaces):" billingId clientId clientSecret; \
	python3 -u examples/receiver.py --billing-id $${billingId} --client-id $${clientId} --client-secret $${clientSecret}
