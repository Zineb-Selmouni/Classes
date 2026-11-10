"""Étape 2 — Decorator : enchanter une arme sans créer une classe par combinaison.

Un enchantement enveloppe une arme (ou une arme déjà enchantée) et offre la même
interface : les propriétés nom, degats et critique.
- ArmeDecorateur(arme) : délègue nom, degats et critique à l'arme enveloppée ;
- EnchantementDeFeu : nom + " de feu", +4 dégâts ;
- EnchantementDeGivre : nom + " de givre", +2 dégâts ;
- EnchantementAffute : nom + " affûtée", +0.15 de critique (au plus 1.0).
"""

# TODO
