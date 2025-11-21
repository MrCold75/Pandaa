import { useAuth } from '../context/AuthContext';
import Card from '../components/common/Card';
import { Link } from 'react-router-dom';
import Button from '../components/common/Button';

const Dashboard = () => {
  const { user } = useAuth();

  return (
    <div className="container mx-auto px-6 py-12">
      <h1 className="text-3xl font-bold mb-8">
        Bienvenue, {user?.full_name} 👋
      </h1>

      <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
        <Card>
          <h3 className="text-xl font-semibold mb-4">📋 Mes demandes</h3>
          <p className="text-gray-600 mb-4">
            Consultez et gérez toutes vos demandes de déménagement
          </p>
          <Link to="/requests">
            <Button size="sm">Voir les demandes</Button>
          </Link>
        </Card>

        {!user?.is_mover && (
          <Card>
            <h3 className="text-xl font-semibold mb-4">➕ Nouvelle demande</h3>
            <p className="text-gray-600 mb-4">
              Créez une nouvelle demande de déménagement
            </p>
            <Link to="/create-request">
              <Button size="sm" variant="secondary">Créer une demande</Button>
            </Link>
          </Card>
        )}

        <Card>
          <h3 className="text-xl font-semibold mb-4">👤 Mon profil</h3>
          <p className="text-gray-600 mb-4">
            Consultez et modifiez vos informations personnelles
          </p>
          <Link to="/profile">
            <Button size="sm" variant="outline">Voir le profil</Button>
          </Link>
        </Card>

        {user?.is_mover && (
          <Card>
            <h3 className="text-xl font-semibold mb-4">⭐ Ma réputation</h3>
            <div className="text-3xl font-bold text-primary mb-2">
              {user.average_rating.toFixed(1)} / 5.0
            </div>
            <p className="text-gray-600">
              {user.total_ratings} évaluation{user.total_ratings > 1 ? 's' : ''}
            </p>
          </Card>
        )}
      </div>
    </div>
  );
};

export default Dashboard;
