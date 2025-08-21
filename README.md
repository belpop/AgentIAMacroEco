# Agent IA Macro (MVP)

Ce projet surveille les flux RSS macroéconomiques (Reuters, Fed, BCE, BoE) et envoie des alertes Telegram quand un événement important est détecté.

## 🚀 Déploiement sur Render

1. Crée un repo GitHub et pousse ce code.
2. Va sur [Render](https://render.com), crée un compte, clique sur **New > Web Service**.
3. Connecte ton repo GitHub.
4. Configure :  
   - **Environment**: Python 3  
   - **Build Command**: `pip install -r requirements.txt`  
   - **Start Command**: `./start.sh`
5. Ajoute tes variables d’environnement :  
   - `TELEGRAM_BOT_TOKEN` (token de ton bot)  
   - `TELEGRAM_CHAT_ID` (ton chat ID perso ou canal Telegram)

Ton bot sera actif en continu et t’enverra des alertes 📲.
