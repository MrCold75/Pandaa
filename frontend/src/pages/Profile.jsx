import { useState, useEffect } from 'react';
import { useAuth } from '../context/AuthContext';
import { movingService } from '../services/movingService';
import Card from '../components/common/Card';
import Button from '../components/common/Button';
import Input from '../components/common/Input';

const Profile = () => {
  const { user, logout } = useAuth();
  const [editing, setEditing] = useState(false);
  const [formData, setFormData] = useState({
    full_name: user?.full_name || '',
    phone: user?.phone || '',
    company_name: user?.company_name || '',
    description: user?.description || '',
    service_area: user?.service_area || '',
  });
  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState('');

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setMessage('');

    try {
      await movingService.updateCurrentUserProfile(formData);
      setMessage('Profil mis à jour avec succès');
      setEditing(false);
      // Reload page to update user data
      window.location.reload();
    } catch (err) {
      setMessage('Erreur lors de la mise à jour du profil');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container mx-auto px-6 py-12">
      <Card className="max-w-2xl mx-auto">
        <div className="flex justify-between items-center mb-6">
          <h1 className="text-3xl font-bold">Mon profil</h1>
          {!editing && (
            <Button size="sm" onClick={() => setEditing(true)}>
              Modifier
            </Button>
          )}
        </div>

        {message && (
          <div className={`px-4 py-3 rounded mb-4 ${
            message.includes('succès') 
              ? 'bg-green-100 border border-green-400 text-green-700'
              : 'bg-red-100 border border-red-400 text-red-700'
          }`}>
            {message}
          </div>
        )}

        {editing ? (
          <form onSubmit={handleSubmit}>
            <Input
              label="Nom complet"
              name="full_name"
              value={formData.full_name}
              onChange={handleChange}
              required
            />
            <Input
              label="Téléphone"
              name="phone"
              value={formData.phone}
              onChange={handleChange}
            />

            {user?.is_mover && (
              <>
                <Input
                  label="Nom de l'entreprise"
                  name="company_name"
                  value={formData.company_name}
                  onChange={handleChange}
                />
                <Input
                  label="Zone de service"
                  name="service_area"
                  value={formData.service_area}
                  onChange={handleChange}
                />
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
                  />
                </div>
              </>
            )}

            <div className="flex gap-4">
              <Button type="submit" disabled={loading}>
                {loading ? 'Enregistrement...' : 'Enregistrer'}
              </Button>
              <Button
                type="button"
                variant="outline"
                onClick={() => {
                  setEditing(false);
                  setFormData({
                    full_name: user?.full_name || '',
                    phone: user?.phone || '',
                    company_name: user?.company_name || '',
                    description: user?.description || '',
                    service_area: user?.service_area || '',
                  });
                }}
              >
                Annuler
              </Button>
            </div>
          </form>
        ) : (
          <div className="space-y-4">
            <div>
              <label className="text-sm text-gray-600">Email</label>
              <p className="text-lg font-medium">{user?.email}</p>
            </div>
            <div>
              <label className="text-sm text-gray-600">Nom complet</label>
              <p className="text-lg font-medium">{user?.full_name}</p>
            </div>
            <div>
              <label className="text-sm text-gray-600">Téléphone</label>
              <p className="text-lg font-medium">{user?.phone || 'Non renseigné'}</p>
            </div>
            <div>
              <label className="text-sm text-gray-600">Type de compte</label>
              <p className="text-lg font-medium">
                {user?.is_mover ? '🚚 Déménageur professionnel' : '👤 Client'}
              </p>
            </div>

            {user?.is_mover && (
              <>
                <div>
                  <label className="text-sm text-gray-600">Entreprise</label>
                  <p className="text-lg font-medium">{user?.company_name || 'Non renseigné'}</p>
                </div>
                <div>
                  <label className="text-sm text-gray-600">Zone de service</label>
                  <p className="text-lg font-medium">{user?.service_area || 'Non renseigné'}</p>
                </div>
                <div>
                  <label className="text-sm text-gray-600">Description</label>
                  <p className="text-lg font-medium">{user?.description || 'Non renseigné'}</p>
                </div>
                <div>
                  <label className="text-sm text-gray-600">Réputation</label>
                  <p className="text-lg font-medium">
                    ⭐ {user?.average_rating?.toFixed(1)} / 5.0 ({user?.total_ratings} avis)
                  </p>
                </div>
              </>
            )}
          </div>
        )}
      </Card>
    </div>
  );
};

export default Profile;
