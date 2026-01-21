'use client';

import React from 'react';
import { useGeneratorStore } from '../lib/store.ts';
import { apiClient } from '../lib/api-client.ts';

export function GeneratorForm() {
  const store = useGeneratorStore();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    if (!store.userPrompt.trim()) {
      store.setError('Please enter a description of your website');
      return;
    }

    if (store.userPrompt.length < 10) {
      store.setError('Description must be at least 10 characters');
      return;
    }

    try {
      store.setIsLoading(true);
      store.setError(null);

      const response = await apiClient.generateWebsite({
        user_prompt: store.userPrompt,
        website_type: store.websiteType,
        title: store.title || `My ${store.websiteType.replace('_', ' ')} Website`,
      });

      store.setGeneratedWebsite(response);
    } catch (error: any) {
      store.setError(
        error.response?.data?.detail || 
        error.message || 
        'Failed to generate website. Please try again.'
      );
    } finally {
      store.setIsLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="w-full max-w-2xl mx-auto p-6 bg-white rounded-lg shadow-lg">
      <div className="space-y-6">
        {/* Title Input */}
        <div>
          <label htmlFor="title" className="block text-sm font-medium text-gray-700 mb-2">
            Website Title (Optional)
          </label>
          <input
            id="title"
            type="text"
            placeholder="e.g., John's Portfolio"
            value={store.title}
            onChange={(e) => store.setTitle(e.target.value)}
            className="w-full px-4 py-2 bg-white text-gray-900 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent placeholder-gray-500"
          />
        </div>

        {/* Website Type Selection */}
        <div>
          <label htmlFor="website-type" className="block text-sm font-medium text-gray-700 mb-2">
            Website Type
          </label>
          <select
            id="website-type"
            value={store.websiteType}
            onChange={(e) =>
              store.setWebsiteType(
                e.target.value as 'portfolio' | 'ecommerce' | 'blog' | 'landing_page'
              )
            }
            className="w-full px-4 py-2 bg-white text-gray-900 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
          >
            <option value="landing_page">Landing Page</option>
            <option value="portfolio">Portfolio</option>
            <option value="blog">Blog</option>
            <option value="ecommerce">E-Commerce</option>
          </select>
        </div>

        {/* User Prompt */}
        <div>
          <label htmlFor="prompt" className="block text-sm font-medium text-gray-700 mb-2">
            Describe Your Website *
          </label>
          <textarea
            id="prompt"
            placeholder="e.g., A modern portfolio website for a software engineer with dark theme, showcase of projects, contact form, and social links..."
            value={store.userPrompt}
            onChange={(e) => store.setUserPrompt(e.target.value)}
            rows={6}
            className="w-full px-4 py-2 bg-white text-gray-900 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent resize-none placeholder-gray-500"
          />
          <p className="text-sm text-gray-500 mt-1">
            {store.userPrompt.length}/2000 characters
          </p>
        </div>

        {/* Error Message */}
        {store.error && (
          <div className="p-4 bg-red-50 border border-red-200 rounded-lg">
            <p className="text-red-700 text-sm">{store.error}</p>
          </div>
        )}

        {/* Submit Button */}
        <button
          type="submit"
          disabled={store.isLoading}
          className="w-full px-6 py-3 bg-blue-600 text-white font-medium rounded-lg hover:bg-blue-700 disabled:bg-gray-400 disabled:cursor-not-allowed transition-colors"
        >
          {store.isLoading ? (
            <span className="flex items-center justify-center gap-2">
              <span className="inline-block animate-spin">⚙️</span>
              Generating Website...
            </span>
          ) : (
            'Generate Website'
          )}
        </button>
      </div>
    </form>
  );
}
