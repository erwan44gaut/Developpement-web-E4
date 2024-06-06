import axios from 'axios';
import { type Question } from '@/types';

// Fonction pour récupérer le nombre total de questions
export const getTotalNumberOfQuestions = async (): Promise<number> => {
  const response = await axios.get('http://localhost:3000/quiz-info');
  return response.data.size;
};

// Fonction pour récupérer une question par position
export const getQuestionByPosition = async (position: number): Promise<Question> => {
  const response = await axios.get('http://localhost:3000/questions', {
    params: { position }
  });
  return response.data;
};