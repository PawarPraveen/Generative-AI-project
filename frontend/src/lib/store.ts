import { create } from 'zustand';
import { GeneratedWebsite, Project } from './api-client';

interface GeneratorStore {
  userPrompt: string;
  websiteType: 'portfolio' | 'ecommerce' | 'blog' | 'landing_page';
  title: string;
  isLoading: boolean;
  error: string | null;
  generatedWebsite: GeneratedWebsite | null;
  projects: Project[];
  currentProject: Project | null;

  // Actions
  setUserPrompt: (prompt: string) => void;
  setWebsiteType: (type: 'portfolio' | 'ecommerce' | 'blog' | 'landing_page') => void;
  setTitle: (title: string) => void;
  setIsLoading: (loading: boolean) => void;
  setError: (error: string | null) => void;
  setGeneratedWebsite: (website: GeneratedWebsite | null) => void;
  setProjects: (projects: Project[]) => void;
  setCurrentProject: (project: Project | null) => void;
  resetForm: () => void;
}

export const useGeneratorStore = create<GeneratorStore>((set) => ({
  userPrompt: '',
  websiteType: 'landing_page',
  title: '',
  isLoading: false,
  error: null,
  generatedWebsite: null,
  projects: [],
  currentProject: null,

  setUserPrompt: (prompt) => set({ userPrompt: prompt }),
  setWebsiteType: (type) => set({ websiteType: type }),
  setTitle: (title) => set({ title }),
  setIsLoading: (loading) => set({ isLoading: loading }),
  setError: (error) => set({ error }),
  setGeneratedWebsite: (website) => set({ generatedWebsite: website }),
  setProjects: (projects) => set({ projects }),
  setCurrentProject: (project) => set({ currentProject: project }),
  resetForm: () =>
    set({
      userPrompt: '',
      title: '',
      websiteType: 'landing_page',
      error: null,
    }),
}));
