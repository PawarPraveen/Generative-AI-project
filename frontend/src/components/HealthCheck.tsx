'use client';

import React, { useEffect, useState } from 'react';
import { apiClient } from '../lib/api-client.ts';
import { AlertCircle, CheckCircle } from 'lucide-react';

export function HealthCheck() {
  const [isHealthy, setIsHealthy] = useState<boolean | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    checkHealth();
  }, []);

  const checkHealth = async () => {
    try {
      const healthy = await apiClient.checkHealth();
      setIsHealthy(healthy);
      setError(null);
    } catch (err) {
      setIsHealthy(false);
      setError('Cannot connect to API server');
    }
  };

  return (
    <div className="p-4 bg-gray-50 rounded-lg">
      <div className="flex items-center gap-3">
        {isHealthy === null ? (
          <div className="animate-spin">⚙️</div>
        ) : isHealthy ? (
          <CheckCircle className="text-green-600" size={20} />
        ) : (
          <AlertCircle className="text-red-600" size={20} />
        )}
        <div>
          <p className="text-sm font-medium text-gray-700">API Status</p>
          <p className="text-xs text-gray-500">
            {isHealthy === null ? 'Checking...' : isHealthy ? 'Connected' : error || 'Disconnected'}
          </p>
        </div>
        <button
          onClick={checkHealth}
          className="ml-auto text-xs px-3 py-1 bg-gray-200 hover:bg-gray-300 rounded transition-colors"
        >
          Retry
        </button>
      </div>
    </div>
  );
}
