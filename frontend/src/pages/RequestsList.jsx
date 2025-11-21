import { useState, useEffect } from 'react';
import { movingService } from '../services/movingService';
import Card from '../components/common/Card';
import Button from '../components/common/Button';
import { Link } from 'react-router-dom';

const RequestsList = () => {
  const [requests, setRequests] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    loadRequests();
  }, []);

  const loadRequests = async () => {
    try {
      const data = await movingService.getMovingRequests();
      setRequests(data);
    } catch (err) {
      setError('Erreur lors du chargement des demandes');
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return (
      <div className="container mx-auto px-6 py-12 text-center">
        <p className="text-xl">Chargement...</p>
      </div>
    );
  }

  return (
    <div className="container mx-auto px-6 py-12">
      <div className="flex justify-between items-center mb-8">
        <h1 className="text-3xl font-bold">Mes demandes de déménagement</h1>
        <Link to="/create-request">
          <Button>Nouvelle demande</Button>
        </Link>
      </div>

      {error && (
        <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-4">
          {error}
        </div>
      )}

      {requests.length === 0 ? (
        <Card>
          <p className="text-center text-gray-600">
            Vous n'avez pas encore de demandes de déménagement.
          </p>
        </Card>
      ) : (
        <div className="grid gap-6">
          {requests.map((request) => (
            <Card key={request.id}>
              <div className="flex justify-between items-start">
                <div className="flex-1">
                  <div className="flex items-center gap-2 mb-2">
                    <span className="text-2xl">📦</span>
                    <h3 className="text-xl font-semibold">
                      {request.pickup_city} → {request.delivery_city}
                    </h3>
                    <span className={`px-3 py-1 rounded-full text-sm ${
                      request.status === 'open' ? 'bg-blue-100 text-blue-800' :
                      request.status === 'accepted' ? 'bg-green-100 text-green-800' :
                      request.status === 'completed' ? 'bg-gray-100 text-gray-800' :
                      'bg-yellow-100 text-yellow-800'
                    }`}>
                      {request.status}
                    </span>
                  </div>
                  <p className="text-gray-600 mb-2">
                    📍 Départ: {request.pickup_address}, {request.pickup_postal_code}
                  </p>
                  <p className="text-gray-600 mb-2">
                    🎯 Arrivée: {request.delivery_address}, {request.delivery_postal_code}
                  </p>
                  <p className="text-gray-600 mb-2">
                    📅 Date: {new Date(request.moving_date).toLocaleDateString('fr-FR')}
                  </p>
                  {request.description && (
                    <p className="text-gray-600 mt-2">
                      {request.description}
                    </p>
                  )}
                </div>
                <Button size="sm" variant="outline">
                  Voir les détails
                </Button>
              </div>
            </Card>
          ))}
        </div>
      )}
    </div>
  );
};

export default RequestsList;
