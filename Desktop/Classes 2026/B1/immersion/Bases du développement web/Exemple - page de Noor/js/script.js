// 1. Mode sombre / clair
const bouton = document.querySelector("#theme");

bouton.addEventListener("click", () => {
  document.body.classList.toggle("sombre");
});

// 2. Message de bienvenue selon l'heure
const heure = new Date().getHours();
const message = document.querySelector("#bienvenue");

if (heure < 18) {
  message.textContent = "Bonjour et bienvenue.";
} else {
  message.textContent = "Bonsoir et bienvenue.";
}

// 3. Validation du formulaire
const formulaire = document.querySelector("#formulaire");
const erreur = document.querySelector("#erreur");

formulaire.addEventListener("submit", (event) => {
  event.preventDefault();
  const email = document.querySelector("#email").value;

  if (!email.includes("@")) {
    erreur.textContent = "E-mail invalide : il manque le @.";
  } else {
    erreur.textContent = "";
    alert("Merci, votre message est bien parti.");
  }
});
