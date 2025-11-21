import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { movingService } from '../services/movingService';
import Button from '../components/common/Button';
import Input from '../components/common/Input';
import Card from '../components/common/Card';

const CreateRequest = () => {
  const [formData, setFormData] = useState({
    pickup_address: '',
    pickup_city: '',
    pickup_postal_code: '',
    delivery_address: '',
    delivery_city: '',
    delivery_postal_code: '',
    moving_date: '',
    description: '',
    estimated_volume: '',
    has_heavy_items: false,
    has_fragile_items: false,
    floor_pickup: 0,
    floor_delivery: 0,
    has_elevator_pickup: false,
    has_elevator_delivery: false,
  });
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  const handleChange = (e) => {
    const { name, value, type, checked } = e.target;
    setFormData({
      ...formData,
      [name]: type === 'checkbox' ? checked : value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    setLoading(true);

    try {
      const requestData = {
        ...formData,
        moving_date: new Date(formData.moving_date).toISOString(),
        estimated_volume: formData.estimated_volume ? parseFloat(formData.estimated_volume) : null,
        floor_pickup: parseInt(formData.floor_pickup),
        floor_delivery: parseInt(formData.floor_delivery),
      };
      
      await movingService.createMovingRequest(requestData);
      navigate('/requests');
    } catch (err) {
      setError(err.response?.data?.detail || 'Erreur lors de la création de la demande');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container mx-auto px-6 py-12">
      <Card className="max-w-4xl mx-auto">
        <h1 className="text-3xl font-bold mb-6">Nouvelle demande de déménagement</h1>

        {error && (
          <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-4">
            {error}
          </div>
        )}

        <form onSubmit={handleSubmit}>
          <div className="mb-6">
            <h2 className="text-xl font-semibold mb-4">📍 Point de départ</h2>
            <div className="grid md:grid-cols-3 gap-4">
              <div className="md:col-span-2">
                <Input
                  label="Adresse"
                  name="pickup_address"
                  value={formData.pickup_address}
                  onChange={handleChange}
                  required
                />
              </div>
              <Input
                label="Étage"
                type="number"
                name="floor_pickup"
                value={formData.floor_pickup}
                onChange={handleChange}
              />
              <Input
                label="Ville"
                name="pickup_city"
                value={formData.pickup_city}
                onChange={handleChange}
                required
              />
              <Input
                label="Code postal"
                name="pickup_postal_code"
                value={formData.pickup_postal_code}
                onChange={handleChange}
                required
              />
              <div className="flex items-center">
                <label className="flex items-center mt-6">
                  <input
                    type="checkbox"
                    name="has_elevator_pickup"
                    checked={formData.has_elevator_pickup}
                    onChange={handleChange}
                    className="mr-2 h-4 w-4"
                  />
                  <span>Ascenseur disponible</span>
                </label>
              </div>
            </div>
          </div>

          <div className="mb-6">
            <h2 className="text-xl font-semibold mb-4">🎯 Point d'arrivée</h2>
            <div className="grid md:grid-cols-3 gap-4">
              <div className="md:col-span-2">
                <Input
                  label="Adresse"
                  name="delivery_address"
                  value={formData.delivery_address}
                  onChange={handleChange}
                  required
                />
              </div>
              <Input
                label="Étage"
                type="number"
                name="floor_delivery"
                value={formData.floor_delivery}
                onChange={handleChange}
              />
              <Input
                label="Ville"
                name="delivery_city"
                value={formData.delivery_city}
                onChange={handleChange}
                required
              />
              <Input
                label="Code postal"
                name="delivery_postal_code"
                value={formData.delivery_postal_code}
                onChange={handleChange}
                required
              />
              <div className="flex items-center">
                <label className="flex items-center mt-6">
                  <input
                    type="checkbox"
                    name="has_elevator_delivery"
                    checked={formData.has_elevator_delivery}
                    onChange={handleChange}
                    className="mr-2 h-4 w-4"
                  />
                  <span>Ascenseur disponible</span>
                </label>
              </div>
            </div>
          </div>

          <div className="mb-6">
            <h2 className="text-xl font-semibold mb-4">📦 Détails du déménagement</h2>
            <div className="grid md:grid-cols-2 gap-4">
              <Input
                label="Date du déménagement"
                type="datetime-local"
                name="moving_date"
                value={formData.moving_date}
                onChange={handleChange}
                required
              />
              <Input
                label="Volume estimé (m³)"
                type="number"
                step="0.1"
                name="estimated_volume"
                value={formData.estimated_volume}
                onChange={handleChange}
              />
            </div>
            
            <div className="mb-4">
              <label className="block text-sm font-medium text-gray-700 mb-1">
                Description
              </label>
              <textarea
                name="description"
                value={formData.description}
                onChange={handleChange}
                rows="4"
                className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary"
                placeholder="Décrivez votre déménagement..."
              />
            </div>

            <div className="space-y-2">
              <label className="flex items-center">
                <input
                  type="checkbox"
                  name="has_heavy_items"
                  checked={formData.has_heavy_items}
                  onChange={handleChange}
                  className="mr-2 h-4 w-4"
                />
                <span>Objets lourds (piano, coffre-fort, etc.)</span>
              </label>
              <label className="flex items-center">
                <input
                  type="checkbox"
                  name="has_fragile_items"
                  checked={formData.has_fragile_items}
                  onChange={handleChange}
                  className="mr-2 h-4 w-4"
                />
                <span>Objets fragiles</span>
              </label>
            </div>
          </div>

          <div className="flex gap-4">
            <Button type="submit" disabled={loading}>
              {loading ? 'Création...' : 'Créer la demande'}
            </Button>
            <Button type="button" variant="outline" onClick={() => navigate('/dashboard')}>
              Annuler
            </Button>
          </div>
        </form>
      </Card>
    </div>
  );
};

export default CreateRequest;
