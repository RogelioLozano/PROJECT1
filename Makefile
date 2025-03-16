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

production:
	(cd $(BACKEND_DIR) && uvicorn app.main:app --host 0.0.0.0 --port $(PORT)) &
	(cd $(FRONTEND_DIR) && npm run start)


stop:
	@pkill -f "fastapi dev app/main.py" || true
	@pkill -f "npm run dev" || true