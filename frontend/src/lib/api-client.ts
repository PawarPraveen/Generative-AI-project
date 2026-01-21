import axios, { AxiosInstance } from 'axios';

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000/api';

export interface GenerateWebsiteRequest {
  user_prompt: string;
  website_type: 'portfolio' | 'ecommerce' | 'blog' | 'landing_page';
  title?: string;
}

export interface GeneratedWebsite {
  id: string;
  title: string;
  website_type: string;
  html: string;
  css: string;
  javascript?: string;
  created_at: string;
}

export interface Project {
  id: string;
  title: string;
  website_type: string;
  user_prompt: string;
  html: string;
  css: string;
  javascript?: string;
  created_at: string;
  updated_at: string;
}

class APIClient {
  private client: AxiosInstance;

  constructor() {
    this.client = axios.create({
      baseURL: API_BASE_URL,
      headers: {
        'Content-Type': 'application/json',
      },
    });
  }

  async generateWebsite(request: GenerateWebsiteRequest): Promise<GeneratedWebsite> {
    const response = await this.client.post('/generate-website', request);
    return response.data;
  }

  async getProject(id: string): Promise<Project> {
    const response = await this.client.get(`/projects/${id}`);
    return response.data;
  }

  async listProjects(skip = 0, limit = 10, websiteType?: string): Promise<Project[]> {
    const params: any = { skip, limit };
    if (websiteType) params.website_type = websiteType;
    const response = await this.client.get('/projects', { params });
    return response.data;
  }

  async deleteProject(id: string): Promise<void> {
    await this.client.delete(`/projects/${id}`);
  }

  async checkHealth(): Promise<boolean> {
    try {
      const response = await this.client.get('/health');
      return response.data.status === 'healthy';
    } catch {
      return false;
    }
  }
}

export const apiClient = new APIClient();
