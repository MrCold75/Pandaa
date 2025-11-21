const Footer = () => {
  return (
    <footer className="bg-gray-800 text-white mt-12">
      <div className="container mx-auto px-6 py-8">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          <div>
            <h3 className="text-xl font-bold mb-4">🚚 SpiritMoov</h3>
            <p className="text-gray-400">
              Votre plateforme de confiance pour trouver des déménageurs professionnels.
            </p>
          </div>
          <div>
            <h4 className="font-semibold mb-4">Liens rapides</h4>
            <ul className="space-y-2 text-gray-400">
              <li><a href="/" className="hover:text-white">Accueil</a></li>
              <li><a href="/about" className="hover:text-white">À propos</a></li>
              <li><a href="/contact" className="hover:text-white">Contact</a></li>
            </ul>
          </div>
          <div>
            <h4 className="font-semibold mb-4">Légal</h4>
            <ul className="space-y-2 text-gray-400">
              <li><a href="/privacy" className="hover:text-white">Confidentialité</a></li>
              <li><a href="/terms" className="hover:text-white">Conditions d'utilisation</a></li>
            </ul>
          </div>
        </div>
        <div className="border-t border-gray-700 mt-8 pt-6 text-center text-gray-400">
          <p>&copy; 2025 SpiritMoov. Tous droits réservés.</p>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
