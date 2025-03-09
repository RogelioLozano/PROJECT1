# Define project directories
BACKEND_DIR=/Users/rogeliolozano/PROJECT1/VQA-model-service
FRONTEND_DIR=/Users/rogeliolozano/PROJECT1/quasar-inventory

# Define commands
install:
	pip install -r $(BACKEND_DIR)/requirements.txt
	npm install --prefix $(FRONTEND_DIR)

start:
	(cd $(BACKEND_DIR) && fastapi dev app/main.py) &
	(cd $(FRONTEND_DIR) && npm run dev)

stop:
	@pkill -f "fastapi dev app/main.py" || true
	@pkill -f "npm run dev" || true