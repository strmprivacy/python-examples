install-dependencies:
	python3 -m pip install -r requirements.txt

run-sender:
	@read -p "Enter [billing id] [client id] [client secret] (separated by spaces):" billingId clientId clientSecret; \
	python -u sender.py --billing-id $${billingId} --client-id $${clientId} --client-secret $${clientSecret}

run-synchronous-sender:
	@read -p "Enter [billing id] [client id] [client secret] (separated by spaces):" billingId clientId clientSecret; \
	python -u syncsender.py --billing-id $${billingId} --client-id $${clientId} --client-secret $${clientSecret}

run-receiver:
	@read -p "Enter [billing id] [client id] [client secret] (separated by spaces):" billingId clientId clientSecret; \
	python -u receiver.py --billing-id $${billingId} --client-id $${clientId} --client-secret $${clientSecret}
