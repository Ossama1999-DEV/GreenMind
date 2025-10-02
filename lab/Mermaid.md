```mermaid
flowchart TD

subgraph User["👤 Utilisateur"]
  UIWeb["🌐 Interface Web"]
  UIMobile["📱 App Mobile"]
end

subgraph Pi["🍓 Raspberry Pi 3"]
  AI["🤖 IA / Vision (Caméra)"]
  WebServer["💻 Serveur Web (Dashboard)"]
  Orchestrator["🧩 Orchestrateur (MQTT / Logique)"]
end

subgraph ESP["⚡ ESP32 (IoT)"]
  Sensors["🌡️ Capteurs (Temp, Humidité)"]
  Actuators["⚙️ Actionneurs (Pompe, LED, Ventilateur, Porte)"]
  Arm["🦾 Bras robotique (semis)"]
end

User --> UIWeb --> WebServer
User --> UIMobile --> WebServer

Pi --> Orchestrator
Orchestrator <--> ESP
AI --> Orchestrator

ESP --> Sensors
ESP --> Actuators
ESP --> Arm

---

## 🔹 Résultat (vue simplifiée)

- **Utilisateur** interagit via **UI Web / App Mobile**  
- La **Raspberry Pi 3** :  
  - héberge le **serveur web** et l’IA (vision caméra),  
  - joue le rôle d’**orchestrateur** (MQTT / règles IA).  
- L’**ESP32** :  
  - gère **capteurs** (T°, humidité),  
  - pilote **actionneurs** (pompe, LED, ventilateur, porte),  
  - contrôle le **bras robotique** pour les semis.  

---

👉 Est-ce que tu veux que je te génère aussi une **version image PNG** directement (que tu pourras afficher dans ton `doc/architecture.png`) à partir de ce diagramme Mermaid ?
