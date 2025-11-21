import api from './api';

export const movingService = {
  // Moving Requests
  async createMovingRequest(requestData) {
    const response = await api.post('/moving-requests', requestData);
    return response.data;
  },

  async getMovingRequests(status = null) {
    const params = status ? { status } : {};
    const response = await api.get('/moving-requests', { params });
    return response.data;
  },

  async getMovingRequest(requestId) {
    const response = await api.get(`/moving-requests/${requestId}`);
    return response.data;
  },

  async updateMovingRequest(requestId, requestData) {
    const response = await api.put(`/moving-requests/${requestId}`, requestData);
    return response.data;
  },

  async deleteMovingRequest(requestId) {
    const response = await api.delete(`/moving-requests/${requestId}`);
    return response.data;
  },

  // Quotes
  async createQuote(quoteData) {
    const response = await api.post('/quotes', quoteData);
    return response.data;
  },

  async getQuotes(movingRequestId = null) {
    const params = movingRequestId ? { moving_request_id: movingRequestId } : {};
    const response = await api.get('/quotes', { params });
    return response.data;
  },

  async getQuote(quoteId) {
    const response = await api.get(`/quotes/${quoteId}`);
    return response.data;
  },

  async acceptQuote(quoteId) {
    const response = await api.put(`/quotes/${quoteId}/accept`);
    return response.data;
  },

  async rejectQuote(quoteId) {
    const response = await api.put(`/quotes/${quoteId}/reject`);
    return response.data;
  },

  // Ratings
  async createRating(ratingData) {
    const response = await api.post('/ratings', ratingData);
    return response.data;
  },

  async getUserRatings(userId) {
    const response = await api.get(`/ratings/user/${userId}`);
    return response.data;
  },

  // Users
  async getCurrentUserProfile() {
    const response = await api.get('/users/me');
    return response.data;
  },

  async updateCurrentUserProfile(userData) {
    const response = await api.put('/users/me', userData);
    return response.data;
  },

  async getUserProfile(userId) {
    const response = await api.get(`/users/${userId}`);
    return response.data;
  },
};
