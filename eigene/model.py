# 📦 Dies ist das Model-Paket für das Software-Installationssystem.
# Es enthält die Klassen und Sammlungen für Programme.

from .programm import Programm  # Importiert die Programm-Klasse
from .programmCollection import programms  # Importiert die Programmliste

__all__ = ["Programm", "programms"]  # Stellt sicher, dass diese Module verfügbar sind
