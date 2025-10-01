// Curseur luminosité
const lightSlider = document.getElementById("lightSlider");
const lightValue = document.getElementById("lightValue");

lightSlider.addEventListener("input", () => {
  lightValue.textContent = lightSlider.value + "%";
  console.log("Luminosité réglée à : " + lightSlider.value + "%");
});

// Bouton ouvrir la porte
document.getElementById("openDoor").addEventListener("click", () => {
  console.log("Commande : Ouvrir la porte");
  alert("🚪 La porte a été ouverte !");
});

// Bouton arroser
document.getElementById("waterPlant").addEventListener("click", () => {
  console.log("Commande : Arroser les plantes");
  alert("💧 Arrosage lancé !");
});
