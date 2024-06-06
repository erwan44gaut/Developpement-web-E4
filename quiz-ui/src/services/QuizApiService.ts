import axios from 'axios';
import { type Question } from '../types.d.ts';

// Fonction pour récupérer le nombre total de questions
export const getTotalNumberOfQuestions = async (): Promise<number> => {
  const response = await axios.get('http://127.0.0.1:5000/quiz-info');
  return response.data.size;
};

// Fonction pour récupérer une question par position
export const getQuestionByPosition = async (position: number): Promise<Question> => {
  const response = await axios.get('http://127.0.0.1:5000/questions', {
    params: { position }
  });
  return response.data;
};