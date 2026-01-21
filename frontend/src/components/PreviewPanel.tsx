'use client';

import React, { useEffect } from 'react';
import { useGeneratorStore } from '../lib/store.ts';
import JSZip from 'jszip';

export function PreviewPanel() {
  const website = useGeneratorStore((state) => state.generatedWebsite);
  const [iframeKey, setIframeKey] = React.useState(0);

  const handleDownloadZip = async () => {
    if (!website) return;

    try {
      const zip = new JSZip();

      // Add HTML file
      zip.file('index.html', website.html);

      // Add CSS file
      zip.file('styles.css', website.css);

      // Add JavaScript file if exists
      if (website.javascript) {
        zip.file('script.js', website.javascript);
      }

      // Generate ZIP file
      const blob = await zip.generateAsync({ type: 'blob' });
      const url = URL.createObjectURL(blob);
      const link = document.createElement('a');
      link.href = url;
      link.download = `${website.title || 'website'}.zip`;
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
      URL.revokeObjectURL(url);
    } catch (error) {
      console.error('Failed to download website:', error);
      alert('Failed to download website. Please try again.');
    }
  };

  const handleOpenInNewTab = () => {
    if (!website) return;

    const htmlContent = `
      <!DOCTYPE html>
      <html lang="en">
      <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>${website.title || 'Generated Website'}</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <style>
          ${website.css}
        </style>
      </head>
      <body>
        ${website.html}
        <script>
          ${website.javascript || ''}
        </script>
      </body>
      </html>
    `;

    const newWindow = window.open();
    if (newWindow) {
      newWindow.document.write(htmlContent);
      newWindow.document.close();
    }
  };

  if (!website) {
    return (
      <div className="flex items-center justify-center h-full bg-gray-50">
        <div className="text-center">
          <p className="text-gray-500 text-lg">Generate a website to preview it here</p>
        </div>
      </div>
    );
  }

  return (
    <div className="flex flex-col h-full bg-white rounded-lg shadow-lg overflow-hidden">
      {/* Header */}
      <div className="bg-gradient-to-r from-blue-600 to-blue-700 p-6 text-white">
        <h3 className="text-xl font-bold mb-2">{website.title}</h3>
        <p className="text-blue-100 text-sm mb-4">
          Type: <span className="capitalize">{website.website_type}</span> • Created:{' '}
          {new Date(website.created_at).toLocaleDateString()}
        </p>
        <div className="flex gap-3">
          <button
            onClick={handleOpenInNewTab}
            className="px-4 py-2 bg-white text-blue-600 font-medium rounded hover:bg-blue-50 transition-colors"
          >
            Open in New Tab
          </button>
          <button
            onClick={handleDownloadZip}
            className="px-4 py-2 bg-blue-500 hover:bg-blue-400 text-white font-medium rounded transition-colors"
          >
            Download as ZIP
          </button>
        </div>
      </div>

      {/* Preview Area */}
      <div className="flex-1 overflow-hidden">
        <iframe
          key={iframeKey}
          title="Website Preview"
          className="w-full h-full border-none"
          srcDoc={`
            <!DOCTYPE html>
            <html lang="en">
            <head>
              <meta charset="UTF-8">
              <meta name="viewport" content="width=device-width, initial-scale=1.0">
              <title>${website.title || 'Preview'}</title>
              <script src="https://cdn.tailwindcss.com"></script>
              <style>
                ${website.css}
              </style>
            </head>
            <body>
              ${website.html}
              <script>
                ${website.javascript || ''}
              </script>
            </body>
            </html>
          `}
        />
      </div>
    </div>
  );
}
