'use client';

import { GeneratorForm } from '@/components/GeneratorForm';
import { PreviewPanel } from '@/components/PreviewPanel';
import { ProjectHistory } from '@/components/ProjectHistory';
import { HealthCheck } from '@/components/HealthCheck';

export default function Home() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-50 to-gray-100">
      {/* Header */}
      <header className="bg-gradient-to-r from-blue-600 to-blue-800 text-white shadow-lg">
        <div className="max-w-7xl mx-auto px-6 py-8">
          <div className="flex items-center justify-between">
            <div>
              <h1 className="text-4xl font-bold">AI Website Generator</h1>
              <p className="text-blue-100 mt-2">
                Generate beautiful, responsive websites with AI-powered design
              </p>
            </div>
          </div>
        </div>
      </header>

      {/* Main Content */}
      <main className="max-w-7xl mx-auto px-6 py-8">
        {/* Health Check */}
        <div className="mb-8">
          <HealthCheck />
        </div>

        {/* Layout: Form on left, Preview on right, History below */}
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8 mb-8">
          {/* Form Section - Left Column */}
          <div className="lg:col-span-1">
            <GeneratorForm />
          </div>

          {/* Preview Section - Right Column (spans 2) */}
          <div className="lg:col-span-2 min-h-96">
            <PreviewPanel />
          </div>
        </div>

        {/* Project History - Full Width */}
        <div className="h-96">
          <ProjectHistory />
        </div>
      </main>

      {/* Footer */}
      <footer className="bg-gray-800 text-gray-200 mt-16 py-8">
        <div className="max-w-7xl mx-auto px-6">
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8 mb-8">
            <div>
              <h4 className="font-bold text-white mb-2">AI Website Generator</h4>
              <p className="text-sm text-gray-400">
                Generate professional websites instantly using AI and advanced design patterns.
              </p>
            </div>
            <div>
              <h4 className="font-bold text-white mb-2">Features</h4>
              <ul className="text-sm text-gray-400 space-y-1">
                <li>• AI-Powered Design</li>
                <li>• Responsive Layouts</li>
                <li>• Multiple Website Types</li>
                <li>• Export as ZIP</li>
              </ul>
            </div>
            <div>
              <h4 className="font-bold text-white mb-2">Technologies</h4>
              <ul className="text-sm text-gray-400 space-y-1">
                <li>• Next.js & React</li>
                <li>• FastAPI Backend</li>
                <li>• OpenAI Integration</li>
                <li>• PostgreSQL Database</li>
              </ul>
            </div>
          </div>
          <div className="border-t border-gray-700 pt-8 text-center text-sm text-gray-400">
            <p>&copy; 2026 AI Website Generator. Built with Next.js and FastAPI.</p>
          </div>
        </div>
      </footer>
    </div>
  );
}
