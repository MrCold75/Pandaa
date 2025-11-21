import { Link } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import Button from '../components/common/Button';

const Home = () => {
  const { isAuthenticated } = useAuth();

  return (
    <div className="min-h-screen bg-gradient-to-b from-blue-50 to-white">
      {/* Hero Section */}
      <section className="container mx-auto px-6 py-20">
        <div className="text-center">
          <div className="text-8xl mb-6">🚚</div>
          <h1 className="text-5xl font-bold text-gray-900 mb-6">
            Bienvenue sur <span className="text-primary">SpiritMoov</span>
          </h1>
          <p className="text-xl text-gray-600 mb-8 max-w-2xl mx-auto">
            La plateforme qui connecte les clients avec des déménageurs professionnels.
            Obtenez plusieurs devis, comparez et choisissez le meilleur service.
          </p>
          {!isAuthenticated && (
            <div className="flex gap-4 justify-center">
              <Link to="/register">
                <Button size="lg">Commencer maintenant</Button>
              </Link>
              <Link to="/login">
                <Button variant="outline" size="lg">Se connecter</Button>
              </Link>
            </div>
          )}
          {isAuthenticated && (
            <Link to="/dashboard">
              <Button size="lg">Accéder au Dashboard</Button>
            </Link>
          )}
        </div>
      </section>

      {/* Features Section */}
      <section className="container mx-auto px-6 py-16">
        <h2 className="text-3xl font-bold text-center mb-12">Pourquoi choisir SpiritMoov ?</h2>
        <div className="grid md:grid-cols-3 gap-8">
          <div className="text-center p-6">
            <div className="text-5xl mb-4">📝</div>
            <h3 className="text-xl font-semibold mb-2">Création de demande</h3>
            <p className="text-gray-600">
              Créez votre demande en quelques minutes avec tous les détails de votre déménagement
            </p>
          </div>
          <div className="text-center p-6">
            <div className="text-5xl mb-4">💰</div>
            <h3 className="text-xl font-semibold mb-2">Comparez les devis</h3>
            <p className="text-gray-600">
              Recevez plusieurs devis de déménageurs professionnels et choisissez le meilleur
            </p>
          </div>
          <div className="text-center p-6">
            <div className="text-5xl mb-4">⭐</div>
            <h3 className="text-xl font-semibold mb-2">Notations transparentes</h3>
            <p className="text-gray-600">
              Consultez les avis des autres clients pour faire le bon choix
            </p>
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="bg-primary text-white py-16">
        <div className="container mx-auto px-6 text-center">
          <h2 className="text-3xl font-bold mb-4">Prêt à déménager ?</h2>
          <p className="text-xl mb-8">Créez votre compte dès maintenant et commencez à recevoir des devis</p>
          {!isAuthenticated && (
            <Link to="/register">
              <Button variant="secondary" size="lg">S'inscrire gratuitement</Button>
            </Link>
          )}
        </div>
      </section>
    </div>
  );
};

export default Home;
