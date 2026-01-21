'use client';

import React, { useEffect } from 'react';
import { useGeneratorStore } from '../lib/store';
import { apiClient } from '../lib/api-client';
import { Trash2, Eye } from 'lucide-react';

export function ProjectHistory() {
  const store = useGeneratorStore();
  const [isLoading, setIsLoading] = React.useState(false);

  useEffect(() => {
    loadProjects();
  }, []);

  const loadProjects = async () => {
    try {
      setIsLoading(true);
      const projects = await apiClient.listProjects(0, 20);
      store.setProjects(projects);
    } catch (error) {
      console.error('Failed to load projects:', error);
    } finally {
      setIsLoading(false);
    }
  };

  const handleDeleteProject = async (projectId: string) => {
    if (!confirm('Are you sure you want to delete this project?')) return;

    try {
      await apiClient.deleteProject(projectId);
      const updatedProjects = store.projects.filter((p) => p.id !== projectId);
      store.setProjects(updatedProjects);
    } catch (error) {
      console.error('Failed to delete project:', error);
      alert('Failed to delete project');
    }
  };

  const handleViewProject = async (projectId: string) => {
    try {
      const project = await apiClient.getProject(projectId);
      store.setCurrentProject(project);
      // Transform project to generatedWebsite format
      store.setGeneratedWebsite({
        id: project.id,
        title: project.title,
        website_type: project.website_type,
        html: project.html,
        css: project.css,
        javascript: project.javascript,
        created_at: project.created_at,
      });
    } catch (error) {
      console.error('Failed to load project:', error);
      alert('Failed to load project');
    }
  };

  return (
    <div className="bg-white rounded-lg shadow-lg p-6 h-full flex flex-col">
      <div className="flex justify-between items-center mb-6">
        <h3 className="text-xl font-bold text-gray-800">Project History</h3>
        <button
          onClick={loadProjects}
          disabled={isLoading}
          className="px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700 disabled:bg-gray-400 transition-colors text-sm font-medium"
        >
          {isLoading ? 'Loading...' : 'Refresh'}
        </button>
      </div>

      {store.projects.length === 0 ? (
        <div className="flex items-center justify-center h-32 text-gray-500">
          <p>No projects yet. Generate your first website to get started!</p>
        </div>
      ) : (
        <div className="flex-1 overflow-y-auto">
          <div className="space-y-3">
            {store.projects.map((project) => (
              <div
                key={project.id}
                className="p-4 border border-gray-200 rounded-lg hover:border-blue-400 hover:shadow-md transition-all"
              >
                <div className="flex items-start justify-between gap-3">
                  <div className="flex-1 min-w-0">
                    <h4 className="font-semibold text-gray-800 truncate">{project.title}</h4>
                    <p className="text-sm text-gray-500 capitalize">
                      Type: {project.website_type.replace('_', ' ')}
                    </p>
                    <p className="text-xs text-gray-400 mt-1">
                      {new Date(project.created_at).toLocaleDateString()} at{' '}
                      {new Date(project.created_at).toLocaleTimeString([], {
                        hour: '2-digit',
                        minute: '2-digit',
                      })}
                    </p>
                  </div>
                  <div className="flex gap-2">
                    <button
                      onClick={() => handleViewProject(project.id)}
                      title="View project"
                      className="p-2 text-blue-600 hover:bg-blue-50 rounded transition-colors"
                    >
                      <Eye size={18} />
                    </button>
                    <button
                      onClick={() => handleDeleteProject(project.id)}
                      title="Delete project"
                      className="p-2 text-red-600 hover:bg-red-50 rounded transition-colors"
                    >
                      <Trash2 size={18} />
                    </button>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}
